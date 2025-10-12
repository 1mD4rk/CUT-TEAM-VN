label day2:
    $ discord.set(details="Tuesday - (16/02/2066)", state="Day 2")
    $ phone.system.battery_level = 80

    #$ phone.system.date = datetime.date(2066, 2, 16)
    
    $ persistent.quick_menu_visible = True
    show screen phone_button
    with Dissolve(0.5)
    
    play ambient int_day fadein(2.0)
    "..."
    play sound door_knock
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
    play sound closet_open
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
    play sound closet_open
    stop ambient fadeout(1.5)
    play ambient ext_day fadein(2.0)
    scene black with Fade(1.5, 1.5, 1.5)
    play sound closet_close
    $ renpy.pause(2.5, hard=True)
    play sound open_car_door
    "Salimos de casa y nos montamos en el carro, rumbo a dejarnos a nosotras primero en la prepa."
    stop ambient fadeout(1.5)
    play sound close_car_door
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
    play sound open_car_door
    stop ambient fadeout(1.5)
    $ renpy.pause(1.7, hard=True)
    play ambient ext_day fadein(2.0)
    "Cuando sentimos que el carro frena, y papá quita los seguros, abrimos la puerta para bajar."
    scene intersection_day with Fade(0.5, 0.0, 0.5)
    dad "Bueno, Laila, nos vemos más tarde."
    "Le doy un asentimiento. Y cierro la puerta."
    play sound close_car_door
    "El carro arranca y veo cómo se va a lo lejos viendo poco a poco desaparece."
    $ renpy.pause(2.0, hard=True)
    "Empezamos a caminar hasta la escuela (que no queda lejos)."
    stop ambient fadeout(1.5)
    window hide
    scene black with Fade(1.5, 0.0, 1.5) 
    scene pasillo2 with dissolve_scene_full
    show blaze 1desinteresada3 with dissolve: 
        walking_center
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
    $ persistent.quick_menu_visible = False
    hide screen phone_button
    with Dissolve(2.5)
    jump aula_day2
    #if persistent.day < 2:
    #    $ persistent.day = 2
    #    $ renpy.save_persistent()

    return

