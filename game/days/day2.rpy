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
    "Después de una interminable hora de Literatura —una disección lenta y cruel de textos que nadie pidió analizar—..."
    play audio bell
    $ renpy.pause(3.0, hard=True)
    "La campana del receso sonó como un indulto."
    scene class3A with dissolve_scene_full2
    show screen pulse_black
    "Mis “compañeros” salieron disparados por la puerta, riendo, empujándose.{w} Mientras nosotros cuatro nos quedamos atrás, varados en el salón como restos olvidados."

    show blaze 1sonriente:
        center2 
    show jeremy 1serio:
        flip
        right5
    show dark 1distraido:
        left    
    with Dissolve(0.5)

    $ renpy.pause(3.0, hard=True)
    "Dark es el primero en ponerse de pie, estirándose un poco y por fin habla."
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
    show jeremy 2serio2t
    $ enfocar("jeremy")
    je "Si que eres un dramático."
    show jeremy 1felizt
    je "Pero si tengo hambre. Estar rodeado de idiotas si drena calorías"
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
    l_thought "No, no quiero moverme, no tengo ganas de hablar siquiera en estos momentos.{w} Ya todo me pesa."
    l "Vayan...{w} Yo...{w} Luego."
    show blaze 1preocupada
    show dark 2juzga2
    show jeremy 1juzga
    "Sale una voz rota, casi irreconocible, apenas con aire.{w} Siento cada músculo de mi cuerpo pesado, tanto que ni me puedo mover."
    l_thought "Realmente esta clase me drenó por completo."
    extend " Lo único que pido es quedarme aquí y desaparecer"
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
        "Jeremy no desea decir aglo, no después de mi incómoda presentación hacia el, pero mira por unos segundos el rostro de Blaze, "
        show jeremy 2estres at sigh_animation
        extend ", solo suspiró con desgano y habla."
        show jeremy 1juzgat
        $ enfocar("jeremy")
        je "A ver si te empeñas... no comed, será una mala idea."
        show jeremy 1seriot
        je "Y tu hermana va a pagar parte del resultado y no es bonito ni de lejos."
        show jeremy 1juzga
        $ normal("jeremy")
        show blaze 2desinteresada3
        "Blaze ignora la forma como lo dijo pero toma la intención de ese mismo, ahora tomando la plática."

    show blaze 1preocupadat
    b "Laila, tienes que comer o te desmayarás."
    show blaze 1preocupada
    "Cómo por arte de magia, las palabras de ese Jeremy se cumplen, y empieza a empeorar como me siento."
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
    show jeremy 1incomodo2
    "Jeremy solo se queda en completo silencio cruzando de brazos un poco extrañado al verle a Blaze de esa forma."
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
        call rutacanon_choice2 from _call_rutacanon_choice2
    else:
        call rutasuicida_choice2 from _call_rutasuicida_choice2

    jump receso_day2_afterchoice
    return

