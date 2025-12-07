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
    show dark 1feli
    $ normal("dark")
    show jeremy 1serio
    "Jeremy le da una mirada enojada a Dark. Dándole a entender que no es un buen momento."
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
        nobody "{sc=4}Mira el esfuerzo que hacen por ti.{/sc}"
        nobody "{sc=}Tu padre cocinando hasta tarde.{/sc}"
        nobody "{sc=6}Blaze rogándote...{/sc}"
        nobody "{sc=4}¿Cuándo dejarás de defraudarlos?{/sc}"
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
play music bgm1
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
$ renpy.pause(2.5, hard=True)
"Blaze me mira con esa expresión de preocupación."
show blaze 2compadecert
$ enfocar("blaze")
b "Y... Laila...{w} ¿Al final irás con papá?"
show blaze 2compadecer
$ normal("blaze")
show jeremy 1neutral
l_thought "Ya suponía  que iba a preguntar eso...{w} El elefante en la habitación."
l "Bueno... Ya debería estar en camino para aca.{w} Eso creo."
"Le digo eso esquivando su mirada mientras guardo mis últimos útiles."
"Dark se inclina contra un pupitre, observándonos como si fuéramos su telenovela personal."
show dark 2juzgat
$ enfocar("dark")
d "Vaya, un drama familiar. ¿Apuestan a que termine en llanto o en portazo?"
show dark 2juzga
$ normal("dark")
show blaze 2desinteresada2
show jeremy 1seriot
$ enfocar("jeremy")
je "Dark, por una vez en tu vida, callate."
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
call chat_dad_day2

l_thought "Pensé que sentiría alivio al no salir... Y hablar sobre cosas que no quiero. Pero no, me siento extraña."
l "No viene."
"Mi voz sale densa. Casi cortante. No era mi intención"
l_thought "¿Y qué más da? Al final, todos se cansan de cargar conmigo."
if (rutaCanon-rutaSuicida)<=-1: 
    show screen red_effect2
    nobody "{sc=3}Exactamente.{/sc}"
    nobody "{sc=3}Hoy fue él, mañana será Blaze.{/sc}"
    nobody "{sc=3}Pasado mañana hasta ese idiota de Dark.{/sc}"
    nobody "{sc=3}La pregunta no es si te abandonarán, sino cuándo.{/sc}"
    hide screen red_effect2 with Dissolve(0.5)
    l_thought "Maldita sea, cállate por una puta buena vez."




return