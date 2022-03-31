import json
from datetime import datetime
from chatterbot import ChatBot  # Import ChatBot
from . import models
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from chatterbot.trainers import ListTrainer  # Import ListTrainer from chatterbot
from django.views.decorators.csrf import csrf_exempt  # Import CSRF Token
from chatterbot.ext.django_chatterbot import settings  # Import settings from Chatterbot


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.
        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))
        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()
        response_data['in_response_to'] = response_data['in_response_to'].lower().replace('-', '')
        if response_data['in_response_to'] == 'ola' or response_data['in_response_to'] == 'oi':
            response_data['text'] = 'Ola eu sou o Curso em Bot, tenho diversos cursos de tecnologia para indicar a ' \
                                    'você, mas antes preciso fazer algumas perguntas, digite "Começar" para ' \
                                    'iniciarmos. '
        elif response_data['in_response_to'] == 'começar':
            areas = models.Areas.objects.all()
            area = ''
            for a in areas:
                area = area + "<br>-" + str(a)
            area = str(area)
            response_data['text'] = 'Qual a sua área de interesse?' + area

        elif response_data['in_response_to'] == 'backend':
            id_back = models.Areas.objects.get(name='Back-End').id
            back = ''
            for b in models.Languages.objects.filter(id_area__exact=id_back):
                back = back + "<br>-" + b.name

            response_data['text'] = 'Qual a linguagem de backend que você gostaria de aprender?' + back

        elif response_data['in_response_to'] == 'java':
            id_java = models.Languages.objects.get(name='Java ').id
            a = ''
            for j in models.LinksCourse.objects.filter(id_language__exact=id_java):
                a = a + 'O curso ' + j.id_course.name + ' e está disponível em <a href="' + j.link + '" class="stretched-link" target="_blank">link.<a><br>'
                response_data['text'] = a

        elif response_data['in_response_to'] == 'frontend':
            id_front = models.Areas.objects.get(name='Front-End').id
            front = ''
            for f in models.Languages.objects.filter(id_area__exact=id_front):
                front = front + " - " + f.name

            response_data['text'] = 'Qual a linguagem de frontend que você gostaria de aprender?' + front

        else:
            response_data['text'] = 'Comando não encontrado digite "Começar" para voltar o chatbot'

        return JsonResponse(response_data, status=200)

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        print(request)
        print(self)
        return JsonResponse({
            'name': self.chatterbot.name
        })


def home(request):
    context = {
        'year': datetime.now().year,
        'title': 'Home Page',
    }
    return render(request, "html/index.html", context)
