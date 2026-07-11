label scene1_day2:
     
    $ quick_menu = True
    show screen phone_button
    with Dissolve(0.5)
    
    play ambient int_day fadein(2.0)
    "..."
    play audio door_knock
    "Escucho como tocan la puerta..."
    $ renpy.pause(6.0, hard=True)
    l_thought "¿Ya amaneció?{w} ¿Tan pronto?"
    $ renpy.pause(6.0, hard=True)
    l_thought "Solo deseo, quiero dormir un poco más."
    $ renpy.pause(6.0, hard=True)
    l_thought "No quiero despertarme, en verdad, no quiero."
    "Una voz se escucha a través de la puerta."
    dad "Laila, despierta."
    dad "Necesito que te levantes.{w} No quiero estar apurandote a último momento, por favor."
    scene lailaroom_d:
        function waking_up_blur2
    show parpadeo_off2
    "Abro lentamente los ojos, viendo como la luz del día me aturde un poco"
    hide parpadeo_off2
    dad "Necesito que te prepares, ya todo está listo para irnos."
    $ renpy.pause(3.0, hard=True)
    dad "Te hice unos hotcakes, tus favoritos."
    "Una vez dice eso último, escucho como sus pasos se dirigen hacia la planta baja."
    $ renpy.pause(3.0, hard=True)
    l_thought "Que recuerdos...{w} Ella solía cocinarlos para eventos especiales..."
    show screen red_effect2
    nobody "{sc=3}¿Y ahora?{/sc}"
    nobody "{sc=3}Ahora es solo un pobre intento de tu padre por comprar tu felicidad.{/sc}"
    nobody "{sc=6}¿Cuánto crees que durará?{/sc}"
    hide screen red_effect2 with Dissolve(0.5)
    l_thought "..."
    "Trago saliva, tratando de ignorar la voz a toda costa, aguantando las ganas de llorar en este momento."
    "Me levanto lentamente.{w} Me froto los ojos para acostumbrarme al entorno demasiado brillante del día de hoy."
    l_thought "Mi cuerpo pesa el doble, como si la noche no hubiera servido de nada. Cada movimiento es un esfuerzo."
    l_thought "Pero el olor a canela y mantequilla llega débilmente hasta aquí... y por primera vez en mucho tiempo, el vacío en mi estómago no se siente sólo con hambre."
    $ renpy.pause(4.0, hard=True)
    play audio closet_open
    scene black with Fade(0.5, 0.5, 0.5)
    "Salgo de mi habitación, empezando con mi terrible rutina matutina."
    $ renpy.pause(5.0, hard=True)
    "Una vez terminado de “arreglarme”, me dirijo a la planta baja."
    "Cada escalón que bajo, es un leve pinchazo en mi mente al casi regaño de papá anoche."
    scene livingroom_d with fade
    show counter 1serio with dissolve:
        center
    show blaze 1sonriente with dissolve:
        right4
    "Noto que Blaze y mi padre me esperan, listos para irnos."
    "Blaze, con una sonrisa, me entrega mi desayuno, cuidadosamente guardado en una bolsa y con un escrito que dice:{w} “Para Laila”."
    show counter 1seriot
    $ enfocar("counter")
    dad "Sé que es algo tarde..."
    show counter 1compadecert
    extend " Así que te hice el desayuno para que te lo comas allá."
    show counter 1compadecer
    $ normal("counter")
    l_thought "N-No te hubieras molestado...{w} De verdad..."
    "Papá me da una sonrisa ligera y acogedora, yo le trato de dar una igual, evitando mirarle a los ojos."
    "Digo un gracias en voz baja, para no menospreciar su amabilidad."
    l_thought "Me impactó un poco ver esa sonrisa genuina...{w} Me sorprende que el hombre detrás de eso, haya sido militar."
    $ renpy.pause(2.5, hard=True)
    "Quito todos mis pensamientos. Lo tomo y lo guardo en mi mochila."
    show counter 1nosurpriset
    $ enfocar("counter")
    dad "¿Ya están listas?"
    show counter 1nosurprise
    $ normal("counter")
    show blaze 1felizt
    $ enfocar("blaze")
    b "¡Siempre lista!"
    show blaze 1feliz
    $ normal("blaze")
    "Simplemente doy un débil asentimiento."
    play audio closet_open
    stop ambient fadeout(1.5)
    play ambient ext_day fadein(2.0)
    scene black with Fade(1.5, 1.5, 1.5)
    play audio closet_close
    $ renpy.pause(2.5, hard=True)
    play audio open_car_door
    "Salimos de casa y nos montamos en el carro, rumbo a dejarnos a nosotras primero en la prepa."
    stop ambient fadeout(1.5)
    play audio close_car_door
    $ renpy.pause(2.0, hard=True)
    play ambient bus fadein(2.0)
    "En el viaje de ida, hay un silencio incómodo, pero no tan tenso como anoche."
    l_thought "Estos viajes siempre son largos...{w=0.5} Independientemente a donde vayamos."
    l_thought "Realmente, siempre lo he sentido así..."
    extend " Pero ¿Qué más da? Simplemente es un pensamiento."
    $ renpy.pause(2.5, hard=True)
    play audio radio_interference
    "Veo como papá empieza a tocar la radio, haciendo que se reproduzca música para aliviar el ambiente."
    $ renpy.pause(0.6, hard=True)
    play music country_radio fadein(2.0) volume 0.1 loop
    $ renpy.pause(4.0, hard=True)
    "Noto que Blaze está metida en su teléfono, muy interesada en la conversación que está teniendo.{w} Pero esta lo deja de lado y:"
    b "Y cuéntame... ¿Qué crees que suceda hoy, Laila?"
    l "Cualquier cosa está bien, supongo..."
    "Ella solamente asiente, con su clásica sonrisa."
    $ renpy.pause(2.5, hard=True)
    dad "Ah, Laila..."
    extend " Te voy a recoger después de la prepa para que podamos salir."
    "Eso me sorprende, realmente no me acordaba de eso."
    b "Ah sí, papá me comentó su salida."
    b "Yo no podré ir, tengo que ayudar a Jeremy y Dark en algunas cosas de consejo."
    "Observo como papá se tensa ligeramente al escuchar el nombre de Jeremy."
    l "B-Bueno...{w} Estaré al tanto de tu llamada, papá. Para estar puntual."
    "Veo como me ve a través del retrovisor y se le forma una sonrisa de satisfacción."
    "Blaze me toma ligeramente la mano, haciendo que me sorprenda.{w} Y me habla con susurros."
    b "{size=25}Espero que te vaya bien con papá! Te deseo suerte.{/size}"
    "Me dice con ese mismo tono de anoche."
    "Aprieto su mano, tratando de creer en sus palabras."
    $ renpy.pause(4.0, hard=True)
    dad "Bueno, niñas, ya estamos llegando."
    stop music fadeout(1.5)
    "Blaze y yo nos soltamos y nos empezamos a preparar para la inminente llegada."
    $ renpy.pause(2.5, hard=True)
    play audio open_car_door
    stop ambient fadeout(1.5)
    $ renpy.pause(1.7, hard=True)
    play ambient ext_day fadein(2.0)
    "Cuando sentimos que el carro frena, y papá quita los seguros, abrimos la puerta para bajar."
    scene intersection_day with Fade(0.5, 0.0, 0.5)
    dad "Bueno, Laila, nos vemos más tarde."
    "Le doy un asentimiento. Y cierro la puerta."
    play audio close_car_door
    "El carro arranca y veo cómo se va a lo lejos viendo poco a poco desaparece."
    $ renpy.pause(2.0, hard=True)
    "Empezamos a caminar hasta la escuela (que no queda lejos)."
    stop ambient fadeout(1.5)
    window hide
    scene black with Fade(1.5, 0.0, 1.5) 
    scene pasillo2 
    show blaze 1desinteresada3: 
        walking_center
    with dissolve_scene_full
    window show
    "Entramos a la escuela y caminamos por los pasillos llenos de estudiantes."
    $ renpy.pause(3.0, hard=True)
    "No puedo evitar lo que dicen, y más si son cosas sobre mí."
    idk1 "Oye, ¿Esa no es la chica que tuvo el problema con el profesor Todd?"
    show blaze 1desinteresada2
    idk2 "¿A la que mandaron a dirección y se volvió a escapar?"
    idk1 "Sí, sí, esa misma."
    idk1 "Pero, viéndola bien, creo que no es la primera vez que resuena su nombre, eh."
    idk2 "Refrescame un poco la memoria."
    idk1 "Creo que ella fue la que alejó a su propia amig-{nw}"
    l_thought "Prefiero dejar de escuchar por mi propia salud mental."
    l_thought "¿No tienen nada mejor que hacer que hablar de mi puta vida o qué?"
    l_thought "Maldita preparatoria, ya parece una mafia."
    $ renpy.pause(2.0, hard=True)
    l_thought "..."
    l_thought "Y pensar que todos tienen razón...{w} Soy todo lo que dicen. Y quizás hasta más."
    "Aprieto la correa de mi mochila hasta que los nudillos se me ponen blancos y aumento el paso, fingiendo que no he oído nada."
    "Blaze lo nota. Y toma su tono de madurez."
    show blaze 1compadecert
    $ enfocar("blaze")
    b "No les hagas caso, Laila. No valen la pena."
    show blaze 1compadecer
    $ normal("blaze")
    show screen red_effect2
    nobody "{sc=3}¿No les harás caso?{/sc}"
    nobody "{sc=3}¿Sabiendo que todo lo que dicen es verdad?{/sc}"
    nobody "{sc=5}Que ingenua eres, Laila.{/sc}"
    nobody "{sc=3}Deberías tenerlo siempre en mente.{/sc}"
    nobody "{sc=5}Ya todos tienen esa percepción sobre ti.{/sc}"
    nobody "{sc=6}No hace falta que ni yo te lo diga.{/sc}"
    hide screen red_effect2 with Dissolve(0.5)
    "Ignorando a todos. Tomo lo primero que pasa por mi mente."
    show blaze 1neutral
    l "Eh... Blaze... Ya vuelvo, voy a llevarle el reporte y nota al director."
    l "Si quieres ve adelantandote."
    show blaze 1sonriente
    "Ella asiente con una sonrisa impecable y sigue su camino."
    window hide
    scene black with Fade(1.5, 0.5, 1.5) 
    $ renpy.pause(3.5, hard=True)
    window show
    "Este no había llegado, así que se lo dejé con su secretaria."
    "Me fui al aula, ignorando nuevamente a todos, simplemente queriendo llegar y despejarme."
    $ quick_menu = False
    hide screen phone_button
    with Dissolve(2.5)

return

    #if persistent.day < 2:
    #    $ persistent.day = 2
    #    $ renpy.save_persistent()