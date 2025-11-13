label rutacanon_choice1:
        l 'Pues... Tuve un pequeño "problema" con el Profesor Todd...'
        "La culpa me sigue invadiendo, haciéndome sentir pequeña y expuesta."
        l "Que concluyó en mí fuera del salón."
        l "Ese es un pequeño resumen que le puedo dar a tu pregunta."
        show dark 2neutral
        "Ahora Dark luce sorprendido."
        pause 1.5
        show dark 2neutralt
        $ enfocar("dark")
        d "Espera... ¿Respondiste?"
        show dark 2neutral
        $ normal("dark")
        l "Claro..."
        "Se le ve una genuina confusión en su rostro."
        l_thought "¿Él esperaba que no lo hiciera?"
        l_thought "¿Le dí tan mala imagen? Bueno, supongo que me la gané."
        pause 1.5
        show dark 2distraidot
        $ _history = False
        d "{size=18}Se suponía que en esta versión eres algo más problemática...{/size}"
        d "{size=18}Como en la de célu-{/size}{nw}"
        $ _history = True
        show dark 2distraido
        "Esa última parte la dice para sí mismo. Aun así lo oí.{w} Otra vez."
        l_thought "¿En esta...{w=0.5} Versión?"
        "Mi rostro refleja la confusión, sus palabras me desconciertan."
        l_thought "¿Qué carajos dice este?"
        extend " Como sea..."
        l_thought "Parece tener la mirada perdida."
        l_thought "Creo que es hora de despertarlo."
        l "Ejem."
        show dark 2neutral
        l_thought "Ya reaccionó."
return

label rutasuicida_choice1:
        l "No es problema tuy-{nw}"
        show dark 2distraidot
        $ enfocar("dark")
        d "Olvidalo." 
        show dark 2seriot
        extend " Ya sé la respuesta."
        "Ni siquiera me dejó terminar la oración. Dejando las palabras medio salir."
        d "¿No será qué estás por aquí por estar durmiendote en las clases?"
        show dark 2juzga2t
        d "O en el peor de los casos"
        show dark 2seriot
        extend ", ¿Tuviste algún problema con el profesor y te echaron?"
        d "¿Y por eso casualmente estás por aquí?"
        show dark 2distraidot
        $ normal("dark")
        $ _history = False
        d "{size=18}En verdad... En esta versión eres {i}muy{/i} problematica.{/size}"
        $ _history = True
        show dark 2enojao
        l_thought "¿En esta...{w=0.5} Versión?"
        l_thought "¿Qué carajos dice este?"
        extend " Como sea..."
        l_thought "Esa fue una observación muy... detallada."
        l_thought "Es como si él hubiera estado allí, cuando sé que no."
        l_thought "Por el bien de mi ya deteriorada salud mental, mejor no quiero saber lo que piensa de mí."
        l "¿Mi opinión? Prefiero guardármela para algo que realmente importe."
        l_thought "No tengo energía para dar opiniones hoy. ¿Puedes simplemente dejarme en paz?"
        show dark 2seriot
        $ enfocar("dark")
        d "Sin ofender, pero."
        extend " Eres una chica demasiado problemática."
        show dark 2enojao
        $ normal("dark")
        "Como si no hubiera escuchado, desvío la mirada."
        l_thought "Wow, viniendo de ti, eso casi suena a proyección."
return

label rutasuicida_nochoice1:
        $ rutaSuicida += 1
        l "No es problema tuy-{nw}"
        show dark 2distraidot
        $ enfocar("dark")
        d "Olvidalo." 
        show dark 2seriot
        extend " Ya sé la respuesta."
        "Ni siquiera me dejó terminar la oración. Dejando las palabras medio salir."
        d "¿No será qué estás por aquí por estar durmiendote en las clases?"
        show dark 2juzga2t
        d "O en el peor de los casos"
        show dark 2seriot
        extend ", ¿Tuviste algún problema con el profesor y te echaron?"
        d "¿Y por eso casualmente estás por aquí?"
        show dark 2distraidot
        $ normal("dark")
        $ _history = False
        d "{size=18}En verdad... En esta versión eres {i}muy{/i} problematica.{/size}"
        $ _history = True
        show dark 2enojao
        l_thought "¿En esta...{w=0.5} Versión?"
        l_thought "¿Qué carajos dice este?"
        extend " Como sea..."
        l_thought "Esa fue una observación muy... detallada."
        l_thought "Es como si él hubiera estado allí, cuando sé que no."
        l_thought "Por el bien de mi ya deteriorada salud mental, mejor no quiero saber lo que piensa de mí."
        l "¿Mi opinión? Prefiero guardármela para algo que realmente importe."
        l_thought "No tengo energía para dar opiniones hoy. ¿Puedes simplemente dejarme en paz?"
        show dark 2seriot
        $ enfocar("dark")
        d "Sin ofender, pero."
        extend " Eres una chica demasiado problemática."
        show dark 2enojao
        $ normal("dark")
        "Como si no hubiera escuchado, desvío la mirada."
        l_thought "Wow, viniendo de ti, eso casi suena a proyección."
        jump dark_scene_afterchoice1
