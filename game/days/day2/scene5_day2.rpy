label scene5_day2:
     
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

    play audio phone_quiet loop
    show blaze 3nerviosa at boo2
    "El teléfono de Blaze vibra en su bolsillo, rompiendo el tenso silencio."
    "Ella se asusta con el sonido, un pequeño salto que delata sus nervios, pero se recompone rápidamente.{w} Y contesta."
    stop audio
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
    play audio bus_arrive fadein 0.5
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
    play audio keylock
    "La cerradura cede con un clic seco, demasiado ruidoso en la calle vacía."
    play audio closet_open
    "Entramos."
    stop ambient fadeout(1.5)
    $ renpy.pause(1.6, hard=True)
    play ambient int_night fadein(2.0)
    scene livingroom_n
    show blaze 1desinteresada3:
        night_purple
        center
    with Fade(0.5, 0.5, 0.5)    
    play audio closet_close
    "La casa está a oscuras. No hay luz en ninguna parte del hogar, ni la televisión encendida, ni sonido de platos desde la cocina. Solo el zumbido bajo y constante del refrigerador y la iluminación de la luna llena que pegaba por una ventana con sus cortinas abiertas."
    "Solo un silencio que pesaba mucho más que cualquier grito de horror."
    play audio light_switch
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
    play audio pageflip
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
    play audio microwave volume 0.05
    "El ruido del microondas encendiéndose abajo me sigue unos peldaños."
    $ renpy.pause(3.5, hard=True)
    stop audio
    "Luego se apaga, absorbido por el silencio."
    $ renpy.pause(1.8, hard=True)
    "Arriba, la oscuridad es lo que más abunda.{w}  Al igual que abajo, la iluminación de la luna se filtra por la ventana, dibujando un rectángulo pálido en el suelo recordando que al menos lo único bello en esta casa es está iluminación. Camino a través de él."
    play audio closet_open
    "Empujo la puerta para entrar a la habitación."
    scene lailaroom_n with Fade(0.3, 0.3, 0.3)
    play audio closet_close
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