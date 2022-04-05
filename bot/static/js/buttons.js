createRowBot('Seja bem-vindo, sou o Curso em bot e estarei te auxiliando a escolher algum determinado curso ou auxiliando a aprender sobre algumas das áreas de TI!Escolha uma das seguintes opções:' +
    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="var buttonValue = sendButton(this.value);" value="Desejo entender mais sobre as áreas de TI">Desejo entender mais sobre as áreas de TI</button>' +
    '</br><button id="buttonSay" class="btn btn-outline-dark mt-2" onClick="sendButton(this.value);" value="Quero visualizar os cursos disponíveis">Quero visualizar os cursos disponíveis</button>');



function sendButton(value){
                submitButton(value);
            }

function submitButton(value) {

            var inputData = {
              'text': value
            };
            console.log(inputData);

            var $submit = $.ajax({
                type: 'POST',
                url: chatterbotUrl,
                data: JSON.stringify(inputData),
                contentType: 'application/json',
                headers: {'X-CSRFToken': csrftoken},
                mode: 'same-origin'
            });

            $submit.done(function(statement) {
                createRowBot(statement.text);
            });

            $submit.fail(function() {
              // : Handle errors
            });
          }