label receso_day2_afterchoice:
    show dark 1distraidot
    $ enfocar("dark")
    d "Pero bueno..."
    show dark 1felit
    extend " Esto fue entretenido, ¿pero ya vamos a comer o no?"
    show dark 1feli
    $ normal("dark")
    show jeremy 1serio
    "Jeremy le lanza una mirada bastante inconforme por el comentario de Dark.{w} Y aunque él esté de acuerdo con su comentario, no era un “momento” adecuado para hacer eso."
    show blaze 1desinteresada2t
    $ enfocar("blaze")
    b"Sí, ya vamos..."
    show blaze 2preocupada
    $ normal("blaze")
    "Ella me mira. Preocupada."
    show blaze 2preocupadat
    $ enfocar("blaze")
    b "¿Puedes caminar?"
    show blaze 2preocupada
    $ normal("blaze")
    "Asiento. Evitando su mirada."
    l "D-Dame un momento."

    if (rutaCanon-rutaSuicida)>=0:
        "El panqueque se siente como una roca en mi estómago. Siento como mi pecho se aprieta."
        l_thought "Ellos piensan que me ayudaron.{w} No entienden que solo agregué “decepcionarlos” a mi lista interminable."
        show screen red_effect2
        nobody "{sc=4}Mira todo ese esfuerzo que hacen por ti.{/sc}"
        nobody "{sc=}Tu padre cocinando hasta tarde.{/sc}"
        nobody "{sc=6}Blaze rogándote...{/sc}"
        nobody "{sc=4}¿Cuándo dejarás de decepcionarlos tan seguido?{/sc}"
        "Tengo ganas de vomitar.{w} Más por lo que yo misma me digo.{w} Pero me aguanto.{w} Me aguanto para no decepcionar más a Blaze."
        hide screen red_effect2 with Dissolve(0.5)
        $ renpy.pause(2.5, hard=True)
    else:
        l_thought "Ellos piensan que me ayudaron.{w} No entienden que solo agregaron “decepcionarlos” a la lista de cosas por las que sentirme culpable."
        show screen red_effect2
        nobody "{sc=4}¿Por qué?{/sc}"
        nobody "{sc=4}¿Porque duele escuchar la verdad?{/sc}"
        nobody "{sc=6}Ellos estarían mejor sin ti.{/sc}"
        nobody "{sc=4}Blaze no tendría que ser tu guardiana.{/sc}"
        nobody "{sc=4}Tu padre no cocinaría para una hija fantasma.{/sc}"
        nobody "{sc=4}Dark no perdería su tiempo.{/sc}"
        nobody "{sc=4}Hasta ese Jeremy pragmático lo ve:{/sc}"
        nobody "{sc=6}Eres un problema que consume recursos.{/sc}"
        nobody "{sc=6}Un mal cálculo.{/sc}"
        nobody "{sc=6}Un error.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
        $ renpy.pause(2.5, hard=True)
        
    "Suspiro. Me levanto con las pocas fuerzas que logré recuperar.{w} Tomo mis cosas y simplemente le doy un asentimiento débil a Blaze, para ir con Dark y Jeremy."
    "Empezamos a caminar hacia los pasillos. Blaze va a mi lado, con su mano tomada con la mía."
    show blaze 2compadecert
    $ enfocar("blaze")
    b "Solo hasta la cafetería. Nada más."
    show blaze 2compadecer
    $ normal("blaze")

    if (rutaCanon-rutaSuicida)>=0:
        "Siento como aprieta mi mano con suavidad."
    else: 
        "Siento como su mano se siente tensa alrededor de la mía.{w} Como si estuviera sosteniendo algo frágil."

    "Salimos."
    play sound closet_open
    $ renpy.pause(1.5, hard=True)
    scene black with fade 
    $ renpy.pause(1.0, hard=True)
    scene pasillo
    show blaze 1seria2:
        flip
        right5
    show jeremy 2serio2:
        center2
    show dark 1distraido:
        left    
    with dissolve
    $ renpy.pause(1.5, hard=True)
    play sound closet_close
    "Jeremy saca varias llaves."
    play sound keylock
    $ renpy.pause(3.0, hard=True)
    show jeremy 2serio2 at boo2
    "Cierra el salón."
    $ renpy.pause(1.5, hard=True)
    scene pasillo_walking
    show blaze 1seria2:
        flip
        right5
        walking_a_normal
    show jeremy 2serio2:
        center2
        walking_b_normal
    show dark 1distraido:
        left    
        walking_c_normal
    $ renpy.pause(2.5, hard=True)
    "Y empezamos a caminar hacia la cafetería."
    $ renpy.pause(7.5, hard=True)

    if (rutaCanon-rutaSuicida)>=0:
        show blaze 1juzga at walking_a_normal
        show jeremy 1juzga at walking_b_normal
        show dark 2desafiantet at walking_c_activo
        d "Laila, si te caes, te juro que te dejo ahí."
        show dark 2neutral at walking_c_normal
        show blaze 1enojada2 at walking_a_normal
        $ renpy.pause(2.5, hard=True)
        show blaze 1feliz at walking_a_normal
        show jeremy 1juzga2 at walking_b_normal
        show dark 2distraidot at walking_c_activo
        d "Mentira, Blaze me mataría."
        show dark 2felit at walking_c_activo
        extend " Pero me quejaré mucho."
        show dark 2desafiante at walking_c_normal
        show blaze 1juzga2 at walking_a_normal
        show jeremy 1juzga2t at walking_b_activo
        je "Dark, felicidades, si tú ser doctor, tu paciente moriría solo con mirarte."
        show jeremy 1juzga2 at walking_b_normal
        show dark 2desafiantet at walking_c_activo
        d "Me gustan los halagos, gracias."
        show dark 2desafiante at walking_c_normal
    else: 
        show blaze 1juzga at walking_a_normal
        show jeremy 1juzga at walking_b_normal
        show dark 2seriot at walking_c_activo
        d "Si ella se desploma y tu Blaze sabes contar,{nw}"
        show jeremy 1serio at walking_b_normal
        extend " no cuentes conmigo."
        show dark 2serio at walking_c_normal
        show blaze 1enojada2t at walking_a_activo
        b "¿En serio no puedes guardar esos comentarios?"
        show blaze 1enojada2 at walking_a_normal
        show dark 2seriot at walking_c_activo
        d "¿Para qué? Ella misma lo ha dejado claro."
        show dark 2distraido2t at walking_c_activo
        d "Prefiere pudrirse antes que aceptar que alguien se preocupe."
        show dark 2distraido2 at walking_c_normal
        l "Exacto.{w} Así que ahórrate la falsa preocupación y preocúpate por tu propia vida."

    show blaze 1seria2:
        walking_a_normal
    show jeremy 2serio2:
        walking_b_normal
    show dark 1distraido:
        walking_c_normal
    $ renpy.pause(5.5, hard=True)

    "Cada paso hacia la cafetería se siente como caminar a través de cemento fresco."

    if (rutaCanon-rutaSuicida)>=0:
        "Pero el peso del panqueque en mi estómago, aunque incómodo, es un recordatorio tangible de que alguien se preocupó lo suficiente como para obligarte a vivir un momento más."

    if (rutaCanon-rutaSuicida)>=0:
        show screen red_effect2
        nobody "{sc=4}Un momento más de miseria.{/sc}"
        nobody "{sc=4}Un respiro temporal en tu inevitable fracaso.{/sc}"
        nobody "{sc=6}¿Realmente crees que esto cambia algo?{/sc}"
        l_thought "No.{w} Pero por ahora, el dolor en mi garganta es un sentimiento más sencillo.{w} Y eso ya es suficiente."
        hide screen red_effect2 with Dissolve(0.5)
    else:
        l_thought "Cada paso es un recordatorio..."
        extend " Que ocupo un espacio que no merezco.{w} Respiro un aire que debería ser para alguien más."
        nobody "{sc=4}Ellos lo saben.{/sc}"
        nobody "{sc=4}Por eso Dark evita hacer algo por ti.{/sc}"
        nobody "{sc=4}Por eso Blaze te vigila como a un animal herido.{/sc}"
        nobody "{sc=6}Eres su lástima, no su hermana.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)

    $ renpy.pause(2.5, hard=True)
    "Tomo aire y suspiro.{w} Tratando de alejar el ruido de mi mente y prestar atención a mi alrededor.{w} Solo para distraerme."
    show jeremy 1juzga2t at walking_b_activo
    show dark 2juzga2
    show blaze 1neutral
    je "Perfecto, Dark, felicitarte... {nw}"
    window show
    show jeremy 2serio3 
    $ renpy.pause(1.0, hard=True)
    show dark 2desafiante
    show jeremy 1juzga2t
    extend " debo!"
    show jeremy 1felizt
    je "Terminaste todas mis responsabilidades en un día."
    show dark 2serio
    show jeremy 1juzga2t
    extend " ¿Qué tan poco tenías que hacer?"
    show jeremy 1juzga2 at walking_b_normal
    show dark 2distraidot at walking_c_activo
    d "Ni tanto, no quería estar en clases. Nada más que eso."
    show dark 2desafiantet
    extend " Allí vi la oportunidad."
    show dark 2desafiante at walking_c_normal
    show jeremy 1juzga2t at walking_b_activo
    je "Saltas de una responsabilidad a otra."
    show jeremy 1sonriente2t
    show blaze 1juzga2
    extend " ¿Quién te entiende, Dark?"
    show jeremy 1juzga at walking_b_normal
    show dark 2felit at walking_c_activo
    d "Pero el Sr. Presidente no estuvo aquí para cumplir sus responsabilidades."
    show dark 2desafiante at walking_c_normal
    show blaze 1neutral
    show jeremy 1juzgat at walking_b_activo
    je "¿Qué dices?"
    show jeremy 1juzga at walking_b_normal
    show dark 1metiche
    "Dark pone una risa burlona."
    show dark 1felit at walking_c_activo
    d "Oh, nada."
    show blaze 3desinteresada2
    show dark 2juzgat
    extend " Solo sugiero que un presidente ausente no tiene moral para criticar mis métodos de gestión."
    show dark 2juzga at walking_c_normal
    "Jeremy levanta una ceja, dudando de esos “métodos” improvisados para realizar tareas."
    show blaze 3desinteresada2t at walking_a_activo
    b "¿Pueden dejar de medir las responsabilidades por un segundo?"
    show blaze 1sonrientet
    extend " Ambos son buenos y ya."
    show blaze 1sonriente at walking_a_normal
    show dark 1distraidot
    d "De todas formas..."
    show dark 1distraido
    stop music fadeout 1.8
    scene black with fade 
    $ renpy.pause(1.0, hard=True)
    scene pasillo2 
    show blaze 1seria2:
        flip
        right5
    show jeremy 2serio2:
        center2
    show dark 1distraido:
        left   
    with dissolve 
    $ renpy.pause(2.5, hard=True)
    "Todos nos quedamos en silencio. Nadie dice nada. solo caminamos."
    $ renpy.pause(7.8, hard=True)
    idk1 "{size=18}¡Jeremy!{/size}"
    $ renpy.pause(2.5, hard=True)
    "Se escucha que alguien grita el nombre de Jeremy."
    l_thought "¿Eh?"
    $ renpy.pause(2.5, hard=True)
    idk1 "¡Jeeeeeeeeeeeereeeeeeeemyyyyyyyyy!"
    show dark 2juzga2
    show jeremy 1juzga
    show blaze 1juzga
    "Blaze, Jeremy y Dark se detienen y voltean a ver quien es."
    $ enfocar("jeremy")
    je "¿...?"
    show jeremy 1juzgat
    je "¿Manuel?"
    show jeremy 1juzga
    $ normal("jeremy")
    $ renpy.pause(0.5, hard=True)
    
    show dark 2juzga2 at slide_left_slight
    show jeremy 1juzga at slide_center_slight
    show blaze 1juzga at slide_right_slight
    show mani 2feliz:
        flip
        slide_in_right_fast
        jadeo_normal
    $ renpy.pause(1.0, hard=True)
    play music bgm9 
    show mani 2felizt:
        right6
        jadeo_activo 
    ma1 "¡Jeremy! ¡Por fin...!{nw=1.0}"
    show mani 1cansado
    $ renpy.pause(1.0, hard=True)
    show mani 2felizt
    extend " Te he buscado...{nw=1.0}"
    show dark 2enojao
    show blaze 3desinteresada2
    show mani 1cansado
    $ renpy.pause(1.0, hard=True)
    show mani 2felizt
    extend " Por toda la maldita escuela...!"
    show mani 1cansado:
        jadeo_normal
    "El chico apoyándose en sus rodillas, sin aliento, habla entrecortado.{w} Pareciera que hubiera corrido un maratón."
    show jeremy 2serio2t
    $ enfocar("jeremy")
    je "Claro..."
    show jeremy 2juzgat
    extend " ¿Qué es ahora, Manuel?"
    show jeremy 1juzgat
    extend " ¿Otra falta que tengo que firmar, o querer hacerme perder el tiempo correr?"
    show jeremy 1juzga
    $ normal("jeremy")
    show dark 2seriot
    $ enfocar ("dark")
    d "Excelente."
    show dark 2serio2t
    extend " ¿Ya no podemos ir a comer? ¿Siempre nos van a interrumpir?"
    show dark 2enojao
    $ normal ("dark")
    $ enfocar ("blaze")
    show blaze 3desinteresada2t
    b "Hola, Manu..."
    show blaze 3desinteresada2
    $ normal ("blaze")
    if (rutaCanon-rutaSuicida)>=0:
        "Siento como su mano se tensa levemente alrededor de la mía."

    l_thought "¿Y este quién demonios es? Parece un maldito golden retriever al borde de un ataque de nervios."
    l_thought "La energía que desprende es...{w} Agotadora..."
    $ renpy.pause(2.5, hard=True)
    show mani 2feliz:
        jadeo_off
    "El random logra enderezarse después de su maratón.{w} Y señala a Jeremy."
    show mani 2felizt
    $ enfocar ("mani")
    ma2 "IDEAS. Tengo unas ideas. ¡Se me olvido comentarlas antes que faltaras ayer!"
    show mani 2feliz
    $ normal ("mani")
    show jeremy 2serio
    "Jeremy entrecierra los ojos. Parece que intenta analizar acertar que podría decir Manu considerando “ideas”."
    $ enfocar("jeremy")
    show jeremy 2seriot
    je "Ok..."
    show jeremy 1juzgat
    show mani 1desanimado
    extend " ¿Y se te ocurrió contar ahora en vez del viernes?"
    show jeremy 1juzga
    $ normal("jeremy")
    show mani 1desanimadot
    $ enfocar ("mani")
    ma2 "Es que...{w} pasó una cosa, luego otra, y luego un pájaro chocó con la ventana de la biblioteca y fui a ver si estaba bien, y..."
    show mani 1desanimado
    $ normal("mani")
    l_thought "Parece un podcast con pausas incómodas hecho persona."
    show dark 2seriot
    $ enfocar ("dark")
    d "Mani. Al punto. Ahora."
    show dark 2distraidot
    extend " No estamos para escuchar tus estúpidas historias."
    show dark 2serio
    $ normal("dark")
    show mani 3neutralt
    $ enfocar ("mani")
    ma "¡Ah, cierto!"
    show mani 2felizt
    ma "Bueno, la primera idea es buenísima, les va a encantar."
    show mani 2feliz
    $ normal("mani")
    l_thought "Creo que este es el chico...{w} ¿Mani? del que hablaban ayer en la azotea..."
    show dark 2juzga2
    show jeremy 1juzga
    show blaze 1juzga
    "Los tres se miran entre sí. Como prediciendo que estupidez va a decir."
    show jeremy 2serio
    "Aunque Jeremy se le queda viendo más tiempo... Supongo que por algo que dijo..."
    show mani 2felizt
    $ enfocar("mani")
    ma "¿Y si... hacemos clubs en la prepa? ¡Como uno de videojuegos, o de literatura, o de... de cocina!"
    show mani 2neutralt
    extend " ¡A Blaze le encantaría ese!"
    show mani 3neutral
    $ normal("mani")


    if (rutaCanon-rutaSuicida)<=-1:
        l_thought "Clubs. Más actividades. Más ruido. Futuro."
        l_thought "Más razones para fingir normalidad. Como si pudiera importarme un club cuando apenas puedo con el club de mis propios pensamientos."
    
    show blaze 1neutral
    $ renpy.pause(2.5, hard=True)
    "Blaze parpadea. Sorprendida."
    show dark 2distraido
    show blaze 1neutralt
    $ enfocar("blaze")
    b "Oh...{w} vaya, no esperaba esa idea"
    show blaze 1neutral
    $ normal("blaze")
    l_thought "Clubs. Más actividades. Más gente. Más ruido. Suena a mi pesadilla personal. Menos mal no tengo pensado unirme a ninguno."
    show jeremy 2serio2
    "Parece que Jeremy por un lado se queda pensando en todas las posibilidades."
    l_thought "Parece que su mente práctica ya está evaluando..."
    $ renpy.pause(3.5, hard=True)
    show dark 2distraido2
    show blaze 1sonriente
    show jeremy 2seriot
    $ enfocar("jeremy")
    je "Funciona."
    show jeremy 1serio3t
    extend " Tendré que llevarlo a consejo, estatutos, un supervisor docente..."
    show jeremy 1felizt
    extend " Todo eso sí, pero es {i}viable{/i}."
    show jeremy 1feliz
    $ normal("jeremy")
    $ renpy.pause(2.5, hard=True)
    show jeremy 2seriot
    $ enfocar("jeremy")
    je "¿Y tu idea 2? Porque solo mencionaste 1."
    show jeremy 2serio
    $ normal("jeremy")
    show mani 2nervioso
    "Veo como...{w} ¿Manu, Manuel, Mani? Se pone nervioso, empezando a juguetear con sus manos."
    show jeremy 2serio2
    show blaze 3desinteresada3
    show dark 2distraido
    show mani 2nerviosot
    $ enfocar("mani")
    ma "¿Hay una segunda? Habrás escuchado mal...{w} jajajaja..."
    show mani 2nervioso
    $ normal ("mani")
    show jeremy 2serio2t
    $ enfocar("jeremy")
    je "Dijiste “ideas”, en plural."
    show dark 2desafiante
    show jeremy 1juzgat
    extend " Clubs ser la 1. ¿Cuál es la 2?"
    show jeremy 2serio
    $ normal("jeremy")
    show dark 2desafiantet
    show blaze 1juzga
    $ enfocar("dark")
    d "Ah, sí. Una famosa “segunda idea”.{w} No nos la guardes, Manin. Estamos al borde de nuestros asientos."
    show dark 2desafiante
    $ normal("dark")
    show mani 3nervioso3
    "Mani se rasca la nuca apenado y asustado, evitando las miradas de todos. Buscando una forma de salir de este aprieto."
    $ renpy.pause(2.0, hard=True)
    l_thought "Este...{w} Este tipo parece tener la actitud de un niño chiquito.{w} Otro tipo raro para la lista."
    l_thought "Aunque, he notado que Jeremy habla un poco raro.{w} Ya de por sí tiene un aura extraña."
    show mani 3nerviosot
    $ enfocar("mani")
    ma "Je, je... es que{w=0.2}, ¿saben? Ahora que lo pienso, tal vez no era tan buena."
    show mani 3nervioso3t
    ma "Seguro era una tontería. ¡Cómo hacer un club de... de observación de nubes!"
    show mani 3nerviosot at boo2
    extend " ¿Una locura, verdad?"
    show mani 3nervioso
    $ normal("mani")
    show blaze 1juzgat
    $ enfocar("blaze")
    b "Ayer cuando te encontré en el receso, sonaste tan emocionado con ella, Manu."
    show blaze 1juzga2t
    extend " Dijiste que era “la mejor de todas” ¿Y ahora nos dejas en suspenso?"
    show blaze 1juzga2
    $ normal("blaze")
    "Su voz se escucha curiosa. Como si estuviera buscando hacer hablar a Mani."
    l_thought "Esto es como ver a un criminal siendo interrogado con luces en la cara.{w} Patético."
    show mani 3nervioso3
    show jeremy 2seriot
    $ enfocar("jeremy")
    je "Manuel. La idea 2. Ahora."
    show jeremy 2serio2t
    je "No me hagas repetir."
    show jeremy 2serio
    $ normal("jeremy")
    "Mani traga saliva.{w} Sus ojos pasan por todos lados menos por el de nosotros."
    show mani 3nervioso
    "De repente, mira su muñeca izquierda... A donde no hay nada."
    show mani 1nerviosot
    $ enfocar("mani")
    ma "¡Oh, mira la hora! ¡El receso está a punto de acabar!{nw}"
    show mani 3nervioso3t
    extend " Debo... ir a...{nw=0.3}"
    show mani 2nerviosot
    extend " ¡Comprar un lápiz! ¡Uno muy específico!"
    show mani 2nervioso3
    $ normal("mani")
    show dark 2juzgat
    $ enfocar("dark")
    d "¿Qué casualidad, no? Aún queda tiempo de receso..."
    show dark 2desafiantet
    show blaze 1sonriente
    show jeremy 1sonriente
    d "Supongo que sobra el tiempo para que digas al menos una oración."
    show dark 2desafiante
    $ normal("dark")
    $ renpy.pause(0.3, hard=True)
    show dark 2desafiante at slow_slide_left_slight
    "Dark bloquea sutilmente su camino de huida."
    $ renpy.pause(2.0, hard=True)
    "Está sudando frío."
    show jeremy 2serio
    show mani 3nervioso
    extend " Mira a Jeremy, cuya paciencia claramente tiene un límite, y luego a Dark, cuyo disfrute de la situación es evidente."
    show mani 1desanimado
    "Sin más camino por donde huir. Traga saliva."
    $ renpy.pause(0.5, hard=True)
    show mani 3nervioso3t
    $ enfocar("mani")
    ma "{cps=*2}Era-hacer-una-fiesta-en-tu-casa-jeremy-después-del-baile-de-fin-de-curso-pero-ya-sé-que-es-una-mala-idea-y-que-no-quieres-gente-revolviendo-tus-cosas-asi-que-la-descarto-totalmente-y-ya-no-hace-falta-hablar-más-del-tema-adiós!{/cps}"
    show mani 1nervioso3
    $ normal("mani")
    $ renpy.pause(1.5, hard=True)
    show jeremy 2neutral
    show dark 1neutral
    show blaze 1neutral
    "Jeremy parpadea, intentando procesar lo que acaba de escuchar. Parece que sus palabras se le enredan en la mente.{w} Entiende el tono, no el mensaje."
    $ renpy.pause(1.0, hard=True)
    show mani 1nervioso3:
        mani_left
    "Sin esperar respuesta, Manin se da la vuelta y casi trota por el pasillo, desapareciendo en un abrir y cerrar de ojos, dejando un silencio cargado."
    $ renpy.pause(3.1, hard=True)
    show blaze 2neutralt
    $ enfocar("blaze")
    b "¿Qué?"
    show blaze 2neutral
    $ normal("blaze")
    show dark 1juzga2t
    $ enfocar("dark")
    d "¿Una fiesta? ¿En la sagrada morada de nuestro presidente?"
    show dark 1neutralt
    extend " Manin, pero que osadía..."
    show dark 2desafiantet
    d "Me anoto."
    show dark 2desafiante
    $ normal("dark")
    show jeremy 2neutral:
        flip
    "Jeremy lo observa en silencio, al comprender lo que Dark mencionó, rápidamente lo entiende{w} y abre los ojos de par en par."
    show jeremy 1seriot
    $ enfocar("jeremy")
    je "No.{w} Ni de broma."
    show jeremy 1serio:
        flip_off
    $ normal("jeremy")
    $ renpy.pause(2.2, hard=True)
    l_thought "Supongo que es algo que no le parece en absoluto, y que ni siquiera es algo bueno que puedan hacer..."
    show jeremy 1serio2 at sigh_animation
    "Jeremy suspira, cruzando los brazos. Su acento todavía tropieza con algunas palabras, pero su tono no deja dudas."
    show jeremy 1serio2t
    $ enfocar("jeremy")
    je "{size=22}—Fiestas...{w} Siempre terminan mal.{/size}"
    show jeremy 1serio2
    $ normal("jeremy")
    show blaze 1neutral:
        flip_off
    "Jeremy dice eso en voz baja, casi que parece un suspiro."
    show blaze 1neutral:
        sigh_animation
    "Blaze suelta un suspiro{nw=0.8}"
    show blaze 1sonriente
    extend ", pero una sonrisa leve asoma en sus labios"
    show dark 1distraido2
    show blaze 1sonrientet
    $ enfocar("blaze")
    b "Al menos lo de los clubes sí era una idea decente."
    show blaze 2desinteresada2t
    extend " Y... bueno, es Manu."
    show blaze 2desinteresadat
    extend " No se puede esperar menos... Ni más."
    b "Aparte que cada vez que Manu aparece es como si alguien drenara las energías que me quedaban."
    show blaze 2desinteresada2
    $ normal("blaze")
    l_thought "¿En serio? ¿Una fiesta en la puta casa del robot? Eso es lo más estúpido que he escuchado en la semana."
    l_thought "Me pregunto cuánto tardaría en llamar a la policía si alguien se sienta en su sofá sin permiso."
    $ renpy.pause(3.5, hard=True)
    "El silencio que deja la huida de Manuel es casi tangible."
    show jeremy 2serio2
    extend " Jeremy parece estar procesando mentalmente cada palabra."
    show dark 1metiche
    extend " Dark, en cambio, no puede contener una sonrisa de genuino deleite."
    show dark 1felit
    $ enfocar("dark")
    d "Bueno, por esta vez, valió la pena el retraso."
    show dark 1desafiantet
    extend " ¿Una fiesta en la fortaleza de Jeremy? Me apunto como coordinador."
    show dark 1desafiante
    $ normal("dark")
    show jeremy 1serio
    "Jeremy, con la mirada tan seria que podría quemar hasta el sol. Lo mira."
    show jeremy 1seriot
    $ enfocar("jeremy")
    je "No.{w} Ni se te ha de ocurrir."
    
    if (rutaCanon-rutaSuicida)<=-1:
        show jeremy 1serio
        $ normal("jeremy")
        l_thought "Una fiesta en su casa perfecta. Una celebración de todo lo que yo arruinaría con mi sola presencia. Solo mi sombra bastaría para echar a perderla."
        show screen red_effect2
        nobody "{sc=3}Exactamente.{/sc}"
        nobody "{sc=3}Por eso el acto más considerado sería desaparecer antes de eso.{/sc}"
        nobody "{sc=3}Asegúrate de no dejar rastro.{/sc}"
        nobody "{sc=3}Sería tu único regalo real para ellos.{/sc}"


    scene black
    hide screen red_effect2 
    stop music fadeout 5.1
    with Fade(5.0, 10.0, 5.0) 
    jump reunionconsejo_day2
    return

