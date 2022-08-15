from os import system as terminal
from time import localtime
from time import sleep as esperar

while True:
    recebe_hora_atual = localtime()
    hora_atual = {
        'hora': recebe_hora_atual.tm_hour,
        'minuto': recebe_hora_atual.tm_min,
        'segundos': recebe_hora_atual.tm_sec
    }
    hora_de_dormir = hora_atual['hora'] >= 0 and hora_atual['minuto'] >= 0
    comando_cmd = 'start explorer'

    if hora_de_dormir:
        terminal(comando_cmd)
        break

    print(f'agora são: {hora_atual["hora"]}:{hora_atual["minuto"]}:{hora_atual["segundos"]}')
    print('ainda não está na hora')

    esperar(1)