return

label rutacanon_choice2:
        "Con movimientos torpes, abro la bolsa."
        $ renpy.pause(2.0, hard=True)
        " El olor a... Panqueques... Simple, casero, hecha por papá.{w} Me golpea como una bofetada.{w} Un recordatorio de otra persona a la que estoy defraudando."
        show dark 2enojao
        show jeremy 1juzga
        l "No...{w} No pongas esa cara. No es para tanto."
        show dark 2seriot
        $ enfocar("dark")
        d "Laila, por el amor de Dios."
        show dark 2serio2t
        extend " Come y callate. Deja de pelear."
        show dark 2enojao
        $ normal("dark")
        $ renpy.pause(3.0, hard=True)
        show blaze 1compadecer
        show dark 2desafiante
        show jeremy 1sonriente
        "Tomo el primer bocado."
        $ renpy.pause(3.0, hard=True)
        "Sabe a culpa.{w} Sabe a preocupación.{w} Sabe a tres pares de ojos observándome como si en cualquier momento pudiera romperme."
        $ renpy.pause(2.4, hard=True)
        "Y lo peor es que tal vez tengan razón."
        $ renpy.pause(2.4, hard=True)
        "Cada mordisco que le doy es más pesado que el anterior."
        $ renpy.pause(2.4, hard=True)
        "Siento como mi estomago se revuelve.{w} Como mi bilis sube hasta mi garganta."
        $ renpy.pause(3.5, hard=True)
        "Pero aguanto.{w=0.5} {i}Por ella.{/i}"
        $ renpy.pause(2.4, hard=True)
        l_thought "Ellos no entienden. No es el hambre. Es el peso de saber que mi propio cuerpo se ha convertido en otra batalla que estoy perdiendo."
        l_thought "Comer esto, que me preparaba ella...{w} Se siente como un castigo."
        show blaze 1compadecer at sigh_animation
        "Blaze suspira aliviada."
        show blaze 1compadecert
        b "Al fin..."
        show blaze 1compadecer
        show jeremy 1sonrientet
        $ enfocar("jeremy")
        je "Eso pasa rápido. Pero si quieres seguir sufriendo, vale. No juzgar."
        show jeremy 1sonriente
        $ normal("jeremy")
        "Blaze gira la silla del puesto de Dark y se sienta al frente mio."
        show blaze 1preocupada
        extend " Con una mirada... Triste."
        show blaze 1preocupadat
        b "Papá...{w} se quedó hasta tarde anoche haciéndolos. Dijo que eran tus favoritos."
        show blaze 1preocupada
        l_thought "Otra daga.{w} Otra persona a la que estoy defraudando con mi miseria silenciosa."
        extend " ¿Por qué no pueden entender que a veces el vacío es más seguro que llenarlo con expectativas?"
        $ renpy.pause(4.0, hard=True)
        "Trago.{w} Con dificultad.{w} Trato de evitar sus miradas. Mientras siento como el bilis me quema mi garganta."
        hide screen pulse_black
        l "Ya está.{w} ¿Contentos?"
        show dark 2desafiantet
        $ enfocar("dark")
        d "Contentos no."
        show dark 2felit
        extend " Pero menos propensos a llamar una ambulancia. Lo tomo como un éxito."
        show dark 2feli
        $ normal("dark")
        show blaze 1preocupadat
        b "No se trata de estar contentos, Laila."
        show blaze 1compadecert
        extend " Se trata de que no queremos perderte."
        show blaze 1compadecer at hug2_off
        "Se aleja y exhala profundamente, el peso en sus hombros se aligera un poco."
        show blaze 1compadecert:
                center2
        $ enfocar("blaze")
        b "Prométeme que lo intentarás de nuevo en la cena. Por mí."
        show blaze 1compadecer
        $ normal("blaze")
        l_thought "“Por mí”.{w} Las dos palabras más pesadas del universo."
        l_thought "Porque significan que mi dolor ya no es solo mío.{w} Significa que cada vez que elijo el vacío, elijo herirla a ella también."
        "Jeremy solo me da una sonrisa. Sin decir nada."
return