#### REUNION CONSEJO MOMENT ####
label reunionconsejo_day2:

    "Pasaron horas. Horas demasiado agotadoras y aburridas de clases. Nada a destacar. Solamente tratar de entender a un profesor que repite lo mismo 7 veces al día."
    scene class3A at afternoon_filter with dissolve
    $ renpy.pause(3.0, hard=True)
    play audio bell
    $ renpy.pause(3.0, hard=True)
    "Una vez suena la última campana del día, veo como mis “compañeros” empiezan a irse."
    show blaze 1desinteresada3:
        center2 
        afternoon_character
    show jeremy 1serio2:
        flip
        right5
        afternoon_character
    show dark 1distraido:
        left
        afternoon_character
    with Dissolve(0.5)
    extend " Pero veo cómo estos 2 y Blaze se quedan aquí."
    l_thought "..."
    l_thought "¿Por que no se van? ¿Qué esperan? ¿Me juzgan por algo?"
    "Cada uno guarda sus cosas lentamente, dejando que hasta la última alma de aquí se vaya."
    $ renpy.pause(4.0, hard=True)
    "Dark es el primero en levantarse y estirarse."
    play music bgm1 volume 0.75
    show jeremy 2juzga
    show blaze 3neutral
    show dark 1desafiantet
    $ enfocar("dark")
    d "Creo que estar en un campo de guerra es más productivo que estar por aquí."
    show jeremy 1serio
    show blaze 2desinteresada2
    show dark 2desafiantet
    extend " Con ustedes."
    show dark 2desafiante
    $ normal("dark")
    show blaze 2desinteresada
    show jeremy 1seriot
    $ enfocar("jeremy")
    je "Tan...{w} Tan buen amigo, como siempre."
    show jeremy 1serio
    $ normal("jeremy")
    "Jeremy y Blaze también se levantan. Y se ajustan sus mochilas."
    show blaze 1juzgat
    $ enfocar("blaze")
    b "¿Y qué les toca hacer hoy? ¿Por qué se tienen que quedar?"
    show blaze 1juzga
    $ normal("blaze")
    "Me quedo en blanco."
    l_thought "N-No entiendo. ¿Qué está pasando?"
    show dark 1neutral
    show jeremy 2neutral
    l "Eh... Blaze"
    show blaze 1neutral
    extend " ¿También te vas a quedar?"
    show dark 2desafiantet
    $ enfocar("dark")
    d "Pregunta filosófica del día, Laila:"
    show dark 2juzgat
    d "¿Qué hacen tres personas con horarios y responsabilidades similares y que están en el consejo, decidan quedarse después de la escuela?"
    show dark 2desafiante
    $ normal("dark")
    "Lo dice con una sonrisa enigmática."
    l_thought "Ah... Creo que Blaze se tenía que quedar a ayudarlos en cosas del consejo..."
    show blaze 1compadecer
    l "Cierto que te tienes que quedar Blaze. No lo recordaba."
    show blaze 1compadecert
    $ enfocar("blaze")
    b "Sí..."
    show blaze 1juzga2t
    show jeremy 1neutral
    b "A estás alturas, me debería convertir en secretaria del consejo. Últimamente me han estado pidiendo mucha ayuda."
    show blaze 1juzga2
    $ normal("blaze")
    "Ella lo dice con obviamente tono de broma, pero como que Jeremy no lo entiende. O eso observo en su expresión."
    show jeremy 1juzgat
    $ enfocar("jeremy")
    je "Siendo honesto, no... mala idea como parecer. Tal vez considere que te conviertan en la secretaría."
    show dark 2juzga
    show jeremy 1juzga
    $ normal("jeremy")
    show blaze 2nerviosa
    "Blaze se sonroja, pero no se le ven ganas de reprochar."
    show dark 2juzgat
    $ enfocar("dark")
    d "Y así, es como cualquiera entra a un gobierno corrupto. ¿Anotaste, Laila?"
    show dark 2juzga
    $ normal("dark")
    l "Prefiero mantener mis crímenes en el sector privado, gracias."
    l_thought "Al menos el sarcasmo sigue siendo un refugio seguro."
    "Me levanto, sintiendo el peso de un día entero en cada hueso."
    $ renpy.pause(3.0, hard=True)
    show blaze 2preocupada
    "Blaze me mira con esa expresión de preocupación."
    show blaze 2compadecert
    $ enfocar("blaze")
    b "Y... Laila...{w} ¿Al final irás con papá?"
    show blaze 2compadecer
    $ normal("blaze")
    show dark 1neutral
    show jeremy 1neutral
    l_thought "Ya suponía  que iba a preguntar eso...{w} El elefante en la habitación."
    l "Bueno... Ya debería estar en camino para aca.{w} Eso creo."
    "Le digo eso esquivando su mirada mientras guardo mis últimos útiles."
    show dark 2desafiante
    "Dark se inclina contra un pupitre, observándonos como si fuéramos su telenovela personal."
    show dark 2juzgat
    $ enfocar("dark")
    d "Vaya, un drama familiar. ¿Apuestan a que termine en llanto o en portazo?"
    show dark 2juzga
    $ normal("dark")
    show blaze 2desinteresada2
    show jeremy 1seriot
    $ enfocar("jeremy")
    je "Dark, por una vez. Silencio."
    show jeremy 1serio
    $ normal("jeremy")
    show blaze 2desinteresadat
    $ enfocar("blaze")
    b "Sí, Dark...{w} Cállate."
    show blaze 2desinteresada2
    $ normal("blaze")
    show dark 2juzgat
    $ enfocar("dark")
    d "Pero no se molesten..."
    show dark 1felit
    d "Amor y paz."
    show dark 1desafiante
    $ normal("dark")
    "Aun así, lo dice con su tono burlón. Que siempre me irrita."
    l_thought "Ese fastidioso tono de diversión... como si mi tormento existencial fuera su entretenimiento personal."
    l_thought "Pero hoy, incluso su cinismo se siente preferible al silencio que me espera afuera."
    "Termino de guardar mis cosas con movimientos lentos, deliberados.{w} Cada segundo extra en este salón es un segundo menos de esa conversación inevitable."
    $ renpy.pause(2.5, hard=True)
    l "..."
    l "Blaze, le enviare un mensaje, me parece raro que no haya llamado, ya es el horario de la salida."
    show blaze 2preocupada
    "Blaze me mira preocupada, como si tuviera miedo de algo, o bueno, de su {i}trabajo{/i}."
    show blaze 2compadecert
    $ enfocar("blaze")
    b "Me parece bien, tienes razón, siempre está atento a esas cosas. Y más si va a salir con alguna de nosotras."
    show blaze 2compadecer
    $ normal("blaze")
    "Eso lo dice con su tono reconfortante de siempre."
    l_thought "Bueno... Ya era hora de usar el celular para algo bueno, en cierto modo, nunca lo uso."
    "Saco mi celular y abro la app de mensajes, mis dedos tiemblan, trago saliva, pero es necesario."
    $ renpy.pause(1.5, hard=True)

    call chat_dad_day2 from _call_chat_dad_day2

    l_thought "Pensé que sentiría alivio al no salir... Y hablar sobre cosas que no quiero. Pero no, me siento extraña."
    l "No viene."
    l_thought "¿Y qué más da? Al final, todos se cansan de mí."

    if (rutaCanon-rutaSuicida)>=0:
        "Mi voz sale densa. casi afilada. No buscaba sonar así."
        show dark 2distraidot
        $ enfocar("dark")
        d "Vaya..."
        show dark 1felit
        d "Esperaba un “¡Bien!” o un “¡Mierda!”"
        show dark 2desafiantet
        extend " Pero supongo que “nada” también cuenta."
        show dark 1distraido2
        $ normal("dark")

    else:
        "Mi voz suena cortante, pero firme."
        show screen red_effect2
        nobody "{sc=3}Exacto.{/sc}"
        nobody "{sc=3}Hoy fue él, mañana será Blaze.{/sc}"
        nobody "{sc=3}Pasado mañana hasta ese idiota de Dark.{/sc}"
        nobody "{sc=3}Aquí No se trata de un “si”...{/sc}"
        nobody "{sc=5}Sino de un “cuando”.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
        l_thought "Maldita sea, cállate por una puta buena vez."
        l_thought "Sólo...{w} Cállate"
        show dark 2distraidot
        $ enfocar("dark")
        d "Vaya. Esperaba algo más {i}dramático{/i} de parte tuya, pero el vacío también cuenta."
        show dark 1distraido2
        $ normal("dark")

    "Blaze se acerca y me pone la mano en el hombro."
    show blaze 2preocupadat
    $ enfocar("blaze")
    b "¿Estás... bien? Sé que querías evitarlo, pero...{nw=0.1}"
    show blaze 2preocupada
    $ normal("blaze")
    l "Estoy perfecta. Menos drama para hoy."

    if (rutaCanon-rutaSuicida)<=-1: 
        show screen red_effect2
        nobody "{sc=5}“Perfecta”.{/sc}"
        nobody "{sc=3}Qué palabra tan vacía para describir este vacío.{/sc}"
        nobody "{sc=3}Pero sigue mintiendo, es lo único que se te da bien.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)

    "Mi voz sale cortante, pero firme."
    l_thought "Mentira. ¿Por qué carajos me importa? ¿De verdad quería que viniera?"

    if (rutaCanon-rutaSuicida)<=-1: 
        show screen red_effect2
        nobody "{sc=3}Porque en el fondo...{/sc}"
        nobody "{sc=3}Todavía eres esa niña estúpida que cree que si se porta bien.{/sc}"
        nobody "{sc=5}Papá vendrá a salvarla.{/sc}"
        nobody "{sc=6}Despierta.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)

    show jeremy 1juzga
    "Jeremy solo levantaba la ceja, como si hubiera estado esperando su turno para hablar"
    show jeremy 2juzgat
    $ enfocar("jeremy")
    je "Vaya casualidad...{w} Ya que tienes extra tiempo..."
    show jeremy 1seriot
    je "Tu reporte necesita firma del consejo. Podéis a...{nw=0.2}"
    window show
    show jeremy 2serio3 
    $ renpy.pause(1.5, hard=True)
    show jeremy 1seriot
    extend " Avanzar si ponéis pilas."
    show jeremy 1serio
    $ normal("jeremy")
    l_thought "Fantástico. Cambiamos de una tortura por otra. Al menos esto finge ser productivo."
    show dark 2juzga2 at shake
    "Dark solo ladea la cabeza no muy convencido de las palabras de Jeremy."
    show dark 2desafiantet
    $ enfocar("dark")
    d "Es la clásica extorsión administrativa, Laila. Solucionas problemas... Creando mas problemas."
    show dark 1felit
    d "Hermoso, ¿no?"
    show dark 2desafiante
    $ normal("dark")
    l "¿A qué hora cierran esta prisión?"
    show blaze 1compadecert
    $ enfocar("blaze")
    b "Te ayudo. No será tan malo."
    show blaze 1compadecer
    $ normal("blaze")
    l_thought "¿Por qué todo se siente como una trampa? ¿Y por qué sigo cayendo?"
    if (rutaCanon-rutaSuicida)<=-1: 
        show screen red_effect2
        nobody "{sc=3}Porque es lo único para lo que sirves.{/sc}"
        nobody "{sc=3}Para caer. Para fracasar.{/sc}"
        nobody "{sc=3}Para recorrer este camino una y otra vez...{/sc}"
        nobody "{sc=5}Hasta que te rindas por completo.{/sc}"
        "Intento ignorar por completo lo que sea que me acaba de decir y continuo hablando."
        hide screen red_effect2 with Dissolve(0.5)

    l "No me queda de otra...{w} ¿O si?"

    if (rutaCanon-rutaSuicida)>=0:
        show jeremy 1serio2t
        $ enfocar("jeremy")
        je "Si deseáis y {i}encantar{/i} retrasar ese reporte hasta que te boten, entonces sí, tienes otra salida."
        show jeremy 1seriot
        je "Pero si deseáis... Evitar problemas {i}—problemas reales—{/i}, mejor ven ahora y terminamos esto."
        show jeremy 1serio
        $ normal("jeremy")
        "Suspiro, derrotada."
        $ renpy.pause(2.5, hard=True)
        "Asiento. Tomamos nuestras mochilas y empezamos a caminar."
        "Dark se adelanta...{w} Y extiende su brazo como si fuera un mayordomo barato."
        show dark 2desafiantet
        $ enfocar("dark")
        d "¿Su carruaje, señorita Problemática? Acompañémonos al infierno de la burocracia escolar."
        show dark 2desafiante
        $ normal("dark")
        show blaze 1juzga2
        show jeremy 1juzga2
        "Lo dice con evidente tono de burla."
        $ renpy.pause(2.5, hard=True)
        show dark 1desafiante
        "Me limito a mirarlo de arriba a abajo con evidente asco. Y le dejo con el brazo colgando. Poniéndome al lado de Blaze."
        show blaze 1juzga2t
        $ enfocar("blaze")
        b "¿Dark siendo caballeroso?"
        show blaze 1sonrientet
        extend " Esto sí es un milagro..."
        show blaze 1juzga2t
        b "¿También le abrirás la puerta o solo es por el momento?"
        show blaze 1juzga2
        $ normal("blaze")
        "Lo dice con tono de broma, como buscando de irritarlo."
        show dark 2desafiantet
        $ enfocar("dark")
        d "Para ti, Blaze, abriría hasta la puerta del infier-{nw=0.1}"
        show dark 1neutral
        show blaze 1neutral:
            flip
            afternoon_character
        $ normal("dark")
        show jeremy 1serio2t
        $ enfocar("jeremy")
        je "Dark, suficiente. No es momento para eso."
        show jeremy 1serio
        $ normal("jeremy")
        show dark 1metiche at shake
        "Interrumpe la frase de Dark con enojo, dándole un golpe en la cabeza con el fin que se le acomoden las ideas."
        "Lo corta con esa sequedad casi inconfundible, desviando la mirada."
        extend " Dark esboza una sonrisa de satisfacción, al parecer su pequeño plan funcionó."
        show dark 1sarcasmo
        "Guarda sus manos en su bolsillo y alza los hombros con indiferencia. Fingiendo un aire de derrota."
        show dark 1sarcasmot
        $ enfocar("dark")
        d "Lo intenté."
        show dark 2desafiantet
        extend " Luego no digan que la caballerosidad está muerta."
        show dark 2desafiante
        $ normal("dark")

    else:
        show jeremy 1serio2t
        $ enfocar("jeremy")
        je "Si {i}deseáis{/i} retrasar ese reporte hasta la graduación, entonces sí, tenéis otra fácil salida."
        show jeremy 1seriot
        show blaze 2preocupada
        show dark 1distraido
        je "Pero...{w} Estar claro que vosotros no queremos hacer eso a último momento."
        show jeremy 1serio
        $ normal("jeremy")
        "Suspiro, no tengo ni siquiera energía para pelearle."
        $ renpy.pause(2.5, hard=True)
        "Asiento. Tomamos nuestras mochilas y salimos."
        "Dark toma la delantera. No se molestó en mirarme."
        $ enfocar("dark")
        show dark 1distraido2t
        d "Vamos, Problemática."
        show dark 1distraidot
        extend " No tenemos todo el día para tus dramas existenciales."
        show dark 1distraido
        $ normal("dark")
        "Su voz suena distante, como si ya estuviera aburrido de mi presencia."
        l_thought "Ni siquiera se molesta en fingir interés ahora. ¿Por qué lo haría?"
        show screen red_effect2
        nobody "{sc=3}Porque ya te conoce. Sabe que eres un caso perdido.{/sc}"
        nobody "{sc=5}Como todos.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)

    scene black with Dissolve(4.0)
    $ renpy.pause(2.5, hard=True)

    if (rutaCanon-rutaSuicida)>=0:
        "Salimos del aula y empezamos nuestra caminata con ellos 2 peleando mientras intento seguir con mis pensamientos mientras los oigo reír."

    play sound closet_close
    $ renpy.pause(2.5, hard=True)
    "En los pasillos quedan algunos que otros estudiantes.{w} Yo solo me limito a caminar al lado de Blaze y desconectarme."
    $ renpy.pause(7.5, hard=True)
    "Subimos al segundo piso y caminamos hasta el final del pasillo, donde una puerta con el letrero “Salón del Consejo” nos espera.{w} Y curiosamente...{w} Está a ciertos pasos de la sala del director."
    play sound keylock
    "Jeremy saca sus llaves, esas que todo el mundo menciona. Abre la puerta y entramos."
    play sound closet_open
    $ renpy.pause(1.8, hard=True)
    scene consejo_afternoon at afternoon_filter
    show blaze 1sonriente:
        right5
        afternoon_character
    show jeremy 1serio2:
        left
        afternoon_character
    show dark 1distraido:
        center2
        afternoon_character
    with fade
    "Y para sorpresa de nadie, la sala es algo genérica si me lo preguntan, mesas hundidas bajo pilas y pilas de papeles... pizarrones holográficos que parpadea de vez en cuando, carpetas apiladas como si fueran murallas improvisadas y bueno..."
    "Es un caos que de algun modo, les parece funcionar..."
    l_thought "Esto parece el cuarto de limpieza... Pero de una oficina de correos. ¿Es en serio que aquí toman las “decisiones” importantes?"
    show dark 1desafiante at sigh_animation
    "Dark llena sus pulmones como si se tratara de una obra de arte."
    show jeremy 1juzga
    show blaze 1neutral
    show dark 1desafiantet
    $ enfocar("dark")
    d "Ahhh... El olor a papel viejo y el abuso de poder. Dulce segundo hogar."
    show dark 1desafiante
    $ normal("dark")
    show jeremy 2seriot
    $ enfocar("jeremy")
    je "Dios me ampare, Dark... No drama-{w}...{nw=0.2}"
    show jeremy 2serio2
    $ renpy.pause(1.8, hard=True)
    show jeremy 1seriot
    extend " No dramatizad tanto."
    je "Hemos venido a estampar firma de Laila y archivar a su escrito."
    show jeremy 2serio
    $ normal("jeremy")
    l_thought "Expediente... Eso ya debe parecer un caso para llevarme juicio."
    "Blaze me toca el brazo con suavidad y habla con una voz suave para relajar mis nervios que empezaban a sobresalir."
    show blaze 1compadecert
    $ enfocar("blaze")
    b "No te preocupes, es solo papeleo. Una firma y nos vamos."
    show blaze 1compadecer
    $ normal("blaze")
    show dark 2desafiantet
    $ enfocar("dark")
    d "“Solo papeleo”, dice."
    extend " La última vez que firmé “solo papeleo”, terminé como vicepresidente.{w} Cuidado con lo que firmas, Laila."
    show dark 2desafiante
    $ normal("dark")
    show jeremy 1juzga
    "Jeremy levanta una ceja sin entender su “chiste”."
    show jeremy 1juzgat
    $ enfocar("jeremy")
    je "Y bueno... ¿Traer el escrito, Dark?{w} No pienso aguardar todo el día."
    show jeremy 1juzga
    $ normal("jeremy")
    show dark 1distraido2t
    $ enfocar("dark")
    d "Sí, sí. Lo busqué cuando me escapé de clases de Matemáticas."
    show dark 1distraido2
    $ normal("dark")
    show jeremy 2serio2:
        left_littemoveon
    "Rebusca en su bolsillo y saca mi reporte, arrugado como si hubiera sobrevivido a una guerra." 
    "Jeremy busca en un cajón donde al parecer tienen los expedientes de toda la escuela."
    $ renpy.pause(2.8, hard=True)
    "Lo abre, revisa con velocidad sorprendente y murmura:"
    show jeremy 1seriot
    $ enfocar("jeremy")
    je "El expediente de Jackson...{w} Laila Jackson."
    show jeremy 1serio
    $ normal("jeremy")
    show blaze 1preocupada
    "Saca una carpeta {b}GRUESA{/b}, mi nombre completo mira de frente como una acusación silenciosa pero mortal."
    l_thought "Un álbum de todos mis desastres escolares en un solo año."
    show blaze 1preocupadat
    show dark 2juzga2
    $ enfocar("blaze")
    b "Oye... ¿En serio estás bien? No tienes que hacer esto si no quieres. Podemos decir que te sentías mal."
    show blaze 1preocupada
    $ normal("blaze")
    l "Ya estoy aquí. Que más da."

    if (rutaCanon-rutaSuicida)>=0:
        l_thought "Su preocupación debería sentirse bien. Debería ser un alivio..."
        l_thought "Entonces ¿Por qué se siente como otra cadena? ¿Otra persona a la que defraudar?"
    else:
        l_thought "Su preocupación es tan falsa como el interés de Dark. Todos cumplen su papel en esta farsa."
        l_thought "Yo soy la problemática, ella es la compasiva, él es el cínico. Nadie es real."
        show screen red_effect2
        nobody "{sc=3}Y tú cumples el tuyo a la perfección:{/sc}"
        nobody "{sc=3}La chica rota que todos pueden señalar con alivio...{/sc}"
        nobody "{sc=5}“Al menos no soy como ella”.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
    show jeremy 1serio:
        left_littemoveoff

    show dark 2desafiantet
    $ enfocar("dark")
    d "Ah, el eterno drama de los lazos familiares. Que conmovedor. ¿Nunca consideraron cambiar el guión?"
    show dark 2desafiante
    show jeremy 1serio:
        left5
    $ normal("dark")
    show blaze 3desinteresada2
    "Jeremy gira lentamente la cabeza hacia Dark, sus ojos reducidos a finas líneas de desaprobación..."
    "Parecía un búho volteando a su presa...{w} Pero con la diferencia que este búho casi ahorca a su amigo."
    show jeremy 2seriot
    $ enfocar("jeremy")
    je "Tu cinismo...{w} Seguido e inutil, que de verdad me... Preguntar:"
    show jeremy 1juzgat
    extend " ¿Cómo una persona... Encontrad gracia a tus chistes...?{w} Ya te pareceis a cierta persona que conozco."
    show jeremy 1juzga
    $ normal("jeremy")
    "Dark se inclina hacia Jeremy con una sonrisa que no llega a sus ojos."
    show dark 2desafiantet
    $ enfocar("dark")
    d "Para nada, Jas. Solo mantengo el equilibrio natural."
    show dark 1felit
    extend " Alguien tiene que contrarrestar tanta..."
    show dark 1distraidot
    extend " Dulzura que da diabetes."
    show dark 2desafiante
    $ normal("dark")
    show blaze 3desinteresada2 at sigh_animation
    "Blaze suspira, frotándose los párpados con fastidio."
    show blaze 1desinteresada2t
    $ enfocar("blaze")
    b "Dark, ¿podrías guardarte los comentarios por cinco minutos?"
    show blaze 1desinteresada2
    $ normal("blaze")
    show jeremy 1juzga2
    show dark 1distraido2
    l "Por favor, apoyo totalmente lo que dijo."
    show dark 1distraidot
    $ enfocar("dark")
    d "Ok, ok..."
    show dark 1distraido2t
    extend " Le quitan la chispa a lo mejor del grupo."
    show dark 1distraido
    $ normal("dark")
    "Se acerca a Jeremy para entregarle el reporte."
    show jeremy 1juzga2t
    $ enfocar("jeremy")
    je "¿Y ahora pretendes... bufón?"
    show dark 1juzga2
    show jeremy 1felizt
    je "¿Hoy si despertar con ansias de ser?{w} Felicidades, por fin dijiste un chiste con gracia."
    show jeremy 1feliz
    $ normal("jeremy")
    show dark 2desafiantet
    $ enfocar("dark")
    d "Todo es un chiste si tienes el sentido del humor lo suficientemente retorcido."
    show dark 2desafiante
    $ normal("dark")
    show jeremy 2juzga
    "Le pone el reporte en la mesa y le hace un gesto para que lo firme."
    show blaze 1desinteresada2t
    $ enfocar("blaze")
    b "Chicos...{w} ¿Podemos simplemente firmar esto? Realmente no quiero pasar lo que resta de tarde aquí encerrada."
    show blaze 1desinteresada2
    $ normal("blaze")
    l_thought "Vaya. Dark realmente sabe cómo sacar de quicio a Jeremy. Pero Jeremy sabe contrarrestar eso. Que interesante."
    show dark 2desafiantet
    $ enfocar("dark")
    d "Claro, Blaze. Solo estoy asegurándome de que tu querido novio no se tome demasiado en serio."
    show jeremy 1serio
    show blaze 2nerviosa
    show dark 1felit
    d "Alguien tiene que recordarle que sigue siendo humano."
    show dark 1feli
    $ normal("dark")
    "Blaze se sonroja como si le hubieran puesto un foco en la cara."
    show blaze 2nerviosat
    $ enfocar("blaze")
    b "¡Dark! ¿Por qué siempre tienes que decir eso? ¡No es mi novio!"
    show blaze 2nerviosa
    $ normal("blaze")
    "A Jeremy se le ve ligeramente sonrojado, pero evita hacer un espectáculo."
    show jeremy 2serio2t
    $ enfocar("jeremy")
    je " SOLO---{w} Firmad el documento!"
    show jeremy 2serio2
    $ normal("jeremy")
    show dark 2desafiantet
    $ enfocar("dark")
    d "Dos reacciones idénticas. Casi como si estuvieran...{w} Coordinados.{w} O algo más."
    show dark 1felit
    d "Me deberían pagar por labores de cupido."
    show dark 2desafiante
    $ normal("dark")
    show blaze 3desinteresada2

    if (rutaCanon-rutaSuicida)>=0:
        l_thought "Esto es más entretenido que la televisión. Dark juega con ellos como un gato con dos ratones.{w} Y lo más gracioso es que les funciona."
    else:
        l_thought "Más mentiras, más fingimiento. Todos actuando como si no sintieran lo que obviamente sienten."
        show screen red_effect2
        nobody "{sc=3}Como si el amor no fuera otra prisión.{/sc}"
        nobody "{sc=3}Todos encerrados en sus propias mentiras.{/sc}"
        nobody "{sc=5}Igual que tú en tu miseria.{/sc}"
        nobody "{sc=3}Mira cómo se avergüenzan de sus sentimientos...{/sc}"
        nobody "{sc=5}exactamente como tú te avergüenzas de existir.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)

    "Jeremy decide tomar el bolígrafo que encontró sobre la mesa firmando el papel, terminando está situación incómoda."
    show jeremy 1seriot
    $ enfocar("jeremy")
    je "Ya! Andad."
    show jeremy 1serio2
    $ normal("jeremy")
    show blaze 1neutralt
    $ enfocar("blaze")
    b "Laila, firma aquí. Por favor."
    show blaze 1neutral
    $ normal("blaze")
    show dark 1metiche
    "Dark sonríe satisfecho con el juego que hizo entre Jeremy y Blazer, solo poniendo sus manos sobre los bolsillos de su pantalón."
    $ renpy.pause(3.5, hard=True)
    "Firmo el documento con movimientos rápidos.{w} Casi torpes."
    l_thought "Firmo mi sentencia mientras estos tres bailan alrededor de lo obvio.{w} Qué manera más ridícula de pasar la tarde."
    show screen red_effect2
    nobody "{sc=3}Tu vida reducida a una firma en un papel.{/sc}"
    nobody "{sc=3}Como si tu existencia pudiera archivarse y olvidarse tan fácilmente.{/sc}"
    hide screen red_effect2 with Dissolve(0.5)
    show jeremy 1serio at sigh_animation
    "Jeremy una vez mira el reporte firmado suspira, no de cansancio, pero es difícil ver el porqué lo hace."
    show jeremy 1seriot
    $ enfocar("jeremy")
    je "Listo..."
    show jeremy 1serio
    $ normal("jeremy")
    "Guarda el documento en mi expediente. Lo cierra y lo deja sobre la mesa."
    show jeremy 2neutralt
    $ enfocar("jeremy")
    je "Ahora, ya que vosotros estar..."
    show jeremy 2neutral
    $ normal("jeremy")
    show dark 2distraidot
    $ enfocar("dark")
    d "La parte donde el trabajo real comienza..."
    show dark 2distraido
    $ normal("dark")
    $ renpy.pause(1.0, hard=True)
    show dark 1distraido2
    show jeremy 2surprise:
        boo2
    show blaze 1neutral:
        flip
        boo2
    stop music
    play audio slam volume 0.85
    "Jeremy, Blaze y yo damos un brinco del susto por el golpe que hizo la puerta al chocar contra la pared agresivamente." with hpunch
    "Dark por otra parte parecía esperarse que alguien hiciera ello."
    show dark 1neutral:
        slide_center_slight2
    show jeremy 2surprise:
        slide_left_slight2
    show blaze 1neutral:
        slide_right_slight2
    show strike 1distraido:
        flip
        afternoon_character
        slide_in_left_slight2
    show steve 2remedar:
        flip
        afternoon_character
        slide_in_left_slight
    show mani 2felizt:
        flip
        afternoon_character
        slide_in_left_fast2
    ma "¡SABÍA QUE ESTARÍAN AQUÍ!"
    $ enfocar("mani")
    ma "¡Jeremy, tengo una NUEVA IDEA para el baile de la graduación escolar!"
    show mani 2feliz
    $ normal("mani")
    "Mani entra como un tornado, como si no fuera suficiente haberlo visto en el receso."
    "Detrás de él están Strike y Steve. Parecen fastidiados de lo que sea que Mani les haya dicho."
    show dark 1neutral:
        pos_center_slight2
    show jeremy 2surprise:
        pos_left_slight2
    show blaze 1neutral:
        pos_right_slight2
    show strike 1distraido:
        pos_in_left_slight2
    show steve 2remedar:
        pos_in_left_slight
    show mani 2felizt:
        pos_in_left_fast2
    show steve 2remedart
    play music bgm9
    $ enfocar("steve")
    tv "Eh... Hola."
    tv "Mani dijo que... Bueno, que había pizz-{nw=0.2}"
    show steve 1neutral
    $ normal("steve")
    $ renpy.pause(3.0, hard=True)
    show strike 1enojado
    show steve 1neutralt
    $ enfocar("steve")
    tv "Ya veo que no."
    show steve 1neutral
    $ normal("steve")
    show dark 2desafiantet
    $ enfocar("dark")
    d "Que inesperada esta interrupción"
    show dark 2juzgat
    extend " ¿No?"
    show dark 2desafiante
    $ normal("dark")
    show jeremy 2serio2t
    $ enfocar("jeremy")
    je "¿Inesperada? Dire que fue a...{w} abrupto..."
    show jeremy 2serio2
    $ normal("jeremy")
    l "Y yo que pensé que este día no podía ponerse más surreal."

    if (rutaCanon-rutaSuicida)<=-1:
        show screen red_effect2
        nobody "{sc=3}Mira, más gente para presenciar tu decadencia.{/sc}"
        nobody "{sc=3}La audiencia crece.{/sc}"
        nobody "{sc=5}Cada nuevo testigo es otro que recordará tu fracaso.{/sc}"
        nobody "{sc=6}Para cuando finalmente te rindas.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)

    "Me apoyo contra la pared, sintiendo cómo el cansancio se intensifica por ahora tener a las 3 personas más incómodas de la historia..."
    show dark 1desafiantet
    $ enfocar("dark")
    d "Creo que ahora si ya estamos todos aquí. Todo el elenco y tal."
    show dark 1desafiante
    $ normal("dark")
    show jeremy 1estres
    "Jeremy solo gruñe un poco, masajeandose las sienes con más fuerza."
    l_thought "Supongo que no esperaba esta interrupción..."
    show jeremy 1estres2t
    $ enfocar("jeremy")
    je "Manuel, ya os he dicho..."
    show jeremy 1estrest
    extend " El baile de graduación es en tres meses."
    show jeremy 1seriot
    show blaze 3desinteresada
    extend " Y no, no vamos a hacer—"
    show jeremy 2serio2
    $ renpy.pause(1.8, hard=True)
    show jeremy 1seriot
    extend " Temática “superhéroes”."
    show jeremy 1serio
    $ normal("jeremy")
    show mani 2felizt
    $ enfocar("mani")
    ma "¡Pero sería tan genial! Podríamos traer a gente disfrazada de spiderman y–{nw=0.1}"
    show mani 3pinguino
    $ normal("mani")
    show strike 1seriot
    $ enfocar("strike")
    st "Eso puede esperar."
    show strike 1serio
    $ normal("strike")
    show steve 1neutralt
    $ enfocar("steve")
    tv "Oye... ¿Estamos interrumpiendo algo? Porque podemos volver luego..."
    show steve 1neutral
    $ normal("steve")
    show dark 1metiche

    if (rutaCanon-rutaSuicida)>=0:
        "Dark sonríe con genuino deleite ante el caos que se despliega."
        show dark 1felit
        d "Para nada, TV."
        show dark 2desafiantet
        extend " Justo estábamos firmando el famoso reporte de Laila. Y ahora aparecen ustedes con una idea muy estúpida."
        show steve 2amargado
        show dark 2juzgat
        d "¿Qué más podríamos pedir?"
        show dark 2desafiante
        $ normal("dark")
        l "Un terremoto."
        show dark 2juzga
        show blaze 2preocupada
        show jeremy 2juzga
        show strike 1juzga
        extend " O un apagón.{w} O que me trague la tierra."

    else:
        show dark 1felit
        d "Para nada, TV."
        show dark 2distraido2t
        show jeremy 1estres
        show blaze 2desinteresada3
        show steve 2remedar
        extend " Justo estábamos firmando otro maldito reporte de la Problemática. Y ahora aparecen ustedes con una idea muy estúpida."
        show dark 2distraidot
        d "El universo tiene un mal sentido del humor."
        show dark 1distraido
        $ normal("dark")
        $ renpy.pause(3.0, hard=True)
        "Sus palabras resuenan en mi cabeza como martillazos."
        show dark 1distraido2
        l "Cada palabra tuya es un recordatorio de por qué prefiero mi propia compañía."
        show screen red_effect2
        nobody "{sc=5}Mentirosa.{/sc}"
        nobody "{sc=5} Prefieres tu compañía porque es lo único que mereces.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
        show dark 2juzga2t
        show blaze 2preocupada
        $ enfocar("dark")
        d "Mira nada más, ahora tenemos una poeta además de Jeremy..."
        show dark 2juzga2
        $ normal("dark")
        "Solo volteo a verle bastante enojada por su comentario por unos segundos, dándole mirada rápida y volver a lo mio."
        show dark 2juzga
        l_thought "¿Este que se cree?."

    show strike 1distraido
    "Strike solo mira alrededor con desdén"
    show strike 1juzga
    extend ", sus ojos se detienen un momento en mí{nw}"
    show strike 1distraido
    extend " antes de continuar su recorrido por la sala."
    l_thought "Supongo...{w} Supongo que ya se conocen, no es normal que se aparezcan aquí de la nada, realmente..."
    l_thought "Y recuerdo que Steve dijo algo sobre Strike como presidente..."
    show strike 1distraidot
    $ enfocar("strike")
    st "Parece que llegamos justo para la parte aburrida. Papeles y más papeles."
    show strike 1distraido
    $ normal("strike")
    show jeremy 2estrest
    $ enfocar("jeremy")
    je "No... menciones..."
    show jeremy 2estres
    $ normal("jeremy")

    if (rutaCanon-rutaSuicida)>=0:
        "Su voz ya se podía percibir bastante cansada con esto, parecía que el ser presidente estudiantil es “agotador”."
        l_thought "Ni que fuera empleado de un mercado."
        l_thought "Además, ¿Porque carajo le doy importancia a esta... observación?"

    else:
        "Dice esto último irritado, como si “firmar” papeles fuera lo más cansado de la historia."
        l_thought "Yo al menos tengo problemas más grandes que lidiar que solo firmar papelitos."


    "Mani, ignorando por completo la tensión"
    show mani 2feliz:
        boo
        pause 0.2
        slide_of_left_to_center_fast
    pause 0.25
    show jeremy 1serio2
    show dark 1neutral:
        boo2
        flip
        slide_left_move
    show blaze 1neutral:
        boo2
        flip_off
        slide_left_move2
    show steve 1juzga
    show strike 1juzga
    extend ", se acerca saltando a Jeremy."
    show dark 1neutral:
        pos_left_move
    show blaze 1neutral:
        flip_off
        pos_left_move2 
    show mani 2felizt:
        pos_of_left_to_center_fast
    $ enfocar("mani")
    ma "¡Pero Jeremy, escucha!{w} Podríamos tener una batalla de baile entre equipos de superhéroes!"
    show mani 2felizt:
        boo2
    show jeremy 1incomodo2
    extend " ¡Y el premio podría ser... Una pizza gratis!"
    show mani 2feliz
    $ normal("mani")
    show dark 1distraido:
        pos_left_move
    show blaze 3sonriente:
        pos_left_move2
    "Blaze parece dividida entre la exasperación y la risa"
    show jeremy 2estres
    extend ", mientras Jeremy cierra los ojos como si rogara por paciencia de la estupidez que oía."
    show jeremy 1estres2t
    $ enfocar("jeremy")
    je "Manuel."
    show jeremy 1estrest
    extend " Por última vez."
    show jeremy 1seriot
    extend " No. Ya lo dije."
    show jeremy 1serio
    $ normal("jeremy")
    show mani 1triste
    show steve 2remedar
    show blaze 1juzga2
    show strike 1distraido

    if (rutaCanon-rutaSuicida)>=0:

        l_thought "Esto es como un circo de tres pistas.{w} Dark disfrutando del caos, Jeremy al borde de un colapso nervioso, Blaze tratando de mantener la cordura..."
        l_thought "Y yo en medio, firmando mi vida mientras un terremoto humano llamado Mani lo saca todo de proporción. Es casi...{w} Divertido."

    else:
        l_thought "Más ruido. Más caos.{w} Más personas fingiendo normalidad."
        show screen red_effect2
        nobody "{sc=3}Cuantos más testigos...{/sc}"
        nobody "{sc=3}Más grande será el alivio cuando finalmente desaparezcas.{/sc}"
        nobody "{sc=3}Todos estos rostros...{w} Todos estos ojos que algún día recordarán:{/sc}"
        nobody "{sc=5}“Ah, sí, esa chica. Qué bueno que ya no está”.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
        l_thought "¿Por qué todo tiene que ser tan...{w} abrumador?"
    
    show mani 1tristet
    $ enfocar("mani")
    ma "Vamoooossss JeEeEeEeERrRreEeEmMmMmMYyYyY..."
    show mani 1desanimadot
    extend " Aceptaste la solicitud de los clubes."
    show mani 1tristepinguin
    $ normal("mani")
    "Se le acerca demasiado y abre los ojos de más, como si la súplica fuera una amenaza mal disfrazada."
    show dark 2desafiante
    "Dark se recuesta contra la mesa, cruzando los brazos."
    show mani 3juzgapinguin:
        boo2
        pause 0.2
        flip_off
    show dark 2juzgat
    $ enfocar("dark")
    d "Tengo una idea mucho mejor..."
    show steve 1juzga
    show strike 1juzga
    show blaze 1preocupada
    show jeremy 1juzga
    show dark 2felit
    extend " Ayúdanos a escribir ese informe para el director.{w} Ya que tú fuiste el que sugirió la idea de integrar los clubes."
    show dark 2desafiante
    $ normal("dark")
    show dark 2feli
    "Pone una gran sonrisa y se acerca a Mani."
    show dark 1felit
    $ enfocar("dark")
    d "Y así nos ahorras el trabajo a nosotros."
    show mani 2expectante
    show dark 1feli
    $ normal("dark")
    show jeremy 1surpriset
    $ enfocar("jeremy")
    je "¿Hablas en serio? ¿¡Sa... Sabes lo que ocurrió la otra vez por—!?"
    show jeremy 1surprise
    $ normal("jeremy")
    show dark 2desafiante
    show steve 1neutral
    "Dark ignora por completo a Jeremy, siguiendo con la persuasión.{w} Extiende el brazo y pone una mano amistosa en el hombro de Mani, pero su sonrisa tiene ese dejo de picardía."
    show mani 2expectantet
    $ enfocar("mani")
    ma "¿En serio?"
    show mani 2felizt:
        boo2
    ma "¡Sí! ¡Puedo hacerlo! ¡Será el mejor informe de la historia!"
    show mani 2feliz
    $ normal("mani")
    show jeremy 2surprise
    "Jeremy abre los ojos de par en par, claramente horrorizado ante la perspectiva."
    show jeremy 2surpriset
    $ enfocar("jeremy")
    je "Dark, ¿¡Qué coj—{nw=0.2}"
    extend " Rayos te sucede!?"
    show jeremy 1seriot
    extend " Absolutamente no."
    show jeremy 1serio
    $ normal("jeremy")
    show blaze 1juzga
    show strike 1seriot
    $ enfocar("strike")
    st "No. Es la peor idea que has tenido."
    show strike 1serio
    $ normal("strike")
    show steve 1triste2t
    $ enfocar("steve")
    tv "Eh..."
    show steve 2neutralt
    extend " Tal vez no sea mala idea."
    show steve 2remedar2t
    extend " Al menos lo mantendrá ocupado."
    show steve 2rizz
    $ normal("steve")
    show strike 1juzgat
    $ enfocar("strike")
    st "Que quieras mantener a Mani ocupado no hará que vayas a hablar con Laila, Junior."
    show strike 1juzga
    $ normal("strike")
    show steve 1amargadot
    $ enfocar("steve")
    tv "No todo se trata sobre {i}eso{/i}, Struke." 
    show steve 2remedart
    extend " Ya pareces mi vieja."
    show steve 1amargado
    $ normal("steve")
    l_thought ".{w} .{w} .{w}"
    l_thought "Mejor no diré nada al respecto.{w} Creo que solo me queda ignorarlo."
    show jeremy 1serio3
    "Jeremy mira a Dark con algo de desconfianza{nw}"
    show jeremy 1estres:
        sigh_animation
    show dark 2juzga2:
        boo2
        slide_center_to_left_move3
    pause 0.1
    show mani 3juzgapinguin:
        flip
        boo2
        slide_of_left_to_center
    extend " y suspira llevándolo lejos del grupito"
    l_thought "Supongo que hablarán sobre su decisión."
    show mani 3juzgapinguin:
        pos_of_left_to_center
    show jeremy 1seriot
    $ inac("steve")
    $ inac("strike")
    $ inac("mani")
    show dark 2juzga2:
        pos_center_to_left_move3
    $ enfocar("jeremy")
    je "Acabas... condenar esto. ¿¡Sabéis acaso que haces!?"
    show jeremy 1juzgat
    je "¿¡Que tienes en mente con lograr eso!?"
    show jeremy 1serio
    $ normal("jeremy")
    show dark 1felit
    $ enfocar("dark")
    d "Nada."
    show dark 2desafiantet
    extend " Solo...{w} Delegando responsabilidades. Es lo que hacen los buenos líderes, ¿no?"
    show dark 2desafiante
    $ normal("dark")
    show blaze 1desinteresada:
        boo2
        slide_of_center_to_left2
    pause 0.1
    show mani 3juzgapinguin:
        boo2
        slide_of_left_to_center3
    "Blaze se une a la conversación de los 2, y yo sí que soy el mal cuarteto que nadie invito..."
    show steve 2remedar
    show strike 1distraido
    show mani 3juzgapinguin:
        pos_of_left_to_center3
    show blaze 1desinteresadat
    $ enfocar("blaze")
    b "Dark, no uses a Mani como distracción."
    show blaze 2desinteresada3t
    extend " Aunque..."
    show blaze 1juzgat:
        pos_of_center_to_left2
    extend " ¿Deberíamos de preocuparnos por esto?"
    show blaze 1juzga
    $ normal("blaze")
    show dark 2desafiantet
    $ enfocar("dark")
    d "Depende como lo veas, Blaze."
    show dark 2desafiante
    $ normal("dark")
    show strike 1enojado:
        xzoom -1.0
        parallel:
            linear 0.3 yzoom 1.03 xzoom -0.99
            pause 0.2
            linear 0.5 yzoom 1.0 xzoom -1.0 yoffset 0
    "Strike resopla. Mostrando nuevamente su inconformidad con la decisión de Dark."
    l_thought "¿No se arta de quejarse todo el tiempo?"
    show dark 2juzga2:
        flip_off
    show blaze 2desinteresada3:
        flip
    show steve 2remedar2
    $ normal("steve")
    $ normal("mani")
    show strike 1enojadot
    $ enfocar("strike")
    st "Eso es pasarle la bomba a alguien que ni siquiera sabe que está encendida."
    show strike 1enojado
    $ normal("strike")
    show jeremy 2serio2
    show mani 1tristepinguin
    $ renpy.pause(2.5, hard=True)
    show dark 1felit
    $ enfocar("dark")
    d "¡Y eso es lo divertido, Strike!"
    show dark 2juzgat
    extend " ¿Hablas por experiencia?"
    show dark 2desafiantet
    d "¿O Acaso todavía duele que el consejo rechazara tu “rebelión” para expulsar gente?"
    show dark 2desafiante
    $ normal("dark")
    "Dark lo dice sarcástico, pero hay veneno en su voz."
    show strike 1serio at shake
    "Strike ni se inmuta, pero sus dedos se tensan levemente."
    l_thought "¿”Rebelión”?{w} ¿Strike intentó expulsar gente antes?"
    l_thought "..."
    l_thought "Creo escuchar un caso de algún alumno abusando de poder o algo así..."
    extend " No recuerdo y realmente no me importa."
    $ renpy.pause(2.5, hard=True)
    show strike 1sarcasmot
    $ enfocar("strike")
    st "Cuidado con lo que insinuas, Dark... Algunos aprendemos de nuestros errores."

    if (rutaCanon-rutaSuicida)>=0:
        show dark 2serio2
        show strike 1curiosot
        st "Aunque no es bueno guardarse los rencores, ¿sabías?"
        show strike 1serio
        $ normal("strike")
        show dark 1distraido:
            pos_center_to_left_move3
        $ enfocar("dark")
        d "Mhpm."
        $ normal("dark")

    else:
        "Sus ojos se deslizan hacia mi por un instante."
        show strike 1seriot
        st "Otros... siguen tropezando con la misma piedra."
        show strike 1serio
        $ normal("strike")
        l_thought "..."
        extend " Supongo que se refiere a mi..."
        extend " Auch."

    l_thought "E-Eso es extraño..."
    extend " Pensé que se llevarian bien. Al parecer tienen historia."
    $ renpy.pause(2.5, hard=True)
    show jeremy 1incomodo2t
    $ enfocar("jeremy")
    je "Como sea..."
    show jeremy 1incomodo2
    $ normal("jeremy")
    "Jeremy intenta decir algo para quitar la tensión que se formó entre los dos."
    show mani 3pinguino at shake
    "Pero Mani ya está rebuscando en sus bolsillos.{nw=0.9}"
    show mani 2feliz at boo2
    extend " Sacando pedazos de papel arrugado y un lápiz mordisqueado."
    show mani 2felizt
    $ enfocar("mani")
    ma "¡Tengo ideas anotadas aquí! ¡Y aquí!"
    show mani 3nervioso3t
    extend " Y... espera..."
    show mani 3nerviosot
    extend " Esto es un código que hacía..."
    show mani 3nervioso
    $ normal("mani")
    show dark 1distraido
    show blaze 1desinteresada2
    show steve 2remedar
    show strike 1juzga
    show jeremy 1incomodo2
    l_thought "Código..."
    extend " ¿Él? ¿Haciendo un código? ¿Primero sobre qué?"

    if (rutaCanon-rutaSuicida)>=0:
        l_thought "Al menos Mani tiene energía para algo. Yo apenas tengo para respirar."
        l "Parece que alguien finalmente encontró su vocación."
        show dark 1felit
        $ enfocar("dark")
        d "¿Ves? Hasta el caos tiene su propósito."
        show dark 1juzgat
        extend " Mani distrae, tú firmas, yo molesto..."
        show dark 2desafiantet
        extend " Al final todos siempre caemos en estereotipos."
        show dark 2desafiante
        $ normal("dark")
        "Lo miro con duda. No entiendo a que se refiere con eso ultimo."

    else:
        l_thought "Incluso Mani, en su estupidez, es más útil que yo. Al menos él puede entretener."
        l_thought " Yo solo soy un agujero negro que consume oxígeno."
        show screen red_effect2
        nobody "{sc=3}Exactamente.{/sc}"
        nobody "{sc=3}Hasta el chiste del grupo sirve para algo.{/sc}"
        nobody "{sc=5}Tú solo sirves como advertencia.{/sc}"
        l_thought "Cállate."
        extend " Solo cállate."
        hide screen red_effect2 with Dissolve(0.5)
    
    show jeremy 1serio3
    "Jeremy no le parece convincente la idea, pero...{w} Se le puede notar agobiado con lo que sea que haya hecho, solo aceptando a regañadientes la propuesta de Dark."
    show jeremy 1estrest
    $ enfocar("jeremy")
    je "Vale... Mani puede ayudar. Pero bajo supervisión."
    show jeremy 1estres
    $ enfocar("jeremy")
    show steve 1sonriente
    show strike 1enojado
    show mani 2feliz:
        boo2
    show strike 1enojadot
    show blaze 2neutral
    $ enfocar("strike")
    st "Yo no voy a supervisar eso. Ya tengo suficiente con--{nw}"
    show strike 1juzga
    $ normal("strike")
    show steve 1sonrientet at boo2
    $ enfocar("steve")
    tv "Yo lo haré."
    show steve 2rizzt
    tv "Oye, Mani, ¿quieres que te ayude a organizar tus ideas?"
    show steve 2rizz
    $ normal("steve")
    l_thought "Espero que no haga esto solo para acercarse más a mi..."
    extend "  No quiero eso."
    show mani 2felizt
    $ enfocar("mani")
    ma "¡Sí! ¡Podemos hacer un equipo! ¡Tú y yo contra el aburrimiento!"
    show mani 2feliz
    $ normal("mani")
    show steve 2triste2t
    $ enfocar("steve")
    tv "¿Me puedo arrepentir de mi decisión?...{w} ¿Verdad?"
    show steve 2triste2
    $ normal("steve")
    show blaze 1juzga2
    show dark 1juzga
    show strike 1distraido
    show jeremy 1felizt
    $ enfocar("jeremy")
    je "{cps=5}¡JAJAJA!{/cps}"
    show jeremy 1seriot
    je "{i}No.{/i}"
    show jeremy 1serio
    $ normal("jeremy")
    "Me toma por sorpresa la forma de cómo pudo sacar una risa auténtica para después cortarla con un “no” tan seco como mis ojos ahora mismo."
    l_thought "Sabe cómo controlar sus emociones de maneras..."
    extend " Espeluznante..."
    show dark 2metiche
    "Dark se frota las manos con satisfacción, claramente disfrutando del caos que acaba de orquestar."
    show dark 1felit
    $ enfocar("dark")
    d "Perfecto. Mientras nuestro querido Mani y TV se encargan del informe..."
    show dark 1feli
    "Su mirada se desliza hacia mí."
    show dark 2desafiantet
    d "Nosotros podemos concentrarnos en cosas más importantes. Cómo decidir qué hacemos con nuestra problemática favorita."
    show dark 2desafiante
    $ normal("dark")
    show strike 1enojado:
        xzoom -1.0
        parallel:
            linear 0.3 yzoom 1.03 xzoom -0.99
            pause 0.2
            linear 0.5 yzoom 1.0 xzoom -1.0 yoffset 0
    "Strike resopla, apoyándose contra la pared con actitud desinteresada."
    l_thought "¿Otra vez con eso? ¿No se cansa de quejarse?"
    show strike 1juzgat
    $ enfocar("strike")
    st "¿No era solo firmar un reporte? ¿Ahora hay que “hacer algo” con ella?"
    show strike 1serio
    $ normal("strike")
    show blaze 2preocupada
    "Blaze me mira con preocupación, pero antes de que pueda hablar, Jeremy interviene."
    show jeremy 2seriot
    $ enfocar("jeremy")
    je "El escrito firmado... estar.{w} El expediente actualizado..."
    $ inac("strike")
    $ inac("steve")
    $ inac("mani")
    show strike 1distraido
    show steve 1neutralt
    show mani 2neutral
    show blaze 2preocupada:
        flip_off
    pause 0.2
    show mani 2neutral:
        flip_off
        
    if (rutaCanon-rutaSuicida)>=0:
        show jeremy 1neutralt
        je "Asumiendo que terminado esta... Blaze y ella ya se pueden ir"
        show jeremy 1seriot
        extend ", vosotros... encargar del resto."
        show jeremy 1serio
        $ normal("jeremy")
        show steve 1neutral
        show mani 2neutralt
        show blaze 1neutral
        "Me sorprendo ante esa resolución, hasta Blaze parece extrañada."
        show blaze 3neutralt
        $ enfocar("blaze")
        b "¿Seguro, Jeremy?"
        show blaze 3neutral
        $ normal("blaze")
        show steve 2juzgat
        show mani 3pinguino
        show jeremy 1seriot
        $ enfocar("jeremy")
        je "Sí, si... Igual... tened nada que hacer..."
        show jeremy 1serio
        $ normal("jeremy")
        l_thought "Este sujeto me sorprende cada vez más... No se si es por lo contradictorio que suele ser o porque realmente nos tiene en consideración."
        l_thought "A Blaze mejor dicho."
        show steve 2juzga
        show mani 3seriot
        show dark 2juzga2
        "Dark levanta una ceja, claramente decepcionado por el anticlímax."
        show dark 2juzga2t
        $ enfocar("dark")
        d "¿Y mi drama, carajo? ¿Mi tensión narrativa?"
        show dark 2juzga2
        $ normal("dark")
        show jeremy 2serio2
        show blaze 3desinteresada3
        $ renpy.pause(2.0, hard=True)
        show steve 2remedar2t
        show mani 3desanimado
        show dark 2distraido at sigh_animation
        "Dark suspira derrotado."
        show dark 2distraidot
        $ enfocar("dark")
        d "Bueno... Supongo que está bien."
        show dark 2desafiantet
        d "Ya mucho drama tienes en tu vida, Laila."
        show dark 2desafiante
        $ normal("dark")
        show blaze 1compadecer
        show jeremy 1sonriente
        show steve 1remedar
        show mani 2felizt
        "Blaze me toma del brazo suavemente."
        l_thought "¿Eso es todo? Después de tanto drama, solo..."
        extend " ¿Nos vamos?"
        l_thought "Casi me siento decepcionada."
        extend " Como si hubiera esperado un castigo que nunca llegó."
        show dark 1felit
        $ enfocar("dark")
        d "Hasta mañana, Laila. No te suicides antes de que pueda burlarme de ti otra vez."
        show dark 1feli
        $ normal("dark")
        show jeremy 1sonrientet
        $ enfocar("jeremy")
        je "Cuidate."
        show jeremy 1sonriente
        $ normal("jeremy")
        $ renpy.pause(1.0, hard=True)
        $ inac("jeremy")
        $ inac("dark")
        "Mientras salimos, escucho el ruido que proviene detrás de nosotros."
        l_thought "¿Por qué esta compasión duele más que el castigo que merezco?"
        scene black with Dissolve(1.0)
        $ renpy.pause(2.5, hard=True)

    else:
        show jeremy 1serio2t
        je "Aun asi. Laila, a la próxima te ve la psicóloga."
        show jeremy 1seriot
        extend " Punto."
        show jeremy 1serio
        $ normal("jeremy")
        show blaze 2preocupada
        show dark 1distraido
        show steve 2remedar
        show mani 1nervioso
        $ renpy.pause(2.0, hard=True)
        "Las palabras caen como una losa en el silencio de la habitación. Mis dedos se enfrían instantáneamente."
        show screen red_effect2
        nobody "{sc=3}¿Lo ves?{/sc}"
        nobody "{sc=3}Hasta ellos reconocen lo rota que estás.{/sc}"
        nobody "{sc=4}Ahora quieren encerrarte con profesionales.{/sc}"
        show blaze 2preocupadat
        $ enfocar("blaze")
        b "Jeremy, ¿es necesario?"
        show blaze 2preocupada
        $ normal("blaze")
        show jeremy 1serio2t
        $ enfocar("jeremy")
        je "Después de lo ocurrido hoy... Sí.{w} Lo es."
        show jeremy 1seriot
        $ normal("jeremy")
        show dark 1feli
        "Dark observa la escena con una sonrisa que no pretende ser amable."
        show dark 1felit
        $ enfocar("dark")
        d "Felicidades, Problemática. Has logrado lo que pocos: volverte un caso de estudio oficial."
        show dark 1feli
        $ normal("dark")
        l_thought "Psicóloga. Otra persona a la que tendré que mentir. Otra que me verá con esa mezcla de lástima y curiosidad clínica."
        l_thought "¿En qué momento me convertí en este... Proyecto de reparación para todos?"
        nobody "{sc=3}Siempre lo has sido.{/sc}"
        nobody "{sc=3}Solo que ahora se cansaron de fingir que no lo notas.{/sc}"
        l "¿Y si me niego?"
        show jeremy 2estrest
        $ enfocar("jeremy")
        je "Creo que sabéis las consecuencias."
        show jeremy 2incomodot
        extend " Solo... dire por si no quedó claro."
        show jeremy 2seriot
        je "Tu padre se va a enterar."
        show jeremy 2serio
        $ normal("jeremy")
        show blaze 2preocupada
        show dark 1distraido
        "La amenaza cuelga en el aire, más efectiva que cualquier regaño{w}, asfixiandome lentamente."
        "Blaze me mira con ojos suplicantes."
        show blaze 2preocupadat
        $ enfocar("blaze")
        b "Laila, por favor... Quizás...{w} Quizás ayude."
        show blaze 2preocupada
        $ normal("blaze")
        l_thought "Ayudar."
        extend " Como si lo que tengo fuera algo que se puede arreglar con una charla y pastillas."
        l_thought "Como si no supiera que algunos pozos son demasiado profundos para llenar."
        "Asiento lentamente, la derrota sabiendo a cenizas en mi boca."
        l "Como quieran. Realmente, no creo que necesite ayuda.{w} Y menos de ustedes."
        show dark 2serio at shake
        show blaze 2desinteresada3
        show steve 2remedar2
        show jeremy 2incomodo2
        show strike 1serio
        "Dark sacude la cabeza, casi con decepción."
        show dark 2seriot
        $ enfocar("dark")
        d "Te damos las herramientas, Laila."
        show dark 2serio2t
        extend "  El resto..."
        show dark 2seriot
        extend " Es tu funeral."
        show dark 2serio2
        $ normal("dark")
        l "Y a mi que mierda me importa, apenas los conozco."
        show dark 2serio2t
        $ enfocar("dark")
        d "Para la próxima ni diremos nada, ya queda en ti en mejorar o no."
        show dark 2seriot
        d "Estamos siendo muy pacientes contigo, y apenas nos estamos conociendo."
        show dark 2serio2t
        "Eso último me golpea en el estómago."
        show dark 2seriot
        d "Y, Laila... La última chica que rechazó la ayuda psicológica..."
        show dark 2distraido2t
        stop music
        extend " No está aquí para contarlo.{w} Piensa en eso."
        show dark 2distraido2
        $ normal("dark")
        show blaze 1desinteresada2
        $ renpy.pause(2.5, hard=True)
        scene black with Dissolve(0.5)
        "Blaze me arrastra afuera del salón. El peso de la próxima cita colgando de mis hombros como una capa invisible.{w} Pero las palabras de Dark quedan en mi mente."
        l_thought "Psicóloga. Un recordatorio más de que soy un caso. Un problema. Algo que necesita ser arreglado...{w} Y eso último..."
        extend " Es aterrador."
        l_thought "¿Cuándo entenderán que algunas cosas no tienen solución?"
        nobody "{sc=3}Ellos lo entienden perfectamente.{/sc}"
        nobody "{sc=3} Solo están cumpliendo con el protocolo hasta que tú cumplas con el tuyo.{/sc}"
        nobody "{sc=4}Una Psicóloga, reporte, decepción...{/sc}"
        nobody "{sc=5}¿Cuántas señales más necesitas para entender tu lugar?{/sc}"
        hide screen red_effect2 with Dissolve(0.5)

    "Jeremy suspira, exhausto."
    je "Genial..."
    play sound closet_close
    "La puerta se cierra detrás de nosotros, ahogando el resto de la conversación."
    stop music fadeout 5.1
    $ renpy.pause(2.5, hard=True)
    "Después de salir del salón del consejo, el silencio entre yo y Blaze es denso, cargado de lo no dicho."
    $ renpy.pause(2.5, hard=True)
    "El camino hacia la salida se siente más largo de lo habitual, cada paso es un eco de las palabras intercambiadas, las miradas, las decisiones tomadas."
    with Fade(5.0, 8.0, 5.0) 
    jump final_day2
