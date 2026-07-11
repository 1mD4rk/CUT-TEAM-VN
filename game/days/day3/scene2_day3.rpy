label scene2_day3:
    stop ambient fadeout(1.5)
    scene black with Fade(0.3, 1.0, 0.3)    

    if (rutaCanon-rutaSuicida)>=0:
        "El bus huele a limpia pisos barato y a humedad antigua. Los asientos de vinilo crujen bajo nuestro peso."
        "Blaze se sienta junto a la ventana, yo en el pasillo.{w} Una barrera física mínima entre ella y el mundo, entre nosotras."

        $ renpy.pause(1.0, hard=True)
        play ambient bus fadein(2.0)
        show bus_mask_sky
        show bus_shake
        show blaze 1desinteresada:
            flip
            size (1000, 1300)
            xalign 0.1
            yalign 0.25
            shake_bus
        with dissolve

        $ renpy.pause(3.0, hard=True)
        "La ruta es familiar.{w} Giros conocidos, paradas predecibles."
        "Mis ojos se fijan en el vidrio frío, observando cómo la ciudad pasa en manchas de color desenfocado."
        $ renpy.pause(5.0, hard=True)
        l_thought "Diez minutos más."
        extend " Solo diez minutos más de este tránsito entre la casa que ya no es hogar y la escuela que nunca lo fue."
        $ renpy.pause(4.0, hard=True)
        "Un estudiante de primaria sube con su madre. Lleva una mochila de dinosaurios que es casi más grande que él.  La madre le arregla el cabello con gestos cariñosos, mecánicos.{w} Él se queja, pero sonríe."
        l_thought "Hubo un tiempo en que alguien me arreglaba el cabello así. Sus dedos eran suaves, nunca tiraban."
        extend " Incluso cuando estaba enojada."
        "Aparto la mirada.{w}  El recuerdo duele{w}, pero hoy el dolor es agudo y limpio, no ese dolor sordo y podrido de otros días."
        $ renpy.pause(6.0, hard=True)
        "Blaze saca sus audífonos, pero en lugar de ponerse los dos"
        show blaze 1compadecer
        extend ", me ofrece uno."
        show blaze 1compadecert
        b "¿Quieres?"
        show blaze 1compadecer
        $ renpy.pause(3.0, hard=True)
        l "¿Qué vas a escuchar?"
        "Digo con tono vacilante."
        l_thought "Me tomó..."
        extend " Por sorpresa."
        extend " Me da algo de miedo esto."
        show blaze 1felizt
        b "Algo tranquilo. Nada con letra."
        show blaze 1feliz
        "Tomó el audífono."
        play music bgm11 fadein(2.0) volume 0.6
        extend " La música es instrumental—piano suave, cuerdas lejanas.{w} No dice nada.{w} No exige nada.{w} Solo existe, llenando el silencio sin romperlo."
        window hide
        $ renpy.pause(10.0, hard=True)
        window show
        l_thought "Es un tipo de compañía que no conocía o llevaba tiempo sin tener."
        extend " La que no necesita palabras."
        window hide
        $ renpy.pause(10.0, hard=True)
        window show
        l_thought "Es... Bueno."
        extend " Limpio. No está para nada mal."
        window hide
        $ renpy.pause(8.0, hard=True)
        window show
        show blaze 1felizt
        b "Es bueno ¿no?"
        show blaze 1feliz
        $ renpy.pause(3.0, hard=True)
        l "Es interesante. Me gusta."
        $ renpy.pause(3.0, hard=True)
        "No responde.{w} No necesita hacerlo."
        "El simple hecho de que haya compartido esto, de que haya preguntado, es un puente tendido en un idioma que apenas estamos aprendiendo a hablar."
        window hide
        $ renpy.pause(8.0, hard=True)
        window show
        "El bus frena bruscamente en una parada.{w} Más estudiantes suben. Reconozco algunos rostros de la escuela, pero nadie me mira."
        "Nadie señala."
        "Hoy soy solo otra estudiante en el bus, no la chica del escándalo."
        l_thought "Anonimato."
        extend " Qué concepto extraño. Y qué alivio."
        l_thought "Ya el furro ese me quito todas las ganas que me quedaban para esta semana..."
        $ renpy.pause(8.0, hard=True)
        stop music fadeout(2.0)
        "Le devuelvo el audífono a Blaze.{w} Nuestros dedos se rozan al pasarlo.{w} No es electricidad.{w} Es solo piel contra piel, cálida y humana."
        show blaze 1sonrientet
        b "Casi llegamos."
        show blaze 1sonriente
        "Y es verdad. La silueta de la escuela aparece a lo lejos."
        "Hoy no se siente como una fortaleza enemiga.{w} Solo se siente como un edificio. Piedra, cemento, vidrio."
        "{b}{size=20}“Fallaste.”{/size}{/b}"
        l_thought "El eco está más lejos ahora."
        extend " Ahogado por el sonido del motor y el piano que todavía resuena en mi oído."

    else:
        "El bus huele a limpia pisos barato y a humedad antigua. Los asientos de vinilo crujen bajo nuestro peso.{w} Parece decir “otra vez ustedes”."
        "Blaze se dirige directamente al fondo, a un asiento doble junto a la ventana. No elige el de atrás—ese está ocupado por dos chicas que comparten audífonos y ríen de algo en un teléfono."
        "Tampoco el del medio—ahí hay un estudiante dormido con la boca abierta."
        "Elige el tercero desde el final, el que está justo antes de que el bus se curve hacia la salida de emergencia."
        l_thought "El asiento de los que quieren estar cerca de la salida."
        extend " Los que planean escapar antes de que el incendio llegue."

        $ renpy.pause(1.0, hard=True)
        play ambient bus fadein(2.0)
        show bus_mask_sky
        show bus_shake
        show blaze 1seria2:
            flip
            size (1000, 1300)
            xalign 0.1
            yalign 0.25
            shake_bus
        with dissolve

        "Me siento junto a ella. Nuestros muslos casi no se tocan.{w} Dejo exactamente el espacio necesario para que el frío del plástico del asiento se cuele entre nosotros."
        "Una frontera invisible, pero tangible."
        "El bus arranca con un jalón brusco. Mi cuerpo se inclina hacia adelante, pero mis manos no buscan apoyo."
        $ renpy.pause(1.5, hard=True)
        "Dejo que la inercia me mueva, que me zarandee como a un muñeco roto."
        "Blaze, en cambio, se agarra al asiento delantero, los nudillos blancos."
        $ renpy.pause(8.0, hard=True)
        "Por la ventana, la ciudad pasa como una película mal editada:"
        "Edificios borrosos, farolas apagándose una por una, carteles publicitarios con caras sonrientes que prometen felicidad en forma de refrescos o seguros de vida."
        $ renpy.pause(8.0, hard=True)
        show blaze 1seria2t
        b "Creo que hoy hay junta del consejo después de clases."
        show blaze 1seria2
        "Blaze habla mirando por la ventana, con voz plana."
        $ renpy.pause(1.5, hard=True)
        l "..."
        show blaze 1seria2t
        b "Jeremy quiere presentar la propuesta de los clubes."
        show blaze 1seria2
        l "¿Y a mí qué?"
        show blaze 1seria
        $ renpy.pause(5.0, hard=True)
        show blaze 1seriat
        b "Nada."
        show blaze 1seria2t
        extend " Solo...{w} te lo decía."
        show blaze 1seria2
        "Su voz solo sale más baja. Con cansancio."
        $ renpy.pause(3.0, hard=True)
        "No es verdad. Nada de lo que dice es solo “decir”."
        "Cada palabra es un sondeo, un intento de medir cuánto queda del fondo.{w} Hoy, el fondo parece más cerca que nunca."
        $ renpy.pause(7.0, hard=True)
        "En la fila del frente, dos chicas de primer año susurran y miran hacia atrás.{w} No directamente a mí, sino a mi reflejo en la ventana."
        "Ven los ojos hundidos, el pelo sin cepillar, la postura derrotada.{w} Una de ellas dice algo y la otra sonríe, tapándose la boca."
        l_thought "Ya ni siquiera me molestan. Son parte del paisaje. Como las luces, como los edificios, como el aire que respiro y no quiero."
        "El bus frena en otra parada. Suben más estudiantes. Algunos vienen en grupos, riendo, empujándose."
        "Otros van solos, con auriculares gigantes y miradas fijas en el suelo."
        l_thought "Me pregunto cuántos de esos que van solos escuchan música, y cuántos solo escuchan el mismo silencio que yo."
        $ renpy.pause(2.0, hard=True)
        "El bus reanuda la marcha. Pasamos por un puente peatonal. Abajo, coches forman un río lento de metal y luces rojas."
        $ renpy.pause(4.0, hard=True)
        "Por un segundo absurdo, pienso en cómo sería caer desde aquí. No alto suficiente para morir al instante.{w} Solo para romperme."
        "Para quedar tirada entre el tráfico, otro obstáculo en el camino de todos."
        show screen red_effect2
        nobody "{sc=4}Serías un titular de tres líneas en la sección local.{/sc}"
        nobody "{sc=6}“Estudiante se accidenta”{/sc}"
        nobody "{sc=4}Ni siquiera “se suicida”.{w} Accidentada.{/sc}"
        nobody "{sc=4}Como si tu vida fuera un tropiezo.{/sc}"
        nobody "{sc=4}Y más con el nombre tan destacado de tu padre.{/sc}"
        nobody "{sc=8}Como paso con {b}ella{/b}...{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
        show parpadeo_on
        $ renpy.pause(10.0, hard=True)
        b "Laila."
        show parpadeo_off
        hide parpadeo_on
        show blaze 1seria
        $ renpy.pause(1.5, hard=True)
        l "¿Qué?"
        $ renpy.pause(4.0, hard=True)
        show blaze 1seria2
        $ renpy.pause(0.5, hard=True)
        "Ella simplemente suspira."
        show blaze 1seria2t
        b "Nada."
        show blaze 1seria2
        "Pero su mano, en el asiento entre nosotros, se mueve.{w} No para tomar la mía."
        "Solo se abre, la palma hacia arriba, sobre el plástico rasgado del asiento.{w} Una oferta muda."
        "Un puente tendido por enésima vez sobre un abismo que se ensancha."
        "La miro."
        "Esa mano es todo lo que Blaze es: limpia, con uñas cortas y cuidadas, las líneas de la palma claras y simples."
        "La mano de alguien que todavía cree que los problemas tienen solución."
        $ renpy.pause(3.0, hard=True)
        l_thought "Qué cansado debe ser para ella."
        extend " Tenderme la mano día tras día, sabiendo que nunca la tomaré."
        l_thought "Ser la hermana buena, la fuerte, la que no se rinde."
        extend " Que papel tan agotador."
        $ renpy.pause(6.0, hard=True)
        "No muevo la mía.{w} Dejo que su oferta se pudra allí, en el aire viciado del bus, entre el olor a desinfectante y el runrún del motor."
        $ renpy.pause(1.5, hard=True)
        "Ella retira la mano lentamente.{w} No con rabia.{w} Con una fatiga tan profunda que casi puedo sentirla irradiar desde su cuerpo."
        l_thought "Un día dejará de hacerlo. Un día esa mano no se extenderá."
        extend " Y ese día, quizás, ambas seremos libres."
        $ renpy.pause(3.0, hard=True)
        "El bus se acerca a la escuela.{w} El edificio se alza, sus ventanas reflejando nubes bajas como ojos ciegos."
        "La parada está llena de estudiantes. Algunos nos ven a través del vidrio. Algunos señalan. Otros apartan la mirada."
        "Ella se levanta rápidamente y se limpia como si tuviera polvo."
        show blaze 1seria2t
        b "Vamos."
        show blaze 1seria2
        "La sigo."

    scene black with fade
    stop ambient fadeout(0.5)
    $ renpy.pause(3.0, hard=True)
    play ambient ext_day fadein(2.0)
    scene intersection_day
    show blaze 1neutral:
        center
    with Fade(0.5, 0.0, 0.5)
    $ renpy.pause(1.0, hard=True)
    "Al bajar, mis pies tocan el suelo y siento cómo el mundo se reacomoda a mi alrededor, pesado, sólido, ineludible. El día ha comenzado.{w} Y yo sigo aquí."
    l_thought "Otro día. Otro intento fallido de ser normal. O de dejar de serlo del todo."
    l_thought "¿Cómo se supone que debo sentirme? ¿Aliviada? ¿Decepcionada? No lo sé. Solo sé que no me siento diferente."

    if (rutaCanon-rutaSuicida)<=-1:
        "Y en algún lugar de mi pecho, más fuerte que el latido de mi corazón, la palabra del sueño no es un eco. Es una promesa:"
        show screen red_effect2
        nobody "{sc=4}Pronto. Pronto dejarás de ver todo.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)

    if (rutaCanon-rutaSuicida)>=0:
        "Caminamos hacia la entrada de la escuela, el peso del mundo todavía en mis hombros, pero hoy no es una losa completa."
        "El eco del piano en mi oído parece haber dejado una capa sutil entre yo y el ruido del mundo."
        window hide
        $ renpy.pause(4.0, hard=True)
        scene school_entrance_day
        show blaze 1neutral:
            flip
            left
        with Fade(0.5, 0.0, 0.5)
        window show
        "Justo cuando estamos a punto de cruzar las puertas principales, dos figuras se materializan desde el costado del edificio."
        $ renpy.pause(1.0, hard=True)
        show blaze 1sonriente
        show jeremy 2serio:
            flip
            center
        show dark 1metiche:
            flip
            right5
        with Dissolve(0.5)
        "Dark, con su postura desgarbada y esa sonrisa de gato que atrapó un ratón, y Jeremy, recto y rígido como si tuviera una tabla clavada en la espalda."
        play music bgm12 volume 1.2
        show blaze 1sonrientet
        $ enfocar("blaze")
        b "¡Hola! ¿Nos esperaban?"
        show blaze 1sonriente
        $ normal("blaze")
        show jeremy 2serio at asentir
        "Jeremy asiente con la cabeza, un movimiento brusco y eficiente."
        "Sus ojos pasan por encima de mí, pero hoy no siento que me estén juzgando.{w} Solo evaluando, como un médico que mira un síntoma interesante."
        "Dark, por su parte, no pierde tiempo."
        show dark 1desafiantet
        $ enfocar("dark")
        d "Parece que el espejo ganó la pelea hoy, Laira."
        show dark 2desafiantet
        extend " ¿Le dijiste algo feo o él te lo dijo a ti?"
        show dark 2desafiante
        $ normal("dark")
        "Su tono es burlón, pero no cortante.{w} Hay una curiosidad genuina detrás del sarcasmo, como si realmente quisiera saber la respuesta."
        l_thought "Este idiota... ¿Cómo logra notar eso?"
        extend " ¿Y por qué me importa que lo note?"
        l "El espejo tiene mejores cosas que hacer que pelear conmigo."
        "La respuesta sale sin esfuerzo, casi natural."
        show dark 2juzga
        show blaze 1juzga2
        show jeremy 2serio2
        extend " Dark levanta una ceja, sorprendido."
        extend " Blaze me mira con una mezcla de sorpresa y admiración."
        extend " Jeremy... Bueno, Jeremy no muestra nada en su rostro."
        show dark 2desafiantet
        $ enfocar("dark")
        d "Vaya. Un chiste...{w} ¿A esta hora? ¿Desayunaste algo más que café?"
        show dark 1feli
        $ normal("dark")
        "Sonríe, una media sonrisa que no llega a sus ojos pero tampoco pretende burlarse."
        l_thought "Sí. Desayuné la oferta de mi padre y la música de Blaze.{w} Y por alguna razón, eso parece haber cambiado la química de mi cerebro."
        "Jeremy se acerca a Blaze, ignorando por completo el intercambio.{w} Pero hablando en voz baja, pero lo suficiente para que escuchemos."
        show jeremy 1neutralt
        $ enfocar("jeremy")
        je "Blaze, sobre lo de secretaria..."
        je "Necesitar hablar contigo. Propuesta lista para consejo."
        show jeremy 1sonriente
        $ normal("jeremy")
        show blaze 1feliz
        l_thought "Se le nota algo de cansancio..."
        "Blaze se ilumina visiblemente.{w} Su cansancio matutino se desvanece por un instante."
        show blaze 1felizt
        $ enfocar("blaze")
        b "¿En serio? ¡Eso es increíble!"
        show blaze 1feliz
        $ normal("blaze")
        show jeremy 1sonrientet
        $ enfocar("jeremy")
        je "Y hoy nosotros... Presentar el primer plano para propuesta de clubes."
        je "El director lo verá en el primer recreo."
        show jeremy 1sonriente
        $ normal("jeremy")
        show dark 1distraidot
        $ enfocar("dark")
        d "Menos mal pusimos a estos a hacer ese informe..."
        show dark 1felit
        d "No quedo de maravilla pero está para presentar."
        show dark 1incomodo
        $ normal("dark")
        l_thought "Me imagino que todos esos procesos son cansados."
        extend " Menos mal no me meten a mí en estas cosas..."
        show blaze 1felizt
        $ enfocar("blaze")
        b "¡Perfecto! Tengo los papeles listos."
        show blaze 1feliz
        $ normal("blaze")
        "Ella habla con cierto tono de nerviosismo. Trata de disimularlo, pero yo la conozco muy bien."
        show blaze 1feliz:
            flip_off
            outwalk_right7
        show jeremy 1sonriente:
            outwalk_right6
        "Los dos comienzan a caminar toman la delantera, absortos en la conversación sobre estatutos y responsabilidades."
        $ renpy.pause(5.0, hard=True)
        show dark 2distraido:
            right5_to_center
        $renpy.pause(1.0, hard=True)
        show dark 1distraido:
            center2
        $renpy.pause(1.0, hard=True)
        show dark 1distraido:
            walking_c_normal
        "Jeremy habla con esa torpeza gramatical que lo caracteriza, pero Blaze parece entenderlo perfectamente."
        "Dark y yo nos quedamos atrás, empujados a nuestro propio ritmo por la corriente de estudiantes."
        $renpy.pause(4.0, hard=True)
        "A este se le ve una cara de desinterés, a la dirección a la que fueron Jeremy y Blaze."
        show dark 1juzga2
        $renpy.pause(1.0, hard=True)
        show dark 2desafiante
        extend " Nota que lo veo y cambia su expresión."
        show dark 2desafiantet at walking_c_activo
        d "Así que el robot tiene planes para tu hermana. Interesante."
        show dark 1desafiante at walking_c_normal
        "Camina a mi lado, sus manos metidas en los bolsillos."
        l "¿Y a ti qué te importa?"
        show dark 1felit at walking_c_activo
        d "A mí nada."
        show dark 1juzgat
        extend " Pero a ella sí."
        show dark 1desafiantet
        extend " Y a ti también, aunque finjas que no."
        show dark 1desafiante at walking_c_normal
        show dark 1distraido
        $ renpy.pause(1.5, hard=True)
        "Hace una pausa, mirando cómo Jeremy y Blaze desaparecen entre la multitud."
        show dark 1distraidot at walking_c_activo
        d "Bueno, ya que tu guardaespaldas emocional está ocupada..."
        show dark 2juzgat
        extend " ¿Vas a sobrevivir hasta el recreo o necesitas un manual de emergencia?"
        show dark 2desafiante at walking_c_normal
        l "Creo que hoy puedo manejarlo."
        show dark 1neutral
        "La respuesta me sorprende a mí misma."
        show dark 1metiche
        extend " Dark sonríe, pero esta vez la sonrisa llega a sus ojos. Es breve, apenas un destello, pero está ahí."
        show dark 1sarcasmot at walking_c_activo
        d "Entonces no te molestaré con mis consejos no solicitados. Pero si cambias de opinión..."
        "Señala su bolsillo."
        show dark 2desafiantet
        d "Tengo un suministro de comentarios sarcásticos para todas las ocasiones."
        show dark 2desafiante at walking_c_normal
        show dark 1distraido
        $ renpy.pause(4.5, hard=True)
        show dark 1distraidot at walking_c_activo
        d "Sabes, Laila...{w} A veces la gente que intenta arreglarlo todo es la que más necesita que la arreglen."
        show dark 1distraido at walking_c_normal
        l_thought "¿De qué habla? ¿De Jeremy? ¿De Blaze? ¿O de sí mismo?"
        l "No sé de qué hablas."
        show dark 1desafiantet at walking_c_activo
        d "Claro que lo sabes. Solo que prefieres no saberlo."
        show dark 1desafiante at walking_c_normal
        $ renpy.pause(1.0, hard=True)
        show dark 1feli at walking_c_normal, move_out_right_fast
        "Antes de que pueda responder, se da media vuelta y se pierde entre la multitud, dejándome con el eco de su presencia."
        "Y el piano de Blaze todavía resonando en algún lugar profundo de mi memoria."
        l_thought "Este idiota..."
        extend " ¿Cómo logra hacer que esta mierda sea un poco menos insufrible?"
        "Y por primera vez, la respuesta no duele:"
        "Porque él también está roto. Y los rotos reconocen su propio reflejo."
        play audio bell
        "La campana suena. El día oficialmente comienza.{w} Pero por primera vez en mucho tiempo, no siento el impulso inmediato de buscar un rincón donde esconderme."
        l_thought "Hoy no soy invisible. Solo estoy aquí."
        extend " Y por ahora, eso es suficiente."

    else:
        window hide
        $ renpy.pause(4.0, hard=True)
        scene school_entrance_day
        show blaze 1seria2:
            flip
            left
        with Fade(0.5, 0.0, 0.5)
        "Casi llegando a la escuela, la multitud se densifica. Estudiantes aparecen desde todas las calles, una marea humana que arrastra consigo risas, conversaciones, vida."
        "Blaze y yo somos basura en ese río, pero islotes separados por metros de agua helada."
        $ renpy.pause(1.0, hard=True)
        show blaze 1neutral
        show jeremy 2serio2:
            flip
            center
        show dark 1distraido:
            right5
        "Es entonces cuando los vemos:{w} Jeremy y Dark están parados junto a la estatua del fundador, esa figura de bronce que siempre parece estar juzgando a todos los que pasan."
        $ renpy.pause(1.0, hard=True)
        play music bgm2
        show jeremy 2serio
        "Jeremy nos ve primero. Su expresión—siempre neutral, siempre calculadora—se endurece un grado perceptible cuando su mirada se posa en mí."
        "No es odio.{w} Es peor{w}: es la evaluación fría de un problema que ha superado su categorización inicial."
        "Dark está medio vuelto, hablando con alguien en su teléfono."
        show jeremy 2serio at shake
        $ renpy.pause(1.0, hard=True)
        show dark 1neutral at boo
        $ renpy.pause(1.5, hard=True)
        show dark 1serio:
            flip
        "Pero cuando Jeremy toca su hombro, se da la vuelta.{w}.{w}.{w}."
        "Sus ojos encuentran los míos y se quedan allí por un segundo demasiado largo."
        extend " No hay sorpresa. No hay preocupación.{w} Solo reconocimiento. El reconocimiento de un depredador que ve a otro herido."
        "Los cuatro nos encontramos en el espacio entre la estatua y las puertas principales.{w} No hay saludos."
        show jeremy 1seriot
        $ enfocar("jeremy")
        je "Blaze, llegar...{nw}"
        show jeremy 2serio3 
        $ renpy.pause(1.0, hard=True)
        show jeremy 1seriot
        show dark 1distraido
        extend " Llegaron temprano."
        show jeremy 1serio
        $ normal("jeremy")
        "Su voz es plana, dirigida exclusivamente a ella."
        show blaze 2seria2t
        $ enfocar("blaze")
        b "¿Ah, sí? Bueno, es que...{w} El bus estuvo rápido..."
        show blaze 2seria2
        $ normal("blaze")
        show dark 2serio
        "Su respuesta suena débil, casi una disculpa."
        "Dark no dice nada.{w} Simplemente observa. Sus brazos cruzados sobre el pecho, su postura relajada pero alerta.{w} Como un gato observando a un pájaro con el ala rota."
        $ renpy.pause(3.0, hard=True)
        show blaze 1seria2:
            flip_off
            walking_a_normal
        show jeremy 2serio2:
            walking_b_normal
        show dark 1distraido:
            walking_c_normal
        "Comenzamos a caminar hacia la entrada."
        "Los cuatro en formación incómoda:{w} Jeremy y Blaze adelante, Dark y yo atrás, pero con suficiente distancia como para que cualquiera que nos vea sepa que no vamos juntos."
        $ renpy.pause(8.0, hard=True)
        "El silencio es sofocante.{w} No es el silencio cómodo del bus. Es un silencio cargado, pesado con todo lo no dicho. Con las preguntas no hechas, con las respuestas no ofrecidas."
        $ renpy.pause(5.0, hard=True)
        "Mis pies, todavía entumecidos por el frío de la mañana, tropiezan con un desnivel del pavimento." with hpunch
        show blaze 1neutral at boo:
            flip
            left
        show jeremy 2serio:
            center
        show dark 1juzga2:
            right5
        $ renpy.pause(2.0, hard=True)
        "Por un segundo, nadie se mueve."
        "Entonces Blaze gira la cabeza, sus ojos se ensanchan."
        show blaze 1preocupadat
        $ enfocar("blaze")
        b "¿Estás bien?"
        show blaze 1preocupada
        $ normal("blaze")
        "Su voz suena automática, como si la pregunta fuera parte de un guión que ya ha recitado demasiadas veces."
        show dark 1distraido2
        $ inac("jeremy")
        "Jeremy ni siquiera voltea."
        show jeremy 2serio2:
            walking_b_inactive
        extend " Sigue caminando, su espalda rígida, sus pasos medidos."
        "Dark se detiene, pero no se acerca.{w} Solo mira, con esa expresión inescrutable que parece decir “¿Y qué esperabas?”."
        l "Sí."
        show blaze 1compadecer
        "La palabra sale áspera, cortante. “Estoy perfecta.”"
        l_thought "¿Qué se supone que debo decir? ¿“No, no estás perfecta, estás herida y eso es normal”? No, eso suena como algo que diría un psicólogo barato en una película mala."
        l_thought "..."
        l_thought "Este silencio es más ruidoso que cualquier insulto. Preferiría que me gritaran. Preferiría que me dijeran directamente lo que todos piensan{w}: que soy un lastre, un problema, una mancha en su grupo perfecto."
        "Dark finalmente habla, pero no a mí.{w} A Blaze."
        show dark 1distraidot
        $ enfocar("dark")
        d "Iremos a llegar tarde si seguimos a este ritmo. No lo digo como queja."
        show dark 1distraido
        $ normal("dark")
        show dark 1distraido at walking_c_inactive
        show blaze 1preocupada
        "Blaze me lanza una última mirada—una mezcla de preocupación, frustración y algo que se parece mucho a resignación—."
        show blaze 1desinteresada3 at walking_a_inactive
        "Antes de seguirlos."
        "Me quedo atrás, viendo cómo los tres se alejan, pero empiezo a caminar, lejos de ellos."
        l_thought "Y así es como se ve el abandono:"
        extend " no con portazos, sino con pasos que se alejan mientras tú te quedas parada, preguntándote si alguna vez estuvieron realmente a tu lado."
        show screen red_effect2
        nobody "{sc=4}Y cuando te vayas, ni siquiera lo notarán.{/sc}"
        nobody "{sc=6}Como si nunca hubieras estado ahí.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
        l_thought "¿Y sabes qué? Probablemente tengan razón. La promesa del sueño vuelve, más clara ahora."
        hide dark with Dissolve(0.5)
        hide jeremy with Dissolve(0.5)
        hide blaze with Dissolve(0.5)
        l_thought "{i}No es una amenaza. Es una oferta.{/i}"
        "Y por primera vez, no la rechazo inmediatamente."
        "Solo la dejo estar, flotando en el aire frío de la mañana, mientras entro sola al edificio que ha dejado de ser una prisión para convertirse en algo peor: un vestíbulo de espera."

    window hide
    stop music fadeout 4.5
    stop ambient fadeout(4.5)
    scene black with dissolve_scene_full3

return    