label rutasuicida_choice2:
        show dark 2serio2
        show jeremy 1serio2
        l "No tengo hambre."
        "Mis dedos se cierran débilmente alrededor de la bolsa, pero no la abro."
        l_thought "Otra expectativa que no puedo cumplir.{w} Otra decepción que estoy cocinando."
        show blaze 1compadecert
        b "Laila, aunque no tengas hambre, necesitas comer algo."
        show blaze 1compadecer
        "Acerca su mano como para ayudarme a abrirla. Pero yo retiro la bolsa hacia mi pecho."
        l "Déjalo...{w} Para después."
        "Mi voz apenas es un hilo de sonido, pero firme en mi negativa."
        $ renpy.pause(3.0, hard=True)
        show blaze 1preocupada
        show jeremy 1serio2t
        $ enfocar("jeremy")
        je "“Para después” suele convertirse en “para nunca”."
        show jeremy 1serio2
        $ normal("jeremy")
        show dark 2seriot
        $ enfocar("dark")
        d "Vamos, no seas dramática."
        show dark 2serio2t
        extend " Son panqueques, no veneno."
        show dark 2serio2
        $ normal("dark")
        "Dark lo dice con sarcasmo...{w} Pero su mirada es más aguda de lo usual."
        show blaze 1preocupadat at sigh_animation
        b "¿Prometes que lo intentarás más tarde? En la cena, al menos..."
        show blaze 1preocupada
        $ renpy.pause(3.5, hard=True)
        "Asiento lentamente, roboticamente, sin ninguna convicción."
        l "Lo...{w} Intentaré."
        l_thought "Incluso para mí... Mis palabras suenan huecas."
        $ renpy.pause(3.0, hard=True)
        l_thought "Otra mentira. Más para la pila.{w} Pero es más fácil que seguir esta pelea."
        "Blaze me mira, buscando en mis ojos alguna señal de verdad.{w} Me limito en evitar su mirada."
        show blaze 2seria2 at hug2_off
        extend " Ellas se aleja, evitando mi mirada."
        show blaze 2seria2t:
                center
        $ enfocar("blaze")
        b "Está bien..."
        "Guarda el desayuno de vuelta en mi mochila."
        show blaze 2compadecert
        b "Pero te lo recordaré."
        show blaze 2seria2
        $ normal("blaze")
        $ renpy.pause(3.0, hard=True)
        "El gesto final de resignación de Blaze duele más que cualquier regaño.{w} Ella sabe que estoy mintiendo, y yo sé que ella lo sabe."
        show dark 2serio2t
        $ enfocar("dark")
        d "Dramatizar es fácil."
        show dark 2distraidot
        d "Morir también."
        show dark 2seriot
        d "Lo difícil es vivir, y parece que ni siquiera lo intentas."
        show dark 2serio
        $ normal("dark")
        l_thought "Ahora tengo a un psicólogo profesional, no, gracias. No quiero cita para hoy."

return

label rutasuicida_nochoice2:
        $ rutaSuicida += 3
        show dark 2serio2
        show jeremy 1serio2
        l "No tengo hambre."
        "Mis dedos se cierran débilmente alrededor de la bolsa, pero no la abro."
        l_thought "Otra expectativa que no puedo cumplir.{w} Otra decepción que estoy cocinando."
        show blaze 1compadecert
        b "Laila, aunque no tengas hambre, necesitas comer algo."
        show blaze 1compadecer
        "Acerca su mano como para ayudarme a abrirla. Pero yo retiro la bolsa hacia mi pecho."
        l "Déjalo...{w} Para después."
        "Mi voz apenas es un hilo de sonido, pero firme en mi negativa."
        $ renpy.pause(3.0, hard=True)
        show blaze 1preocupada
        show jeremy 1serio2t
        $ enfocar("jeremy")
        je "“Para después” suele convertirse en “para nunca”."
        show jeremy 1serio2
        $ normal("jeremy")
        show dark 2seriot
        $ enfocar("dark")
        d "Vamos, no seas dramática."
        show dark 2serio2t
        extend " Son panqueques, no veneno."
        show dark 2serio2
        $ normal("dark")
        "Dark lo dice con sarcasmo...{w} Pero su mirada es más aguda de lo usual."
        show blaze 1preocupadat at sigh_animation
        b "¿Prometes que lo intentarás más tarde? En la cena, al menos..."
        show blaze 1preocupada
        $ renpy.pause(3.5, hard=True)
        "Asiento lentamente, roboticamente, sin ninguna convicción."
        l "Lo...{w} Intentaré."
        l_thought "Incluso para mí... Mis palabras suenan huecas."
        $ renpy.pause(3.0, hard=True)
        l_thought "Otra mentira. Más para la pila.{w} Pero es más fácil que seguir esta pelea."
        "Blaze me mira, buscando en mis ojos alguna señal de verdad.{w} Me limito en evitar su mirada."
        show blaze 2seria2 at hug2_off
        extend " Ellas se aleja, evitando mi mirada."
        show blaze 2seria2t:
                center
        $ enfocar("blaze")
        b "Está bien..."
        "Guarda el desayuno de vuelta en mi mochila."
        show blaze 2compadecert
        b "Pero te lo recordaré."
        show blaze 2seria2
        $ normal("blaze")
        $ renpy.pause(3.0, hard=True)
        "El gesto final de resignación de Blaze duele más que cualquier regaño.{w} Ella sabe que estoy mintiendo, y yo sé que ella lo sabe."
        show dark 2serio2t
        $ enfocar("dark")
        d "Dramatizar es fácil."
        show dark 2distraidot
        d "Morir también."
        show dark 2seriot
        d "Lo difícil es vivir, y parece que ni siquiera lo intentas."
        show dark 2serio
        $ normal("dark")
        l_thought "Ahora tengo a un psicólogo profesional, no, gracias. No quiero cita para hoy."
        $ renpy.pause(5.0, hard=True)
        hide screen pulse_black
        jump receso_day2_afterchoice
return