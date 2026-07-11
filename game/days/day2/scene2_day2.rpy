label scene2_day2:

    $ quick_menu = True
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
    with Dissolve(5.0)
     
return