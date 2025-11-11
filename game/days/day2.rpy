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

#### JEREMY MOMENT ####
label aula_day2:
    $ renpy.pause(5.0, hard=True)
    $ persistent.quick_menu_visible = True
    show screen phone_button
    with Dissolve(1.5)
    scene class3A with dissolve_scene_full2
    "Llegó al salón, simplemente estoy distraída ante todo. Como si estuviera en modo automático, voy y dejo mis cosas en mi asiento. Y me siento."
    show blaze 1sonriente with Dissolve(0.5):
        center2 
    play music bgm8
    queue music bgm82
    "Blaze nota que ya llegué."
    show blaze 1sonrientet
    $ enfocar("blaze")
    b "¡Hey! ¿Cómo te fue con el reporte?"
    show blaze 1sonriente 
    $ normal("blaze")
    "Suspiro."
    show blaze 1compadecer
    l "No estaba. Dejé el reporte con la secretaria."
    show blaze 1compadecert
    $ enfocar("blaze")
    b "¿Y ella dijo algo? ¿Parecía...{nw=0.5}"
    show blaze 2preocupadat
    extend " enojada?"
    show blaze 2preocupada
    $ normal("blaze")
    l "Solo tomó el papel."
    show blaze 1compadecer
    extend " Ni me miró."
    show blaze 1compadecert
    $ enfocar("blaze")
    b "Bueno, ya tienes una cosa menos, supongo que ya se acabó el problema."
    $ normal("blaze")
    show blaze 1compadecer
    "Eso lo dice con un tono alivida. Simplemente asiento.{w} No sé que decirle."
    l_thought "No creo que los problemas desaparezcan así de fácil..."

    if (rutaCanon-rutaSuicida)<=-1:
        show screen red_effect2
        nobody "{sc=3}Los problemas solo desaparecen con una solución permanente.{/sc}"
        nobody "{sc=5}Tú sabes cuál es.{/sc}"
        hide screen red_effect2 with Dissolve(1.0)
        "Ignorando a la voz de mi grandiosa mente..."

    $ renpy.pause(1.5, hard=True)
    "Mis ojos se posan hacia el asiento de atrás de ella. Dándome cuenta que..."
    show jeremy 2incomodo with Dissolve(0.5):
        flip
        right5
    l_thought "Eh... ¿Q-Quién es este?"
    l_thought "¿Ese asiento no estaba vacío ayer?"
    show dark 1distraido2 with Dissolve(0.5):
        left
    "Al lado de Dark y detrás de Blaze, está un chico con un aspecto algo... desaliñado.{w} Por decirlo de forma bonita."

    if (rutaCanon-rutaSuicida)<=-1:
        l_thought "Otro testigo más de mi decadencia. Otro par de ojos que verán cómo me desmorono."
    
    "Entre cierro los ojos, tratando de entender quien es."
    $ renpy.pause(1.5, hard=True)
    l_thought "Por qué..."
    extend " ¿Por qué tiene la manga de su sudadera en su camisa?"
    l_thought "Genuinamente, a este NUNCA lo he visto por aquí."
    l_thought "O bueno... Puede ser que tampoco le preste mucha atención."
    l_thought "Como sea. Ahora estoy conociendo a extraños.{w} Justo lo que necesitaba para el inicio de esta semana de mierda."
    show jeremy 1juzga 
    "El chico desaliñado voltea hacia mí sintiendo su mirada. Sus ojos me examinan con la misma curiosidad con que yo lo examino a él."
    show dark 1metiche
    "Dark, desde su asiento, al parecer notó mi mirada curiosa por el chico, sonríe como un gato que ve jugar a dos ratones."

    if (rutaCanon-rutaSuicida)>=0:
        show dark 1desafiantet
        $ enfocar("dark")
        d "¿Y bueno, Blaze?"
        show jeremy 1serio
        show blaze 1enojada
        extend " ¿No nos vas a presentar a tu nuevo novio?"
        show dark 1desafiante
        $ normal("dark")
        "El random y Blaze lo fulminan con la mirada.{w} A Dark solo se le ve disfrutando la situación."
        show blaze 1seria2t
        $ enfocar("blaze")
        b "Jaja, muy gracioso..."
        show blaze 1seria2
        $ normal("blaze")
    else:
        show dark 1desafiantet
        $ enfocar("dark")
        d "¿Y bueno, Blaze?"
        show jeremy 1serio
        show blaze 1enojada
        extend " ¿No nos vas a presentar a tu nuevo enfermero emocional?"
        show dark 1desafiante
        $ normal("dark")
        show blaze 1enojada2t
        $ enfocar("blaze")
        b "¡Dark, basta!"
        show blaze 1enojada2
        $ normal("blaze")
        show jeremy 1incomodot
        $ enfocar("jeremy")
        idk1 "Tu humor negro es tan predecible como tu falta de empatía."
        show jeremy 1incomodo
        $ normal("jeremy")

    l_thought "Puede ser que este sea “Jeremy”... Blaze lo mencionó en el camino."
    show jeremy 1incomodot
    $ enfocar("jeremy")
    idk1 "Vaya que tu sabes como anime el día, eh."
    show jeremy 2seriot
    show dark 2desafiante
    idk1 "Creeme que tú necesidad de atención es patética, Dark."
    show jeremy 2serio
    $ normal("jeremy")
    l_thought "¿...?"
    $ renpy.pause(2.9, hard=True)
    show jeremy 1juzgat
    $ enfocar("jeremy")
    idk1 "Y, bro, literalmente me conoces desde hace años, cabron."
    show jeremy 1juzga
    $ normal("jeremy")

    if (rutaCanon-rutaSuicida)>=0:
        "Blaze acomoda su voz antes de hablar."
        show blaze 1seriat
        $ enfocar("blaze")
        b "Y no solamente eres tú quien dice que somos pareja."
        b "Ya nos cansa eso..."
        show blaze 3desinteresada2t
        extend " TV, Strike, Manu..."
        show blaze 3desinteresada2
        $ normal("blaze")
        l_thought "Supongo que TV es Steve... Pero...{w} ¿Manu?"
        show dark 1desafiantet
        $ enfocar("dark")
        d "Piensalo mejor. Y eso ni es un cuarto de la secundaria."
        show dark 1desafiante
        $ normal("dark")
        show blaze 3juzga
        show jeremy 1juzga
        "Los dos miran extrañados a Dark, en busca de respuestas ante ese comentario."
        show jeremy 1juzgat
        $ enfocar("jeremy")
        idk1 "No es mi problema si la gente no tiene nada mejor que hacer que inventar cosas."
        show jeremy 1juzga
        $ normal("jeremy")
        l_thought "Vaya. Este... ¿Jeremy? Como sea... Le devuelve el sarcasmo a Dark sin inmutarse.{w} Interesante."

    show blaze 1desinteresada3 at sigh_animation
    "Blaze suspira y se masajea las sienes. Ya agotada por los comentarios de Dark."
    show blaze 1desinteresada2t
    $ enfocar("blaze")
    b "Como sea..."
    b "¿No tenemos cosas más importantes que hacer?"
    show blaze 1desinteresada2
    $ normal("blaze")
    show dark 2desafiantet
    $ enfocar("dark")
    d "Creo que deberías presentarlos, aún no se conocen."
    show dark 2desafiante
    $ normal("dark")
    "Dice mientras me apunta a mi y a Jeremy. Me estoy empezando a sentir un poco incómoda."
    l_thought "Realmente... No quiero estar aquí. En ningún lado la verdad."
    show blaze 1desinteresada2t
    $ enfocar("blaze")
    b "Ya que..."
    b "Laila...{w} él es Jeremy, un amigo que conocí hace tiempo y es el presidente del consejo estudiantil."
    show blaze 1desinteresada2
    $ normal("blaze")
    l_thought "Eh...{w} ¿Él? ¿Con su estilo tan... desaliñado?"
    l_thought "Pues, no soy nadie para criticar, estoy peor. Pero..."
    show blaze 1desinteresada2t
    $ enfocar("blaze")
    b "Y Jeremy, ella es mi hermana adoptiva, Laila."
    show blaze 1desinteresada2
    $ normal("blaze")
    "Asiente brevemente hacia mí. Su mirada me analiza rápida y prácticamente."

    if (rutaCanon-rutaSuicida)>=0:
        show jeremy 1seriot
        $ enfocar("jeremy")
        je "Ya tuve el... Placer de leer sobre ti."
        show jeremy 1serio
        $ normal("jeremy")
        $ renpy.pause(1.8, hard=True)
        show jeremy 1juzga
        l "El sentimiento es mutuo. Aunque yo solo tuve el placer de ver tu...{w} Interesante estilo al vestir."
        l_thought "Bien, Laila.{w} Insulta al presidente del consejo en nuestro primer intercambio de palabras. Eso no va a traer consecuencias en absoluto.{w} Para nada."
        show blaze 1seria
        "Blaze hace una ligera cara además de un ligero codazo. Su cara dice: “¡No me dejes mal!”."
    else:
        show jeremy 1seriot
        $ enfocar("jeremy")
        je "Ya tuve el... Placer de leer sobre ti."
        extend " Tus registros médicos son más interesantes que tu personalidad."
        show jeremy 1serio
        $ normal("jeremy")
        show blaze 3desinteresada2
        l "Al menos yo tengo excusas médicas.{w} ¿Tú naciste así o practicaste para ser tan desagradable?"
        show blaze 3preocupadat
        $ enfocar("blaze")
        b "¡Laila! ¡Jeremy!"
        show blaze 3preocupada
        $ normal("blaze")
        l_thought "Bien. Ahora he conseguido que el presidente del consejo me odie."
        extend " ¿Cuánto tardará en expedientarme como “estudiante problemática”?"
    
    show jeremy 1serio2
    show dark 2incomodot
    $ enfocar("dark")
    d "Vaya. Directo a la yugular, Laila. Interesante, Interesante."
    show dark 2desafiante
    $ normal("dark")
    "Al parecer Jeremy ignora por completo el comentario sobre su ropa y cambia de tema."
    show jeremy 1serio2t
    $ enfocar("jeremy")
    je "Y Blaze... ¿Qué hicieron ayer? Dark no me pasó nada."
    show jeremy 1juzgat
    extend " Y no creo que haya copiado algo."
    show jeremy 1juzga
    $ normal("jeremy")
    show blaze 1desinteresada2t
    $ enfocar("blaze")
    b "Bueno...{w} Pasamos por una mala racha ayer...{w} pero nada tan grave por ahora."
    show blaze 1desinteresada2
    $ normal("blaze")
    show dark 2felit
    $ enfocar("dark")
    d "Una “mala racha” es perder todo en el casino, lo de ustedes fue un espectáculo total."
    show dark 2desafiantet
    show blaze 3nerviosa
    extend " Y eso que yo ni estuve aquí."
    show dark 2desafiante
    $ normal("dark")
    "Siento la punzada de culpar volver como un peso cargado en mi espalda."
    show jeremy 1serio
    "Jeremy mira fijamente a Dark, su desconfianza natural se intensifica."
    show jeremy 1seriot
    $ enfocar("jeremy")
    je "¿Espect-{nw}"
    show jeremy 2surprise
    $ normal("jeremy")
    show dark 2neutral
    show blaze 3nerviosat
    $ enfocar("blaze")
    b "EL PUNTO ES QUE AL MENOS TENEMOS ESTE DÍA PARA PASARLA BIEN."
    show blaze 3nerviosa
    $ normal("blaze")
    show dark 2seriot
    $ enfocar("dark")
    d "Sin gritar, Blaze, no me quiero llevar otro regaño del Director."
    show dark 2serio
    $ normal("dark")
    show jeremy 2serio
    show blaze 2desinteresada2 at sigh_animation
    "Blaze suspira, frustrada."
    show blaze 2desinteresada2t
    $ enfocar("blaze")
    b "Eso fue tu culpa ayer."
    show blaze 2desinteresada2
    show jeremy 2neutral
    $ normal("blaze")
    show dark 2seriot
    $ enfocar("dark")
    d "Creeme que Laila me debe una por eso."
    show dark 2serio
    $ normal("dark")
    l_thought "¿Qué? ¿Le regañaron... por mi culpa?"
    show screen red_effect2
    "Una punzada de culpa se clavó en mi estómago. La tensión se apoderó de mí."
    $ renpy.pause(1.9, hard=True)
    
    if (rutaCanon-rutaSuicida)>=0:
        show dark 1neutral at boo2
        show blaze 2preocupada
        show jeremy 1juzga
        l "¿P-por mi culpa...?"
        nobody "{sc=3}Hasta TUS actos les afectan a los demás.{/sc}"
        nobody "{sc=4}Solo conseguirás que te odie.{/sc}"
        nobody "{sc=5}Como todos en esta escuela.{/sc}{sc=6} Si es que no te odia ya.{/sc}"
        show jeremy 1feliz
        show blaze 2compadecer
        show dark 2distraido2t
        $ enfocar("dark")
        d "Aunque, también fue mi responsabilidad, te deje ir y eso."
        show dark 2distraido2
        $ normal("dark")
        show dark 2desafiante
        show jeremy 1felizt
        $ enfocar("jeremy")
        je "Por fin, asumes la responsabilidad en algo. Te felicito, amigo."
        show jeremy 1feliz
        $ normal("jeremy")
        "Dark solo se ríe de su comentario. Al parecer era un chiste."
        l "..."
        show dark 1neutral
        l "Gracias."
        hide screen red_effect2 with Dissolve(2.5)
        "A pesar de mis pensamientos intrusivos me fuerzo a decir eso. A él se le ve la sorpresa en su cara."
        show dark 1neutralt
        $ enfocar("dark")
        d "Eh..."
        show dark 1distraido2t
        extend " No te acostumbres mucho. Yo debo mantener mi reputación..."
        show dark 1distraido2
        $ normal("dark")
        show jeremy 1juzga2t
        $ enfocar("jeremy")
        je "¿Reputación? ¿Tú?"
        je "¿No nos vas a contar otro chiste?"

    else:
        l "¿P-por mi culpa...?"
        show dark 2seriot
        $ enfocar("dark")
        d "Bueno, técnicamente sí. No voy a disfrazar la verdad. Pero ya no te preocupes ya tengo una advertencia escrita por dejar escapar estudiantes problemáticos."
        show dark 2serio
        show blaze 3neutral
        show jeremy 2surprise
        $ normal("dark")
        stop music
        show screen pulse_black
        l "¿Eso se supone que me debe tranquilizar o como? Para eso no digas ni mierda."
        "Dark solo se ríe, pero esta vez es una risa cortante, casi de desafío."
        show dark 2desafiantet
        $ enfocar("dark")
        d "¿Estás segura de querer sacar los trapos sucios al sol?"
        show dark 2desafiante
        $ normal("dark")
        show jeremy 1seriot
        $ enfocar("jeremy")
        je "Dark, un poco de tacto."
        show jeremy 1serio
        $ normal("jeremy")  
        show dark 2seriot
        $ enfocar("dark")
        d "¿Tacto? Yo solo digo lo que todos piensan. Es una chica problemática, literalmente le cuesta decir un simple “gracias”."
        show dark 2serio
        $ normal("dark")
        l_thought "Ahí está. La verdad sin adornos, como un puñetazo en el estómago. Duele, pero al menos es honesto."
        "Mis nudillos se ponen blancos al apretar los puños. La culpa que sentía se transforma en algo más familiar, más manejable: rabia pura."
        l "¿Y qué quieres? ¿Que me arrodillara y decirte gracias? Ni lo pienses. Ni estando drogada haría esa puta estupidez."
        show dark 2seriot
        $ enfocar("dark")
        d "Gracias a tu espectáculo de ayer, ahora tengo una advertencia por “negligencia estudiantil”. Felicidades."
        show dark 2serio
        $ normal("dark")
        l "¿Y quieres que me disculpe? Si te importara tanto tu maldita reputación, no te acercarías a mí."
        show jeremy 1seriot
        $ enfocar("jeremy")
        je "Tiene un punto. Asociarte con ella es como prender fuego a tu propio expediente académico."
        show jeremy 1serio
        $ normal("jeremy") 
        show blaze 1enojada2t
        $ enfocar("blaze")
        b "¡YA CÁLLENSE!"
        show blaze 1enojada2
        $ normal("blaze")
        "Blaze alzaría la voz, furiosa."
        nobody "{sc=3}Mira cómo se desmorona todo a tu alrededor.{/sc}"
        nobody "{sc=4}Cada palabra tuya aleja a quienes deciden quererte.{/sc}"
        nobody "{sc=5}Sería un acto de misericordia liberarlos de tu presencia.{/sc}"

    scene black
    hide screen pulse_black
    hide screen red_effect2 
    stop music fadeout 5.1
    with Fade(5.0, 10.0, 5.0) 
    jump receso_day2 
    return

    #### RECESO MOMENT ####
