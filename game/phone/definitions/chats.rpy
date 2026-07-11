default pc_sk  = phone.character.Character("SkyHub", phone.asset("skyhub_icon.png"), "sk", 22, "#096092")
default pc_laila  = phone.character.Character("Laila", phone.asset("default_icon.png"), "la", 22, "#6a5d7ac7")
default pc_counter  = phone.character.Character("Papá", phone.asset("default_icon.png"), "dad", 22, "#cab099ff")
default pc_blaze  = phone.character.Character("Blaze", phone.asset("default_icon.png"), "bz", 22, "#da7603")
default pc_dark  = phone.character.Character("Dark", phone.asset("default_icon.png"), "dk", 22, "#da0303")

default dad_gc = phone.group_chat.GroupChat("Papá", phone.asset("default_icon.png"), "dad_chat"). add_character("dad").add_character("la")
default bz_gc = phone.group_chat.GroupChat("Blaze", phone.asset("default_icon.png"), "bz_chat"). add_character("bz").add_character("la")
default dk_gc = phone.group_chat.GroupChat("Dark", phone.asset("default_icon.png"), "dk_chat"). add_character("dk").add_character("la")

init phone register dad_gc:
    time month 1 day 1 year 2066 hour 1 minute 1
    "dad" "..."
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
    "Jeremy solo se queda callado mirándole con el fin de que dejara sus comentarios fuera de lugar.{w} Pero no tuvo tanto éxito."
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
        "dad" "Cambio de planes, me llamaron de una emergencia de trabajo, no podremos ir hoy. Lo hablaremos en casa. Quédate con Blaze."
        "dad" "Si se complica y no puedo pasar por ustedes, vayanse caminando a casa. No esperen."
    
    "Mis dedos se detienen, dejan de temblar y solo me quedo mirando fijamente a la pantalla vacía... Realmente no siento nada."

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

label chat_dad_day3: # CANON
    
    phone discussion "dad_chat":
        time month 2 day 24 year 2066 hour 17 minute 50
        "dad" "Saliendo del trabajo."
        "dad" " 10 minutos. Ahí te recojo."

    l_thought "Ni un “lo siento”."
    extend " Ni una excusa larga."
    extend " Solo él siendo él: directo, sin adornos, pero cumpliendo."
    l_thought "Pero va a venir."
    extend " Dijo que vendría y va a venir."
    "No sé por qué me sorprende. Pero lo hace."
    
    phone end discussion
    return