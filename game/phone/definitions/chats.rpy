default pc_sk  = phone.character.Character("SkyHub", phone.asset("skyhub_icon.png"), "sk", 22, "#096092")
default pc_laila  = phone.character.Character("Laila", phone.asset("default_icon.png"), "la", 22, "#6a5d7ac7")
default pc_counter  = phone.character.Character("Papá", phone.asset("default_icon.png"), "dad", 22, "#cab099ff")
default pc_blaze  = phone.character.Character("Blaze", phone.asset("default_icon.png"), "bz", 22, "#da7603")

default dad_gc = phone.group_chat.GroupChat("Papá", phone.asset("default_icon.png"), "dad_chat"). add_character("dad").add_character("la")
default bz_gc = phone.group_chat.GroupChat("Blaze", phone.asset("default_icon.png"), "bz_chat"). add_character("bz").add_character("la")

init phone register dad_gc:
    time month 1 day 1 year 2066 hour 1 minute 1
    "dad" "hola"
    "la" "..."

init phone register bz_gc:
    time month 1 day 1 year 2066 hour 1 minute 1
    "bz" "W<W"
    "la" "..."

label chat_blaze:
    phone discussion "bz_chat":
        "bz" "si"
        "la" "si"
    phone end discussion

    return

label chat_dad_day2:
    
    phone discussion "dad_chat":
        time month 2 day 23 year 2066 hour 17 minute 30
        "la" "Papá ¿Pasó algo?"
        "la" "No me has llamado para nuestra salida."

    $ renpy.pause(2.5, hard=True)
    "Siento la miradas de todos esperando alguna respuesta."
    show dark 2desafiantet
    $ enfocar("dark")
    d "Apuesto a que se olvidó. Diez a uno."
    show dark 2desafiante
    $ normal("dark")
    show jeremy 2seriot
    $ enfocar("jeremy")
    je "Callate."
    show jeremy 2serio
    $ normal("jeremy")
    "Hablan en voz baja, aun así los escucho."
    l_thought "Jajajaja. Mejor así, no seré una carga para él por hoy."
    show blaze 2compadecert
    $ enfocar("blaze")
    b "Tal vez solo está atrapado en el tráfico..."
    show blaze 2preocupada
    $ normal("blaze")
    l "Eso espero..."
    $ renpy.pause(2.5, hard=True)

    phone discussion "dad_chat":
        "dad" "Emergencia en el trabajo. No podremos ir hoy. Hablamos de eso en casa. Quédate con Blaze."
        "dad" "Las paso recogiendo más tarde. En tal caso que no pueda, váyanse a casa ustedes solas."
   
    if (rutaCanon-rutaSuicida)>=0:
        l_thought "¿Emergencia? ¿O es solo otra excusa? ¿O... quizás un alivio?"

    else:
        l_thought "¿Emergencia? Claro. La emergencia de no querer lidiar con su hija rota. Como siempre"
        show screen red_effect2
        nobody "{sc=3}Por supuesto.{/sc}"
        nobody "{sc=3}Prefiere cualquier crisis laboral...{/sc}"
        nobody "{sc=3}Antes que una hora contigo.{/sc}"
        nobody "{sc=3}¿En serio te sorprende?{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
   
   
   
    phone end discussion

    return