label receso_day2:
    "Después de una agonizante hora de clase con la de Literatura..."
    play audio bell
    $ renpy.pause(3.0, hard=True)
    "Por fin sonó la campana del receso."
    scene class3A with dissolve_scene_full2
    show screen pulse_black
    "Todos mis “compañeros” salen apresurados por la puerta.{w} Dejándonos a nosotros 4 en el salón."

    show blaze 1sonriente:
        center2 
    show jeremy 1serio:
        flip
        right5
    show dark 1distraido:
        left    
    with Dissolve(0.5)

    $ renpy.pause(3.0, hard=True)
    "Dark es el primero en levantarse."
    show dark 1desafiantet
    show blaze 1juzga
    show jeremy 1juzga
    $ enfocar("dark")
    d "Bueno, este toque de literatura realmente me agoto."
    show dark 1juzgat
    extend " ¿Quién tiene hambre?"
    show dark 1desafiante
    $ normal("dark")
    play music bgm2
    show jeremy 2seriot
    $ enfocar("jeremy")
    je "Tu drama es... cómo decir...{w} inútil, sí..."
    show jeremy 1felizt
    je "Pero bien, necesito combustible."
    show jeremy 1incomodot
    extend " Mi cerebro se cansa con tanto... “cinismo constante”, como dicen ahora."
    show jeremy 1feliz
    $ normal("jeremy")
    show blaze 1sonrientet
    $ enfocar("blaze")
    show dark 1juzga
    b "Laila, ¿vienes con nosotros?"
    show blaze 1compadecert
    b "Podemos sentarnos en la mesa de atrás del comedor, donde no hay tanta gente."
    show blaze 1compadecer
    $ normal("blaze")
    l_thought "No, no tengo ganas de hacer nada en estos momentos.{w} Ya todo me está sobrellevando."
    l "Vayan...{w} Yo...{w} Luego."
    show blaze 1preocupada
    show dark 2juzga2
    show jeremy 1juzga
    "Logro sacar una voz ronca, apenas audible.{w} Siento cada músculo de mi cuerpo pesado, tanto que ni me puedo mover."
    l_thought "Realmente esta clase me agotó, no tengo nada de energía."
    extend " Realmente solo quiero pegarme aquí y nunca más moverme."
    "El dolor de cabeza empieza a llegar, siento como mareo.{w} Siento como tengo un vacío en el estómago por no haber comido durante días."
    show dark 2juzga2t
    $ enfocar("dark")
    d "Hey, si no te mueves, van a pensar que te pegamos con la literatura."
    show dark 2juzga2
    $ normal("dark")
    "Escucho como Blazes salta de su puesto hacia a mi lado a paso rápido."
    show blaze 1preocupadat at hug2_on
    b "Laila, ¿Estás bien?"
    show blaze 1preocupada
    l_thought "Quiero responder. Quiero decir algo sarcástico sobre la comida de la cafetería o sobre la oferta de Blaze."
    l_thought "Pero hasta eso requiere una energía que no tengo. Mis párpados pesan como losas, cada músculo está hecho de plomo."

    if (rutaCanon-rutaSuicida)>=0:
        show dark 2juzga2t
        $ enfocar("dark")
        d "Mira, si te desmayas de hambre, tendré que cargarte hasta la enfermería."
        show dark 2desafiantet
        extend " Y te aseguro que no es tan romántico como en las películas."
        show dark 2desafiante
        $ normal("dark")  
        show jeremy 1juzgat
        $ enfocar("jeremy")
        je "Supongo que tiene razón. Pero por motivos... incorrectos. El cerebro sin comida... trabaja mal."
        show jeremy 1juzga
        $ normal("jeremy")
    else:
        show dark 1distraido2
        "Dark no dice nada. Simplemente me mira. Como si yo fuera insignificante.{w} {i}Nada.{/i}"
        "Su mirada no es de preocupación, es de desinterés.{w} Como si mi existencia en este estado fuera un inconveniente personal para él."
        show jeremy 1juzgat
        $ enfocar("jeremy")
        je " Por motivos... incorrectos. El cerebro sin comida... trabaja mal."
        show jeremy 1juzga
        $ normal("jeremy")

    show blaze 1preocupadat
    b "Laila, tienes que comer o te desmayarás"
    show blaze 1preocupada
    "El dolor de cabeza persiste.{w} No digo nada.{w} No tengo nada que decir."
    $ renpy.pause(2.0, hard=True)
    show blaze 1preocupada at sigh_animation
    "Escucho a Blaze suspirar, no entiendo porque suspirar. Si es por alivio, estrés o ansiedad."
    $ renpy.pause(3.5, hard=True)
    "Se quedan en silencio. No entiendo que está pasando. Solo siento mi cabeza dar vueltas."
    $ renpy.pause(2.0, hard=True)
    l_thought "No... No quiero que se preocupen por mi.{w} Yo puedo sola.{w} NO soy una niña."
    "Reúno las pocas fuerzas que me quedan y me levanto."
    extend ".. A pesar de no querer hacerlo."
    $ renpy.pause(1.5, hard=True)
    show blaze 1seria
    "Blaze toma mi mochila y saca el desayuno que me había preparado papá."
    show dark 2serio
    show jeremy 2serio
    show blaze 1seriat
    b "Come. Ahora."
    show blaze 1seria
    l_thought "Suena como una orden..."
    l "Blaze, yo...{nw}"
    show blaze 1seriat
    b "{size=50}Nada de “Blaze”. Come.{/size}"
    show blaze 1seria
    "Levanta un poco su voz y me pone la bolsa en mis manos."
    l_thought "Ella nunca alza la voz. Nunca.{w} ¿Qué he hecho? ¿En qué me he convertido para que MI hermana, la que siempre habla en susurros, me grite?"
    "Mis manos tiemblan al tomar la bolsa. La veo abrirse paso entre mis dedos entumecidos."
    show jeremy 2seriot
    $ enfocar("jeremy")
    je "Sí. A veces la autoridad... Es necesaria en casos de emergencia médica."
    show jeremy 2serio
    $ normal("jeremy")
    show blaze 1seriat
    b "No me mires así, Laila. Te conozco."
    show blaze 1compadecert
    b "Sé que si no es una orden, lo vas a dejar ahí hasta que se pudra..."
    show blaze 1preocupadat
    extend " Así que por favor..."
    show blaze 1preocupada

    menu (time=5, timeout='rutasuicida_nochoice2'):
        l_thought "..."

        "Ceder y comer algo.":
            $ rutaCanon += 3
            l_thought "“Por favor”. Esa palabra duele más que la orden. Porque significa que le importa."
            l_thought "Significa que he logrado asustarla de verdad."

        "Rechazar rotundamente.":
            $ rutaSuicida += 3
            l_thought "“Por favor”. ¿En serio? Ni siquiera mis intentos por desaparecer les dan paz."
            l_thought "Soy una carga incluso en mi silencio."
            l_thought "Ella no lo entiende. No es hambre lo que me falta, es la capacidad de tragar algo que no sea una amargura constante."

    if (rutaCanon-rutaSuicida)>=0:
        call rutacanon_choice2
    else:
        call rutasuicida_choice2

    jump receso_day2_afterchoice
    return

label receso_day2_afterchoice:
    show dark 1distraidot
    $ enfocar("dark")
    d "Pero bueno..."
    show dark 1felit
    extend " Esto fue entretenido, ¿pero ya vamos a comer o no?"
    show dark 1felit
    $ normal("dark")


    return