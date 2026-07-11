label scene4_day2:
     
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

    play audio closet_close
    $ renpy.pause(2.5, hard=True)
    "En los pasillos quedan algunos que otros estudiantes.{w} Yo solo me limito a caminar al lado de Blaze y desconectarme."
    $ renpy.pause(7.5, hard=True)
    "Subimos al segundo piso y caminamos hasta el final del pasillo, donde una puerta con el letrero “Salón del Consejo” nos espera.{w} Y curiosamente...{w} Está a ciertos pasos de la sala del director."
    play audio keylock
    "Jeremy saca sus llaves, esas que todo el mundo menciona. Abre la puerta y entramos."
    play audio closet_open
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
    play audio closet_close
    "La puerta se cierra detrás de nosotros, ahogando el resto de la conversación."
    stop music fadeout 5.1
    $ renpy.pause(2.5, hard=True)
    "Después de salir del salón del consejo, el silencio entre yo y Blaze es denso, cargado de lo no dicho."
    $ renpy.pause(2.5, hard=True)
    "El camino hacia la salida se siente más largo de lo habitual, cada paso es un eco de las palabras intercambiadas, las miradas, las decisiones tomadas."
    with Fade(5.0, 8.0, 5.0)

return