label scene3_day2:

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

        "Ceder y comer.":
            $ rutaCanon += 3
            l_thought "“Por favor”. Esa palabra duele más que la orden. Porque significa que le importa."
            l_thought "Significa que he logrado asustarla de verdad."

        "Rechazar rotundamente.":
            $ rutaSuicida += 5
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
    play audio closet_open
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
    play audio closet_close
    "Jeremy saca varias llaves."
    play audio keylock
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
    with Dissolve(5.0)

return