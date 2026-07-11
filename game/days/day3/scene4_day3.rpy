image dark parpadeo_sorpresa:
    "dark 1blink"
    pause 0.08
    "dark 1neutral"
    pause 0.08
    "dark 1blink"
    pause 0.08
    "dark 1neutral"
    pause 1.0
    "dark 1blink"
    pause 0.08
    "dark 1neutral"

image dark guinio:
    "dark 1guinio"
    pause 0.095
    "dark 1feli"

image blinking_moment:
    "parpadeo_on"
    pause 0.200
    "parpadeo_off"

image steve parpadeo_sorpresa:
    "steve 1blink"
    pause 0.08
    "steve 1neutral"
    pause 0.08
    "steve 1blink"
    pause 0.08
    "steve 1neutral"

label scene4_day3:

    scene class3A
    $ quick_menu = True
    play audio bell

    if (rutaCanon-rutaSuicida)>=0:
        window show
        "El timbre corta el silencio como un cuchillo.{w} A mi alrededor, sillas chirrían, mochilas se cierran, voces se elevan en alivio colectivo."
        "A mi alrededor, el caos se organiza.{w} Risas. Empujones. Planes para el receso que no me incluyen."
        show jeremy 1serio with Dissolve(0.3):
            flip
            right5
        "Jeremy se levanta primero, ajustando su mochila con esa precisión militar que parece innata en él."
        $ enfocar("jeremy")
        show jeremy 1sonrientet
        je "Blaze, vamos.{w} Revisar el puesto y solicitud de clubes, recordar."
        show jeremy 1sonriente
        $ normal("jeremy")
        show blaze 1feliz with Dissolve(0.2):
            center2
        $ renpy.pause(2.5, hard=True)
        show blaze 1sonriente
        $ renpy.pause(2.5, hard=True)   
        show blaze 1preocupada
        "Blaze se voltea a verme, veo algo de duda en sus ojos."
        show blaze 1compadecert
        $ enfocar("blaze")
        b "¿Vienes, Laila?"
        show blaze 1compadecer
        $ normal("blaze")
        l_thought "..."
        l_thought "Parece que siempre soy la sombra de ella, o su cola."
        extend " Siempre voy con ella a todos lados..."
        extend " Realmente, no quiero, por esta vez."
        "Muevo la cabeza, apenas un gesto.{w} No tengo fuerzas para seguirles."
        show blaze 2preocupada2 at asentir
        show jeremy 1juzga
        "Ella asiente, con algo de duda."
        show blaze 1compadecert
        $ enfocar("blaze")
        b "Okay...{w} ¡Te veré en la siguiente clase!"
        show blaze 1compadecer
        $ normal("blaze")
        $ renpy.pause(2.5, hard=True)
        show blaze 2preocupada2: 
            outwalk_right8
        "Ella sale rápidamente del aula. Sin decir nada más. Supongo que no era necesario."
        show jeremy 2serio2t
        $ enfocar("jeremy")
        je "Supongo que ya nos vamos entonces..."
        show jeremy 2seriot
        je "Y Dark. Por favor... cerrar el salón ¿de acuerdo?, no queremos otro regaño por olvidar eso."
        show jeremy 2serio
        $ normal("jeremy")
        show dark 1distraido3 with Dissolve(0.2)
        $ renpy.pause(1.2, hard=True)
        show dark 1distraido2
        "Dark lo mira algo neutral{nw}"
        show dark 1distraido2:
            asentir
        extend " y simplemente asiente, sin decir ni una sola palabra."
        show jeremy 1serio2:
            xanchor 0.5 yanchor 1.0
            parallel:
                ease 5.0 xpos -400
            parallel:
                block:
                    ease 0.5 yoffset 15
                    ease 0.21 yoffset 0
                    repeat 11
                yoffset 0
        "Jeremy se va, automático, sin mostrar ningún tipo de emoción en su rostro. Como siempre."
        show dark 1distraido
        $ renpy.pause(4.5, hard=True)
        hide jeremy
        hide blaze
        l_thought "Blaze... Se fue..."
        extend " Simplemente se fue con él."
        l_thought "¿Será que me odia? ¿Soy una carga para su círculo social?"
        l_thought "Aunque... Es algo egoísta pensar que se quedaría conmigo..."
        l_thought "Realmente, soy egoísta. Una simple y asquerosa egoísta."
        $ renpy.pause(1.2, hard=True)
        l_thought "¿Por qué me sorprendo...?"
        extend " Siempre he sido así, siempre he sido la sombra de los demás, la que se queda atrás, la que no tiene voz ni opinión."
        l_thought "Es lo que soy, una persona patética."
        show vignette at vineta_organico zorder 100
        "Mi dolor de cabeza aumenta poco a poco, siento como si me estuvieran pegando con un bate en la nuca."
        show screen red_effect2
        nobody "{sc=4}{b}¿Ya ves?{/b}{/sc}"
        show dark 1juzga2
        nobody "{sc=4}¿Que ella solo esperaba el momento para irse?{/sc}"
        nobody "{sc=5}Tarde o temprano iba a pas—{/sc}{nw=0.5}"
        hide screen red_effect2
        hide vignette
        play music bgm1
        show dark 1distraido2t
        $ enfocar("dark")
        d "—A pasar."
        show dark 2distraido2
        $ normal("dark")
        "La voz de Dark cortó el pensamiento intrusivo como un cuchillo.{w} No era su tono burlón de siempre.{w} Era plano, directo."
        show dark 2distraido2t
        $ enfocar("dark")
        d "Lo ibas a pensar.{w} Que ella solo esperaba la excusa."
        show dark 2distraido2
        $ normal("dark")
        $ renpy.pause(3.0, hard=True)
        show dark 1seriot
        $ enfocar("dark")
        d "Vaya. Parece que hoy sí logré quedarme con el premio de consolación."
        show dark 1serio
        $ normal("dark")
        "Su tono recupera el sarcasmo, pero sus ojos permanecen serios.{w} No sonríen. Solo observan."
        $ renpy.pause(2.5, hard=True)
        l_thought "¿Por qué se quedó?"
        extend " Jeremy le pidió cerrar el salón, pero eso toma 30 segundos, no 10 minutos."
        show dark 2distraido2t
        $ enfocar("dark")
        d "Sí, me podría haber ido."
        show dark 1incomodot
        extend " Pero si no me invitan, quién soy yo para ir sin permiso?"
        show dark 1incomodo
        $ normal("dark")
        l_thought "—-!!?"
        l "¿No tienes nada mejor que hacer, vicepresidente?"
        show dark 1incomodot
        $ enfocar("dark")
        d "Siempre hay algo mejor que hacer."
        show dark 2desafiantet
        extend " Pero a veces lo interesante está justo aquí."
        show dark 2serio
        $ normal("dark")
        "Él está sentado en el puesto de Blaze, reclinado en su silla, observándome con una mirada que no lograba descifrar."
        "No era lástima. Era...{w} No lo sé."
        $ renpy.pause(3.0, hard=True)
        show dark 2juzga2t
        $ enfocar("dark")
        d "¿Problemas en el paraíso mental? Eso es lo que veo. Rebuscas cosas que ni siquiera hay."
        show dark 1serio
        $ normal("dark")
        "La voz de Dark era un susurro cortante a mi lado."
        l "Realmente te pido que te calles, Dark."
        "Artículo eso con un susurro. Esperando que pare."
        show dark 1neutralt
        $ enfocar("dark")
        d "No. En serio.{w} Tienes la cara de quien acaba de ver un tiroteo."
        show dark 1distraidot
        d "Y ella se fue hace..."
        show dark 2juzga2t
        d "¿3 minutos?"
        show dark 2juzga2
        $ normal("dark")
        "Ahora, se instala un silencio incómodo."
        $ renpy.pause(5.0, hard=True)
        show dark 1neutralt
        $ enfocar("dark")
        d "Ella no te odia, ¿sabes?"
        show dark 1neutral
        $ normal("dark")
        l_thought "¿Y tú qué sabes de la frustración de {b}mi{/b} hermana?"
        l "No actúes como si la {b}{i}conocieras{/i}{/b}."
        show dark 2desafiante
        "Dije con más amargura de lo que pretendía."
        "Dark no se inmutó. Al contrario, un destello de esa sonrisa burlona volvió a sus labios, pero esta vez no llegaba a sus ojos."
        show dark 1felit
        $ enfocar("dark")
        d "No la conozco como tú, obvio."
        show dark 2seriot
        extend " A pesar de todo lo que sigue pasando..."
        l_thought "Eso último sonó más fuerte... Se le fue lo burlón un momento"
        show dark 1felit
        d "Pero es como un estereotipo.{w} La chica responsable, la hermana que intenta mantener a flote a su otra hermana.{w} La que sonríe para que nadie pregunte cómo está."
        d "Todos somos estereotipos hasta que alguien decide vernos como personas."
        show dark 1incomodot
        d "Toma el ejemplo de que, a pesar de que es algo del consejo, me dejaron atrás."
        show dark 1feli
        $ enfocar("dark")
        l_thought "¿De qué habla? ¿Acaso se fumó algo? ¿O ya se volvió más loco que la mierda?"
        l_thought "“La hermana que intenta mantener a flote a su otra hermana.”..."
        l_thought "¿Será que Blaze se cansara de mí?"
        l_thought "Aunque recién noto eso un punto... No le dijeron para ir con ellos."
        "Un nuevo miedo se instala, pero Dark sigue hablando."
        show dark 1felit
        $ enfocar("dark")
        d "Mira, Blaze es la hermana que sostiene el mundo. Tú eres la que lo hace pedazos. Jeremy es el que intenta ser el “presidente perfecto”."
        "Marca el “presidente perfecto” entre muchas comillas."
        l_thought "Supongo que se limitó a contar cosas de este último…"
        l_thought "Pero ¿Presidente perfecto? ¿Qué mierda es eso? ¿Acaso Jeremy es un presidente? ¿O es solo un título que se le dio por ser el más popular del consejo estudiantil?"
        show dark 2distraido2t
        d "Lo único que sé es que sobramos. Los dos. Por diferentes razones, pero sobramos."
        show dark 1incomodo
        $ normal("dark")
        "Eso lo siento caer como un balde de agua fría.{w} No lo esperaba. Pero no porque me sorprenda la verdad. Me sorprende que él la haya dicho en voz alta."
        l_thought "“Sobramos.” Qué palabra tan fea. Tan exacta. Tan..."
        extend " final."
        l_thought "Como si no hubiera vuelta atrás. Como si ya no quedará nada que hacer para dejar de sobrar."
        l_thought "Y lo peor es que no puedo decirle que está equivocado."
        extend " Porque si le digo que no sobra, tendría que creer que yo tampoco."
        l_thought "Y no sé si estoy lista para creer eso."
        l_thought "Supongo que no era necesario tanta sinceridad..."
        l_thought "Aunque... Él sigue haciendo mucho hincapié en que no lo llevaron..."
        extend " Raro para una persona como él. Raro que alguien tan orgulloso admita que le duele quedarse fuera."
        l_thought "O tal vez por eso puede decirlo. Porque conmigo no tiene que fingir..."
        extend " No creo que sea eso, es muy improbable y raro."
        l "¿No tienes deberes de vicepresidente que hacer? ¿Persuadir a alguien para que limpie la cafetería o algo?"
        "Trato de hacer que se enoje y se vaya, pero parece que hablo con la pared."
        show dark 2desafiantet
        $ enfocar("dark")
        d "Huir a veces no funciona, si te funcionó otras veces fue por casualidad."
        show dark 2desafiante
        $ normal("dark")
        "Su tono era casual, pero su mirada no se despegaba de mí."
        l "No estoy huyendo.{w} ¿Qué sabes tú lo que funciona o no?"
        $ renpy.pause(1.0, hard=True)
        "Me levanté, dispuesta a refugiarme en el baño de mujeres más lejano, pero su siguiente palabra me detuvo en seco."
        show dark 2seriot
        $ enfocar("dark")
        d "Laila."
        show dark 2serio
        $ normal("dark")
        "La llamada suena autoritaria.{w} Voz que rara vez hace desde ayer. Me di la vuelta, desafiante."
        show dark 2serio:
            sigh_animation
        "Suspira."
        show dark 2serio2t
        $ enfocar("dark")
        d "Mi punto es, en verdad no entiendo por lo que pasas, pero eso no justifica que a veces la gente no entienda por qué disparas a todos los que se acercan."
        show dark 2seriot
        d "Incluso si solo quieren ayudar."
        show dark 1serio
        $ normal("dark")
        l "¿Y tú qué sabes de mis disparos?{w} ¡¿QUÉ PUTAS SABES?!"
        "Mis palabras suenan huecas incluso para mí. Mis puños se apretaron. Cada músculo listo para atacar o huir."
        "Pero Dark solo esperaba, con esa paciencia que no le conocía."
        show dark 2seriot
        $ enfocar("dark")
        d "No tengo que saber. Solo tengo que ver."
        show dark 2serio
        $ normal("dark")
        "Algo en su tono—no piedad, sino reconocimiento—me desarmó."
        "La rabia se desinfló, dejando solo el vacío que siempre estuvo allí."
        show dark 1distraido3
        "Señala a la puerta, donde hace pocos minutos Jeremy y Blaze se fueron."
        show dark 1seriot
        $ enfocar("dark")
        d "Sé que la pareja se acaba de ir, que por cierto, ahí está al que insultaste ayer gratuitamente..."
        show dark 1neutralt
        d "Y simplemente lo hizo porque iba con él. No porque te odie o te quiera dejar sola."
        show dark 1seriot
        extend " Eso es algo que ya tú estás exagerando, dramática."
        show dark 2neutralt
        d "Ella te ama, Laila. A pesar de todo."
        d "Y tú aquí, jugando a la víctima porque se fue a hacer algo sin ti."
        show dark 2seriot
        d "Patético, pero comprensible."
        show dark 2distraidot
        d "No te juzgo."
        show dark 1incomodo
        $ normal("dark")
        "Sus palabras resonaron en el silencio del aula vacía, encontrando un eco en el vacío que sentía en el pecho."
        "Ya no había burla en su voz. Era un hecho. Una advertencia."
        $ renpy.pause(3.0, hard=True)
        l_thought "El amor... ¿El amor de quién?"
        extend " ¿El de mi papá? ¿El de Blaze?"
        extend " ¿O el mío propio, que se ha convertido en puro veneno?"
        "Miré a Dark. Realmente lo miré."
        "Ya no era un arrogante, un provocador.{w} Era alguien que, por la razón que fuese, había decidido quedarse en un salón vacío para decirme verdades que nadie más se atrevía a mencionar."
        l "¿Y tú? ¿Qué...{w} Qué estereotipo eres tú?"
        show dark 1neutral:
            shake2
        "La pregunta surgió sin filtro."
        show dark parpadeo_sorpresa
        extend " Él parpadeó, ligeramente sorprendido."
        show dark 1desafiante
        "Esbozó su sonrisa habitual, pero esta vez fue más lenta... Más pensativa."
        show dark 2serio2t
        $ enfocar("dark")
        d "Yo qué sé."
        show dark 2seriot
        extend " El que se queda callado cuando debería hablar."
        show dark 2desafiantet
        extend " El que habla cuando debería quedarse callado."
        show dark 1incomodot
        extend " El que está, pero no importa."
        show dark 1feli
        $ normal("dark")
        "Se encoge de hombros, como si restara importancia, pero sus palabras tenían un peso nuevo."
        l_thought "Se está describiendo a sí mismo..."
        extend " Para que yo me sienta menos sola."
        "Tomo aire, para tratar de comprender esta conversación.{w} Sintiendo como poco a poco el ambiente se siente cómodo."
        show dark 2distraido3
        $ renpy.pause(3.5, hard=True)
        show dark 2desafiantet
        $ enfocar("dark")
        d "En fin, creo que no debemos estar mucho tiempo aquí, Laira."
        show dark 1sarcasmot
        extend " Los rumores se esparcen como pólvora."
        $ normal("dark")
        show dark 1sarcasmo
        "Dice con una sonrisa burlona. Sabiendo que me irrita que me llame así."
        l "¿Tú y yo? ¿En una clase de chisme así? Jamás."
        show dark 1sarcasmot
        $ enfocar("dark")
        d "Jaja."
        show dark 1seriot
        d "Y en verdad no creo que quieras escuchar unos de los discursos de Jeremy."
        show dark 1serio2t
        extend " No tengo ganas de escucharlo en lo que queda de hora."
        $ normal("dark")
        show dark 1serio
        "Se ríe algo seco al decir eso."
        $ renpy.pause(2.5, hard=True)
        "Recogemos nuestras cosas lentamente y salimos del aula."
        scene black
        scene pasillo
        show dark 1distraido
        with Fade(0.5, 0.9, 0.5)
        play ambient school_hallway fadein(2.0) volume 0.75
        "Yo salgo primero, dejando que él salga de último para cerrar el salón."
        l_thought "Él sonó muy sincero sobre todo eso..."
        extend " Quizás debo hablar con un poco de sinceridad también."
        l "No sé qué pienso del amor..."
        "La confesión sale en un susurro, aprovechando que está de espaldas cerrando la puerta."
        l "Pero le tengo miedo al odio.{w} Al de las personas que más—"
        show dark 1neutral:
            boo3
        "Las palabras se atoran, ahogadas por un nudo de lágrimas que me niego a soltar."
        l_thought "Es lo más honesto que he dicho en meses."
        extend " Y se lo dije a él, de todas las personas."
        "Dark no respondió de inmediato."
        play audio keylock
        $ renpy.pause(0.8, hard=True)
        extend " Terminó de cerrar la puerta y la cerró con un clic suave, cumpliendo con el encargo de Jeremy."
        show dark 1felit
        $ enfocar("dark")
        d "Bueno toma eso como un comienzo."
        $ normal("dark")
        show dark 1feli
        l_thought "Un comienzo... ¿Para qué?"
        "Nos quedamos en silencio, sin nada que decir, ni saber a dónde ir."
        show dark 2distraido
        $ renpy.pause(2.5, hard=True)
        show dark 2distraidot
        $ enfocar("dark")
        d "De todas formas..."
        show dark 2felit
        extend " ¿Tienes celular?"
        show dark 2feli
        $ normal("dark")
        "La pregunta me desconcierta. Un interrogante tan básico que resulta ofensivo en este contexto.{w} Me desconcierta y, de paso, me irrita."
        l "Eh... ¿Obviamente?"
        l_thought "¿Qué clases de preguntas son esas? ¿Y para qué pregunta?"
        show dark 2felit
        $ enfocar("dark")
        d "Pasame tu número."
        show dark 2desafiantet
        extend " Por si te vuelves a meter en problemas y necesitas que alguien con autoridad dudosa te rescate."
        show dark 2desafiante
        $ normal("dark")
        l "¿Autoridad dudosa?"
        show dark 2sarcasmot
        $ enfocar("dark")
        d "Vicepresidente, bombón.{w} Por si te vuelves a meter en problemas y necesitas que alguien con autoridad dudosa te rescate."
        show dark 2sarcasmo
        $ normal("dark")
        show dark guinio
        "Dice guiñando el ojo mientras saca su teléfono."
        extend " Su pregunta me deja completamente sin palabras.{w} Era lo último que me esperaba."
        show dark 1incomodot
        $ enfocar("dark")
        d "Mi reputación con el director ya está por los suelos después de tu escape."
        show dark 2desafiantet
        extend " Considérame un... Contacto estratégico."
        show dark 2desafiante
        $ normal("dark")
        l_thought "¿Debería tener su número? Literalmente me confesó que lo metí en un problema."
        extend " Y aun me siento culpable por eso."
        "Suspiro."
        l "Supongo que está bien..."
        "Sacó mi teléfono del bolsillo.{w} Mis dedos dudan sobre la pantalla.{w} Darle mi número significa aceptar que alguien podría querer llamarme.{w} O que yo podría querer llamar a alguien.{w} Dudo de esto último."
        $ renpy.pause(2.5, hard=True)
        "Ya nos dimos la información para el contacto.{w} No lo pensé mucho, ni siquiera sé qué pasó."
        "Pero antes de darle el botón de “Guardar contacto” una idea pasa por mi cabeza."
        l "¿Y tu nombre?"
        show dark 2juzga2
        "Dark me mira confundido."
        l "Para el contacto, idiota.{w} No voy a poner “Vicepresidente Pendejo”."
        show dark 2desafiantet
        $ enfocar("dark")
        d "Pues dejalo como Dark, mujer."
        show dark 2desafiante
        $ normal("dark")
        "Eso último lo dice con tono burlón. Me irrita."
        l_thought "Me sigue pareciendo ridículo que Dark sea su nombre."
        "Miro mi teléfono y luego lo miro.{w} Lo examino un segundo. No sé qué busco."
        "Tal vez una grieta en esa máscara que siempre lleva puesta."
        l "¿En serio?"
        l "Suena a personaje de videojuego barato."
        l "¿No tienes uno normal?{w} ¿Uno que no parezca que te escapaste de un anime?"
        show dark 2desafiantet
        $ enfocar("dark")
        d "Es el que uso.{w} El que me queda."
        show dark 2desafiante
        $ normal("dark")
        l_thought "“Es el que me queda”. Lo dice tan natural."
        l_thought "Como si fuera un hecho."
        l "Bueno.{w} Supongo que “Dark” es mejor que “Imbécil”."
        show dark 2sarcasmot
        $ enfocar("dark")
        d "O mejor pon algo como “El que te salvó el culo el lunes”."
        show dark 2desafiantet
        extend " Como prefieras."
        show dark 2desafiante
        $ normal("dark")
        l "Dark. Punto."
        $ renpy.pause(2.5, hard=True)
        show dark 2juzga2t
        $ enfocar("dark")
        d "¿Y eso fue todo?"
        show dark 2juzga2
        $ normal("dark")
        l "¿Y qué más quieres? ¿Una carta de presentación?"
        l "No te estoy pidiendo matrimonio."
        show dark 1sarcasmot
        $ enfocar("dark")   
        d "Me gusta cómo suena eso."
        show dark guinio
        $ normal("dark")
        l_thought "Me da un poco de asco."
        extend " O tal vez no."
        l_thought "Tal vez solo me da miedo que alguien me diga algo así y no sepa cómo responder."
        # añadir el contacto
        $ nuevo_contacto = phone.group_chat.GroupChat("Dark", phone.asset("default_icon.png"), "dk_chat"). add_character("dk").add_character("la")
        $ renpy.notify('¡Has añadido a Dark a tu lista de contactos!')
        show dark 1felit
        $ enfocar("dark")
        d "Bueno, realmente tengo algunas cosas que hacer."
        show dark 2incomodot
        extend " O eso digo para no parecer demasiado patético."
        show dark 2incomodo
        $ normal("dark")
        "Guardamos los teléfonos, hacemos una pausa. Supongo que ya no queda más nada para decir."
        $ renpy.pause(2.5, hard=True)
        show dark 1neutralt
        $ enfocar("dark")
        d "Estoy para cualquier cosa. Incluso si no es una emergencia."
        show dark 1distraidot
        extend " Incluso si solo quieres decirle a alguien que hoy el mundo es una mierda."
        show dark 1incomodo
        $ normal("dark")
        $ renpy.pause(1.0, hard=True)
        show dark 1desafiante at flip, walking_c_normal, move_out_right_fast
        "Da media vuelta y empieza a caminar."
        l "Vete a la mierda, ni creas que te voy a llamar."
        "El simplemente se ríe. Se da media vuelta y se va por el otro lado del pasillo.{w} Desapareciendo por la multitud."
        l_thought "Un comienzo..."
        stop music fadeout 0.5
        
        #### 4.1

        "La palabra resuena en mi cabeza mientras Dark desaparece entre la multitud.{w} No sé qué significa, pero por primera vez, no suena a amenaza."
        l_thought "Él sonó sincero."
        extend " Demasiado sincero para ser otro de sus juegos."
        l_thought "Y lo más aterrador es que tenía razón..."
        extend " Blaze no me odia. Yo soy la que está construyendo ese odio, ladrillo por ladrillo, con cada pensamiento como este."
        l_thought "Un comienzo..."
        extend " ¿Para dejar de construir muros?"
        extend " ¿De otra decepción?"
        extend " ¿De otro error de cálculo?"
        "Pero por primera vez, la voz intrusiva no responde inmediatamente.{w} Como si las palabras de él la hubieran silenciado temporalmente."
        "Miro a ambos lados del pasillo. Izquierda: ruido, gente.{w} Derecha: silencio, sombras...{w} La posibilidad de estar sola sin estar perdida."
        "No es una decisión realmente.{w} Es un impulso. Y por primera vez, ese impulso no se siente como huida."
        "Camino hacia la {i}biblioteca{/i}.{w} Mis pies no arrastran el peso habitual."
        "No voy huyendo de algo.{w} Voy... buscando algo. No sé qué, pero algo diferente al vacío que he tenido."
        "La biblioteca siempre ha sido un lugar extraño. Demasiado silenciosa para un lugar lleno de palabras. Demasiado ordenada para un mundo caótico."
        scene black
        scene library
        stop ambient fadeout(0.5)
        with Fade(0.9, 2.0, 0.8)
        "Empujo la puerta de la biblioteca.{w} Hoy, por primera vez, se siente menos como una tumba y más como...{w} un refugio."
        "El aire huele a papel polvoriento y tiempo detenido. La luz entra en rayos oblicuos, iluminando motas de polvo que bailan como partículas de memoria suspendidas."
        l_thought "Supongo que volví aquí... ¿Lamentablemente?"
        play music bgm13 fadein(2.0)
        "Un hueco se abre en mi estómago.{w} No es hambre.{w} Es el eco de algo que una vez fue mío. Aquí, con Arai—{nw=0.3}"
        "Corto el pensamiento. No hoy."
        l_thought "Este lugar fue mi consuelo."
        extend " Por un tiempo."
        l_thought "Extraño eso."
        extend " Extraño creer que un lugar podía ser seguro."
        "Empiezo a caminar lentamente.{w} Como si tuviera una cadena."
        "Paso por la recepción y el bibliotecario, el hombre que siempre huele a té de manzanilla, me hace un gesto de saludo.{w} Asiento. No sonrío, pero no frunzo el ceño."
        l_thought "Al menos él no pregunta."
        l_thought "Supongo que esto ha cambiado un poco... No lo recuerdo tan avanzado."
        extend " O tan lleno de libros."
        "Miro alrededor.{w} Estudiantes dispersos, cabezas gachas sobre libros, auriculares que aíslan mundos enteros. No es soledad vacía.{w} Es soledad compartida."
        l_thought "Está bien. Con esta poca gente..."
        extend " Está bien."
        $ renpy.pause(4.0, hard=True)
        "Mis pies me llevan a los estantes.{w} Fingiendo que vengo por un libro.{w} Fingiendo que aún sé cómo querer algo."
        "Mis dedos pasan por los lomos, leyendo títulos como quien lee epitafios:"
        "{b}Outcast...{w} Salvation...{w} Exit Music...{/b}"
        l_thought "Qué apropiados."
        "Mi dedo se detiene en uno."
        "{b}Tales of City Sky{/b}."
        l_thought "Cuentos de esta ciudad..."
        extend " Irónico."
        l_thought "¿Quién escribiría sobre esto? ¿Sobre el domo, la niebla perpetua, las luces que parpadean como neuronas moribundas?"
        "Sigo."
        "{b}Cut-Team: Novel — Revised 3rd Edition{/b}."
        l_thought "Reescrito muchas veces..."
        extend " Como si la historia original nunca fuera suficiente."
        extend " Como si siempre hubiera algo que corregir."
        "{b}Marno's Biography{/b}."
        l_thought "Marno..."
        extend " Ese nombre otra vez. Papá lo mencionó. ¿Quién demonios es?"
        extend " Creo que simplemente no presté mucha atención a las clases de historia."
        window hide
        $ renpy.pause(5.0, hard=True)
        window show
        l_thought "Aquí hay paz."
        extend " Una paz indescriptible, que no pide nada a cambio."
        extend " Llevaba tanto sin sentir esto."
        l_thought "Ella no estaría orgullosa de cómo so—{nw=0.3}"
        extend " Basta."
        extend " Concéntrate en otra cosa."
        "Suspiro.{w} Agarro cualquier libro y busco mi rincón habitual."
        scene black
        scene library_back
        with Fade(0.8, 1.8, 0.8)
        "La mesa al fondo, escondida entre estanterías de literatura clásica que nadie lee.{w} Mi mesa.{w} O lo era."
        "Hoy, alguien ya está sentado allí."
        show steve 1leyendo:
            flip
            center
        with Dissolve(0.3)
        "Steve{w} —Junior… TV, quien sea— está inclinado sobre una mesa, un cómic abierto frente a él."
        "No lee con la intensidad de quien estudia, sino con la distracción de quien busca perderse en algo que no sea su propia cabeza."
        "Sus dedos pasan las páginas con un cuidado que contrasta con su apariencia algo arreglada pero forzada."
        l_thought "Mierda."
        extend " ¿No podía ser otra persona?"
        "Mis pies ya están girando para irse cuando recuerdo las palabras de Dark{w}: {b}“Un comienzo”{/b}."
        "Me detengo.{w} Podría dar media vuelta.{w} Podría encontrar otro rincón."
        "Pero algo —quizás lo que dijo Dark, quizás el cansancio de huir siempre— me hace caminar despacio hacia la mesa de al lado."
        l_thought "…"
        extend " Aunque, prefiero que sea él y no Strike. O peor, Mani."
        "Me siento.{w} El roce de la silla es un susurro áspero."
        "Él no levanta la vista inmediatamente. Sigue leyendo, pero su postura cambia. Una leve tensión en los hombros, como si hubiera registrado mi presencia pero decidiera no actuar."
        l_thought "Bien."
        extend " Silencio compartido."
        extend " Eso puedo manejar."
        "Abro mi libro.{w} Las palabras bailan.{w} Mis ojos, en cambio, se desvían hacia él."
        $ inac("steve")
        "Está leyendo un cómic viejo, de esos que venden en cajas en mercadillos.{w} Portada gastada, colores desteñidos."
        " Algo sobre superhéroes fracasados. Pero vuelvo a fingir que leo este libro."
        l_thought "Qué curioso."
        l_thought "Strike el detective, Dark el cínico, Jeremy el pragmático..."
        extend " Y este, el que lee cómics en la biblioteca. Qué grupo tan..."
        extend " Diverso."
        "Steve da vuelta la página.{w} Un sonido suave, casi reverente."
        show screen semiblack
        $ renpy.pause(1.5, hard=True)
        l_thought "Ahora que me pongo a pensar..."
        extend " Me parece raro que Dark se haya comportado así conmigo."
        extend " Demasiado raro."
        l_thought "Lo conozco hace dos días."
        extend " {i}DOS DÍAS{/i}."
        l_thought "Y me da una charla así, me pide mi número..."
        extend " ¿Qué carajos?"
        "Mis dedos aprietan el libro sin que me dé cuenta.{w} El papel cede bajo la presión."
        l_thought "¿Está fingiendo?"
        extend " ¿Actuando?"
        extend " Nadie hace eso por alguien que apenas conoce."
        l_thought "A menos que..."
        "Dos posibilidades chocan en mi mente:"
        l_thought "Opción 1: Blaze le habrá dicho algo. Soy ahora su proyecto de compasión, el “caso difícil” que el vicepresidente quiere arreglar para sentirse mejor consigo mismo."
        l_thought "Opción 2: Fue genuino. Y por alguna razón que no entiendo, decidió que yo valía esos minutos de honestidad."
        l_thought "La primera duele, pero es familiar. La segunda asusta, porque significa que tal vez, solo tal vez, no soy completamente transparente en mi miseria."
        $ renpy.pause(3.5, hard=True)
        "El recuerdo de hace minutos llega.{w} Dark, dándome su número de teléfono.{w} Ahora ese recuerdo me pesa más."
        l_thought "Mierda."
        extend " Caí."
        extend " De nuevo."
        extend " Siempre caigo."
        show steve 1juzga
        l_thought "Por un segundo lo creí."
        l_thought "Por un segundo pensé que alguien me veía—no como un problema, sino como una persona."
        l_thought "Y ahora esta parte de mí, la que conoce el dolor, la traición, el abandono..."
        show screen red_effect2
        nobody "{sc=4}Cuidado.{/sc}"
        nobody "{sc=4} Nadie hace esto por alguien que apenas conoce.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
        l_thought "Pero..."
        extend " ¿Y si esta vez es diferente?"
        $ renpy.pause(3.5, hard=True)
        "La pregunta se queda flotando, sin respuesta.{w} Porque la verdad es que no sé."
        " Y no saber es peor que creer lo peor.{w} Al menos lo peor es predecible."
        l_thought "Quizás lo raro no es él. Quizás lo raro soy yo, por pensar que podía ser diferente."
        hide screen semiblack with dissolve
        $ normal("steve")
        "Steve deja el cómic."
        $ normal("steve")
        show steve 1sonriente:
            flip_off
        "Escucho como lo pone en la mesa, sacándome de mis pensamientos.{w} Y mira hacia la ventana. No hacia mí, sino a través de mí, como si viera algo en el vidrio que yo no puedo percibir."
        l_thought "Está..."
        extend " Nervioso."
        extend " O pensativo."
        extend " O ambas."
        "El silencio aquí no es incómodo.{w} Es denso, cargado de cosas no dichas, pero no es hostil."
        "Cierro el libro que no estoy leyendo. Lo dejo sobre la mesa con un golpe suave."
        show steve 1neutral
        "Sus ojos se encuentran con los míos. No sonríe, pero tampoco rompe el contacto."
        "Y por primera vez en mucho tiempo, no siento la necesidad inmediata de romper el contacto, de lanzar un comentario cortante, de proteger mi espacio con púas."
        l_thought "Como si..."
        extend " Como si el silencio compartido no tuviera que ser siempre soledad."
        "Es todo lo que me atrevo a pensar antes de que él, no yo, sea el que rompa el silencio que nos une."
        show steve 1juzgat
        $ enfocar("steve")
        tv "...{w} ¿Laila?"
        show steve 1juzga
        $ normal("steve")
        l "...{w} ¿Sí?"
        "No añado nada.{w} No un “¿y qué?”, no un “¿te importa?”.{w} Solo la confirmación seca pero sin veneno."
        show steve 1rizzt
        $ enfocar("steve")
        tv "No pensé verte aquí. Es como si estuviera en el cielo."
        show steve 1rizz
        $ normal("steve")
        "Decido omitir la segunda afirmación...{w} ANTES QUE RESPONDA MA–{nw=0.3}"
        l "¿Y por qué no?"
        show steve 2neutralt
        $ enfocar("steve")
        tv "La primera vez que te vi fue en la azotea, pensé que era tu “tu lugar de paz”."
        show steve 2neutral
        $ normal("steve")
        l "Lo fue. Hasta que tú y el furro intervinieron."
        l_thought "Aun sigo odiando a ese tipo. Gracias a..."
        extend " Si es que existe un Dios, que no está aquí."
        show steve 2remedar2t
        $ enfocar("steve")
        tv "Ah...{w} Sí."
        show steve 2sonrientet
        extend " Lo siento por eso."
        show steve 2sonriente
        $ normal("steve")
        l "Ya."
        "Una palabra.{w} Seca, pero no cortante.{w} Es lo máximo que puedo ofrecer sin parecer demasiado...{w} Abierta."
        show steve 1triste2t
        $ enfocar("steve")
        tv "Aunque, yo... También vengo aquí cuando necesito silencio."
        show steve 1triste2
        $ normal("steve")
        "Lo dice mirando sus manos, no mis ojos.{w} Hay una vulnerabilidad en el gesto que me toma por sorpresa."
        l "¿De qué?{w} ¿Tu “lugar de paz” también lo arruinaron?"
        show steve 2neutralt
        $ enfocar("steve")
        tv "Algo así. Más bien...{w} Es donde vengo cuando el ruido de afuera se mete adentro."
        show steve 2neutral
        $ normal("steve")
        l_thought "“El ruido de afuera se mete adentro.”"
        extend " Qué frase tan..."
        extend " precisa."
        "Por un segundo, no escucho su voz."
        "Escucho la de ella, susurrando en mi oído durante una pesadilla infantil: “Shhh, mi niña. Los monstruos solo son ruido. No les des forma”."
        l "¿Ruido?"
        show steve 2remedart
        $ enfocar("steve")
        tv "Cuando José o Strike se ponen intensos, realmente a veces cansa."
        show steve 2remedar2t
        extend " Y más por lo que ha pasado últimamente."
        show steve 2remedar
        $ normal("steve")
        l_thought "..."
        l_thought "Supondré que José es “Mani”."
        "Hace una pausa, jugando con la esquina del cómic."
        show steve 2neutralt
        $ enfocar("steve")
        tv "Por cierto...{w} Strike...{w} no es mal tipo."
        show steve 2sonrientet
        tv "En serio. Solo es...{w} desconfiado por naturaleza."
        show steve 2sonriente
        $ normal("steve")
        l "Ya me di cuenta.{w} Es bastante obvio."
        $ renpy.pause(3.5, hard=True)
        show steve 1distraido
        $ renpy.pause(2.5, hard=True)
        show steve 1distraido:
            sigh_animation
        $ renpy.pause(2.5, hard=True)
        show steve 1amargadot
        $ enfocar("steve")
        tv "Es que... hubo un incidente el año pasado."
        show steve 2distraidot
        tv "Simplemente hizo algo que no debía estando en el consejo y...{w} Se formó un gran problema."
        show steve 2triste2t
        tv "Desde entonces, él..."
        $ normal("steve")
        show steve 1neutral
        "Se interrumpe, como si dijera demasiado."
        show steve 2neutralt
        $ enfocar("steve")
        tv "Bueno, no es excusa para cómo te trató.{w} Solo... contexto."
        show steve 2neutral
        $ normal("steve")
        l_thought "¿Algo que no debía?"
        extend " ¿En el consejo estudiantil? Qué melodramático."
        l "No necesito su contexto.{w} Solo quiero que me deje en paz."
        show steve 2neutralt
        $ enfocar("steve")
        tv "Lo hará. Si le demuestras que no eres..."
        show steve 2triste2t
        extend " Bueno, una amenaza."
        show steve 2triste2
        $ normal("steve")
        l "¿Y cómo se supone que haga eso?"
        show steve 2neutralt
        $ enfocar("steve")
        tv "No sé. Tal vez...{w} Mostrándole que no estás escuchando conversaciones.{w} O que no estás aquí por algo turbio."
        $ normal("steve")
        show steve 1neutral
        l_thought "“Algo turbio”."
        extend " Como si mi sola existencia no fuera lo suficientemente turbia."
        l "No estoy aquí por nada.{w} Solo quiero silencio."
        show steve 2sonrientet
        $ enfocar("steve")
        tv "Lo sé. Por eso vine a esta mesa. Sabía que no me ibas a hablar."
        $ normal("steve")
        show steve 2sonriente
        l_thought "¿Entonces por qué...?"
        show steve 1sonrientet
        $ enfocar("steve")
        tv "Como sea... Cuéntame de ti."
        show steve 2rizzt
        extend " ¿Quién es Laila Jackson?"
        show steve 2rizz
        $ normal("steve")
        "La pregunta cae como una piedra en un estanque.{w} Demasiado directa.{w} Demasiado personal."
        l_thought "¿En serio? ¿Ahora quieres mi biografía? ¿Aquí, en la biblioteca, después de todo el día de mierda?"
        "Pero miro sus ojos.{w} No hay curiosidad morbosa.{w} No hay juicio. Solo... interés genuino. Como si realmente quisiera saber la respuesta, no por chisme, sino porque le importa."
        "Y eso es lo que me desconcierta."
        l_thought "¿Quién es Laila Jackson? Una chica problemática."
        extend " La que se peleó con el profesor Todd."
        extend " La que gritó a su hermana."
        extend " La que tiene un expediente más grueso que este libro."
        extend " ¿Eso quieres oír?"
        l "¿Quién soy?{w} Una chica que quiere que la dejen en paz.{w} ¿Eso cuenta?"
        l "Además ¿Por qué quieres saber?{w} ¿Está recopilando información para Strike?"
        show steve 1juzgat
        $ enfocar("steve")
        tv "No."
        show steve 1neutralt
        tv " Solo... tratando de entender."
        show steve 1neutral
        $ normal("steve")
        l_thought "Ya me está hartando un poco esta conversación, simplemente no llegamos a nada."
        l "¿Entender qué?"
        show steve 1neutralt
        $ enfocar("steve")
        tv "Por qué alguien que busca silencio en una biblioteca hace tanto ruido en todas partes."
        show steve 1neutral
        $ normal("steve")
        l "¿Y tú?{w} ¿Quién es Steve—“TV”?{w} ¿El chico que lee cómics y se mete donde no lo llaman?"
        show steve 2rizzt
        $ enfocar("steve")
        tv "El chico que lee cómics porque ahí los héroes siempre encuentran una salida."
        show steve 1sonrientet
        tv " Y que se mete donde no lo llaman porque a veces la gente necesita que alguien se meta, aunque no lo sepa."
        show steve 1sonriente
        $ normal("steve")
        l "¿Y siempre funciona esa filosofía?"
        show steve 1sonrientet
        $ enfocar("steve")
        tv "Casi nunca. Pero sigo intentando."
        show steve 1sonriente
        $ normal("steve")
        "Sus palabras se quedan flotando entre nosotros.{w} No son un reproche, no son una lección. Son solo...{w} una declaración. Simple. Honesta."
        l_thought "Qué terco. O qué estúpido."
        extend " O ambas."
        "Pero por primera vez, no lo digo con desprecio.{w} Lo pienso con algo parecido a...{w} curiosidad."
        "¿Cómo puede alguien seguir intentando cuando todo falla? ¿Qué lo mantiene levantándose cada mañana para volver a intentarlo?"
        "El silencio vuelve, pero es diferente.{w} Antes era vacío.{w} Ahora está lleno de esta pregunta no hecha, de esta confesión no pedida."
        "Miro el cómic en sus manos.{w} Un héroe con los colores desteñidos, sonriendo contra todo pronóstico."
        l_thought "Tal vez los cómics no están tan alejados de la realidad."
        extend " Tal vez todos somos personajes buscando una próxima viñeta que nos dé sentido."
        show steve 1sonrientet
        $ enfocar("steve")
        tv "Bueno... Supongo que te dejo.{w} No quiero ser otro ruido en tu silencio."
        show steve 1sonriente
        $ normal("steve")
        "Se levanta, recoge su cómic.{w} Sus movimientos son lentos, deliberados, como dando tiempo a que yo diga algo."
        "Pero las palabras se atoran. Viejos hábitos, muros antiguos.{w} Solo asiento."
        l "Hasta luego."
        "Es lo más cercano a un “gracias” que puedo dar."
        show steve 2sonriente:
            asentir
        "Él asiente, una media sonrisa asoma en sus labios.{w} No es de triunfo, no es de lástima. Es solo...{w} Comprensión."
        show steve 2felizt
        $ normal("steve")
        tv "Hasta luego, Laila. Si necesitas...{w} bueno, silencio compartido, ya sabes dónde encontrarme."
        show steve 2feliz
        $ normal("steve")
        $ renpy.pause(1.5, hard=True)
        show steve 1feliz:
            flip
            pause 0.6
            xanchor 0.5 yanchor 1.0
            parallel:
                ease 5.0 xpos -400
            parallel:
                block:
                    ease 0.5 yoffset 15
                    ease 0.21 yoffset 0
                    repeat 11
                yoffset 0
        "Se aleja.{w} Sus pasos son casi silenciosos sobre la alfombra gastada.{w} Se sienta en otra mesa, no demasiado lejos.{w} Voltea una página de su cómic."
        l_thought "Silencio compartido..."
        "Las palabras de Dark vuelven: “Un comienzo”.{w} Las de Steve: “Sigo intentando”."
        l_thought "No son respuestas. No son soluciones."
        l_thought "Son solo..."
        hide steve
        extend " Posibilidades."
        extend " Pequeñas grietas en el muro que he construido alrededor de mí misma."
        "Miro mi libro.{w} Las palabras siguen bailando, pero ahora no me importa."
        " No necesito leerlas. Solo necesito estar aquí. En este silencio que ya no es vacío. En esta soledad que ya no es completa."
        l_thought "Steve... TV... ¿Quién eres realmente? ¿Y por qué te importa?"
        "No lo sé.{w} Y por primera vez, no tener la respuesta no se siente como una amenaza. Se siente como...{w} una historia por descubrir."
        "Cierro el libro.{w} No lo he leído, pero ha servido su propósito.{w} Me ha dado una excusa para estar aquí, para esta conversación."
        "Me levanto."
        extend " La campana del receso está por sonar. Tengo que volver a clase.{w} A las ecuaciones, a las miradas, a la rutina."
        "Pero algo ha cambiado.{w} Algo pequeño, casi imperceptible."
        l_thought "Tal vez la biblioteca no sea solo un refugio."
        scene black with Dissolve(0.5)
        "Salgo. Al pasar frente a su mesa, nuestros ojos se encuentran un instante.{w} No digo nada.{w} Él tampoco."
        "Pero en ese silencio compartido, hay un entendimiento nuevo: Hoy, por unos minutos, no estuvimos solos."
        "El pasillo está llenándose de gente.{w} El ruido regresa. Pero el eco del silencio compartido sigue conmigo, un susurro cálido en medio del caos."
        l_thought "Un comienzo..."
        "Sí. Quizás solo eso. Pero después de tanto tiempo estancada, incluso un comienzo se siente como un milagro."
        "Camino hacia mi siguiente clase, y por primera vez en mucho tiempo, mis pasos no suenan como los de una condenada. Suenan como los de alguien que, tal vez, solo tal vez, está aprendiendo a caminar de nuevo."
        
    else:
        window show
        "La campana del receso suena como un disparo. Un sonido agudo, metálico, que perfora el zumbido constante en mis oídos y me hace estremecer en mi asiento."
        "Mis compañeros se levantan en una oleada de risas y empujones. El aula, que hace segundos era un espacio de silencio forzado, se convierte en un caos organizado de mochilas, sillas arrastradas y conversaciones que resurgen de donde las dejaron."
        $ renpy.pause(3.5, hard=True)
        show vignette at vineta_organico zorder 100
        "Yo me quedo pegada a la silla, los dedos aferrados al borde del pupitre como si fuera el borde de un precipicio.{w}  Las uñas se clavan en la madera gastada, buscando anclaje en un mundo que de repente parece inclinarse."
        $ renpy.pause(3.5, hard=True)
        show jeremy 1serio2:
            flip
            right5
        show blaze 1desinteresada3:
            center2
        with Dissolve(0.2)
        "Blaze y Jeremy se levantan de sus asientos, listos para ir a su pequeña labor política para que mi hermana consiga un puesto “privilegiado”."
        $ renpy.pause(2.5, hard=True)
        play music bgm2 
        $ enfocar("jeremy")
        show jeremy 1seriot
        je "Blaze, vamos.{w} Revisar el puesto y clubes, recordar."
        show jeremy 1serio2
        $ normal("jeremy")
        show blaze 2preocupada
        "Blaze se voltea a verme, veo algo de duda en sus ojos."
        show blaze 2desinteresada3
        $ enfocar("blaze")
        b "Eh..."
        show blaze 2preocupadat
        extend " Laila, tengo que ir a ver lo del puesto..."
        show blaze 2preocupada
        $ normal("blaze")
        l "Está bien, no me tienes que pedir permiso."
        "Mi voz salió más fría de lo que pretendía.{w} Más cortante.{w} Un bisturí verbal que cortó cualquier posible continuación."
        show blaze 2desinteresada2
        "Hace una mueca leve, como si la hubiera golpeado."
        show blaze 2sonrientet
        $ enfocar("blaze")
        b "Solo...{w} no te alejes mucho, ¿sí?"
        show blaze 2sonriente
        $ normal("blaze")
        "Dice eso con una sonrisa forzada que no llega a sus ojos.{w} Es una frase de manual."
        "La que se dice cuando ya no sabes qué más decir, pero sientes la obligación de decir algo."
        "No respondo.{w} Miro mis manos.{w} Las uñas están sucias de los rastros de madera del pupitre."
        "Jeremy coloca una mano en el hombro de Blaze, un gesto posesivo que no me pierdo."
        $ enfocar("jeremy")
        show jeremy 1seriot
        je "Blaze, tener poco tiempo."
        show jeremy 1serio
        $ normal("jeremy")
        show blaze 2desinteresada3:
            asentir
        "Ella asiente, casi con alivio.{w} Tener una excusa para irse es un regalo que se acepta sin cuestionar."
        show jeremy 1serio2:
            xanchor 0.5 yanchor 1.0
            parallel:
                ease 5.0 xpos -400
            parallel:
                block:
                    ease 0.5 yoffset 15
                    ease 0.21 yoffset 0
                    repeat 11
                yoffset 0
        show blaze 2preocupada2: 
            outwalk_right8
        "Se dan la vuelta y salen del aula, fusionándose con la multitud que ya se desvanece por la puerta."
        $ renpy.pause(2.5, hard=True)
        hide jeremy
        hide blaze
        "Me quedo sola.{w} O casi."
        show dark 2distraido with Dissolve(0.2)
        "Dark está todavía en su asiento, reclinado hacia atrás en la silla, observando el techo como si esperara que se abriera para revelar algo interesante."
        "No se ha movido desde que sonó la campana."
        l_thought "¿Por qué no se va? ¿Qué quiere?"
        $ renpy.pause(2.5, hard=True)
        "Los segundos pasan. El silencio en el aula ahora es diferente.{w} Ya no es el silencio tenso de la clase, sino el silencio vacío del abandono.{w} Es peor."
        $ renpy.pause(3.0, hard=True)
        show dark 1serio2
        "Finalmente, Dark se levanta.{w} No con el movimiento rápido de los demás, sino con una lentitud estudiada, como si cada hueso le pesara más de lo normal."
        "Recoge su mochila de un tirón y se dirige hacia la puerta."
        "Pasa junto a mi asiento. No me mira. Pero se detiene."
        show dark 1seriot
        $ enfocar("dark")
        d "No te metas en líos, Jackson."
        show dark 2serio2
        $ normal("dark")
        "Es una advertencia.{w} No un consejo.{w} No es una muestra de preocupación."
        "Es la frase que un guardia le dice a un prisionero antes de dejarlo solo en su celda: “No hagas nada estúpido. No me causes problemas”."
        l "¿Y qué?{w} ¿Me vas a encerrar también?"
        "Mi voz es un susurro ronco. La pregunta sale sola. Un desafío automático de mi boca rebelde."
        "Dark se detiene en el marco de la puerta."
        show dark 2incomodo
        extend " Gira la cabeza apenas, suficiente para que yo vea el perfil de su sonrisa—no una sonrisa de diversión, sino de algo más cercano al desprecio."
        show dark 2incomodot
        $ enfocar("dark")
        d "No me importa lo que hagas. Pero luego no te quejes."
        show dark 2serio
        $ normal("dark")
        $ renpy.pause(1.5, hard=True)
        show dark 1serio:
            flip
            xanchor 0.5 yanchor 1.0
            parallel:
                ease 5.0 xpos -400
            parallel:
                block:
                    ease 0.5 yoffset 15
                    ease 0.21 yoffset 0
                    repeat 11
                yoffset 0
        $ renpy.pause(1.5, hard=True)
        "Y sale. Sin mirar atrás."
        play audio closet_close
        stop music
        "La puerta se cierra con un chasquido suave que resuena como un portazo en mi cabeza."
        $ renpy.pause(3.0, hard=True)
        l "Sola.{w} Completamente sola."
        hide dark
        "El aula está vacía.{w} Las sillas desordenadas, los pupitres con graffiti, la pizarra parpadea aun llena de ecuaciones que ya no significan nada."
        l_thought "¿Qué hago? ¿A dónde voy?"
        l_thought "¿A dónde mierda se supone que debería ir ahora?"
        extend " ¿A esconderme en un baño? ¿A casa?"
        extend " Como si “casa” fuera un refugio y no otra habitación con cuatro paredes que esperan que me componga."
        l_thought "Todos los caminos parecen llevar a otro tipo de prisión."
        extend " A otra versión de la misma expectativa: que en algún momento deje de ser esto."
        l_thought "Que deje de ser yo."
        $ renpy.pause(3.0, hard=True)
        l_thought "¿Y si no puedo? ¿Y si esto es todo lo que soy?"
        $ renpy.music.play("heartbeat.ogg", channel="heartbeat", loop=True)
        "Mi corazón empieza a latir con un ritmo irregular, como un motor que no quiere arrancar.{w} Un pulso acelerado que empuja la sangre contra mis sienes con fuerza."
        "Siento cada latido como un golpe.{w} Como una advertencia.{w} Como si mi propio cuerpo estuviera diciéndome que no aguanto más."
        l_thought "Tengo que salir. No puedo quedarme aquí."
        l_thought "Si me quedo, el silencio me va a devorar."
        extend " Estas paredes me van a tragar."
        extend " Este pupitre va a ser mi tumba y nadie va a venir a buscarme."
        l_thought "Pero salir es solo otro tipo de vacío."
        extend " Otro lugar donde no pertenezco."
        l_thought "Otro sitio donde voy a estar mirando a la gente vivir mientras yo me pudro por dentro."
        l_thought "Entonces ¿qué hago?"
        extend " ¿Me quedo?"
        extend " ¿Me voy?"
        extend " ¿Desaparezco?"
        $ renpy.pause(3.0, hard=True)
        l_thought "¿Desaparecer? Eso suena bien."
        extend " Eso suena a alivio."
        extend " Pero no puedo. No ahora."
        l_thought "Todavía no. Porque soy una cobarde. Porque siempre he sido una cobarde."
        "Aun así, me levanto.{w} Mis piernas tiemblan. Mis manos también.{w} No sé si es miedo o frío o las dos cosas."
        "O nada."
        "Tal vez solo es el cansancio de años de estar aquí, en este cuerpo, en esta vida."
        "Agarro mi mochila con torpeza y camino hacia la puerta. Cada paso es un esfuerzo consciente."
        "Un paso.{w} Solo un paso.{w} Y luego otro.{w} Y otro.{w} Y otro."
        l_thought "Eso es todo lo que sé hacer. Poner un pie delante del otro. Sin dirección. Sin propósito."
        l_thought "Solo avanzar porque detenerse sería peor."
        "Camino hacia la puerta. Mi mano toca el marco.{w} La madera está fría."
        "O tal vez soy yo. Tal vez siempre he estado fría por dentro y solo ahora lo noto."
        l_thought "Fuera. Necesito estar fuera."
        l_thought "Y quizás, en algún lugar afuera, encuentre una razón para no volver a entrar."
        play audio closet_open
        scene black
        scene pasillo
        with Fade(0.5, 1.5, 0.5)
        "Al salir al pasillo, la luz fluorescente me golpea en los ojos."
        play ambient school_hallway fadein(2.0) volume 0.5
        show blinking_moment
        extend " Parpadeo, desorientada."
        show vignette at vineta_organico zorder 100
        "El pasillo está lleno de gente—grupos que ríen, parejas que susurran, individuos que caminan con propósito hacia sus destinos."
        l_thought "Demasiada gente. Demasiado ruido."
        "Bajo la cabeza.{w} Mirada fija en el suelo.{w} En las líneas de las baldosas.{w}"
        l_thought "Una, dos, tres..."
        extend " Contar."
        extend " Contar para no pensar."
        "Pero las miradas me encuentran.{w} Las siento como puntas de aguja en la nuca, en los brazos, en la espalda."
        idk1 "¿Esa no es la qué...?"
        idk2 "Sí, la que gritó al profesor Todd. Qué vergüenza."
        idk1 "Y encima su hermana es Blaze. Pobre."
        l_thought "Pobre Blaze. Siempre “pobre Blaze”."
        extend " Nunca “pobre Laila”. Porque ella es la víctima. Yo soy el monstruo que creó."
        "Mi respiración se acelera.{w} El aire parece espesarse, volverse denso como gelatina.{w} Cada inhalación es un trabajo forzado."
        show screen red_effect2
        nobody "{sc=4}Claro. Porque eres el problema. El error.{/sc}"
        nobody "{sc=4}La mancha en la familia perfecta.{/sc}"
        nobody "{sc=5}¿No lo entiendes todavía?{/sc}"
        l_thought "Lo entiendo. Perfectamente."
        nobody "{sc=5}Entonces ¿por qué sigues aquí?{/sc}"
        nobody "{sc=5}¿Por qué obligas a todos a fingir que eres tolerable?{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
        $ renpy.pause(3.0, hard=True)
        scene black
        scene pasillo2
        show vignette
        with Fade(0.5, 1.0, 0.5)
        "Me doy la vuelta en una esquina, buscando un respiro.{w} Un lugar vacío.{w} Cualquier lugar."
        "Y lo encuentro{w}: un rincón entre dos filas de casilleros, escondido de la vista principal.{w} Un pequeño nicho donde la luz fluorescente parpadea, defectuosa."
        "Me arrastro hacia allí. Me apoyo contra los casilleros metálicos.{w} El frío del metal penetra mi ropa, llegando hasta la piel."
        l_thought "Respira. Solo respira."
        "Pero no puedo. Mis pulmones se niegan a expandirse.{w} Es como si llevara un corsé invisible apretado hasta el límite."
        "Miro mis manos.{w} Están temblando. No un temblor suave...{w} un temblor violento, convulsivo, como si mis nervios se hubieran declarado en huelga."
        l_thought "No aquí. Por favor, no aquí."
        show parpadeo_on
        "Cierro los ojos con fuerza. Las imágenes regresan: el sueño de anoche. La mano helada en mi cuello. La voz invitándome a 'dejarme llevar'. La paz negra."
        show screen red_effect2
        nobody "{sc=4}¿Ves? Allí había paz.{/sc}"
        nobody "{sc=4}Aquí solo hay esto.{/sc}"
        nobody "{sc=6}Ruido.{w} Miradas.{w} Expectativas fallidas.{/sc}"
        nobody "{sc=6}¿Por qué elegir esto?{/sc}"
        l_thought "Porque... porque..."
        "No tengo respuesta.{w} Solo tengo miedo."
        nobody "{sc=5}El miedo se acaba cuando tú te acabas.{/sc}"
        nobody "{sc=5}Es simple matemática, Laila.{/sc}"
        "Una risa hueca se me escapa—o tal vez fue un sollozo ahogado.{w} No lo sé.{w} Ya no distingo los sonidos que salen de mí."
        "Mis rodillas ceden.{w} Me deslizo por los casilleros hasta quedar sentada en el suelo, las rodillas contra el pecho, los brazos envolviéndome en un abrazo que no consuela."
        $ renpy.pause(3.5, hard=True)
        hide screen red_effect2 with Dissolve(0.5)
        show parpadeo_off
        hide parpadeo_on
        l_thought "Tengo que irme de aquí."
        extend " Antes de volverme loca."
        $ renpy.music.stop(channel="heartbeat")
        "La biblioteca.{w} El único lugar donde el silencio es una regla, no una anomalía."
        "Donde puedo esconderme entre estantes y palabras de otras personas, y fingir que no existo."
        "Con un esfuerzo que siento en cada músculo, me levanto.{w} Mis piernas protestan, pero obedecen."
        "Camino, tambaleante, hacia la biblioteca.{w} Cada paso es una huida.{w} Cada respiración, una batalla."
        l_thought "Último refugio."
        extend " Antes del colapso."
        "Y en algún lugar profundo de mi mente, una parte de mí se pregunta si esta vez el colapso será el último.{w} Si tal vez, en la quietud de la biblioteca, encontraré el coraje para hacer lo que el sueño me invitó a hacer."
        "Pero esa es una pregunta para después.{w} Por ahora, solo tengo que llegar."
        scene black
        scene library
        stop ambient fadeout(0.5)
        with Fade(0.9, 2.0, 0.8)
        play music bgm1
        "Empujo la puerta de la biblioteca.{w} Se siente como...{w} Nada."
        "La biblioteca huele a polvo de papel viejo y desinfectante barato.{w} El silencio aquí es diferente—no es ausencia de sonido, es una presencia física que se adhiere a la piel."
        l_thought "Supongo que volví aquí... Lamentablemente."
        "Un hueco se abre en mi estómago.{w} No es hambre.{w} Es el eco de algo que una vez fue mío. Aquí, con Arai—{nw=0.3}"
        "Corto el pensamiento.{w} No hoy."
        l_thought "Este lugar fue mi consuelo. Por un tiempo."
        l_thought "Extraño eso. Extraño creer que un lugar podía ser seguro."
        "Empiezo a caminar lentamente.{w} Como si tuviera una cadena."
        "Paso por la recepción y el bibliotecario, el hombre que siempre huele a té de manzanilla, me hace un gesto de saludo.{w} Asiento.{w} No sonrío, pero no frunzo el ceño."
        l_thought "Al menos él no pregunta."
        l_thought "Supongo que esto ha cambiado un poco..."
        extend " No lo recuerdo tan avanzado."
        "Miro alrededor.{w} Estudiantes dispersos, cabezas gachas sobre libros, auriculares que aíslan mundos enteros.{w} No es soledad vacía.{w} Es soledad compartida."
        "Una mesa en la esquina más alejada, junto a la ventana que da al patio interior.{w} Ese es mi lugar.{w} O lo era."
        "Hoy parece un territorio hostil que tengo que reconquistar."
        "Me dirijo allí con pasos que intentan ser silenciosos pero suenan como martillazos en mi cabeza."
        scene black
        scene library_back
        with Fade(0.8, 1.8, 0.8)
        "Al llegar, me desplomo en la silla. No con gracia. Mi cuerpo cede, como si finalmente hubiera terminado una maratón que nadie me pidió correr."
        "Cierro los ojos. Solo por un segundo. Solo para que el mundo deje de girar."
        "Pero en la oscuridad de mis párpados, veo las palabras otra vez:"
        show black with Dissolve(0.3):
            alpha 0.8
        centered "{sc=4}{b}PERDÓN{/b}{/sc}"
        centered "{sc=4}{b}CULPA{/b}{/sc}"
        centered "{sc=4}{b}ADIÓS{/b}{/sc}"
        "Y debajo, en letras más pequeñas, como un posdata del sueño que no recordaba hasta ahora:"
        l_thought "“Solo es más fácil del otro lado.”"
        $ renpy.music.set_audio_filter("music", [af.Reverb(0.0), af.Lowpass(22000)], replace=True)
        $ apply_filter_with_fade("music", [af.Reverb(0.5), af.Lowpass(440)], duration=1.5)
        show screen red_effect2
        nobody "{sc=4}Más fácil.{/sc}"
        $ renpy.music.play("heartbeat.ogg", channel="heartbeat", loop=True)
        nobody "{sc=4}Como respirar bajo el agua.{/sc}"
        nobody "{sc=4}Cómo dormir sin despertar.{/sc}"
        nobody "{sc=5}Ella lo hizo.{/sc}"
        nobody "{sc=5}Cruzó al otro lado.{/sc}"
        nobody "{sc=5}{b}¿Por qué tú no puedes?{/b}{/sc}"
        nobody "{sc=5}{b}¿Qué te detiene?{/b}{/sc}"
        nobody "{sc=5}{b}¿El miedo?{/b}{/sc}"
        nobody "{sc=5}{b}¿O la cobardía?{/b}{/sc}"
        nobody "{sc=5}{b}“Perdón”{/b}. ¿A quién le pides perdón?{w} ¿A ella?{/sc}"
        nobody "{sc=8}{b}Ella ya no está{/b}.{/sc}"
        nobody "{sc=8}{b}¿A Blaze?{/b}{w} Te odia en secreto.{/sc}"
        nobody "{sc=8}{b}¿A tu padre?{/b} Prefiere su trabajo.{/sc}"
        nobody "{sc=7}{b}“Culpa”{/b}.{w} Es lo único que sabes cargar bien.{/sc}"
        nobody "{sc=7}{b}La única mochila que nunca olvidas.{/sc}"
        nobody "{sc=7}{b}“Adiós”{/b}.{w} La palabra más amable que podrías darles.{/sc}"
        nobody "{sc=7}{b}Un regalo final.{w} Un “ya no tendrán que fingir que les importo”.{/sc}"
        nobody "{sc=5}El otro lado...{w} Donde no hay voces.{/sc}"
        nobody "{sc=5}Donde no hay espejos.{/sc}"
        show black:
            alpha 0.9
        nobody "{sc=5}Donde no tienes que preguntar “¿quién mierda eres?”.{/sc}"
        nobody "{sc=8}{b}Porque ya no serás nadie{/b}.{/sc}"
        nobody "{sc=5}¿Y si hoy?{/sc}"
        nobody "{sc=5}¿Y si aquí, entre estos libros mudos, entre este silencio que ya habla?{/sc}"
        nobody "{sc=5}¿Qué te detiene?{w} ¿El bibliotecario?{w} ¿Las cámaras?{/sc}"
        nobody "{sc=5}¿O ese último hilo de miedo que ni siquiera es tuyo?{/sc}"
        nobody "{sc=5}Es el que ella dejó enganchado en tu alma.{/sc}"
        nobody "{sc=7}Fácil.{w} Solo cerrar los ojos y no abrirlos.{/sc}"
        nobody "{sc=7}Solo dejar de luchar.{w} Solo rindirte.{/sc}"
        nobody "{sc=7}Como siempre supiste que terminarías haciendo.{/sc}"
        nobody "{sc=5}¿O prefieres seguir así?{w} ¿Otro día?{w} ¿Otro sueño?{/sc}"
        nobody "{sc=5}¿Otro rechazo?{w} ¿Otra decepción?{w} ¿Cuántas más, Laila?{/sc}"
        nobody "{sc=5}¿Cuántas más hasta que admitas que esto no es vivir, es arrastrarse?{/sc}"
        show black:
            alpha 1.0
        nobody "{sc=5}La biblioteca calla.{w} Espera.{w} Observa.{w} Sabe lo que estás pensando.{/sc}"
        nobody "{sc=5}Sabes que hoy podrías decidir no salir por esa puerta.{/sc}"
        nobody "{sc=5}Fácil.{w} Tan fácil que duele que no lo hayas hecho antes.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
        $ renpy.music.set_audio_filter("music", None, replace=True)
        $ renpy.pause(0.6, hard=True)
        hide black
        $ renpy.music.stop(channel="heartbeat")
        "Abro los ojos bruscamente.{w} La biblioteca vuelve a enfocarse, pero las palabras ya no están solo en mi mente."
        "Las veo grabadas en la mesa, en los estantes, en el aire{w}: {b}PERDÓN CULPA ADIÓS MÁS FÁCIL MÁS FÁCIL MÁS FÁCIL—{/b}{nw=0.3}"
        "Y entonces lo veo."
        show steve 1leyendo:
            flip
            center
        with Dissolve(0.3)
        "Steve.{w} Sentado a dos mesas de distancia, hojeando un cómic viejo."
        "No me había dado cuenta de que estaba ahí. Quizás porque hoy no veo a nadie, solo fantasmas y amenazas."
        $ renpy.pause(2.5, hard=True)
        show steve 1neutral:
            boo
        "Nuestras miradas se encuentran."
        show steve parpadeo_sorpresa
        extend "Él parpadea, como sorprendido de verme aquí.{w} O sorprendido de verme viva."
        l_thought "Mierda. No ahora."
        extend " No él."
        "Steve cierra su cómic con cuidado.{w} Se levanta.{w} No con brusquedad, pero tampoco con lentitud. Es un movimiento calculado, como si supiera que cualquier acercamiento puede ser malinterpretado."
        "Y lo sabe.{w} Todos lo saben ya."
        "Camina hacia mí.{w} Cada paso suyo me hace retroceder mentalmente."
        " Quiero levantarme, huir, pero mis piernas han decidido traicionarme.{w} Se han convertido en piedra."
        "Steve se detiene a una distancia segura.{w} Lo suficientemente lejos como para no invadir, lo suficientemente cerca como para que sus palabras no se pierdan en el silencio de la biblioteca."
        show steve 1neutralt
        $ enfocar("steve")
        tv "Eh... Laila.{w} No esperaba verte aquí."
        show steve 1neutral
        $ normal("steve")
        "Su voz es suave.{w} Demasiado suave.{w} Como si estuviera hablando con un animal herido. Eso me irrita más que si me hubiera gritado."
        l "¿Y por qué no? ¿La biblioteca es solo para gente normal?"
        "La palabra sale con más veneno de lo que pretendía.{w} Steve no se inmuta.{w} O sí lo hace, pero lo disimula bien."
        show steve 1neutralt
        $ enfocar("steve")
        tv "No, no es eso."
        show steve 2neutralt
        extend " Es que... Pensé que estarías en la azotea con los demás."
        show steve 2neutral
        $ normal("steve")
        "Miente.{w} Sabe que no iría con ellos.{w} Todos lo saben."
        l "¿Y qué te importa? ¿Ahora eres mi guardián?"
        "Steve respira hondo.{w} No se va."
        "Eso es lo raro. La mayoría se iría. Él se queda."
        show steve 1remedar2t
        $ enfocar("steve")
        tv "A veces vengo aquí cuando todo es demasiado..."
        show steve 2neutralt
        tv "Ya sabes, ruidoso. José de hablador, Struke de...{w} Ser él."
        show steve 2remedar
        $ normal("steve")
        "Sus palabras son una oferta.{w} Un puente tirado sobre un abismo que no quiero cruzar."
        l "¿Y? ¿Quieres una medalla por tener un refugio? Todos tenemos uno."
        "La referencia a la muerte flota entre nosotros, no dicha pero escuchada por ambos."
        show steve 1leyendo
        "Steve mira hacia el cómic que dejó en su mesa."
        show steve 1amargado
        extend " Luego de vuelta a mí.{w} Sus ojos son extrañamente claros, como si vieran más de lo que muestran."
        show steve 1amargadot
        $ enfocar("steve")
        tv "Recuerdo, que cuando el grupo eramos más unidos..."
        show steve 2sonrientet
        extend " Veníamos a aquí a hacer todo tipo de cosas."
        show steve 2sonriente
        $ normal("steve")
        "Su voz se quiebra apenas.{w} No por tristeza, sino por algo más complejo."
        "Quizás nostalgia envenenada. Como si estuviera recordando un tiempo que ya no puede recuperar, con personas que ya no son las mismas."
        l "¿Y? ¿Quieres que me una al club de los nostálgicos?"
        l "Perdí mi tarjeta de membresía cuando dejé de importarme."
        show steve 1neutral
        "Steve no se inmuta ante mi sarcasmo.{w} Al contrario, parece verlo por lo que es: una barrera.{w} Una muralla de púas que él decide escalar de todos modos."
        $ renpy.pause(3.0, hard=True)
        show steve 1sonrientet
        $ enfocar("steve")
        tv "Un viejo amigo... Él también venía aquí cuando las cosas se ponían complicadas."
        show steve 1sonriente
        $ normal("steve")
        "La revelación cae entre nosotros.{w} No es un grito, es un susurro."
        "Una confesión que no pide reciprocidad, pero que ofrece un espejo.{w} “Yo también tengo pedazos rotos”."
        "Pero sus pedazos rotos no son como los míos.{w} Sus pedazos tienen nombre, tienen historia.{w} Los míos son solo polvo y culpa."
        l "Qué conmovedor. ¿Te trajo aquí para que jugaran a los detectives?"
        l "¿A espiar a la chica rota para ver cuándo se desarma del todo?"
        show steve 1amargado
        "Mis palabras son cuchillos, y sé que llegan.{w} Veo cómo su mandíbula se tensa, cómo sus dedos se aferran al borde de la mesa frente a él.{w} Pero no se va."
        show steve 2remedart
        $ enfocar("steve")
        tv "Él se fue. Hace dos años. Lo cambiaron de escuela...{w} Dijo que regresaría."
        show steve 2remedar
        $ normal("steve")
        "Pausa. El aire se espesa."
        show steve 2remedar2t
        $ enfocar("steve")
        tv "Nunca regresó."
        show steve 2remedar2
        $ normal("steve")
        "Ahí está.{w} Su dolor, expuesto como una herida que no ha cicatrizado."
        " Me lo ofrece como moneda de cambio.{w} “Mira, yo también sangro. Podríamos compartir venda”."
        "Pero yo no quiero vendas. Quiero que la herida se infecte.{w} Quiero que se pudra hasta que no quede nada que doler."
        "Es lo que me merezco."
        l "¿Y qué quieres que haga? ¿Que llore por ti?{w} Mis lágrimas están reservadas para mi propio funeral."
        l_thought "Y va a ser pronto."
        "La amenaza flota en el aire, cruda, sin adornos."
        show steve 1neutral
        "Por primera vez, Steve se queda sin palabras.{nw=0.3}"
        show steve parpadeo_sorpresa
        extend " Sus ojos parpadean rápido, procesando.{w} No es shock, es reconocimiento.{w} Reconoce la verdad en mi declaración."
        show steve 1tristet
        $ enfocar("steve")
        tv "Laila..."
        show steve 1triste
        $ normal("steve")
        "Noto que sus dedos aprietan el borde de la mesa."
        l "No.{w} No me digas que no lo haga."
        l "No me digas que hay esperanza. No me ofrezcas tu dolor como si fuera un consuelo. Tu amigo se fue por elección."
        l_thought "El mío..."
        extend " Ella no tuvo elección."
        "La diferencia es abismal.{w} Su pérdida es una tragedia. La mía es un crimen.{w} Y yo soy la cómplice."
        "Steve retrocede un paso.{w} No físicamente, pero emocionalmente.{w} Ve el precipicio y decide no saltar. Es más inteligente de lo que aparenta."
        show steve 1neutralt
        $ enfocar("steve")
        tv "Está bien."
        show steve 1neutral
        $ normal("steve")
        "Dos palabras. Un repliegue.{w} Una rendición."
        "Su mirada no es de enojo, es de reconocimiento.{w} Como si acabara de leer una sentencia"
        "No dice “lo siento”.{w} No dice “te entiendo”."
        "Solo “está bien”, como si estuviera aceptando que algunas guerras no se pueden ganar porque el enemigo ya está muerto."
        show steve 1remedart
        $ enfocar("steve")
        tv "El silencio aquí es bueno...{w} Hasta que empieza a hablar.{w} Cuidado con lo que le contestas."
        show steve 1remedar
        $ normal("steve")
        "Se da media vuelta.{w} Camina de regreso a su mesa.{w} Recoge su cómic, su mochila. No me mira de nuevo."
        show steve 1remedar:
            flip
            pause 0.6
            xanchor 0.5 yanchor 1.0
            parallel:
                ease 5.0 xpos -400
            parallel:
                block:
                    ease 0.5 yoffset 15
                    ease 0.21 yoffset 0
                    repeat 11
                yoffset 0
        "Pero antes de irse, se detiene en la puerta.{w} No voltea, pero su voz llega clara, como un eco en la caverna de mi silencio:"
        "Y se va.{w} La puerta se cierra con un suspiro."
        "Me quedo sola. Más sola que antes."
        "Porque ahora el silencio no está vacío.{w} Está lleno de sus palabras. De sus recuerdos. De su amigo perdido. De su oferta de compañía que acabo de patear al abismo."
        l_thought "Cuidado con lo que le contestas..."
        "Miro mis manos. Las marcas del sueño han desaparecido de mi piel, pero ahora siento otras marcas, invisibles, más profundas."
        "Las marcas de cada puente que quemo. Cada mano extendida que aparto. Cada “está bien” es en realidad un “adiós”."
        "Y en el silencio que ahora sí habla, escucho la invitación otra vez.{w} No como un susurro, sino como un coro."
        show screen red_effect2
        nobody "{sc=4}Ven.{w} Es más fácil.{/sc}"
        nobody "{sc=5}Ellos ya se rindieron contigo.{/sc}"
        nobody "{sc=6}Steve se rindió.{/sc}"
        nobody "{sc=6}Dark se rindió.{/sc}"
        nobody "{sc=6}Blaze está cansada.{/sc}"
        nobody "{sc=6}Tu padre prefiere su trabajo.{/sc}"
        nobody "{sc=7}¿A quién le importas?{/sc}"
        show black with Dissolve(0.3):
            alpha 0.9
        centered "{sc=8}{b}¿A quién salvas quedándote?{/b}{/sc}"
        hide black with Dissolve(0.3)
        hide screen red_effect2 with Dissolve(0.5)
        "Me inclino sobre la mesa, apoyando la frente en las manos.{w} La madera está fría.{w} Como la mano en mi sueño. Como la mano en mi cuello."
        l_thought "Quizás Steve tenía razón."
        extend " Quizás el silencio sí habla."
        l_thought "Y quizás, hoy, por primera vez, estoy lista para escuchar lo que tiene que decirme."
        show parpadeo_on
        "Cierro los ojos.{w} No para descansar.{w} Para ensayar."
        "Ensayo cómo sería no abrirlos nunca más."
        "Ensayo cómo sería el último suspiro."
        "Ensayo cómo sería la paz que prometió el sueño."
        "Y en la penumbra de la biblioteca, con el peso de todas las palabras no dichas y todos los puentes quemados, empiezo a entender algo aterrador:"
        l_thought "Que hoy, el colapso no es una posibilidad que temo."
        l_thought "Es una promesa que espero."
        l_thought "Y parte de mí. La parte más cansada, la más rota, la más honesta..."
        l_thought "Está contando los minutos para que se cumpla."

    window hide
    stop music fadeout 1.5
    stop ambient fadeout(4.5)
    $ quick_menu = False 
    scene black with dissolve_scene_full3
    hide parpadeo_on

return