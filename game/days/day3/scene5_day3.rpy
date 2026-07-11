image dark laugh:
    "dark 1laugh1"
    pause 0.25
    "dark 1laugh"

image blaze laugh:
    "blaze 1felizt"
    pause 0.25
    "blaze 1feliz"    

label scene5_day3:

    $ quick_menu = True
    window show

    if (rutaCanon-rutaSuicida)>=0:
        "La campana del almuerzo me alcanza todavía perdida en las ecuaciones que nunca voy a entender.{w} No espero a nadie."
        "Solo necesito moverme, hacer algo, ser un cuerpo que ocupa espacio aunque por dentro no sienta nada."
        scene cafeteria with dissolve_scene_full2
        play ambient school_cafeteria fadein(2.0)
        "El comedor está lleno de gente ruidosa que ríe, habla, existe con una facilidad que me parece un idioma extranjero."
        "Me deslizo entre las mesas como un fantasma, buscando la única esquina donde el sol no pega directamente, donde puedo encogerme y nadie me va a pedir nada."
        l_thought "¿Por qué vine para acá? No tengo ni la menor idea."
        extend " Quizás porque en la biblioteca no me dejan comer..."
        "Encontré una mesa al fondo, contra la pared, justo al lado de la ventana que nadie usa porque en el domo se vuelve todo gris. Perfecto para desaparecer."
        "Me siento.{w} La bandeja frente a mí es un gesto vacío, no recuerdo haber tomado nada, pero ahí está. Comida de cafetería. Gris. Insípida.{w} Perfecta para mí."
        l_thought "Bien."
        extend " Cinco minutos de silencio antes de la siguiente clase."
        l_thought "Nadie se acercará si pareces lo suficientemente rota."
        $ renpy.pause(4.5, hard=True)
        show blaze 1sonriente with Dissolve(0.5):
            flip
            left
        play music bgm14
        "Blaze llega primero, con su bandeja equilibrada con esa gracia que ni ensayando se logra."
        show blaze 1sonrientet
        $ enfocar("blaze")
        b "¿Puedo?"
        show blaze 1sonriente
        $ normal("blaze")
        "No es una pregunta. Es un aviso.{w} Se sienta a mi lado. Levanto la vista. Ya está dejando su bandeja al lado de la mía."
        show dark 1metiche with Dissolve(0.3):
            center2
        show jeremy 1serio2 with Dissolve(0.3):
            flip
            right5
        "Pero detrás vienen ellos."
        show dark 1metiche:
            shake
        "Dark se desliza como si esto fuera obvio, sentándose justo enfrente de mí con una sonrisa que ya me irrita."
        show dark 1desafiantet
        $ enfocar("dark")
        d "Mesa VIP.{w} ¿Necesitas invitación o ya podemos empezar el show?"
        show dark 1desafiante
        $ normal("dark")
        show jeremy 2juzga
        "Jeremy duda.{w} Su bandeja pesa en sus manos como si fuera un objeto ajeno."
        show jeremy 1serio3
        extend " Mira el asiento junto a Blaze"
        show jeremy 1serio
        extend ", luego a mí"
        show jeremy 1serio2
        extend ", luego al techo.{w} Como si rogara paciencia a un dios en el que no cree."
        show dark 2distraido
        show jeremy 2serio2t
        $ enfocar("jeremy")
        je "...{w} ¿Dónde sentar?"
        show jeremy 2serio2
        $ normal("jeremy")
        show blaze 1sonrientet
        $ enfocar("blaze")
        b "Aquí, tonto."
        show blaze 1sonriente
        $ normal("blaze")
        "Blaze tira suavemente de su brazo."
        show jeremy 2sonriente:
            shake
        extend " Jeremy obedece, pero su espalda permanece rígida, como si esperara una emboscada."
        l_thought "Genial."
        extend " Los cuatro fantásticos."
        l_thought "Solo falta que aparezca Maní con una pizza, Steve con un cómic estiúpido y Strike con su actitud de mierda..."
        extend " Y ahí tendríamos el circo completo."
        l_thought "No invité a nadie."
        extend " No di permiso."
        l_thought "Y sin embargo, aquí están."
        show jeremy 1serio2
        $ renpy.pause(3.0, hard=True)   
        show blaze 1compadecert
        $ enfocar("blaze")
        b "¿Qué tal la clase de matemáticas?"
        show blaze 1compadecer
        $ normal("blaze")
        "Blaze intenta romper el hielo con la torpeza de quien no sabe que el hielo es lo único que me protege."
        "Me encojo de hombros.{w} No tengo energía para fingir interés."
        "Dark, por supuesto, no necesita invitación para hablar."
        show dark 1sarcasmot
        $ enfocar("dark")
        d "Oh, vamos, Blaze.{w} Matemáticas.{w} El arte de hacer números con problemas que nadie pidió resolver."
        show dark 1sarcasmo
        $ normal("dark")
        show jeremy 1juzga
        "Jeremy levanta una ceja, picado por el comentario."
        show jeremy 1felizt
        $ enfocar("jeremy")
        je "Prefiero eso a... tus métodos creativos para resolver..."
        show jeremy 1seriot
        extend " nada."
        show jeremy 1serio
        $ normal("jeremy")
        "Se lleva una mano al pecho, fingiendo ofensa."
        show dark 1incomodot
        $ enfocar("dark")
        d "¿Nada? Ayer resolví el problema de por qué la máquina de café siempre está vacía a las 9 de la mañana."
        show dark 1incomodo
        $ normal("dark")
        show blaze 1sonrientet
        $ enfocar("blaze")
        b "¿Y? ¿Cuál era la solución?"
        show blaze 1sonriente
        $ normal("blaze")
        show dark 1felit
        $ enfocar("dark")
        d "La gente toma café a las 9 de la mañana."
        show dark 2juzgat
        extend " Profundo, ¿verdad?"
        show dark 2juzga
        $ normal("dark")
        show blaze 3desinteresada3
        "Blaze rueda los ojos"
        show blaze 3sonriente:
            boo
        extend ", pero una sonrisa se le escapa."
        show jeremy 1sonriente:
            sigh_animation_flipped
        "Jeremy resopla, pero no puede evitar un gesto de diversión.{w} Yo sigo callada, removiendo la comida sin ganas."
        show blaze 1juzga2t
        $ enfocar("blaze")
        b "¿Vas a comer eso o solo a declararle la guerra?"
        show blaze 1juzga2
        $ normal("blaze")
        show jeremy 1juzga
        "Señala mi bandeja."
        l "Está en negociaciones."
        show dark 2desafiantet
        $ enfocar("dark")
        d "Apuesto a que la comida va a perder."
        show dark 1sarcasmot
        extend " Como siempre."
        show dark 1sarcasmo
        $ normal("dark")
        $ renpy.pause(1.0, hard=True)
        show blaze 1enojada2
        show dark 1neutral:
            boo
        l_thought "Su tono es ligero, pero sé a qué se refiere."
        extend " Al desayuno. Al panqueque. A todo."
        show dark 2distraido
        show blaze 1neutralt
        $ enfocar("blaze")
        b "Jeremy, ¿ya terminaste el trámite de los clubes?"
        show blaze 1neutral
        $ normal("blaze")
        show jeremy 2felizt
        $ enfocar("jeremy")
        je "Casi. Solo falta...{nw}"
        show jeremy 2serio2
        $ renpy.pause(1.0, hard=True)
        show jeremy 2felizt
        extend " firma del director!"
        show jeremy 2seriot
        je " Pero él... Siempre pone peros."
        show jeremy 2serio
        $ normal("jeremy")
        show dark 1desafiantet
        $ enfocar("dark")
        d "“Peros” es su segundo nombre."
        show dark 2felit
        extend " El primero es “burocracia”."
        show dark 1desafiante
        $ normal("dark")
        show blaze 2juzgat
        $ enfocar("blaze")
        b "¿Y el club de cocina?{w} ¿Creen que lo aprueben?"
        show blaze 2preocupada
        $ normal("blaze")
        show jeremy 1seriot
        $ enfocar("jeremy")
        je "Depende. Necesitar…{w} Supervisión. Y espacio."
        show jeremy 1serio
        $ normal("jeremy")
        show dark 1sarcasmot
        $ enfocar("dark")
        d "Y alguien que no incendie la cocina."
        show dark 2juzgat
        extend " Eso descarta a Mani."
        show dark 2juzga
        $ normal("dark")
        show blaze 1seria2t
        $ enfocar("blaze")
        b "Ay, no seas malo."
        b " Mani tiene..."
        show blaze 1sonrientet
        extend " Entusiasmo."
        show blaze 1sonriente
        $ normal("blaze")
        show jeremy 1seriot
        $ enfocar("jeremy")
        je "Entusiasmo no apagar incendios."
        show jeremy 1serio
        $ normal("jeremy")
        "Por primera vez, algo se me escapa."
        "Una exhalación que podría ser una risa.{w} Pequeña.{w} Casi inexistente. Pero está ahí."
        show dark 1neutral:
            boo
        "Dark la caza al instante."
        show dark 2juzgat
        $ enfocar("dark")
        d "¿Escuché eso? ¿La señorita Problemática tiene sentido del humor?"
        show dark 2juzga
        $ normal("dark")
        "Bajo la mirada rápidamente."
        l "Tengo gripe."
        show dark 2desafiantet
        $ enfocar("dark")
        d "Claro. Gripe. Muy convincente."
        show dark 2desafiante
        $ normal("dark")
        show jeremy 1juzga
        "Jeremy me observa con esa mirada analítica que pone cuando está procesando información.{w} No es incómoda, solo... curiosa."
        show jeremy 1neutralt
        $ enfocar("jeremy")
        je "Tú... reír de vez en cuando..."
        show jeremy 1felizt
        extend " ¿No te mataría?"
        show jeremy 1feliz
        $ normal("jeremy")
        show blaze 1felizt
        $ enfocar("blaze")
        b "¡Exacto! Podrías intentarlo.{w} Es gratis."
        show blaze 1feliz
        $ normal("blaze")
        l "Nada es gratis. Siempre hay un precio."
        show dark 1juzga2
        show blaze 1juzga
        show jeremy 1serio2
        $ renpy.pause(1.5, hard=True)
        "Silencio breve. Demasiado breve."
        show dark 1juzga2t
        $ enfocar("dark")
        d "¿Cómo cuál?"
        show dark 1juzga2
        $ normal("dark")
        l_thought "¿Por qué pregunta eso? ¿Qué quiere escuchar?"
        l "Como...{w} no sé."
        l "Pagas con tu tiempo. Tu atención. Tu...{w} energía."
        show dark 2desafiantet
        $ enfocar("dark")
        d "Interesante. ¿Y si alguien está dispuesto a pagar ese precio?"
        show dark 2desafiante
        $ normal("dark")
        show blaze 1neutral
        show jeremy 1neutral
        "La pregunta cae en la mesa como una moneda.{w} Todos la miramos.{w} Él no aparta la vista de mí."
        show blaze 2preocupadat
        $ enfocar("blaze")
        b "Dark..."
        show blaze 2preocupada
        $ normal("blaze")
        show dark 1desafiantet
        $ enfocar("dark")
        d "Solo pregunto."
        show dark 1desafiante
        $ normal("dark")
        "Jeremy carraspea, incómodo.{w} Busca desesperadamente un tema neutral."
        show jeremy 1serio2t
        $ enfocar("jeremy")
        je "Esta... comida."
        show jeremy 1juzgat
        extend " ¿Alguien saber... qué es?"
        show jeremy 1juzga
        $ normal("jeremy")
        show blaze 1juzgat
        $ enfocar("blaze")
        b "¿Cómo que qué es? Es pasta."
        show blaze 1juzga
        $ normal("blaze")
        show jeremy 1seriot
        $ enfocar("jeremy")
        je "No parece. Tener...{w} textura rara."
        show jeremy 1serio
        $ normal("jeremy")
        show dark 1desafiantet
        $ enfocar("dark")
        d "Bienvenido al club de los que desconfían de la cafetería, Jeremy."
        show dark 2juzgat
        extend " ¿Primera vez?"
        show dark 2juzga
        $ normal("dark")
        show jeremy 1seriot
        $ enfocar("jeremy")
        je "No."
        show jeremy 2incomodo2t
        je " Pero hoy... especialmente sospechoso."
        show jeremy 2incomodo2
        $ normal("jeremy")
        "Blaze mete el tenedor en su propia porción, examinándola con fingida seriedad."
        show blaze 1neutralt
        $ enfocar("blaze")
        b "Tiene razón. Esto podría ser..."
        show blaze 1juzgat
        extend " ¿lasaña disfrazada?"
        show blaze 1juzga
        $ normal("blaze")
        show dark 1sarcasmot
        $ enfocar("dark")
        d "¿O un experimento de ciencias que salió mal?"
        show dark 1sarcasmo
        $ normal("dark")
        "Yo miro mi bandeja sin querer participar, pero el absurdo de la conversación me gana.{w} Solo un poco."
        l "Parece cartón con salsa."
        show blaze 1neutral
        show dark 1neutral
        show jeremy 1neutral
        "Suelto eso en un murmullo para mí, pero creo que escucharon."
        $ renpy.pause(2.5, hard=True)
        "Silencio."
        show blaze 1feliz
        show jeremy 1sonriente
        show dark laugh:
            boo3
        "Luego, Dark suelta una carcajada."
        show dark 1felit
        $ enfocar("dark")
        d "¿Cartón con salsa? Eso es terriblemente preciso."
        show dark 1feli
        $ normal("dark")
        show blaze 1felizt
        $ enfocar("blaze")
        b "Laila tiene razón. Es exactamente eso."
        show blaze 1feliz
        $ normal("blaze")
        show jeremy 2sonriente:
            asentir
        "Jeremy asiente, solemnemente."
        show jeremy 2sonrientet
        $ enfocar("jeremy")
        je "Cartón con salsa.{w} Nueva descripción oficial del menú escolar."
        show jeremy 2sonriente
        $ normal("jeremy")
        show blaze 1felizt
        $ enfocar("blaze")
        b "Deberían ponerlo en el letrero de entrada."
        show blaze 1feliz
        $ normal("blaze")
        show dark 1felit
        $ enfocar("dark")
        d "“Bienvenidos a la preparatoria, donde servimos cartón con salsa desde 1987”."
        show dark 1feli
        $ normal("dark")
        show jeremy 1feliz:
            shake
        "Jeremy resopla, esta vez con una sonrisa genuina."
        show jeremy 1neutralt
        $ enfocar("jeremy")
        je "1987..."
        show jeremy 1felizt
        extend " año exacto de esta... pasta."
        show jeremy 1feliz
        $ normal("jeremy")
        show blaze 1felizt
        $ enfocar("blaze")
        b "Paren, me duele el estómago de tanto reírme."
        show blaze 1feliz
        $ normal("blaze")
        show dark 1sarcasmot
        $ enfocar("dark")
        d "Eso es la comida, Blaze.{w} Te está atacando desde adentro."
        show dark 1sarcasmo
        $ normal("dark")
        "La mesa se descontrola por un momento. Risas.{w} Verdaderas.{w} Incluso yo..."
        l_thought "¿Me estoy riendo?"
        l_thought "..."
        l_thought "Sí. Un poco. Muy poco. Pero sí."
        show blaze 3compadecer
        "Blaze me mira, y en sus ojos hay algo que no veía hace tiempo{w}: esperanza. No dice nada. Solo sonríe."
        show dark 1feli
        show jeremy 1sonriente
        "Cuando las risas se calman, Dark me lanza una mirada rápida. No dice nada. No hace falta."
        "Jeremy, todavía con una sonrisa residual, vuelve a su comida con menos desconfianza."
        show jeremy 1neutralt
        $ enfocar("jeremy")
        je "Bueno... quizás no tan malo."
        show jeremy 1neutral
        $ normal("jeremy")
        show dark 1sarcasmot
        $ enfocar("dark")
        d "Eso es porque no has probado el cartón, Jeremy."
        show dark 1sarcasmo
        $ normal("dark")
        "Y la conversación sigue. Fluida.{w} Sin presión. Como si esto fuera...{w} normal."
        l_thought "Normal."
        extend " Qué palabra tan extraña. Y sin embargo..."
        l_thought "Por primera vez en mucho tiempo, no quiero que el receso termine."

    else:
        "La campana del receso me encuentra todavía en el aula, con la mirada perdida en la pizarra donde el profesor escribió ecuaciones que nunca voy a entender."
        "A mi alrededor, sillas chirrían, mochilas se cierran, el caos habitual de los que tienen un lugar a donde ir."
        "Yo no tengo ningún lugar."
        "Pero mis pies se mueven solos.{w} Hacia el comedor."
        "Porque no hay otro sitio. Porque el cuerpo sigue las rutinas aunque la mente ya las haya abandonado."
        $ renpy.pause(3.0, hard=True)
        scene cafeteria with dissolve_scene_full2
        play ambient school_cafeteria fadein(2.0)
        "El comedor está lleno.{w} Ruido.{w} Gente.{w} Vidas que no me incluyen.{w} Me deslizo entre las mesas como un fantasma, buscando un hueco donde nadie me pida nada."
        l_thought "Solo un sitio."
        extend " Cualquier sitio donde no tenga que fingir."
        "Encuentro una mesa al fondo.{w} Contra la pared.{w} Cerca de la ventana que da al patio gris. Perfecta para desaparecer."
        "Me siento.{w} La bandeja aparece frente a mí.{w} No recuerdo haberla cogido. Comida de cafetería. Gris. Como todo."
        l_thought "Bien. Cinco minutos de silencio."
        extend " Nadie se acercará si pareces lo suficientemente rota."
        show blaze 1sonriente:
            flip
            left
        show dark 1distraido3:
            right5
            flip
        show jeremy 1sonriente:
            center2
        with Dissolve(0.3)
        "Y entonces los veo."
        "Blaze. Jeremy. Dark."
        "Están en una mesa cerca de la entrada. No demasiado lejos. Lo suficiente para que pueda verlos.{w} Lo suficiente para que no puedan verme a mí."
        l_thought "Ahí están. Los tres. Juntos. Riendo. Hablando."
        "Blaze está sentada junto a Jeremy.{w} Sus hombros se rozan.{w} Él dice algo{nw}"
        show blaze laugh:
            boo
        extend " y ella se ríe. Una risa genuina. La que yo ya no escucho desde hace meses."
        "Jeremy tiene sus papeles sobre la mesa, pero no los mira. Está mirando a Blaze. Hay algo en su mirada que no sé nombrar.{w} Algo que no es para mí."
        "Dark está al otro lado. Con las manos en los bolsillos. Pero hoy no los está mirando. Está mirando por la ventana. Como si también estuviera en otro lugar."
        l_thought "Ni siquiera se han dado cuenta de que no estoy con ellos."
        show screen red_effect2
        nobody "{sc=4}¿Por qué iban a darse cuenta?{/sc}"
        nobody "{sc=4}¿Cuándo fue la última vez que te miraron y te vieron?{/sc}"
        l_thought "Cállate."
        nobody "{sc=4}Es verdad. Míralos. Están bien sin ti.{/sc}"
        show dark 1neutral
        nobody "{sc=6}{b}Mejor sin ti.{/b}{/sc}"
        show dark laugh:
            boo
        show blaze laugh:
            boo
        "Blaze dice algo y los tres se ríen. Incluso Dark sonríe. Una sonrisa real. No la máscara."
        l_thought "Son felices. Sin mí."
        extend " Siempre lo fueron."
        "Mis dedos se cierran alrededor del tenedor. La comida sigue intacta.{w} Puré gris.{w} Carne gris.{w} Verduras grises.{w} Como todo en mi vida."
        nobody "{sc=6}Ni siquiera mereces eso.{/sc}"
        nobody "{sc=6}La comida es para los que tienen hambre.{/sc}"
        nobody "{sc=8}{b}Tú solo tienes vacío.{/b}{/sc}"
        l_thought "Solo quiero comer. Callate."
        l_thought "Tengo que dejar de pensar."
        nobody "{sc=6}No puedes comer.{w} No puedes pensar.{w} No puedes nada.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
        "Bajo la mirada.{w} No quiero verlos.{w} No quiero ver cómo sonríen sin mí."
        "Pero no puedo dejar de ver."
        $ inac("dark")
        $ inac("jeremy")
        show blaze 1sonriente at boo
        "Blaze se levanta.{w} Camina hacia la fila de la comida.{w} Pasa cerca de mi mesa.{w} No me mira."
        l_thought "Pasó a un metro de mí."
        extend " No me vio."
        show blaze 1felizt
        $ enfocar("blaze")
        b "¿Quedan panecillos?"
        show blaze 1feliz
        $ normal("blaze")
        "La chica asiente. Blaze sonríe.{w} Vuelve a su mesa con dos panecillos. Le da uno a Jeremy.{w} El otro se lo queda ella."
        $ inac("blaze")
        "No me ofrece nada."
        "No me ve."
        l_thought "No me ve. Nunca me ve."
        extend " Soy invisible."
        show screen red_effect2
        nobody "{sc=6}No eres invisible.{w} Eres un recuerdo.{/sc}"
        nobody "{sc=6}Algo que fue y ya no es.{/sc}"
        "El tenedor cae de mi mano.{w} Golpea la bandeja.{w} El sonido metálico debería llamar la atención.{w} Nadie gira la cabeza."
        l_thought "Ni siquiera el ruido me delata."
        extend " Ni siquiera eso."
        "Respiro hondo.{w} El aire no entra bien."
        "Como si hubiera algo bloqueando el paso."
        nobody "{sc=6}¿Qué pasa, Laila?{w} ¿No puedes respirar?{/sc}"
        nobody "{sc=6}¿No puedes estar? ¿Para qué sigues intentando?{/sc}"
        l_thought "No lo sé."
        nobody "{sc=6}Claro que lo sabes.{w} Por cobardía.{/sc}"
        nobody "{sc=8}{b}Porque tienes miedo de hacerlo.{/b}{/sc}"
        "Miro mi bandeja. La comida sigue ahí. Intacta. Fría.{w} Como yo."
        l_thought "No voy a comer. No puedo comer. No merezco comer."
        nobody "{sc=8}{b}Exacto. No mereces nada.{/b}{/sc}"
        "Mis manos empiezan a temblar. No es frío.{w} Es otra cosa.{w} Algo que se acerca y no puedo detener."
        l_thought "No. Ahora no. Por favor."
        extend " No aquí."
        nobody "{sc=6}¿Por qué no aquí?{w} ¿Qué mejor lugar que este?{/sc}"
        nobody "{sc=8}Rodeada de gente que no te ve.{w} De gente que vive sin ti.{/sc}"
        show vignette at vineta_organico zorder 100
        $ renpy.music.set_audio_filter("ambient", [af.Reverb(0.0), af.Lowpass(22000)], replace=True)
        $ apply_filter_with_fade("ambient", [af.Reverb(0.5), af.Lowpass(440)], duration=1.5)
        "La respiración se acelera.{w} El aire no llega.{w} Mi pecho se aprieta."
        "Miro hacia su mesa. Siguen riendo.{w} Blaze dice algo."
        show jeremy 1feliz:
            asentir
        extend " Jeremy asiente."
        show dark 1distraido2:
            boo
        extend " Dark se encoge de hombros."
        "Nadie me mira."
        "Nadie sabe que estoy aquí."
        "Nadie sabe que me estoy desmoronando."
        l_thought "Estoy aquí. En medio de cientos de personas. Y nadie me ve."
        nobody "{sc=5}Porque ya no estás.{/sc}{w} {sc=6}No para ellos.{/sc}"
        "El tenedor está en el suelo.{w} No recuerdo haberlo dejado caer.{w} O tal vez sí.{w} Ya no sé."
        "Las manos tiemblan más. Los dedos se cierran sobre el borde de la mesa.{w} La madera está fría. Áspera.{w} Real."
        l_thought "Agárrate. Solo agárrate."
        extend " No te caigas."
        extend " No aquí."
        extend " No delante de todos."
        nobody "{sc=5}¿De quién? Nadie te mira.{/sc}"
        nobody "{sc=7}Podrías desmayarte y nadie lo notaría.{/sc}"
        $ renpy.music.play("heartbeat.ogg", channel="heartbeat", loop=True)
        "La respiración se vuelve irregular. Corta.{w} Jadeante. El corazón late demasiado rápido.{w} Demasiado fuerte."
        l_thought "No puedo. No puedo. No puedo—{nw=0.3}"
        nobody "{sc=7}No puedes.{w} Nunca pudiste.{/sc}"
        show layer master: 
            function apply_blur_gradually2   
        "La visión se nubla. Los bordes se vuelven borrosos. Las caras se convierten en manchas de color."
        show dark 1neutral:
            boo2
        $ normal("dark")
        "Y entonces—Dark mira hacia mi dirección."
        "Por un segundo, sus ojos se encuentran con los míos."
        l_thought "Me vio."
        extend " Me está viendo."
        "Se queda quieto.{w} No se mueve.{w} No dice nada.{w} Solo me mira."
        l_thought "Va a venir."
        extend " Va a hacer algo. Va a—{nw=0.3}"
        extend " Va a—{nw=0.3}"
        show dark 1distraido
        $ inac("dark")
        "Dark baja la mirada.{w} Vuelve a su conversación.{w} Como si no hubiera visto nada."
        l_thought "No viene."
        nobody "{sc=5}No.{w} No va a venir.{/sc}"
        nobody "{sc=8}No eres su problema.{w} No eres problema de nadie.{/sc}"
        l_thought "Me vio."
        extend " Y no hizo nada."
        nobody "{sc=7}Porque no importas. Porque nunca importaste.{/sc}"
        "La respiración empeora.{w} El pecho se contrae.{w} Las lágrimas amenazan con salir.{w} Bajo la cabeza."
        l_thought "No puedo llorar aquí."
        extend " No puedo."
        "Me levanto."
        "La silla chirría.{w} Un sonido áspero.{w} Agresivo.{w} Nadie gira la cabeza."
        "Camino.{w} Mis piernas se mueven sin permiso. La salida está al fondo.{w} Treinta pasos.{w} Veintinueve.{w} Veintiocho."
        "No miro atrás. No quiero ver si me miran. No quiero saber que no lo hacen."
        hide dark
        hide jeremy
        hide blaze
        with Dissolve(0.3)
        $ renpy.music.set_audio_filter("ambient", None, replace=True)
        stop ambient fadeout(1.0)
        scene pasillo2:
            function apply_blur_gradually2
        with Fade(1.0, 0.5, 1.0)
        "Salgo al pasillo.{w} Está vacío.{w} Silencioso."
        "El ruido del comedor queda atrás, apagado por las puertas."
        l_thought "Sola."
        extend " Completamente sola."
        "Me apoyo contra la pared.{w} El frío del metal cala a través de mi ropa.{w} Duele.{w} Me gusta."
        "La respiración sigue acelerada.{w} Las manos siguen temblando."
        l_thought "Me vio."
        extend " Y no hizo nada."
        nobody "{sc=7}Porque no eres su responsabilidad.{/sc}"
        nobody "{sc=7}Porque no eres responsabilidad de nadie.{/sc}"
        l_thought "Pero me vio."
        nobody "{sc=7}{b}Y decidió que no valía la pena.{/b}{/sc}"
        show parpadeo_on
        "Cierro los ojos.{w} Cuento hasta diez.{w} El corazón sigue latiendo demasiado rápido."
        l_thought "Un día."
        extend " Un día más. Un día menos."
        extend " Un día menos."
        nobody "{sc=7}{b}¿Y después? ¿Qué viene después?{/b}{/sc}"
        l_thought "No lo sé."
        nobody "{sc=7}{b}Claro que lo sabes.{/b}{/sc}"
        hide parpadeo_on
        show parpadeo_off
        "Abro los ojos.{w} El pasillo sigue vacío.{w} El silencio es total."
        l_thought "El receso termina en cinco minutos. Tengo que volver."
        hide parpadeo_off
        nobody "{sc=5}¿A qué? ¿A la nada de siempre?{/sc}"
        l_thought "A la nada de siempre."
        $ renpy.music.stop(channel="heartbeat")
        scene black with dissolve_scene_full2
        "Empujo la puerta del comedor.{w} Entro.{w} La bandeja sigue en mi mesa.{w} La comida intacta.{w} Fría."
        "Me siento.{w} El resto del receso pasa en silencio."
        "Nadie viene."
        "Nadie pregunta."
        $ renpy.pause(3.0, hard=True)
        play audio bell
        "El timbre suena.{w} Me levanto.{w} Recojo mi bandeja, boto la comida en la basura.{w} La dejo en el carrito de los platos sucios."
        "El comedor se vacía.{w} Todos vuelven a sus clases.{w} A sus vidas.{w} A sus rutas que no me incluyen."
        "Salgo del comedor. El pasillo está lleno de gente. Todos tienen prisa. Todos tienen un lugar a donde ir."
        "Yo no tengo ningún lugar."
        l_thought "Ni siquiera un sitio donde sentarme."
        extend " Ni siquiera una migaja de atención."
        extend " Ni siquiera un “¿estás bien?”."
        nobody "{sc=7}{b}No. Porque no importas.{/b}{/sc}"
        "Camino hacia el aula.{w} Mis pasos son automáticos.{w} Mi cuerpo se mueve solo."
        l_thought "Un día más."
        extend " Uno menos para la cuenta."
        "Me siento en mi pupitre.{w} El de atrás.{w} El que nadie reclama."
        l_thought "Bienvenida al club de los que sobran. La cuota es silenciosa. Y la pagas todos los días."
        "El profesor entra. La clase empieza."
        "Yo no escucho nada."
        hide screen red_effect2 with Dissolve(0.5)
        hide vignette with dissolve

    window hide
    stop music fadeout 4.5
    stop ambient fadeout(4.5)
    scene black
    $ quick_menu = False
    with dissolve_scene_full3

return