return

label final_day2:
    play ambient ext_night fadein(2.0)
    $ renpy.pause(5.0, hard=True)
    b "Laila...{w} ¿Estás realmente bien?"
    "Su voz es tan suave que casi se pierde entre el murmullo del tráfico. Carga con la preocupación como un peso extra en sus hombros{w}, un peso que yo le puse allí."
    $ renpy.pause(3.5, hard=True)
    "Miro al frente, evitando su mirada. Mis ojos se clavan en una grieta del pavimento.{w} Suspiro, un sonido que sale más cansado de lo que pensé."
    l "Sí.{w} Solo quiero llegar a casa."
    "Mis palabras suenan planas, huecas.{w} Una mentira tan obvia que ni yo soy capaz de creerlo."
    "Ella asiente, sabiendo que no fue una respuesta convincente."
    "Sus dedos juegan nerviosamente con la correa de su mochila, un tic que solo aparece cuando está realmente inquieta."
    $ renpy.pause(3.5, hard=True)
    scene intersection_night
    show blaze 1preocupada:
        center
        night_urban
    with Dissolve(2.0)
    "Llegamos a la esquina iluminada por las luces de la ciudad, cada paso resonando en el silencio que nos envuelve."
    show blaze 2compadecert
    $ enfocar("blaze")
    b "Si necesitas hablar...{w} Yo estoy aquí. Siempre."
    show blaze 2compadecer
    $ normal("blaze")
    "{i}“SIEMPRE”{/i}.{w} Esta FAMOSA palabra que resuena en el aire entre nosotras, es pesada y frágil a la vez, es una promesa que ya hemos roto demasiadas veces que no parece genuina a este punto."
    
    if (rutaCanon-rutaSuicida)>=0:
        "Asiento despacio, un movimiento casi imperceptible. Trato de convencerme, aferrarme a esas palabras como a un salvavidas."
        l_thought "Ella siempre está ahí. Aún después de todo lo que le dije, de todo lo que le hice pasar en el salón."
        extend " ¿Por qué? ¿Qué gana con esto? ¿Qué ve en mí que yo no puedo ver?"
        show blaze 2desinteresada3
        show screen red_effect2
        nobody "{sc=3}¿Ganar? Quizás gane puntos en su conciencia.{/sc}"
        nobody "{sc=3}Pero tal vez solo está siendo parte de un guión que le entregaron como:{/sc}"
        nobody "{sc=3}“La buena hermana”.{/sc}"
        nobody "{sc=4}Pero sabes que hasta los buenos actores se cansan de sus papeles.{/sc}"
        l_thought "Papá no vino. El reporte está firmado, sellado, archivado. Una mancha más en mi expediente y por fin el día terminó."
        l_thought "¿Y ahora qué? ¿Será otro día igual que mañana? ¿Acaso será una nueva promesa rota, una decepción distinta, o solo será una excusa diferente?"
        nobody "{sc=3}Las promesas son fáciles de elaborar.{/sc}"
        nobody "{sc=3}Son frágiles y difíciles incluso de cumplir.{/sc}"
        nobody "{sc=3}¿Por qué crees que tu padre eligió la emergencia real?{/sc}"
        nobody "{sc=3}Porque al menos esa si tiene una solución, a comparación de ti.{/sc}"
        nobody "{sc=5}Que solo eres un problema crónico.{/sc}"
        nobody "{sc=5}Uno que nadie quiere resolver.{/sc}"
        nobody "{sc=3}Los problemas crónicos se gestionan.{/sc}"
        nobody "{sc=5}Pero jamás se solucionan.{/sc}"
        l_thought "Yo sólo quiero dormir. Poder cerrar los ojos y que todo desaparezca de una vez por todas."
        l_thought "Olvidar sus expresiones, la desilusión que carga Blaze en mi, el descaro impredecible de Dark, y esa actitud seca de Jeremy solo me carcome por dentro. Desearía poder olvidar que existo, dejar cargar esta culpa que soy incapaz de manejar."
        nobody "{sc=3}Mañana despertarás e igual seguirás siendo la misma.{/sc}"
        nobody "{sc=3}¿Qué es lo que cambiaría?{/sc}"
        nobody "{sc=3}Solo serán los mismos problemas y decepciones de siempre.{/sc}"
        nobody "{sc=5}La misma Laila.{/sc}"
        nobody "{sc=5}Olvidar solo es temporal.{/sc}"
        nobody "{sc=5}El fracaso solo rebotara en ti sin detenerse hasta que lo entiendas.{/sc}"
        hide screen red_effect2

    else:
        "Guardo silencio. Un silencio denso y pesado que se instala entre nosotras."
        "Tengo mi mirada perdida, mirando al frente, viendo cómo los coches pasan sin detenerse, sin importarles que aquí hay dos hermanas cuyo mundo se está desmoronando, sin responder a su pregunta."
        "Como una estatua que solo está hecha para ser observada."
        show blaze 2desinteresada3
        show screen red_effect2
        nobody "{sc=3}Mira cómo pasan. La vida sigue para todos, menos para ti.{/sc}"
        nobody "{sc=3}Solo eres un bache que surge en el camino, que todos siempre evitan.{/sc}"
        l_thought "¿Por qué me siento tan... Vacía?"
        l_thought "Ella solo cumple con su papel. La hermana buena. La comprensiva. La que siempre dice las palabras correctas y empáticas."
        l_thought "Pero se que en esos ojos... si miro con más detenimiento, seré capaz de ver otra cosa."
        l_thought "Un cansancio y resignación sin cesar. Solo puedo hacerme la pregunta silenciosa, “¿hasta cuándo?”."
        nobody "{sc=5}“¿Hasta cuándo?”{/sc}"
        nobody "{sc=3}Esa la pregunta correcta que deberías realizarte.{/sc}"
        nobody "{sc=3}¿Hasta cuánto tiempo podrán aguantar tu miseria?{/sc}"
        nobody "{sc=3}¿Cuándo serán capaces de soltar está máscara?{/sc}"
        nobody "{sc=3}¿Decidir no fingir que les importas?{/sc}"
        nobody "{sc=3}Cada día es una moneda  que gastan en ti.{/sc}"
        nobody "{sc=3}El centavo que nadie desea tener.{/sc}"
        l_thought "Papá no vino. Ni siquiera se molestó en avisarnos antes. Tuve que preguntar yo. Como siempre."
        l_thought "Como si mi tiempo, mis expectativas, y mi poca esperanza de que..."
        extend " Tal vez, solo esta vez sería diferente como si nada de eso importara."
        nobody "{sc=3}La frágil esperanza.{/sc}"
        nobody "{sc=3}¿Hasta cuánto tiempo podrán aguantar tu miseria?{/sc}"
        nobody "{sc=3}Es fácil idearlo, es sencillo crearla.{/sc}"
        nobody "{sc=3}Es un concepto tan perfecto como patético para alguien como tú.{/sc}"
        nobody "{sc=3}Es como esperar que un muñeco roto sea capaz de arreglarse solo.{/sc}"
        nobody "{sc=3}Tu padre solo eligió la emergencia real...{/sc}"
        nobody "{sc=5}Porque al menos esa tiene solución.{/sc}"
        nobody "{sc=5}Tú solo eres un parásito.{/sc}"
        l_thought "Sólo soy un fracaso que está programado."
        extend " ¿Cuándo dejarán de intentar arreglarme?"
        extend " ¿Cuándo admitirán que habrán cosas que están demasiado rotas como para ser reparadas?"
        l_thought "Eso yo ya lo sé. Solo estoy esperando a que ellos también lo descubran."
        nobody "{sc=3}Y si ya lo sabes...{/sc}"
        nobody "{sc=3}¿Porque sigues teniendo esa esperanza?{/sc}"
        nobody "{sc=3}De igual forma también ya lo saben.{/sc}"
        nobody "{sc=3}Solo seguirán fingiendo que no.{/sc}"
        nobody "{sc=3}Es más fácil fingir que puedes ser reparable.{/sc}"
        nobody "{sc=3}Simplemente es admitir la verdad:{/sc}"
        nobody "{sc=5}Que solo eres un material hecho para desecharse.{/sc}"
        nobody "{sc=5}Un error de fabricación que deberían haber retirado del mercado hace tiempo.{/sc}"
        hide screen red_effect2

    play sound phone_quiet loop
    show blaze 3nerviosa at boo2
    "El teléfono de Blaze vibra en su bolsillo, rompiendo el tenso silencio."
    "Ella se asusta con el sonido, un pequeño salto que delata sus nervios, pero se recompone rápidamente.{w} Y contesta."
    stop sound
    show blaze 1desinteresada3t
    $ enfocar("blaze")
    b "¿Sí, papá?"
    b "Sí, ya salimos..."
    extend " No, tranquilo, llegaremos bien..."
    show blaze 1desinteresada3
    $ normal("blaze")
    $ renpy.pause(1.5, hard=True)
    b "..."
    "Una pausa."
    show blaze 1seria
    "Sus ojos se encuentran con los míos por un instante."
    show blaze 1desinteresada3t
    $ enfocar("blaze")
    b "¿En serio?{w} Está bien, se lo diré."
    show blaze 1desinteresada3
    $ normal("blaze")
    show blaze 2preocupada
    "Cuelga y me mira, con lástima."
    show blaze 2compadecert
    $ enfocar("blaze")
    b "Papá dice que lo siente.{w} Tuvo que ir a una emergencia de verdad..."
    show blaze 2desinteresada3
    $ normal("blaze")
    $ renpy.pause(1.5, hard=True)
    "Hace una pausa, buscando las palabras correctas."
    show blaze 2compadecert
    $ enfocar("blaze")
    b "Dice que mañana sin falta saldrán{w}, si tú quieres."
    show blaze 2compadecer
    $ normal("blaze")

    if (rutaCanon-rutaSuicida)>=0:
        "Asiento forzosamente.{w} Ya es un movimiento que se ha hecho automático. La cabeza que baja y sube porque es lo que se espera."
        l "Lo hablaré con él en la mañana."
        show blaze 2preocupada
        "Mi voz suena a resignación, no a esperanza.{w} Como si ya supiera cómo terminará esta conversación."
        l_thought "“Si tú quieres”. Tres palabras que cargan con el peso de todas mis decisiones fallidas."
        l_thought "¿Y si no quiero? ¿Y si ya no quiero nada?"

    else:
        "Asiento, sin palabras.{w} Mi cabeza se mueve, pero es  un reflejo hueco. No hay intención detrás, solo el movimiento mecánico de un cuerpo que sigue funcionando por inercia."
        show blaze 2preocupada
        l_thought "“Sin falta”. Ya he escuchado eso antes."
        extend " En innumerables cenas pospuestas, en paseos cancelados, en esas clásicas promesas de “la próxima semana seguro”."
        l_thought "Ya para mí esa palabra dejó de tener un valor significativo..."
        l_thought "Una emergencia de verdad..."
        extend " ¿Y yo qué soy?"
        extend " ¿Una emergencia falsa?"
        l_thought "¿Un problema de baja prioridad que puede esperar, y esperar, y esperar?"

    $ renpy.pause(2.5, hard=True)
    "A lo lejos, por la calle, se ve una silueta de un camión, mostrando que va por nuestra calle donde vivimos."
    show blaze 2compadecer
    "Blaze me toca suavemente el brazo, un gesto que antes me brindaba un consuelo y que ahora solo es un recuerdo vago de lo desconectada que estoy de todo."
    show blaze 2compadecert
    $ enfocar("blaze")
    b "Vamos."
    show blaze 2compadecer
    $ normal("blaze")
    "Es una palabra simple, pero se lleva cargando todo lo que no decimos mutuamente, por mi parte la sigo, {i}como siempre{/i}."
    "Nos acercamos a la parada del bus."
    play sound bus_arrive fadein 0.5
    $ renpy.pause(14.0, hard=True)
    "Este se detiene. Y abre sus puertas. Nos montamos."
    scene black with Dissolve(0.5)
    stop ambient fadeout(1.5)
    $ renpy.pause(1.8, hard=True)
    play ambient bus fadein(2.0)
    $ renpy.pause(8.5, hard=True)
    stop ambient fadeout(1.5)
    play ambient ext_night fadein(2.0)
    "El transporte público nos lleva a la parada, solo  bajamos y se puede ver qué ya está todo oscuro, solo se aprecian las luces que emanan las farolas mientras el ruido urbano estaba de fondo."
    $ renpy.pause(2.8, hard=True)
    "Caminamos por un largo tramo hasta llegar a casa finalmente, dentro de mi ya estaba feliz de que había llegado a mi gran zona de confort. "
    l "¿No sabes a qué hora llegará papá?"
    b "Ni idea. No me lo dijo en la llamada."
    "La puerta está cerrada.{w} Blaze busca las llaves en su mochila, tengo las manos temblorosas por el frío o por otra cosa que no quiero nombrar."
    play sound keylock
    "La cerradura cede con un clic seco, demasiado ruidoso en la calle vacía."
    play sound closet_open
    "Entramos."
    stop ambient fadeout(1.5)
    $ renpy.pause(1.6, hard=True)
    play ambient int_night fadein(2.0)
    scene livingroom_n
    show blaze 1desinteresada3:
        night_purple
        center
    with Fade(0.5, 0.5, 0.5)    
    play sound closet_close
    "La casa está a oscuras. No hay luz en ninguna parte del hogar, ni la televisión encendida, ni sonido de platos desde la cocina. Solo el zumbido bajo y constante del refrigerador y la iluminación de la luna llena que pegaba por una ventana con sus cortinas abiertas."
    "Solo un silencio que pesaba mucho más que cualquier grito de horror."
    play sound light_switch
    scene livingroom_l
    show blaze 1sonriente:
        center
    "Blaze enciende la luz."
    "Camino a la cocina para beber un vaso con agua."
    scene kitchen
    with Fade(0.5, 0.5, 0.5)  
    "Veo una nota.{w} Un rectángulo blanco clavado con un imán en la puerta de la nevera.{w} La letra de papá, firme, apresurada, impersonal."
    show blaze 1seria with Dissolve(0.3):
        center
    "Blaze se acerca y la lee en silencio. Sus hombros, que ya estaban encorvados, parecen hundirse un poco más."
    "Yo me quedo donde estoy como si cruzar el umbral significa admitir que esto es real."
    $ renpy.pause(1.5, hard=True)
    play sound pageflip
    $ renpy.pause(1.5, hard=True)
    show blaze 2seriat
    $ enfocar("blaze")
    b "Laila, Blaze: Hay comida en el refrigerador. Calienten lo que quieran. Mañana hablamos. Cuídense."
    show blaze 2desinteresada3t
    extend " – Papá."
    show blaze 2seria
    $ normal("blaze")
    "Su voz es plana al leerlo. No hay sorpresa. Solo confirmación."
    show blaze 2desinteresada2 at sigh_animation
    "Ella suelta un suspiro que parece sacado de lo más hondo."
    show blaze 2enojada2
    "Se gira hacia mí, y por un segundo veo algo en sus ojos —algo que se parece al enfado, a la frustración—..."
    show blaze 2compadecer
    "Antes de que su expresión habitual, la de la hermana comprensiva, vuelva a cubrirlo todo como una manta."
    show blaze 2compadecert
    $ enfocar("blaze")
    b "Voy a calentar algo.{w=0.2} ¿Comes?"
    show blaze 2compadecer
    $ normal("blaze")
    $ renpy.pause(2.5, hard=True)
    "La pregunta flota en el aire entre nosotras. Yo miro hacia la nevera, imaginando los recipientes de plástico con comida recalentada, preparados con prisa esta mañana.{w} Niego con la cabeza."
    l "No tengo hambre. Voy arriba."
    show blaze 3seria
    "Mis palabras caen al suelo como piedras. Ella me mira, y esa mirada lo dice todo. Sabe que es mentira."
    l_thought "Insistir es inútil. Es una danza que hemos bailado demasiadas veces."
    extend "  Ella ofrece, yo rechazo."
    extend "  Ella se preocupa, yo me encierro."
    $ renpy.pause(1.8, hard=True)
    show blaze 2desinteresada2
    "Asiente, un gesto pequeño y derrotado."
    show blaze 2compadecert
    $ enfocar("blaze")
    b "Está bien...{w} Buenas noches, Laila."
    show blaze 2compadecer
    $ normal("blaze")

    if (rutaCanon-rutaSuicida)>=0:
        l "Buenas noches, Blaze."
        "Intento darle una sonrisa conmovedora. Solo fallando en el intento, igual no es...{w} Lo mejor que he hecho."

    scene black with dissolve
    "Doy media vuelta, salgo de la cocina y empiezo a subir las escaleras."
    play sound microwave volume 0.05
    "El ruido del microondas encendiéndose abajo me sigue unos peldaños."
    $ renpy.pause(3.5, hard=True)
    stop sound
    "Luego se apaga, absorbido por el silencio."
    $ renpy.pause(1.8, hard=True)
    "Arriba, la oscuridad es lo que más abunda.{w}  Al igual que abajo, la iluminación de la luna se filtra por la ventana, dibujando un rectángulo pálido en el suelo recordando que al menos lo único bello en esta casa es está iluminación. Camino a través de él."
    play sound closet_open
    "Empujo la puerta para entrar a la habitación."
    scene lailaroom_n with Fade(0.3, 0.3, 0.3)
    play sound closet_close
    extend " Y cierro sin pensarlo."
    $ renpy.pause(1.8, hard=True)
    "Dejo que el peso me venza. Tiro mi mochila y camino hacia la cama y me desplomo alli mismo."
    "Respiro hondo, pero el aire parece espeso, difícil de tragar, por fin llegué a mi refugio."
    $ renpy.pause(3.1, hard=True)

    if (rutaCanon-rutaSuicida)>=0:
        l_thought "Un día menos, es otro día que he sobrevivido."
        extend " Eso es todo lo que puedo anotar en mi diario mental"
        extend ": sobreviví."
        l_thought "Blaze sigue aquí. Abajo, comiendo sola."
        extend " Aún después de mis gritos, de mi vergüenza, de mi rechazo."
        l_thought "¿Qué es lo que la mantiene aquí? ¿Debería sentirme acaso, agradecida o asustada de ese peso?"
        $ renpy.pause(2.5, hard=True)
        l_thought "Papá..."
        extend " Al menos dejó una nota."
        extend " “Mañana hablamos”."
        extend " Palabras."
        extend " Solo palabras que él mismo diría pero son más de las que he llegado a recibir."
        l_thought "Cuatro líneas en un imán de nevera. Es algo."
        extend " ¿No?"
        show screen red_effect2
        nobody "{sc=3}Es lo mínimo.{/sc}"
        nobody "{sc=3}Lo máximo de decir: “Cuídense”.{/sc}"
        nobody "{sc=3}Pero no será un “las quiero”.{/sc}"
        nobody "{sc=3}No será de un “lo siento de verdad”.{/sc}"
        nobody "{sc=3}Pero será lo que se escribe cuando no sabes qué más poner.{/sc}"
        hide screen red_effect2 with Dissolve(0.3)
        l_thought "Firmé el reporte."
        extend " Es solo un papel."
        extend " Uno más en la colección de mi expediente, junto a todos los otros."
        extend " Una recopilación de mis fracasos, archivada y olvidada por todos excepto por mí."
        l_thought "Ese “mañana”... “sin falta”."
        extend " “Si tú quieres”."
        extend " Las dos condiciones y excusas que están..."
        extend " Preparadas."
        l_thought "Una para él si falla, otra para mí si decido no querer más esto."
        show screen red_effect2
        nobody "{sc=3}¿Y qué quieres, Laila?{/sc}"
        nobody "{sc=3}¿De verdad quieres esa salida, esa conversación forzada, ese intento más?{/sc}"
        nobody "{sc=3}Pero no será un “las quiero”.{/sc}"
        nobody "{sc=3}No será de un “lo siento de verdad”.{/sc}"
        nobody "{sc=3}O sólo quieres que la promesa se rompa de una vez para poder decir:{/sc}"
        nobody "{sc=3}“Te lo dije”.{/sc}"
        nobody "{sc=3}Para solo hundirte en paz.{/sc}"
        hide screen red_effect2 with Dissolve(0.3)
        l_thought "Sólo quiero dormir."
        extend " Que este zumbido en mi cabeza pare."
        extend " Que el vacío en mi estómago se calme."
        l_thought "Cerrar los ojos y que, por unas horas, deje de ser Laila la Problemática, Laila la Decepción, Laila la Hermana Rota."
        show screen red_effect2
        nobody "{sc=3}Dormir no es un escape, es un ensayo.{/sc}"
        nobody "{sc=3}Un ensayo para el gran silencio.{/sc}"
        nobody "{sc=5}Ya lo haces muy bien.{/sc}"
        hide screen red_effect2 with Dissolve(0.3)

    else:
        l_thought "Un día más."
        extend " Otro día añadido a la cadena."
        extend " Otro eslabón de horas vacías y promesas rotas que me han hecho."
        l_thought "Blaze sigue aquí."
        extend " Pero no es por mí, es por inercia, por esa lealtad hacia un fantasma—el fantasma de la hermana que alguna vez fui, o que ella creyó que volvería a ser."
        l_thought "Esta cenando sola abajo, aliviada quizás de no tener que fingir por unas horas."
        show screen red_effect2
        nobody "{sc=3}Deberías de sentirte aliviada...{/sc}"
        nobody "{sc=3}Tú eres el trabajo extra que nadie pidió.{/sc}"
        nobody "{sc=3}El turno nocturno sin paga.{/sc}"
        hide screen red_effect2 with Dissolve(0.3)
        $ renpy.pause(2.5, hard=True)
        l_thought "La nota que Papá..."
        extend " Esas cuatro líneas."
        extend " “Mañana hablamos”."
        extend " No es el: “hablemos”, solo es “hablamos”."
        extend " Es una declaración."
        l_thought "Otro sermón que me espera en el calendario, entre una emergencia real y la siguiente."
        $ renpy.pause(1.8, hard=True)
        l_thought "“Cuídense”."
        extend " Un mandato irónico."
        extend " ¿Cómo carajo espera que me cuide?"
        extend " ¿Cómo cuidas algo que realmente está dañado?"
        l_thought "Solo lo guardas en una caja, se etiqueta “frágil” y lo abandonas en el ático."
        show screen red_effect2
        nobody "{sc=3}Exactamente.{w} Ese es tu lugar.{/sc}"
        nobody "{sc=3}El ático de sus vidas.{/sc}"
        nobody "{sc=3}Sólo bajan a buscarte cuando el polvo de tu ausencia les hace estornudar.{/sc}"
        hide screen red_effect2 with Dissolve(0.3)
        $ renpy.pause(1.8, hard=True)
        l_thought "Firmé el reporte."
        extend " Un trámite que marcó mi deterioro constante."
        extend " Y pronto habrá más."
        extend " Más informes."
        extend "  Más carpetas con mi nombre."
        l_thought "Me estoy convirtiendo en papel."
        extend " En un caso."
        extend " En un problema a gestionar."
        show screen red_effect2
        nobody "{sc=3}¿Apenas te enteras de eso?{/sc}"
        nobody "{sc=3}Solo es el comienzo, te estás convirtiendo en algo “oficial”.{/sc}"
        nobody "{sc=3}No solo serás la vergüenza de la escuela...{/sc}"
        nobody "{sc=3}Tal vez seas incluso lo serás a nivel estatal.{/sc}"
        nobody "{sc=3}Solo es cuestión que  ni siquiera necesitarán mirarte a los ojos.{/sc}"
        nobody "{sc=5}Bastará con leer tu archivo.{/sc}"
        hide screen red_effect2 with Dissolve(0.3)
        l_thought "Mañana..."
        extend " “sin falta”."
        extend " Las palabras más gastadas de tantas que hay en el diccionario. Una emergencia “de verdad” siempre aparecerá."
        extend "  Siempre hay una."
        extend " Yo nunca seré la emergencia para él."
        extend " Solo soy la falla de fondo, el ruido estático en su línea clara."
        $ renpy.pause(1.8, hard=True)
        l_thought "Yo no quiero dormir."
        extend " Dormir implica despertar."
        extend " Y despertar es encontrarme con esa decepción de que nada ha cambiado, excepto que soy un día más vieja, un día más cansada, un día más cerca del momento en que ya no pueda resistir más."
        show screen red_effect2
        nobody "{sc=3}Ese momento se acerca más y más.{/sc}"
        nobody "{sc=3} Lo sientes, ¿verdad?{/sc}"
        $ renpy.pause(1.8, hard=True)
        nobody "{sc=5}No seas una cobarde y acaba de una vez por todas con tu cruel realidad.{/sc}"
        hide screen red_effect2 with Dissolve(0.3)
        l_thought "Cierro los ojos, pero no contra la oscuridad."
        extend " La oscuridad ya está aquí, dentro."
        extend " Solo cierro los ojos contra mañana."
   
    $ renpy.pause(3.0, hard=True)
    "No me cambio. No me lavo la cara. Solo me quito los zapatos."
    "Desde aquí, veo la mochila en el suelo, la silueta oscura contra la luz de la ventana.{w} Dentro está el desayuno, intacto.{w} Los restos del día."
    $ renpy.pause(2.5, hard=True)
    "Afuera, un coche pasa veloz, su luz barriendo fugazmente el techo antes de desaparecer. Luego, otra vez la oscuridad.{w} Y el silencio."
    "No es un silencio pacífico.{w}  Es el silencio de una casa que contiene demasiados ruidos ahogados.{w} El silencio de las palabras no dichas en la nota de la nevera."
    "El silencio de los pasos que no resonaron en la entrada.{w} El silencio de mi propio cuerpo, que ya ni siquiera tiene lágrimas que ofrecer."
    scene black
    stop ambient fadeout 6.5
    with Dissolve(5.0)

return