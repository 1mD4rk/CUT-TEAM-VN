define phone_bz  = Character("Blaze", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue", callback=blaze_sound)
define phone_dad = Character("Papá", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue", callback=counter_sound)
define phone_la = Character("Laila", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue", callback=laila_sound)

label call_blaze: #call call_blaze
    hide screen phone_button with dissolve     
    phone call "bz"
    phone_bz "Ohayouuu!!!!!!!!!!!!!!!!"
    phone_la "Hey!"
    "Why is she always this energetic?"
    phone end call
    "..."
    show screen phone_button with dissolve
    return

label call_dad_day3_rutasuicida:
    hide screen phone_button with dissolve     
    phone call "dad"
    phone_la "¿B-Bueno?"
    phone_dad "Laila.{w} ¿Dónde estás?"
    "No es una pregunta.{w} Es un diagnóstico."
    "Su voz es cortante, profesional. Como si fuera algo más del trabajo."
    phone_la "En... en la escuela.{w} Ya salía."
    phone_dad "Llevo quince minutos esperando.{w} ¿Dónde rayos te habías metido?"
    window show
    l_thought "Quince minutos."
    l_thought "Quince minutos parado ahí, viendo pasar a otros estudiantes, a otros hijos que sí llegan a tiempo."
    l_thought "Quince minutos de acumular esa decepción silenciosa que tanto conozco."
    window hide
    phone_la "Yo... me entretuve.{w} Lo siento."
    "Silencio al otro lado. Un silencio que pesa más que cualquier grito..."
    phone_dad "Baja ya."
    phone_dad "Estoy en la esquina de siempre. Para nuestra salida."
    "Su tono es plano, pero hay algo en la manera que dice “nuestra salida” que duele más que un reproche directo."
    window show
    l_thought "Salida..."
    extend " Cierto que hoy se suponía que íbamos a salir..."
    window hide
    phone_la "Lo sé, papá. Perdón, es que..."
    "Mi voz se traba.{w} ¿Qué excusa podría sonar creíble?"
    phone_dad "No necesito explicaciones, Laila."
    phone_dad "Solo necesito que estés aquí en los próximos tres minutos."
    phone_dad "Realmente pensé que hoy ibas a llegar a tiempo."
    show screen red_effect2
    window show
    nobody "{sc=5}Tres minutos.{/sc}"
    nobody "{sc=5}Ni siquiera te da tiempo de componer esa máscara de normalidad...{/sc}"
    nobody "{sc=7}{b}Que tanto te cuesta mantener{/b}.{/sc}"
    window hide
    hide screen red_effect2 with Dissolve(0.3)
    phone_la "Tres minutos. Entendido."
    phone end call
    show screen phone_button with dissolve
    return

label phone_video_call_blaze:
    scene pasillo onlayer phone_video_call
    show blaze 1felizt onlayer phone_video_call
    phone call "bz" video
    phone_bz "Hey! That's my room"
    phone end call
    "..."

    return