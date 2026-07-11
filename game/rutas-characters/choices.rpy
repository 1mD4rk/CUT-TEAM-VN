######################## Day 1 #############################

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

######################## Day 2 #############################

label rutacanon_choice2:
        "Con movimientos torpes, abro la bolsa."
        $ renpy.pause(2.0, hard=True)
        "El olor a... Panqueques... Simple, casero, hecha por papá.{w} Me golpea como una bofetada.{w} Un recordatorio de otra persona a la que estoy defraudando."
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
        je "Va a pasar rápido. Pero si quieres seguir así, vale. No... juzgar."
        show jeremy 1sonriente
        $ normal("jeremy")
        "Blaze gira la silla del puesto de Dark y se sienta al frente mio."
        show blaze 1preocupada
        extend " Con una mirada... Triste."
        show blaze 1preocupadat
        b "Papá...{w} Se levantó temprano para poder hacerlos. Dijo que eran tus favoritos."
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
        je "Créedme que él “después”... Es hábito de nunca."
        show jeremy 1serio2
        $ normal("jeremy")
        "Jeremy solo sale con un sermón barato de que debo de cumplir con lo que digo..."
        l_thought "¿Acaso le pregunté su opinión?"
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
        je "Créedme que él “después”... Es hábito de nunca."
        show jeremy 1serio2
        $ normal("jeremy")
        "Jeremy solo sale con un sermón barato de que debo de cumplir con lo que digo..."
        l_thought "¿Acaso le pregunté su opinión?"
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

######################## Day 3 #############################

label rutacanon_choice3:
        "Luego, sin decidirlo del todo, mis dedos se cierran alrededor de la porcelana."
        "Por un momento, solo siento el frío. El contraste.{w} El “todavía puedo apartarme”."
        "Pero luego el calor comienza a filtrarse, lento, persistente."
        "No quema.{w} No lastima.{w} Solo existe.{w} Como {i}ella{/i}."
        "Como este recuerdo que no pedí pero tampoco rechazo."
        show black with Fade(0.5, 0.5, 0.5)
        $ renpy.pause(0.9, hard=True)
        "Una imagen: ella en esta misma cocina, inclinada sobre su taza."
        "Me sonreía por encima del borde, sus ojos entrecerrados por el sueño o la felicidad{w}—nunca supe cuál."
        "“Buenos días, mi niña”, decía siempre."
        "Como un mantra que creí olvidado y que ahora vuelve sin permiso. como un mantra que creí olvidado."
        $ renpy.pause(0.9, hard=True)
        dad "Disculpa por ayer."
        hide black with Fade(0.5, 0.5, 0.5)
        "La voz de papá me devuelve al presente. Pero esta vez no suena como un intruso. Suena como alguien que también está aprendiendo."
        show counter 1compadecert
        $ enfocar("counter")
        dad "La emergencia en el trabajo fue..."
        show counter 1distraido2t
        extend " Más larga de lo esperado."
        show counter 1compadecer
        $ normal("counter")
        $ renpy.pause(1.2, hard=True)
        "Pausa."
        show counter 1seriot
        $ enfocar("counter")
        dad "No era mi intención dejarte plantada."
        show counter 1compadecer
        $ normal("counter")
        "No espera respuesta. No pide perdón abiertamente.{w} No sabe hacerlo. Pero lo intenta. A su manera."
        "Y eso, de alguna forma, es más sincero que cualquier “lo siento” ensayado."
        show counter 1enojao2
        "Su mandíbula, siempre tensa como un resorte a punto de saltar, se relaja apenas visiblemente. La veo. Él no sabe que la veo."
        "Tomo un sorbo.{w} El café está amargo.{w} Exactamente como a {i}ella{/i} le gustaba. No como a mí."
        "Pero hoy el amargor no me parece un castigo. Me sabe a verdad. A algo auténtico. A {i}ella{/i}."
        l_thought "Las manos calientes...{w} Quizás tenía razón."
        l_thought "Quizás algunas batallas se libran mejor con una taza entre las manos."
        $ renpy.pause(2.0, hard=True)
        "Mis dedos aún sienten el calor. No es un triunfo. Es solo un gesto.{w} Una pequeña rendición. Pero es algo."
        $ renpy.pause(5.0, hard=True)
        "Mientras tomo otro sorbo, mis ojos encuentran algo en el borde de la mesa."
        show counter 1distraido
        "Una pequeña flor seca.{w} Amarillenta.{w} Frágil.{w} Pegada con cinta adhesiva transparente a la madera."
        "Una de las margaritas que ma—..."
        extend " {i}Ella{/i} coleccionaba en primavera."
        "Papá no la ha retirado. Ni siquiera la ha movido."
        l_thought "La ve todos los días. Cada mañana. Cada desayuno. Y no la tira."
        l_thought "¿O solo es otro fantasma que aprendió a vivir?"
        $ renpy.pause(2.0, hard=True)
        l_thought "No es un fantasma. Es una decisión. Una pequeña. Insignificante para cualquiera. Pero para él..."
        l_thought "Es todo lo que le queda de ella."
        $ renpy.pause(4.0, hard=True)
        "Termino el café y dejo la taza vacía en el fregadero.{w} El tintineo de la porcelana contra el acero es el único sonido en la cocina."
        "Papá ya se está preparando para irse. Dobla el periódico con movimientos precisos, como si cada pliegue fuera una orden. Lo deja en la mesa. Recoge su portafolios."
        show counter 1seriot
        $ enfocar("counter")
        dad "Ya sabes, Laila. Nos vemos después de la escuela."
        show counter 1serio
        $ normal("counter")
        l_thought "¿Después? ¿Hoy sí?"
        "No lo dice como una pregunta. Es una afirmación. Una promesa. Y por alguna razón, esta vez quiero creerle."
        l "S-Sí, claro."
        show counter 1distraido at outwalk_right5
        $ renpy.pause(8.0, hard=True)
        "Papá ya se fue. El motor del auto se pierde en la distancia. Pero la cocina aún guarda su presencia."
        "El periódico doblado con precisión militar. La silla está empujada perfectamente bajo la mesa. Y ahora, esta taza vacía que acepté."
        l_thought "Una taza de café. Una flor seca. Una promesa frágil."
        hide counter
        l_thought "No es mucho. Pero es más de lo que tuve ayer."
