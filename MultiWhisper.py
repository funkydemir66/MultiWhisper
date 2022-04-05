import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction
from time import sleep




extension_info = {
    "title": "MultiWhisper",
    "description": ":mw pla1&pla2&pla3&:mwc (text) ",
    "version": "1.0",
    "author": "funkydemir66"
}

ext = Extension(extension_info, sys.argv, silent=True)
ext.start()


MESSAGE = ":mwc "

pla1 = ":mw pla1 "

pla2 = ":mw pla2 "

pla3 = ":mw pla3 "

ac = False
sec_kod = False
sec_player = False
sec_player3 = False
sc = True
oc = True

tla1 = "not_selected"

tla2 = "not_selected"

tla3 = "not_selected"

def konusma(msj):
    global sc, sec_kod, sec_player, sec_player3, tla1, tla2, tla3, ac, oc


    text = msj.packet.read_string()

    if text.startswith(pla1):
        msj.is_blocked = True
        if sc:
            tla1 = str(text[(len(pla1)):])
            ext.send_to_client('{in:Chat}{i:123456789}{s:"' + str(tla1) + ' you chose this player (pla1) "}{i:0}{i:30}{i:0}{i:0}')


    if text.startswith(pla2):
        msj.is_blocked = True
        if sc:
            tla2 = str(text[(len(pla2)):])
            ext.send_to_client('{in:Chat}{i:123456789}{s:"' + str(tla2) + ' you chose this player (pla2) "}{i:0}{i:30}{i:0}{i:0}')


    if text.startswith(pla3):
        msj.is_blocked = True
        if sc:
            tla3 = str(text[(len(pla3)):])
            ext.send_to_client('{in:Chat}{i:123456789}{s:"' + str(tla3) + ' you chose this player (pla3) "}{i:0}{i:30}{i:0}{i:0}')


    if text.startswith(MESSAGE):
        msj.is_blocked = True
        mod = str(text[(len(MESSAGE)):])
        if sc:
            ext.send_to_client('{in:Chat}{i:123456789}{s:" telling to ' + str(tla1) + ' & ' + str(tla2) + ' & ' + str(tla3) + ': " '  + str(mod) + ' " "}{i:0}{i:30}{i:0}{i:0}')
            ext.send_to_server('{out:Whisper}{s:"' + str(tla1) + ' ' + str(mod) + '"}{i:3}')
            sleep(0.70)

    if text.startswith(MESSAGE):
        msj.is_blocked = True
        mod = str(text[(len(MESSAGE)):])
        if sc:
            ext.send_to_server('{out:Whisper}{s:"' + str(tla2) + ' ' + str(mod) + '"}{i:3}')
            sleep(1.30)


    if text.startswith(MESSAGE):
        msj.is_blocked = True
        mod = str(text[(len(MESSAGE)):])
        if sc:
            ext.send_to_server('{out:Whisper}{s:"' + str(tla3) + ' ' + str(mod) + '"}{i:3}')
            sleep(2)



ext.intercept(Direction.TO_SERVER, konusma, 'Chat')