label aula_day2:
    $ renpy.pause(5.0, hard=True)
    $ persistent.quick_menu_visible = True
    show screen phone_button
    with Dissolve(1.5)
    "Las horas pasaron sin que lo notara"
    play sound bell
    extend ", hasta que llegó el receso... me tomó completamente por sorpresa."
    "Estaba tan perdida en mis pensamientos que ni siquiera percibí cómo las clases se desvanecen a mi alrededor.{w} Ni la campana, ni las voces, nada. Es como si todo hubiera desaparecido de un segundo a otro."
    "Lo extraño es que ningún profesor me pidió participar, cuando suelen aprovechar cualquier silencio para hacerlo.{w} Por una vez, agradezco que me hayan dejado en paz."
    scene class3A with dissolve_scene_full2
    "Cuando levanto la vista, descubro que el salón está vacío."
    "Absolutamente vacío."
    l_thought "¿En qué momento se fueron todos?"
    l_thought "¿Acaso me quedé dormida sin notarlo?"
    "Me froto los ojos, incrédula."
    $ renpy.pause(2.0, hard=True)
    "Decido no darle demasiada importancia."
    "Reviso la hora en el celular, pero la pantalla parpadea un instante y vuelve en negro.{w} Maldigo en voz baja."
    $ renpy.pause(2.0, hard=True)
    "Me levanto del pupitre y salgo al pasillo."
    scene pasillo with Fade(0.5, 1.0, 0.5)
    $ renpy.pause(3.0, hard=True)
    "Ahí es cuando la incomodidad comienza a crecer"
    extend ": todo está demasiado limpio, demasiado callado.{w} Ni un papel en el piso, ni un murmullo lejano.{w} Es un silencio grueso, que parece pegarse en la piel."
    l_thought "¿Acaso me perdí de una asamblea importante en la escuela?{w} ¿O peor... hubo un maldito tiroteo y yo sigo aquí tan tranquila?"
    $ renpy.pause(3.0, hard=True)
    "Camino despacio, los pasos resonando como golpes huecos en la losa."
    $ renpy.pause(3.0, hard=True)
    show vignette at vineta_organico zorder 100
    "El aire se siente pesado, como si costara respirar."
    "Trato de convencerme de que es paranoia, pero no lo logro.{w} Cada sombra parece más alargada de lo normal, cada puerta cerrada parece ocultar un par de ojos detrás."
    $ renpy.pause(3.0, hard=True)
    "No puedo evitarlo: siento que alguien me observa."
    "La nuca se me enfría, y el impulso de voltear me gana{w}.{w}.{w}.{w} Pero no hay nada."
    "Solo pasillos interminables, vacíos, demasiado perfectos para ser reales."
    l_thought "¿Qué demonios está pasando aquí?"
    $ renpy.pause(3.0, hard=True)
    play sound drop
    "Y de pronto—un sonido seco."
    extend " Un golpe, como si algo cayera detrás de mí.{w} Mi corazón se acelera, volteo de inmediato...{w} nada."
    "Solo el eco se ríe de mí."
    "La tensión se estira tanto que apenas puedo pensar."
    show layer master: 
        function apply_blur_gradually2  
    "Mis manos tiemblan, siento que la vista se me nubla."
    "Y entonces solo parpadeo."
    scene black with Fade(1.5, 0.5, 1.5)
    $ renpy.pause(5.0, hard=True)
    scene class3A
    play ambient classroom
    "Estoy otra vez en mi pupitre."
    show screen pulse_black
    "El salón lleno, mis compañeros hablando, el ruido de siempre alrededor.{w} El profesor sigue dando clase como si nada."
    "Me quedo helada, mirando a todos con el corazón desbocado."
    l_thought "¿Soñé despierta? ¿Fue una alucinación? ¿O de verdad estuve... en otro lugar?"
    "Volteo a ver a Blaze"
    show blaze 1desinteresada3 with Dissolve(0.5):
        center2 
    extend ", y me alivio que solo era una simple pesadilla."
    show blaze 1seria
    "Pero ella me mira con el ceño ligeramente fruncido."
    l_thought "Supongo que noto que me acabo de despertar..."
    $ inac2("blaze")
    "Tomo un largo suspiro, tratando de entender que era {i}eso{/i}."
    $ renpy.pause(2.5, hard=True)
    hide screen pulse_black
    l_thought "No, no entiendo el significado de eso.{w=1.0} Realmente esta vez necesito que alguien me lo explique con manzanas y peras."
    "En eso, escucho a dos personas hablando detrás de mí. Se ríen bastante fuerte. O bueno, Dark se ríe muy fuerte."
    l_thought "Realmente, nunca me han importado quienes se ríen atrás, pero sabiendo de quién es, ahora me irrita el doble."
    "Volteo, para decirle que se calle la puta boca."
    show dark 1feli with Dissolve(0.5):
        left
    show jeremy 1juzga with Dissolve(0.5):
        flip
        right5
    l "Por el amor de dios, podrías callarte y dar el ejemplo de vice president–{nw}"
    "Dark, Blaze y..."
    l_thought "¿Y quién es este?"
    show dark 1felit
    $ enfocar("dark")
    d "Oh, hola, mujer con bolas."
    show dark 2desafiantet
    extend " ¿Amaneciste en el lado correcto de la cama hoy?"
    show dark 2desafiante
    $ normal("dark")
    "No le respondo, dejando mi mirada posada en el otro chico."
    l_thought "¿Y quien es este? genuinamente a este NUNCA lo he visto por aquí."
    l_thought "O bueno... Puede ser que tampoco le preste mucha atención."
    l_thought "Como sea. Ahora estoy conociendo a extraños, que espectacular."
    $ renpy.pause(2.5, hard=True)
    show jeremy 1incomodo2
    "El chico solo parece incómodo con mi mirada fija y me ignora."
    show blaze 1juzga
    $ normal("blaze")
    show jeremy 1incomodo2t
    $ enfocar("jeremy")
    idk1 "Y Blaze... ¿Qué hicieron ayer?"
    show jeremy 1seriot
    extend " Dark no me pasó nada."
    show jeremy 1serio3
    $ normal("jeremy")
    show dark 1distraido
    $ inac("blaze")
    $ inac("dark")
    $ inac("jeremy")
    show blaze 1felizt
    l_thought "..."
    show blaze 1feliz
    show jeremy 1surpriset
    l_thought "¿Conoce a Blaze?"
    show jeremy 1surpriset
    l_thought "Puede ser que este sea “Jeremy”... Blaze lo mencionó en el camino."
    show jeremy 1juzga2
    show blaze 1sonrientet
    l_thought "Claro que la conoce. Todos la conocen.{w} Ella es... normal. Sociable."
    show blaze 1sonriente
    l_thought "probablemente sea otro de sus amigos perfectos que me va a juzgar en silencio."
    show dark 1juzga2
    $ renpy.pause(2.5, hard=True)
    show jeremy 1felizt
    show dark 1juzga2t
    $ enfocar("dark")
    d "Ya puedes dejar de mirarlo{w}, das miedo."
    show jeremy 1feliz
    show blaze 3juzga2t
    $ normal("dark")
    show dark 1juzga2
    l "Jodete, realmente jodete."
    show dark 1seriot
    show blaze 3juzga
    $ enfocar("dark")
    d "No comiences otro altercado en el salón."
    show dark 2distraidot
    show blaze 2desinteresada2
    show jeremy 2incomodo
    extend " Ya el director me regañó ayer porque te deje ir."
    show dark 2desafiantet
    d "Realmente me debes una."
    show dark 2desafiante
    $ normal("dark")
    show screen red_effect2
    l_thought "¿Qué? ¿Le regañaron...{w} por mi culpa?"
    "Una punzada de culpa se clavó en mi estómago. La tensión se apoderó de mí."
    show jeremy 1neutral
    show blaze 2preocupada
    show dark 1neutral at boo2
    l "¿P-por mi culpa...?"
    nobody "{sc=3}Hasta TUS actos les afectan a los demás.{/sc}"
    nobody "{sc=4}Solo conseguirás que te odie.{/sc}"
    nobody "{sc=5}Como todos en esta escuela.{/sc}{sc=6} Si es que no te odia ya.{/sc}"
    show jeremy 1feliz
    show blaze 2compadecer
    show dark 1incomodot
    $ enfocar("dark")
    d "Realmente fue más mía, te deje ir y eso."
    show dark 1incomodo
    $ normal("dark")
    hide screen red_effect2 with Dissolve(3.5)
    $ renpy.pause(1.5, hard=True)
    show dark 1neutral
    l "..."
    l "Gracias."
    "A pesar de mis pensamientos intrusivos{w}, me fuerzo a decir eso."
    "Dark se queda anonadado al escuchar eso."
    show dark 1neutralt
    $ enfocar("dark")
    d "Eh..."
    show dark 1incomodot
    extend " Tranquila, realmente no es nada."
    show dark 1incomodo
    $ normal("dark")
    "Dice mientras fuerza una sonrisa, pero se nota la sinceridad."
    $ renpy.pause(2.5, hard=True)
    show screen red_effect2
    nobody "{sc=3}Eres como una plaga.{/sc}"
    show screen pulse_black
    "Pero ellos vuelven."
    nobody "{sc=3}Dondequiera que vas, destruyes la tranquilidad de los que te rodean.{/sc}"
    nobody "{sc=3}Y aún así, te atreves a ponerte esa cara de víctima.{/sc}"
    nobody "{sc=5}No eres más que una egoísta.{/sc}"
    nobody "{sc=7}Tarde o temprano, todos se cansarán de ti.{/sc}"
    show blaze 1sonriente
    $ inac2("blaze")
    show dark 2distraido
    $ inac2("dark")
    show jeremy 1felizt
    $ inac2("jeremy")
    "Me volteo en silencio, procesando lo que me dijo esa voz."
    show jeremy 1feliz
    show blaze 3desinteresadat
    "{cps=5.0}Creyendole.{/cps}"
    $ renpy.pause(5.0, hard=True)
    show blaze 3desinteresada
    show jeremy 1juzgat
    show dark 2juzga2
    $ renpy.pause(8.0, hard=True)
    show jeremy 1juzga
    show blaze 3neutralt
    show dark 2desafiantet
    $ enfocar("dark")
    d "Laila, ¿Qué piensas del amor?"
    show blaze 3neutral
    show jeremy 1incomodot
    show dark 2desafiante
    $ normal("dark")
    hide screen pulse_black
    hide screen red_effect2
    "Me quita de mi niebla del pensamiento, pero me extraña su pregunta."
    l_thought "¿Como? ¿A qué vino eso?"
    show jeremy 1incomodo
    show blaze 1sonrientet
    show dark 2juzgat
    $ enfocar("dark")
    d "No es necesario que respondas. Cosas que pienso."
    show dark 2juzga
    show blaze 1sonriente
    show jeremy 1felizt
    $ normal("dark")
    "Me quedo extrañada, pero prefiero no darle importancia."
    "Volteo a ver a Blaze, la veo algo entretenida en su conversación con ese chico."
    l_thought "Que facilidad tiene ella para hablar. Ojalá poder ser así."
    "Volteo a ver mi asiento, sin nada interesante."


    return