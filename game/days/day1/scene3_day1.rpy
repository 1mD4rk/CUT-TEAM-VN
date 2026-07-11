label scene3_day1:

    play audio bell
    $ renpy.pause(3.0, hard=True)
    $ quick_menu = True 
    with Dissolve(0.5)
    "Después de ese encuentro... inesperado, con al parecer el {i}{outlinecolor=#da0303}Vicepresidente del Consejo Estudiantil{/outlinecolor}{/i}. El receso empezó.{w} Me salvé por ahora."
    "Decidí irme a la azotea... un lugar donde al menos nadie viene y casi siempre está solo."

    l_thought "Por fin algo de paz me vendría bien después de eso."
    "Digo en mi propia mente para convencerme que lo que acabo de hacer no me llena de culpa."
    "Pero incluso en el silencio, mis pensamientos gritan más fuerte."

    play audio closet_open
    $ renpy.pause(1.0, hard=True)
    scene azotea with fade
    play ambient ext_day fadein(2.0)
    play audio closet_close

    "Recién llegué a la azotea y me puse en una esquina, junto a las vallas de alambre que están alrededor del tejado."
    "Solo miro a la nada...{w} Las nubes de la ciudad y su cielo...{w} Y las aves que siempre chocan con el domo..."
    l_thought "Agradezco que este lugar jamás me decepciona, a pesar de todo siempre estará aquí. En un momento de paz que por fin estoy recibiendo."
    "Digo soltando un suspiro agotado, como si el propio cielo y ambiente me llegará a escuchar mi sentir."
    l_thought "El sonido de los árboles, el viento soplando las hojas secas, y los animales pasar, me relaja..."
    pause 1.5
    "De repente, la culpa trepa de nuevo por mi espalda{w=0.5} justo cuando menos lo necesito."
    l_thought "Creo que... tendré unos problemas muy grandes por mi..."
    extend " Acto de rebelión."
    l_thought "Y para rematar el día de mierda, casi me gano un problema con el {i}{outlinecolor=#da0303}Vicepresidente del Consejo Estudiantil{/outlinecolor}{/i}."
    l_thought "Supongo que librarme cuenta como suerte... aunque con mi historial, dudo que sea más que un aplazamiento temporal."
    pause 1.5
    l_thought "Sigo sin creer que acabo de hacer esto...{w=0.5} Desobedecer una orden del profesor..."
    extend " Creo que ahora sí estoy bastante jodida."
    l_thought "¡Pero no! ¡La gran e inútil LAILA necesitaba demostrar una vez más lo PERR—{nw}"
    "Rápidamente se me hace un gran nudo en la garganta al querer completar mi propio arrepentimiento. Suelto un gran suspiro interrumpiendo mis palabras."
    l_thought "Sólo es mi culpa...{w} ¡MI PUTA CULPA!"
    "Con la rabia aún ardiendo en mi pecho,"
    play audio pushing_a_metal1
    extend " cierro el puño y lo estrello contra la valla. Al principio... No busco dolor, busco sentir algo —cualquier cosa— que no sea esta culpa que me consume."
    $ renpy.pause(1.7, hard=True)
    "Al principio... nada.{w=0.5} Solo el impacto sordo de hueso contra metal, amortiguado por esta capa de algodón que separa mis sentidos del mundo."
    "Respiro algo agitada. Y cuando decido apoyar la cabeza en mis manos, intentando calmarme."
    show screen red_effect
    "Entonces llega. Un dolor punzante, nítido y agudo."
    extend " Por un segundo, es un alivio. Es real. Es algo que puedo localizar y entender, no como este vacío que me carcome por dentro."
    l_thought "..."
    l_thought "Mierda."
    show screen red_effect2
    hide screen red_effect
    "Aunque a estas alturas decido ignorar el dolor ocasionado."
    play audio ear_ringing volume 0.5 
    "Y como si alguien estuviera hablando frente mio, escucho alguien decir algo... Mientras escucho como un pitido resuena en mi oído, incrementando."
    pause 1.0
    nobody "{sc=3}¿Crees que no es tu culpa? Aw, ternura.{/sc}"
    nobody "{sc=4}Eso mismo dirán cuando encuentren tu cuerpo sin vida:{/sc}"
    nobody "{sc=6}“Ahora tiene lo que se merecía”{/sc}"
    pause 1.5
    stop audio fadeout 1.8
    l_thought "..."
    l_thought "¿Q-Qué fue eso?"
    "Eso logra sacarme de mis pensamientos rápidamente. Volteando a todos lados quien fue el que me dijo esas...{w=0.5} Palabras."
    extend " Pero aún siento como aplastan mi pecho al oír eso."
    hide screen red_effect2 with Dissolve(1.0)
    l_thought "Logré sentirme bastante extraña... Por esas palabras... Pareciera que alguien conocido me lo hubiera dicho en mi oído..."
    pause 1.5
    "Al no encontrar a nadie decidí tomar un bocado de aire para tratar de calmarme nuevamente."
    'Tal vez estoy bastante nerviosa de lo que vaya a suceder con mi "aventura".'
    l_thought "¡Felicidades Laila, oficialmente vas a terminar en el manicomio! Dónde es imposible suici—{nw}"
    l_thought "—poder socializar... Claro, como si fuera muy social."
    "Aclaro que esto último lo digo con un tono vacilante."
    l_thought "¿Que estoy diciendo? ¡No tengo idea de como tuve el valor de decirle cosas tan... crueles a mi hermana... ¡Mi hermanastra!"
    pause 1.5
    l_thought "¿¡Qué clase de persona me estoy convirtiendo!?"
    l "Soy una fábrica de decepciones. Hasta lo hago bien. Convierto cada oportunidad en ruinas, cada conexión en escombros."
    l_thought "Incluso mi—{w=0.8} ella, estaría decepcionada de lo que soy..."

    play audio closet_open
    "De repente, alguien rompe mi burbuja de pensamiento tan abruptamente, asustándome al escuchar la puerta del otro lado de la azotea abrirse junto a varias voces."
    "2 voces para ser precisas..."
    "Los oigo discutir sobre algo... más bien sobre {i}alguien{/i} y aunque quisiera ignorar lo que hablan e irme."
    "Pero, la voz de ese alguien resalta más siéndome imposible retomarlo nuevamente."
    l_thought "Pero...{w=0.5} Si nadie suele estar aquí, ¿por qué ahora de la nada hay gente aquí?"
    '(Asumamos que, en este contexto, "gente" representa solo a 2 personas.)'
    l_thought "Y en este preciso momento."
    "Me quedo completamente quieta, tengo un presentimiento que ellos no me han notado aún, y espero que siga así."
    "Y solo me queda escuchar parte de su conversación...  ahora que por culpa de ellos ya no puedo estar sola."

    idk1 "Ya te dije, él me dijo que lo esperaramos acá, Struke."
    idk2 "¿Para qué?"
    "Parece que ellos ni siquiera han entrado como tal, están en el marco de la puerta. Además, no he oído que se cerrara."
    idk1 "¿Me lo preguntas a mi? ¿A la persona que le llegó el mismo mensaje que a ti?"
    idk1 "¿En serio, Struke?"
    "Escucho un quejido proveniente de alguno de los dos, probablemente del que se escucha más serio."
    idk2 "No quiero estar aquí."
    idk1 "No entiendo la necesidad de Mani de hacer las reuniones aquí."
    l_thought "¿Maní?"
    l_thought "Que nombre tan... Curioso."
    l_thought "Para decirlo de una manera más... ¿bonita?"
    idk1 "Ni mi vieja con las amigas se complican tanto."
    play audio closet_close
    "Por fin se escucha el cierre de la puerta, dándome a entender que ya están aquí."
    l_thought "Si no me muevo, no me ven. No quiero lidiar con más personas hoy, ya me bastó con..."
    extend " El último problema y {outlinecolor=#da0303}Dark{/outlinecolor}."
    pause 1.5
    idk2 "¿De casualidad no te dijo el por qué nos citó aquí?"
    $ renpy.notify('"tavy" significa "tonto" o "loco" en guaraní.')
    idk1 "Creeme que no, y eso que vivimos juntos. Estos días estuvo muy tavy."
    idk1 "Trate de sacarle información, pero creeme que no se dejó. Por primera vez, no se dejó."
    l_thought "Están tan concentrados en quejarse que ni se han percatado que alguien más está aquí."
    l_thought "Bueno, uno se queja más que él otro."
    l_thought "Él segundo parece que simplemente evita quejarse de ese alguien."

    "Sigo pendiente en su conversación, porque sé que si muevo asi sea un musculo, se daran cuenta que hay alguien aqui..."
    l_thought "Tengo que ver cómo salir de aquí."
    "Estoy al lado de la puerta para entrar a la azotea, mientras ellos están al otro lado de esta."
    l_thought "No creo que la puerta vaya a rechinar tanto para que ellos lo escuchen... ¿Verdad?"
    "Me giro lentamente a la puerta, moviéndome lentamente para no ser localizada tan rápido. Eso me lo enseñó papá."
    pause 1.5
    "..."
    "Tocó el pomo de la puerta y la giró lentamente."
    play audio closet_open
    "Abro lentamente la puerta. Pero de todas formas, se le escucha rechinar."
    l_thought "Qué inesperado,{w=0.5} ¿verdad?"
    "Ahora siento el peso de sus miradas sobre mí. Mi torpeza fue el impertinente faro que les alertó de mi aquí."
    pause 2.0
    "Hay silencio. No escucho sus voces. Solo sus pasos viniendo hacia aca."
    
    l_thought "¡Fantástico! Justo lo que necesitaba: otros dos randoms para alegrar el día."
    
    show strike 1serio:
        flip
        inwalk_right_toleft
    $ renpy.pause(5.5, hard=True)
    "Un chico llega antes de que pueda regresar a mi lugar donde estaba escondida. Y en vez de que diga algo sutil, decide hacer peor el momento."
    show strike 1seriot:
        right1
    $ enfocar("strike")
    st "Ah. Quién diría que hubo alguien escuchando {i}nuestra{/i} conversación." 
    show strike 1serio
    $ normal("strike")
    show steve 1neutral at inwalk_left_toright
    $ renpy.pause(5.5, hard=True)
    show steve 2juzgat at left1
    $ enfocar("steve")
    tv "¿De qué hablas ahora Struk-{nw=0.1}"
    $ normal("steve")
    play music bgm2 
    show steve 1enamorao
    "Se queda paralizado al verme, pareciera que {i}NUNCA{/i} había visto una mujer... o no se por su expresión tan asombrada al verme."

    "Me quedo incómoda ante su mirada tan... estupida que está poniendo..."
    "Intento escaparme, dando el primer paso ignorando la mirada que me están dando los dos."
    pause 1.5
    "Pero antes de que pudiera salirme con la mía, el chico raro que se cree 'El Joker' por su estupido color de cabello y furro me detiene poniendo su mano en mi cara justo cuando estaba por avanzar."
    l_thought "Maldita sea... Lo que me faltaba. Otra interacción más."
    show strike 1juzgat
    $ enfocar("strike")
    st "{i}Laila Jackson{/i}. No esperaba encontrarte aquí. ¿Escuchando conversaciones que no te pertenecen?"
    show strike 1juzga
    $ normal("strike")
    "Me pongo aún más incómoda por cómo pronuncia mi nombre."
    l_thought "¿Cómo mierda sabe mi nombre? ¿Acaso me ha estado siguiendo? ¿O soy solo otro chisme más en su colección de problemas ajenos?"
    l_thought "Lo dijo con tanta naturalidad... Como si ya me conociera de antes."
    "Pero prefiero mantener la guardia."
    l "Disfrutando del silencio hasta que llegaron ustedes. Un concepto novedoso, lo sé."
    l "¿Puedo pasar? Prometo olvidar todo sobre su emocionante conversación sobre... ¿Maní?"
    show steve 2rizzt
    $ enfocar("steve")
    tv "Con que Laila, eh? Es lind-{nw=0.1}"
    $ normal("steve")
    show steve 1amargado
    show strike 1seriot
    $ enfocar("strike")
    st "No parece que tuvieras nada mejor que hacer..."
    show strike 1juzgat
    extend " ¿O me equivoco?"
    show strike 1sarcasmot
    st "Después de todo, no es la primera vez que terminas donde no deberías."
    show strike 1serio
    $ normal("strike")
    "Él tipo sigue manteniendo la mirada fijamente en mi. Pero {i}muy fijamente{/i}."
    "Gracias a eso, siento un escalofrío recorrer mi espalda."
    show strike 1seriot
    $ enfocar("strike")
    st 'Creeme que a estas alturas, todo el mundo habla de ti. Diría que hasta las paredes saben de tus... {i}"maravillosas anécdotas"{/i}.'
    "La palabra la pronuncia con un desprecio casi tangible."
    show strike 1sarcasmot
    st "{i}A excepción de este{/i}, que parece vivir en una burbuja. Qué suerte tiene, ¿no?"
    show strike 1sarcasmo
    $ normal("strike")
    "Cada palabra sale empapada en un sarcasmo tan ácido que quema el aire entre nosotros."
    l_thought "Al menos el chico de camisa amarilla no ha escuchado nada de mí... Un pequeño alivio irónico en medio de este momento de mierda."
    l_thought "..."
    l_thought "GENIAL, JUSTO LO QUE NECESITABA, QUE ME RECUERDEN COMO UNA PERRA PROBLEMÁTICA."
    "Suspiro profundamente para mis adentros, pero mi mente ya está ardiendo."
    l_thought "Fantástico. Ahora soy el espectáculo principal. Ahora que me vean, diré “¿Quieren un autógrafo?, les firmaré un ‘lo siento’ con sangre si me dejan ir”."
    l_thought "O mejor: “¿Quieren una foto? Sale en 50 pesos y un 'por favor, olviden que existo'”."
    show steve 1amargadot
    $ enfocar("steve")
    tv "Vamos Struke. ¿Por qué tanto énfasis en mencionarlo? ¿Qué tal si ella solo quiere ir al baño?"
    show steve 1amargado
    $ normal("steve")
    show strike 1enojadot
    $ enfocar("strike")
    st "La defiendes porque no sabes de lo que es {i}capaz{/i}."
    show strike 1enojado
    $ normal("strike")
    show steve 1juzgat
    $ enfocar("steve")
    tv "Loco, pareciera que la estás acusando de cometer un asesinato o de algo así..."
    show steve 1juzga
    $ normal("steve")
    $ renpy.pause(1.8, hard=True)
    show steve 1neutralt
    $ enfocar("steve")
    tv "¿O sí lo hizo?"
    show steve 1neutral
    $ normal("steve")
    "Dice medio tosiendo, como queriendo restarle peso."
    show steve 2remedar2t
    $ enfocar("steve")
    tv "Además, ¿qué tal si quiere ir al baño?"
    show steve 1remedar2
    $ normal("steve")
    show strike 1sarcasmot
    $ enfocar("strike")
    st "En serio se nota que ni conoces sus {i}grandes hazañas{/i}..."
    show strike 1sarcasmo
    $ normal("strike")
    l_thought "Su actitud, en serio me está sacando de quicio..."
    l_thought "A ver furro de mier-{nw}"
    show strike 1juzga
    l "Tu actitud es simplemente inspiradora. ¿Cómo logras ser tan... {i}especial?{/i}"
    show strike 1distraidot
    $ enfocar("strike")
    st "Ah, gracias. Pero no se compara con tu talento para los dramas."
    show strike 1sarcasmot
    extend " Ataques verbales, casi físicos..."
    show strike 1juzgat
    extend " ¿Quieres un escenario o así vas bien?"
    show strike 1seriot
    st "Por esas cosas, prefiero prevenir antes que lamentar."
    show strike 1serio
    $ normal("strike")
    l "Parece que te has tomado muy en serio tu papel de detective aficionado. ¿También tienes fotos mías o solo te conformas con chismes de pasillo?"
    l "Si vas a insultarme, al menos sé creativo."
    l_thought "Qué amable de tu parte recordarme lo mierda que soy. ¿Quieres un aplauso o solo buscas que te pegue para completar tu colección?"
    l_thought "Ya estoy harta. ¿En serio este tipo cree que está diciendo algo nuevo? Me cansa hasta la miseria."
    show steve 2rizzt
    $ enfocar("steve")
    tv "Bueno... A mi sí me gus-{nw=0.1}"
    show steve 2amargado
    $ normal("steve")
    show strike 1enojadot
    $ enfocar("strike")
    st "Junior. Por favor cállate. No ayudas con esto."
    show strike 1enojado
    $ normal("strike")
    show steve 1amargadot
    $ enfocar("steve")
    tv "Amigo, te estás poniendo demasiado a la defensiva con ella. Habrá hecho cosas feas, sí, pero... Tampoco es que quisiera hacerte daño."
    show steve 2remedart
    tv "Si la sigues jodiendo, te va a terminar arreglando la cara."
    show steve 1amargado
    $ normal("steve")
    show strike 1sarcasmo
    "El chico piensa un poco con lo mencionado."
    l_thought "Tal vez estás empujando los límites de mi temperamento actual. Y más te vale que lo hagas."
    pause 1.5
    show steve 1vacilante
    show strike 1distraidot
    $ enfocar("strike")
    st "{i}Por esta vez, tienes razón{/i}."
    st "Disculpa, Laila. No quería despertar a la fiera que llevas dentro."
    show strike 1distraido
    $ normal("strike")
    l "¿Ahora {i}si{/i} me dejas hablar?"
    $ enfocar("strike")
    show strike 1sarcasmot
    st "Claro. Adelante."
    show strike 1sarcasmo
    $ normal("strike")
    l "BIEN. Ahora..."
    l "¡¿Me dejas ir al baño!?"
    l_thought "Ya solo quiero largarme de aquí, aunque la excusa sea patética."
    l_thought "Pero cualquier excusa es buena para salir de esta situación."
    show steve 1remedar
    show strike 1seriot
    $ enfocar("strike")
    st "Si te soy honesto, no creo que realmente tengas {i}ganas{/i} de ir al baño."
    show strike 1serio
    $ normal("strike")
    l "¿Quieres que me cague aquí mismo? Y juzgando tus… “rasgos” de cosplayer promedio. No creo que eso te agradaría para tu “nariz sensible”."
    $ enfocar("strike")
    show strike 1enojadot
    st "Y cuando pusiste esa cara cuando mencioné que estabas escuchando... ¿Acaso esperabas que no me diera cuenta?"
    show strike 1enojado
    $ normal("strike")
    l_thought "Genial, La soga ya está perfectamente atada… como mi voluntad de vivir. Tengo que hacer algo ahora."
    l "¿Qué querías que hiciera? ¿Aplaudir tu increíble capacidad de detective frustra--{nw=0.1}"
    show steve 2remedart
    $ enfocar("steve")
    tv "Struke tu serias la 3ra persona más desastrosa de la escuela aparte de Manin y… Por lo que me dices, incluyamos a esta señorita."
    show steve 1amargado
    $ normal("steve")
    l "¿Disculpa? ¿Hay ranking?"
    l_thought "Ah, ¿así que ahora soy un “desastre”? Qué honor..."
    show strike 1seriot
    $ enfocar("strike")
    st "A ver, dame al menos 3 justificaciones razonables del porqué consideras que sería alguien desastroso."
    "Antes de que Steve soltara una palabra siquiera, lo interrumpe."
    show strike 1enojadot
    st "Y si vas a mencionar lo de mi campaña para presidente del consejo, mejor cállate. Que eso salió mal... Para {i}todos{/i}."
    show strike 1enojado
    $ normal("strike")
    show steve 2amargado
    "Steve finalmente guarda sus palabras al acertar qué diría ese mismo suceso solo sobando su cuello apenado."
    l_thought "Con amigos así… ¿para qué necesitas enemigos?"
    l_thought "Esto parece más una relación de tortura mutua."
    l "¿Y exactamente qué propones para “solucionar” esto? Porque me tienes aquí contra mi voluntad, y mis ganas de ir al baño no son negociables."
    show steve 1neutralt
    $ enfocar("steve")
    tv "Oye, porfa no digas que la vas a seguir al baño."
    show steve 2neutralt
    extend " Eso ya sería de otro nivel de raro."
    show steve 2neutral
    $ normal("steve")
    show strike 1juzgat
    $ enfocar("strike")
    st "No estaba pensando en esa idea. Pero tampoco voy a ignorar que hay un mentiroso."
    show strike 1seriot
    extend " Por no decir {i}mentirosa{/i}."
    show strike 1juzga
    $ normal("strike")
    l_thought "Este furro con complejo de sheriff no me va a dejar ir ni aunque me meé aquí mismo."
    show steve 1juzgat
    $ enfocar("steve")
    tv "Dice el que no puede darme una respuesta cuando le pregunto que carajo hace en {i}aquel cuarto de cierta parte{/i} de la escuel—{nw=0.1}"
    show steve 1juzga
    $ normal("steve")
    show strike 1enojadot
    $ enfocar("strike")
    st "{i}Eso no te incumbe{/i}."
    show strike 1enojado
    $ normal("strike")
    "Interrumpe a Steve, diciendo eso con un tono muy cortante al instante que dijo eso."
    l_thought "Quizás Steve sabe algo que Strike prefiere mantener {i}oculto{/i}. Aunque, viniendo de él, con esa cara de tarado, quién sabe."
    show screen semiblack
    $ renpy.pause(1.5, hard=True)
    show strike 1enojadot
    "Solo los escucho discutir brevemente de ese tema. Honestamente no le quiero dar importancia a eso, solo me meto más en mis pensamientos con respecto al cuarto mencionado."
    l_thought "¿Un cuarto? ¿En esta escuela? La verdad, nunca he prestado atención más allá de la dirección, mi salón y esos malditos casilleros que parecen multiplicarse como cucarachas."
    show strike 1enojado
    show steve 1juzgat
    l_thought "Quizás yo estaba tan metida en mi mente que me sorprendió de que existiera algo más... Algo que no fuera yo misma dándole vueltas a lo mismo de siempre."
    show strike 1sarcasmot
    show steve 1juzga
    $ renpy.pause(1.5, hard=True)
    show steve 2triste2t
    "Empiezo a sentir una tristeza profunda al recordar los momentos con {i}ella{/i}."
    show strike 1seriot
    l_thought "Cuartos secretos... Suena a algo que ella y yo hubiéramos fantaseado encontrar entre clases. Pero nunca miramos más allá de escapar entre clases."
    show strike 1serio
    show steve 2juzgat
    l_thought "Ahora solo me guardo eso a mí misma..."
    l_thought "Solo me quedan los ecos de su risa y este vacío que crece cada vez que recuerdo."
    show steve 2juzga
    extend " Ahora todo es diferente. Y me duele recordarlo."
    hide screen semiblack with dissolve
    show strike 1sarcasmot
    $ enfocar("strike")
    st "Ugh. Ese no es el punto Steve. Y no discutamos estos temas frente a la{nw}"
    show strike 1enojadot
    extend" {i}señorita chismosa{/i}."
    show strike 1enojado
    $ normal("strike")
    "Solo miro frunciendo el ceño, levantando una ceja bastante incrédula de lo que está diciendo."
    l_thought "Aunque, siendo honesta el hecho que le den tanto énfasis a eso despierta mi curiosidad"
    l "Ajá, sí, sí. Discutan como viejas chismosas después. ¿Ya me dejan ir al baño? ¡Se me va a reventar la puta vejiga!"
    "Steve logró taparle la boca a Strike enseguida, sabiendo que no lo dejaría ni hacer nada hasta acabar el receso."
    show strike 1juzga
    show steve 1amargadot
    $ enfocar("steve")
    tv "Ve Laila, será mejor que vayas antes de que el pelotudo se le ocurra encadenarte y dejarte ahí."
    show strike 1sarcasmo
    show steve 2remedar
    $ normal("steve")
    l_thought "¿Encadenar? ¿Aquí todos tienen fetiches raros o es solo el ambiente?"
    hide steve with Dissolve(0.5)
    hide strike with Dissolve(0.5)
    "Solo me voy sin chistar, fingiendo que voy al baño mientras los oigo de nuevo discutir."
    play audio closet_open
    pause 1.0
    stop ambient fadeout(1.5)
    scene black with Fade(1.0, 1.0, 1.0)
    play audio closet_close
    l_thought "Ya no quiero oír nada de ese estúpido furro. Tal vez de Steve pero no de su amigo."

return