return

label rutasuicida_choice3:
        l "No—"
        show counter 1surprise
        "La palabra sale más áspera de lo que pretendía. La taza se tambalea y se voltea la taza, el café oscuro se derrama."
        "El periódico abierto es la pobre víctima, manchando titulares sobre cosas que no me interesan pero que a papá le importan más que esta escena."
        "Una mancha marrón se expande sobre el periodico."
        "Me quedo mirando al café derramado, sin saber que hacer."
        show screen red_effect2
        nobody "{sc=3}¿Ves? Hasta rechazas la ayuda de tu padre.{/sc}"
        nobody "{sc=5}Y para rematar, la cagas.{/sc}"
        hide screen red_effect2
        $ renpy.pause(0.5, hard=True)
        show counter 1serio
        "Lo miro. Papá no dice nada. Su mandíbula se tensa de nuevo."
        $ renpy.pause(6.0, hard=True)
        "Guarda el periódico con movimientos precisos, como si cada doblez fuera una represión calculada.{w} Recoge su portafolio del suelo, el cuero gastado crujiendo bajo su agarre."
        "Se levanta. Su sombra me cubre por un instante."
        show counter 1distraido2t
        $ enfocar("counter")
        dad "Ya sabes, Laila. Nos vemos después de la escuela."
        show counter 1serio
        $ normal("counter")
        "No es una sugerencia. Es una orden fría, disfrazada de despedida."
        show counter 1serio at outwalk_right5
        "Da media vuelta y se va, sus pasos resonando en el pasillo hasta que la puerta principal se cierra con un clic definitivo."
        $ renpy.pause(7.0, hard=True)
        "Quedo sola en la cocina, el aroma a café ahora me parece agresivo, un recordatorio de lo que rechacé."
        "Del puente que volví a quemar."
        $ renpy.pause(1.0, hard=True)
        "Suspiro."
        hide counter
        l_thought "Siempre igual. Yo rechazo, él se va."
        extend " Un baile perfecto de distancias."
return

label rutasuicida_nochoice3:
        l "No—"
        show counter 1surprise
        "La palabra sale más áspera de lo que pretendía. La taza se tambalea y se voltea la taza, el café oscuro se derrama."
        "El periódico abierto es la pobre víctima, manchando titulares sobre cosas que no me interesan pero que a papá le importan más que esta escena."
        "Una mancha marrón se expande sobre el periodico."
        "Me quedo mirando al café derramado, sin saber que hacer."
        show screen red_effect2
        nobody "{sc=3}¿Ves? Hasta rechazas la ayuda de tu padre.{/sc}"
        nobody "{sc=5}Y para rematar, la cagas.{/sc}"
        hide screen red_effect2
        $ renpy.pause(0.5, hard=True)
        show counter 1serio
        "Lo miro. Papá no dice nada. Su mandíbula se tensa de nuevo."
        $ renpy.pause(6.0, hard=True)
        "Guarda el periódico con movimientos precisos, como si cada doblez fuera una represión calculada.{w} Recoge su portafolio del suelo, el cuero gastado crujiendo bajo su agarre."
        "Se levanta. Su sombra me cubre por un instante."
        show counter 1distraido2t
        $ enfocar("counter")
        dad "Ya sabes, Laila. Nos vemos después de la escuela."
        show counter 1serio
        $ normal("counter")
        "No es una sugerencia. Es una orden fría, disfrazada de despedida."
        show counter 1serio at outwalk_right5
        "Da media vuelta y se va, sus pasos resonando en el pasillo hasta que la puerta principal se cierra con un clic definitivo."
        $ renpy.pause(7.0, hard=True)
        "Quedo sola en la cocina, el aroma a café ahora me parece agresivo, un recordatorio de lo que rechacé."
        "Del puente que volví a quemar."
        $ renpy.pause(1.0, hard=True)
        "Suspiro."
        hide counter
        l_thought "Siempre igual. Yo rechazo, él se va."
        extend " Un baile perfecto de distancias."
return