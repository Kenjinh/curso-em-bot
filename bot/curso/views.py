import json
from datetime import datetime
from unidecode import unidecode
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

    chatterbot = ChatBot(**settings.CHATTERBOT)  # Import chatterbot data from settings.py

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
        response_data['in_response_to'] = response_data['in_response_to'].lower().replace('-','')  # Remove "-" and change for lower
        response_data['in_response_to'] = unidecode(response_data['in_response_to']) # Remove accents
        # region Welcome
        if response_data['in_response_to'] == 'ola' or response_data['in_response_to'] == 'oi' or response_data[
            'in_response_to'] == 'olá' or response_data['in_response_to'] == 'começar':
            response_data[
                'text'] = 'Seja bem-vindo, sou o Curso em bot e estarei te auxiliando a escolher algum determinado curso ou auxiliando a aprender sobre algumas das áreas de TI!Escolha uma das seguintes opções:' + \
                          '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="sendButton(this.value);" value="Quero visualizar os cursos disponíveis">Quero visualizar os cursos disponíveis</button>'

        elif response_data['in_response_to'] == 'desejo entender mais sobre as areas de ti':
            response_data['text'] = '????'
        # endregion

        # region Select Train
        elif response_data['in_response_to'] == 'quero visualizar os cursos disponiveis':
            response_data['text'] = 'Em qual área você tem interesse em treinamentos:' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="Desenvolvimento Front-end">Desenvolvimento Front-end</button>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="Desenvolvimento Back-end">Desenvolvimento Back-end</button>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="Mobile">Desenvolvimento Mobile</button>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="git e github">Versionamento de códigos com Git e GitHub</button>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="Redes de computadores">Redes de computadores</button>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="automação">Criação de automação de testes</button>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="Banco de dados">Banco de dados</button>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'
        # endregion

        # region FRONT-END
        elif response_data['in_response_to'] == 'desenvolvimento frontend' or response_data[
            'in_response_to'] == 'frontend':
            response_data[
                'text'] = 'Interessado em criar o design das telas de softwares então? Então veja essas recomendações!' + \
                          '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="html e css">HTML e CSS</button>' + \
                          '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="react js">React JS (Recomendado conhecimento em JavaScript)</button>' + \
                          '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="angular js">Angular JS (Recomendado conhecimento em JavaScript)</button>' + \
                          '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'

        elif response_data['in_response_to'] == 'html e css':
            response_data['text'] = 'Perfeito, com isso irá aprender a criar a estrutura de uma página e seu design!' + \
                                    '</br>Módulo 1:</br>' + \
                                    '<a class="" href="https://www.cursoemvideo.com/curso/html5-css3-modulo1/" target="_blank">Curso em Vídeo HTML5 e CSS3: Modulo 1</a>' + \
                                    '</br>Módulo 2:</br>' + \
                                    '<a class="" href="https://www.cursoemvideo.com/curso/curso-html5-e-css3-modulo-2-de-5-40-horas/" target="_blank">Curso em Vídeo HTML5 e CSS3: Modulo 2</a>' + \
                                    '</br>Módulo 3</br>' + \
                                    '<a class="" href="https://www.cursoemvideo.com/curso/curso-html5-e-css3-modulo-3-de-5-40-horas/" target="_blank">Curso em Vídeo HTML5 e CSS3: Modulo 3</a>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'

        elif response_data['in_response_to'] == 'react js':
            response_data['text'] = 'Então você quer aprender um dos novos queridinhos do front-end?' + \
                                    '</br><a class="" href="https://www.youtube.com/playlist?list=PLnDvRpP8BneyVA0SZ2okm-QBojomniQVO" target="_blank">Curso de React JS</a>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'

        elif response_data['in_response_to'] == 'angular js':
            response_data['text'] = 'Esse framework está sendo muito utilizado, excelente escolha!' + \
                                    '</br><a class="" href="https://www.youtube.com/playlist?list=PLGxZ4Rq3BOBoSRcKWEdQACbUCNWLczg2G" target="_blank">Curso de Angular JS</a>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'
        # endregion

        # region BACK-END
        elif response_data['in_response_to'] == 'desenvolvimento backend':
            response_data[
                'text'] = 'Ok, você tem interesse pelo back-end! Você tem algum conhecimento em lógica de programação?' + \
                          '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="backend sim">Sim</button>' + \
                          '<button id="buttonSay" class="btn btn-outline-dark mt-2 mx-2"  onClick="var buttonValue = sendButton(this.value);" value="backend não">Não</button>'

        elif response_data['in_response_to'] == 'backend sim':
            response_data['text'] = 'Muito bem, qual linguagem você tem interesse?' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="java">Java</button>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="python">Python</button>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="javascript">JavaScript</button>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'

        elif response_data['in_response_to'] == 'backend nao':
            response_data['text'] = 'Vamos iniciar nesse mundo de lógica de programação!' + \
                                    '</br><a class="" href="https://www.cursoemvideo.com/curso/curso-de-algoritmo/" target="_blank">Curso de lógica de programação</a>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'

        elif response_data['in_response_to'] == 'java':
            response_data['text'] = 'Vamos aprender a orientação a objetos com Java?' + \
                                    '</br>Curso Java com orientação a objetos iniciante:' + \
                                    '</br><a class="" href="https://www.youtube.com/playlist?list=PLGxZ4Rq3BOBq0KXHsp5J3PxyFaBIXVs3r" target="_blank">Curso de Java iniciante</a>' + \
                                    '</br>Curso Java com orientação a objetos Intermediário:' + \
                                    '</br><a class="" href="https://www.youtube.com/playlist?list=PLGxZ4Rq3BOBoqYyFWOV_YbfBW80YGAGEI" target="_blank">Curso de Java intermediário</a>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'

        elif response_data['in_response_to'] == 'python':
            response_data['text'] = 'Python, a linguagem back-end mais querida pelos devs!' + \
                                    '</br>Curso Python iniciante e intermediário:' + \
                                    '</br><a class="" href="https://www.youtube.com/playlist?list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0" target="_blank">Curso de Python iniciante e intermediário</a>' + \
                                    '</br>Curso Python com Django:' + \
                                    '</br><a class="" href="https://www.udemy.com/course/python-3-na-web-com-django-basico-intermediario/" target="_blank">Curso de Python com Django</a>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'

        elif response_data['in_response_to'] == 'javascript':
            response_data['text'] = 'Javascript, a linguagem que foi na onda do nome Java!' + \
                                    '</br>JavaScript iniciante:' + \
                                    '</br><a class="" href="https://www.cursoemvideo.com/curso/javascript/" target="_blank">Curso de JavaScript iniciante</a>' + \
                                    '</br>Node JS:' + \
                                    '</br><a class="" href="https://www.youtube.com/playlist?list=PLJ_KhUnlXUPtbtLwaxxUxHqvcNQndmI4B" target="_blank">Curso de Node JS</a>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'
        # endregion

        # region Mobile
        elif response_data['in_response_to'] == 'mobile':
            response_data['text'] = 'Que tal aprender Kotlin e criar seus aplicativos mobile?' + \
                                    '</br><a class="" href="https://www.youtube.com/playlist?list=PLPs3nlHFeKTr-aDDvUxU971rPSVTyQ6Bn">Curso de Kotlin</a>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'
        # endregion

        # region Git and Github
        elif response_data['in_response_to'] == 'git e github':
            response_data['text'] = 'Com isso sua organização de códigos irá além!' + \
                                    '</br><a class="" href="https://www.cursoemvideo.com/curso/curso-de-git-e-github/">Curso de Git e Github</a>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'
        # endregion

        # region Redes
        elif response_data['in_response_to'] == 'redes de computadores':
            response_data['text'] = 'Tudo bem, vamos aprender como nos conectamos com a tecnologia!' + \
                                    '</br><a class="" href="https://www.cursoemvideo.com/curso/redes-de-computadores/">Curso Redes de computadores</a>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'
        # endregion

        # region tests/QA
        elif response_data['in_response_to'] == 'automacao' or response_data['in_response_to'] == 'criacao de automacao de testes':
            response_data['text'] = 'Certo, então quer ser um analista de testes/QA!' + \
                                    '</br><a class="" href="https://www.youtube.com/playlist?list=PLedtsFT8ymsgVCqgLvPiSrfYeGdujcqvv">Curso Automação de testes</a>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'
        # endregion

        # region Database
        elif response_data['in_response_to'] == 'banco de dados':
            response_data['text'] = 'Beleza, vamos criar tabelas e definir uma organização nos dados de seus sistemas!' + \
                                    '</br>Banco de dados MySQL - Criar banco de dados:' + \
                                    '</br><a class="" href="https://www.cursoemvideo.com/curso/mysql/">Criar banco de dados Mysql</a>' + \
                                    '</br>Caso não conheça sobre a modelagem de banco de dados, recomendamos dar uma olhada neste curso também:' + \
                                    '</br>Modelagem de banco de dados:' + \
                                    '</br><a class="" href="https://www.youtube.com/playlist?list=PLucm8g_ezqNoNHU8tjVeHmRGBFnjDIlxD">Curso de Modelagem</a>' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'
        # endregion
        else:
            response_data['text'] = 'Comando não encontrado' + \
                                    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="ola">Voltar ao menu inicial</button>'

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
