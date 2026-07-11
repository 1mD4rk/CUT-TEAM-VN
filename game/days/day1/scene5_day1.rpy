label scene5_day1:
     
    $ quick_menu = True
    with Dissolve(0.5)
    play music bgm3
    "Hay algo que siempre me ha gustado hacer... aunque suene patético: recapitular mi día."
    "Sí, ya sé, suena deprimente porque mis días son un bucle de la misma mierda, pero no sé..."
    "Me gusta pasarlo, como si fuera una forma de recordarme que todavía estoy aquí."
    extend " Que sobreviví otra vez. Así que… Déjenme contarles lo que viví, ¿de acuerdo?"
    show math with dissolve
    "Empecemos con lo “importante”, o lo que yo considero relevante:"
    show cbg_dark with dissolve
    "Conocí a alguien nuevo. Dice llamarse {outlinecolor=#da0303}{i}Dark{/i}{/outlinecolor}. Sí, así como lo oyen. {outlinecolor=#da0303}{i}Dark{/i}{/outlinecolor}."
    "No sé quién en su sano juicio se pondría un nombre así{w}, ¿Un villano de manga barato? pero bueno...{w} se lo paso."
    "Según él, es el {i}vicepresidente estudiantil{/i}. Suena formal, pero él... No. Para nada."
    "Creo que lo he visto merodeando por los pasillos como un alma perdida, o a veces en el salón, dibujando como si el mundo no existiera."
    "Pero realmente, no lo recuerdo o no me había fijado mucho en él. Raro. {i}Muy raro.{/i}"
    hide cbg_dark with dissolve
    "Una vez eso, fui a mi lugar favorito, dónde quería algo de paz..."
    show cbg_st_tv with dissolve
    "Pero aparecieron un {outlinecolor=#2634aa}{i}furro{/i}{/outlinecolor} y un {outlinecolor=#805d12}{i}chico aparentemente normal{/i}{/outlinecolor}."
    "Realmente no quería hablar con nadie, pero el maldito intento fracasado de sheriff me estaba sacando de quicio."
    "No sé cómo no le metí un golpe {i}allí mismo{/i}."
    "Aunque... No puedo negar que lo que decía era verdad."
    extend " Cada palabra que salía de su boca estaba pegada con una verdad inminente, que me caía como el peso de un yunque sobre mi cuerpo."
    "..."
    "Ah, y esta el chico normal, ese extrañamente se enamoró de mí... No sé cómo ni el porqué, y es mejor dejarlo así."
    hide cbg_st_tv with dissolve
    pause 1.5
    show cbg_dirc with dissolve
    "Después... el {outlinecolor=#5d4037}Director{/outlinecolor}. Y sí, lo digo como si fuera algo especial, porque lo fue. Nadie se había preocupado por mí en mucho tiempo."
    "O al menos, {i}eso sentí{/i}."
    "(Exceptuando mi padre y {outlinecolor=#da7603}Blaze{/outlinecolor})."
    "Como si hablara “de mi lado” por primera vez, como si alguien recordara que existo."
    "Incluso con todo el desastre que yo misma provoqué, fue capaz de hacer algo. Fue...{w} Extraño."
    "Incomodísimo, pero extraño. Me dejó algo agotada, sinceramente."
    hide cbg_dirc with dissolve
    $ renpy.pause(2.1, hard=True)
    show cbg_b_ptod with dissolve
    "Y luego... está {outlinecolor=#da7603}{i}Blaze{/i}{/outlinecolor}."
    "Ugh... preferiría no hablar de eso. No después de cómo la traté en clase.{w} Dios... La humillé delante de todos."
    "¿En qué carajos estaba pensando? Mentira, ni siquiera estaba pensando, como siempre."
    "Ahora seguro me {i}odia{/i}. Y si soy sincera, yo también lo haría. Si ella me hubiera hecho pasar por lo mismo, la odiaría sin dudarlo."
    $ renpy.pause(1.0, hard=True)
    show cbg_bz with dissolve
    hide cbg_b_ptod
    "Lo peor es que ella... Ella es demasiado buena."
    "De esas personas que todavía creen en el bien aunque el mundo les escupe en la cara. Es como si fuera un alma “pura”."
    "Y yo fui la que la hizo pedazos delante de {i}todos{/i}."
    "Bravo, Laila. Aplausos para ti."
    show screen red_effect2
    nobody "{sc=3}¿Cuántos llevas ya?{/sc}"
    nobody "{sc=5}¿Cuántos más necesitas para convencerte de que eres tú el problema?{/sc}"
    hide screen red_effect2
    pause 1.5
    hide cbg_bz with dissolve
    "..."
    "C-Como decía, las clases fueron igual de aburridas. No pienso mencionar nada más que esto."
    scene black with Fade(1.0, 1.0, 1.0)
    $ renpy.pause(2.0, hard=True)
    show layer master at night_purple
    "Me quedé dormida otra vez."
    extend " Ni siquiera escuché el timbre. Que, por cierto, suena como una canción de cuna distorsionada. Deberían cambiarlo."
    show pasillo2 with Fade(1.0, 1.0, 1.0)
    "Camino entre los pasillos abandonados y solitarios de la escuela."
    "Me crea una inquietud grande, como si alguien pareciera seguir mi ritmo y acercarse en la oscuridad y la poca luz lunar que ahora pega."
    "Y no hablo de alguien real. Hablo de esa sensación... como si algo (o alguien) me estuviera devorando por dentro."
    "Algo que ya vive conmigo. ¿Eso es posible?"
    l_thought "Después de todas las pesadillas que he tenido... ya nada me parece descabellado."
    $ renpy.pause(1.5, hard=True)
    #scene gatenight_l with Fade(1.0, 1.0, 1.0)
    play ambient ext_night fadein(2.0)
    "Salgo por fin del colegio, arrastrando los pies con un cansancio que va más allá de lo físico."
    "Ya a este punto solo veo a gente yendose de sus clubes, pues salí muy tarde de la escuela..."
    "No encontré a {outlinecolor=#da7603}Blaze{/outlinecolor} por los pasillos. Es lo mejor, me repito, aunque el alivio se siente como otro tipo de vacío."
    l_thought "No podría mirarla a los ojos después de lo de hoy. No todavía."
    scene intersection_night with Fade(0.5, 0.5, 0.5)
    "Camino hacia la esquina donde siempre me recogen, con la esperanza de que papá ya haya pasado por ella."
    "Miro a mi alrededor, esta “ciudad” que todavía se siente más como un decorado que como un hogar."
    "Y para mi gran sorpresa (o quizá mi mala suerte) los veo."

    show blaze 1sonriente with dissolve:
        right3
        night_urban
    show dark 1feli with dissolve:
        left3
        night_urban

    "Allí está {outlinecolor=#da7603}Blaze{/outlinecolor}. Y a su lado, como si hoy no hubiera sido lo suficientemente largo, está hablando con el susodicho {outlinecolor=#da0303}Dark{/outlinecolor}."
    l_thought "En cierta parte, me sorprende verlos... pero no debería. Después de todo, ya eran amigos."
    l_thought "Pero verla ahí, riendo tan fácilmente, como si entre ellos no existiera el peso que ahora me ahoga—{nw}"
    "Suspiro."
    l_thought "Cada sonrisa suya es un recordatorio de lo que le arrebaté hoy en el salón."
    "Siento cómo algo se contrae dentro de mi pecho. Como si algo filoso me atravesara."
    "Tomo el poco esfuerzo que me queda y me acerco sigilosamente."
    "Cada paso es calculado, silencioso. El corazón me late con un ritmo ansioso que contradice mi aparente calma."
    show blaze 1juzga2t
    $ enfocar("blaze")
    b "¿Y qué hiciste el fin de semana, Dark?"
    b "Jeremy y yo te llamamos para salir pero estuviste desaparecido."
    $ normal("blaze")
    show blaze 1juzga2
    show dark 1desafiantet
    $ enfocar("dark")
    d "Noté varias llamadas perdidas en mi celular. Si te contara, me tomaría toda la noche."
    d "Pero en resumen"
    show dark 2distraidot
    extend ", tuve que viajar a {i}cierto sitio{/i}..."
    show dark 1juzgat
    d "Y ahí me encontré luchando contra un tipo extraño de pelo blanco."
    d "No paraba de gritar “Jackpot” como si estuviera en su propio show."
    show dark 2desafiantet
    d "Era un poquito mayor que nosotros, pero créeme... Fue bastante entretenido."
    $ normal("dark")
    show dark 2desafiante
    show blaze 1felizt
    l_thought "¿Jackpot? ¿En serio? Esto suena a una historia MUY absurda."
    l_thought "Pero Blaze se ríe como si fuera lo más normal del mundo."
    extend " A veces me pregunto si vivo en la misma realidad que ellos..."
    show blaze 1feliz
    "Me quedo allí, paralizada, preguntándome si dar un paso adelante y enfrentar la situación o retroceder."
    pause 1.5
    show dark 1neutral
    "Es entonces cuando Dark gira ligeramente la cabeza. Sus ojos se encuentran con los míos por una fracción de segundo demasiado larga."
    show dark 2desafiantet
    $ enfocar("dark")
    d "Mira a quien tenemos por aquí... Laila Jackson."
    show dark 2desafiante
    $ normal("dark")
    "Dice eso con una soberbia muy absurda. Irritandome."
    show blaze 3seria
    "Blaze, volteando por curiosidad, me ve. Su expresión cambia instantáneamente. Su sonrisa se borra lentamente,  sus ojos se entrecierran y ligeramente frunce el ceño, mierda sí parece decepcionada."
    "Me quedo completamente quieta, atrapada en el acto."
    "No digo nada. El silencio se espesa entre nosotros, pesado e incómodo."
    show dark 2juzga2
    "Dark mira de Blaze a mí, como esperando que alguna rompa la tensión."
    l_thought "¿Y ahora? ¿Qué se supone que debo hacer? ¿Disculparme? ¿Gritar? ¿Correr? Cada opción me parece igual de equivocada."
    $ renpy.pause(2.5, hard=True)
    "Los segundos pasan. Una tensión palpable se instala en el aire crepuscular."
    "Finalmente, Dark rompe el silencio."
    show dark 1desafiantet
    $ enfocar("dark")
    d "Tengo entendido que tu nueva pasión es coleccionar conversaciones ajenas. Ya tengo algo nuevo de ti."
    show dark 1desafiante
    $ normal("dark")
    "Aunque lo dice con un tono ligero, sus palabras me golpean como un puñetazo en el estómago."
    "El mundo parece reducirse a ese instante, y siento cómo el suelo se inclina bajo mis pies."
    l_thought "¿Qué? ¿Qué significa eso? ¿Acaso conoce a Strike y a Steve? ¿Cuánto sabe exactamente?"
    l_thought "¿Cuánto escuchó? ¿Lo suficiente para hundirme? ¿O solo está jugando conmigo como un gato con un ratón?"
    show dark 1neutral
    "Dark lo nota."
    "Sus ojos se estrechan ligeramente, captando cada microexpresión de mi rostro que delata el torbellino interno."
    show dark 1distraido2
    $ enfocar("dark")
    d "..."
    $ normal("dark")
    "Un silencio incómodo se cuela entre nosotros, cargado de todo lo que no se dice."
    show dark 1distraidot
    $ enfocar("dark")
    d "Eh... Olvidé que tengo que llegar temprano a casa. Tengo algunas cosas que hacer..."
    "La retirada es abrupta, casi torpe. Se da media vuelta y se empieza a ir con rapidez."
    $ normal("dark")
    show dark 1distraidot at outwalk_right3
    #play audio miedomujere

    if (rutaCanon-rutaSuicida)>=0:
        d "Nos vemos, Blaze. Nos vemos, Laila."
        l_thought "¿Es genuino? ¿O es una huida elegante para no profundizar en lo que acaba de insinuar?"
    else:
        d "Nos vemos, Blaze. Tú... cuídate. O lo que sea."
        l_thought "Por fin se fue. Su sola presencia me exaspera. Cada palabra suena falsa, cada mirada es un juicio."

    hide dark
    stop music
    show blaze 3desinteresada3 at anim_center
    "No volteo. Me quedo paralizada, escuchando cómo sus pasos se alejan. cada una de sus pisadas un eco que resuena en el silencio que deja atrás."
    "Cada paso que se aleja debería ser un alivio, pero solo siento el vacío que deja su partida repentina, y la inquietante sensación de que esto está lejos de terminar."
    "Mis pies parecen pesar una tonelada mientras me arrastro hasta el lado de Blaze, cada paso una batalla perdida contra la gravedad de mi propia culpa."
    "Las fuerzas me abandonan pero igual me arrastro hasta su lado."
    extend " Porque aunque no merezco su perdón, es el único lugar que me queda."
    $ renpy.pause(3.0, hard=True)
    "El auto de papá aún no llega. El silencio entre Blaze y yo es más denso que la niebla de la mañana."
    $ renpy.pause(3.0, hard=True)
    "Ella no me mira. Yo no me atrevo a mirarla del todo. Cada segundo que pasa es un recordatorio de lo que hice."
    l_thought "¿Cómo puedo empezar? ¿un “Lo siento” basta?"
    l_thought "..."
    l_thought "Nada basta. Nada borra lo que dije."
    l_thought "Ella debe odiarme. Sería lo justo."
    $ renpy.pause(3.0, hard=True)
    l_thought "Si me disculpo, ¿me aceptara? ¿me dirá que me vaya a la mierda?"
    l_thought "¿Siquiera podría verla a los ojos nuevamente?"
    l_thought "Si yo fuera la víctima... Creeme que ni siquiera me hubiera quedado a esperarla."
    $ renpy.pause(3.0, hard=True)
    "Respiro hondo. Siento como la culpa me sube poco a poco por la espalda."
    play music bgm4 
    l "..."
    l "B-Blaze."
    show blaze 3neutral at shake
    "Ella no responde."
    extend " Noto que está un poco a la defensiva al empezar la conversación, simplemente presiona levemente la correa de su mochila."
    l "Oye...{w} yo..."
    "Las palabras no salen. Se atoran en mi garganta, junto con el nudo de llanto que me he tragado todo el día."
    show blaze 2seria2t
    $ enfocar("blaze")
    b "Ya sé que quieres disculparte… no hace falta que lo digas."
    show blaze 2seria2
    $ normal("blaze")
    l "Sí hace falta. Yo... lo que dije... no lo pensé."
    show blaze 2compadecer at sigh_animation
    "Ella suspira."
    show blaze 2compadecert
    $ enfocar("blaze")
    b "¿Al menos estás bien?"
    show blaze 2compadecer
    $ normal("blaze")
    l "..."
    l "¿Qué?"
    "La simple pregunta, la misma que hizo Dark horas antes, me desarma por completo. No es lo que esperaba."
    "Pero no suena con un reproche, sino con una preocupación serena."
    l_thought "Por favor, Grítame. Odiame. Cualquier cosa es mejor que esta simpatía por mi."
    l_thought "Eso duele más. Porque significa que te importé. Que te importo."
    "Miro hacia el concreto en el cual estoy parada. No la puedo mirar a los ojos."
    show blaze 3desinteresada3t
    $ enfocar("blaze")
    b "Es verdad que estoy furiosa contigo..."
    show blaze 3desinteresada2t
    extend " No voy a mentirte."
    show blaze 2compadecer
    $ normal("blaze")
    "Se acerca un paso, lentamente, como si se acercara a un animal asustado."
    show blaze 2compadecert
    $ enfocar("blaze")
    b "Pero también sé que no quisiste herirme."
    b"Fue... el dolor, el cansancio, esos pensamientos que a veces te consumen por dentro."
    extend " ¿Correcto?"
    show blaze 2compadecer
    $ normal("blaze")
    "Niego con la cabeza, incapaz de articular palabras."
    "Se queda en silencio, pensando en las siguientes palabras que dirá."
    $ renpy.pause(1.5, hard=True)
    show blaze 2compadecert
    $ enfocar("blaze")
    b "Yo te conozco, Laila. Te conozco desde que éramos niñas y te escondías en el armario cuando mamá y papá discutían."
    show blaze 1compadecert
    b"Eres mi hermana. Aunque no compartamos sangre. Eres mi hermana. Y eso no lo cambia un mal día, ni una palabra dicha por frustración."
    show blaze 1neutral
    $ normal("blaze")
    l "¿Por qué no me odias? Deberías odiarme. Yo... yo te lo dije delante de todos. Te grité. Te humillé."
    "Después de todo, por fin logró articular palabras coherentes."
    l "Dije que no eras mi hermana... y lo sabes, Blaze, sabes que no es verdad."
    l "Tú... tú eres lo más preciado que tengo..."
    show layer master:
        function apply_blur_gradually2
    "Siento como las lágrimas empiezan a brotar poco a poco." 
    l "Lo siento. Lo siento. Lo siento, Blaze. Lo siento mucho."
    l "Lo siento por ser una hermana terrible, lo siento por no ser la hermana que necesitas, lo siento, lo siento."
    show blaze 3feliz at hug_on
    "Blaze cierra la distancia restante y me envuelve en un abrazo firme y seguro."
    "No es un abrazo dramático, sino uno contenido, lleno de una fuerza tranquila."
    show blaze 3felizt
    b "Shhh... Ya lo sé. También lo siento."
    show blaze 3feliz
    "Me quedo paralizada. No esperaba ningún acercamiento por ahora."
    "Pero, sintiendo el peso de todo el día en mi espalda. Me derrumbo contra ella, Me aferro a su camisa como si fuera un salvavidas."
    l "Tú... ¿por qué? Tú no hiciste nada malo. Yo fui la... la..."
    show blaze 3compadecert
    b "Lamento haberte respondido así... Todo ha sido tan difícil..."
    b "Pero sobre todo, siento que hayas tenido que cargar con todo esto sola."

    if (rutaCanon-rutaSuicida)>=0:
        show blaze 3desinteresadat
        b "Dark me contó lo de la dirección... y que casi te metes en otro problema en la azotea. Apenas me pude enterar por él. Parece preocupado por ti."
        show blaze 3desinteresada
        "Siento cómo su tono se vuelve más compasivo, más comprensivo."
        l_thought "¿Preocupado? ¿De verdad?{w} No sé por qué, pero esa idea... Duele de una manera diferente."
        l_thought " Como si alguien hubiera visto a través de mi armadura sin que yo lo notara."
    else:
        show blaze 3desinteresadat
        b "Dark me contó lo de la dirección... y que estuviste en la azotea. Parece preocupado por ti."
        show blaze 3desinteresada
        l "¿Preocupado?"
        "Una risa amarga escapa de mis labios."
        l "Ese finge preocupación mejor de lo que yo finjo estar bien."
        show blaze 1preocupadat
        b "Laila, no seas así. Él sol-{nw}"
        show blaze 1preocupada
        l '¿Solo QUÉ, Blaze? ¿Quiere "ayudar"?'
        "Hago comillas en el aire con los dedos."
        l "Nadie quiere ayudar, Blaze.{w} Déjame adivinar: ¿quieres que crea que le importo? ¿Que a ALGUIEN le importo?"
        l_thought "La verdad es que soy un caso perdido y todos lo saben. Solo están esperando a que me rinda por completo."

    show blaze 3compadecert
    b "Sé que la muerte de mamá te ha afectado mucho. Te entiendo. A mi también me ha afectado."
    show blaze 3compadecer
    l "¿Cómo... cómo puedes ser así? Después de lo que hice..."
    show blaze 3felizt
    b "Porque {i}te amo{/i}. No tienes la culpa de eso y…"
    b "Porque no quiero que te sientas sola... Te disculpo."
    show blaze 3feliz
    "El peso en mi pecho se alivia un poco, solo un poco, pero es el primer respiro de aire fresco que tengo en todo el día."
    $ renpy.pause(1.8, hard=True)
    show blaze 3neutral2 at hug_off
    "Blaze se separa un poco, manteniendo las manos en mis hombros para mirarme a los ojos. Su expresión es seria pero suave."
    show blaze 3neutral2 at center
    $ renpy.pause(1.8, hard=True)
    "Hace una pausa, su tono se vuelve un poco más práctico, mostrando su lado de “mano dura” pero con cariño."
    show blaze 1seriat
    $ enfocar("blaze")
    b "Pero eso no significa que lo de hoy esté bien. No lo está. Tienes que trabajar en eso, Laila. De verdad."
    b "No puedes seguir así. Te estás haciendo daño a ti misma y alejando a todos los que intentan ayudarte."
    b "Hoy pude haber sido yo, quizás nadie tenga la misma paciencia que yo."
    show blaze 1desinteresadat
    extend " Creelo."
    show blaze 1desinteresada
    $ normal("blaze")
    show layer master:
        matrixcolor IdentityMatrix()
    with dissolve    
    "Me limpio un poco las lágrimas."
    l "Lo sé..."
    show blaze 1feliz at sigh_animation
    "Ella suspira, como si se hubiera quitado un peso de encima."
    show blaze 1felizt
    $ enfocar("blaze")
    b "Me alegro que lo sepas. Realmente me alegro."
    show blaze 1feliz
    $ normal("blaze")
    "Sonríe, una sonrisa genuina que por primera vez hoy no me duele ver."
    show blaze 1sonriente
    "Me mira profundamente con sus ojos verdes, y siento tranquilidad."
    "Se aleja un poco más de mí, con su sonrisa impecable y reconfortante."
    "El ambiente ya no se siente tenso, se siente... tranquilo. Como si una tormenta hubiera pasado."
    l_thought "El aire por fin se puede respirar de nuevo."
    $ renpy.pause(0.5, hard=True)
    "Pero no significa que la discusión dentro de mí se haya apaciguado."
    show screen semiblack
    l_thought "Ahora tengo un nuevo problema. {i}El reporte{/i}."
    l_thought "La puta hoja de papel. La confirmación física de todo mi fracaso de hoy. La evidencia que tengo que entregarle a papá."
    l_thought "¿Y qué le digo? ¿“Firma esto, por favor. Es solo la constancia de que tu hija es una decepción andante”? ¿“Oye, ¿te importaría avalar mi comportamiento de mierda con tu firma”?"
    l_thought "Él ni siquiera sabe lo de Blaze todavía. Lo de Todd era suficiente, pero ahora esto... esto es peor."
    l_thought "Esto es personal. Esto es... herir a la única persona en esa casa que todavía me mira sin ese destello de preocupación constante en los ojos."
    "Siento el papel como si quemara a través de la tela. Cada palabra del director repicando en mi cabeza:"
    dirc "...piensa en tu futuro... no puedes seguir siendo un ejemplo negativo…"
    l_thought "Ejemplo negativo. Viniendo de él, hasta suena educado. Yo sé lo que soy. Un problema. Una carga. Un recordatorio ambulante de todo lo que sale mal."
    l_thought "Y ahora tengo que poner eso en las manos a papá. Ver cómo se le apagan los ojos. Cómo su ya eterno cansancio se profundiza solo un poco más, por mi culpa."
    l_thought "Siempre por mi culpa."
    show blaze 1neutralt
    $ enfocar("blaze")
    b "¿Laila?"
    show blaze 1neutral
    $ normal("blaze")
    hide screen semiblack with dissolve
    "La voz de Blaze me saca del torbellino. Suena preocupada de nuevo. He guardado silencio demasiado tiempo."
    "Suspiro."
    l_thought "Supongo que se lo debo contar a ella primer-{nw}"
    show blaze 1desinteresada2t
    $ enfocar("blaze")
    b "Piensas en el reporte, ¿verdad?"
    show blaze 1desinteresada2
    $ normal("blaze")
    "La miro perpleja. Eso me desconcierta."
    l_thought "¿Cómo carajos lo sabe? ¿Acaso lo vio? ¿O es que mi cara de “tengo un problema gigante” es tan obvia?"
    show blaze 2neutralt
    $ enfocar("blaze")
    b "Realmente, lo sospeché. Después de lo de la dirección... era lo lógico."
    show blaze 2seria2t
    b "Y bueno... Durante nuestra conversación Dark... mencionó algo."
    show blaze 2seria
    $ normal("blaze")
    l_thought "Claro que sí. {i}El vicepresidente metiche{/i}."
    l_thought "¿Qué más le contó? ¿Que también parezco una mendiga y que me insulté con unos randoms en la azotea? ¿Que estoy tan rota que hasta el director me dio lástima?"
    "Un escalofrío de rabia y vergüenza me recorre. Mi privacidad es una broma para todos."
    show blaze 2nerviosat
    $ enfocar("blaze")
    b "¡No me dio detalles!"
    "Agrega rápidamente, como si percibiera mi incomodidad creciente."
    show blaze 2compadecert
    b "Solo eso. Lo suficiente para preocuparme."
    show blaze 2compadecer
    $ normal("blaze")
    l_thought "Preocupación..."
    "El fuego de mi ira se apaga un poco, dejando solo las cenizas de la ansiedad."
    show blaze 2compadecert
    $ enfocar("blaze")
    b "Solo... respira. Cuando se lo des... no va a gritarte."
    show blaze 3seria2
    $ normal("blaze")
    $ renpy.pause(1.5, hard=True)
    "Hace una pausa infinitesimal, y un destello de duda honesta cruza sus ojos."
    show blaze 3seria2t
    $ enfocar("blaze")
    b "{i}O eso... espero{/i}."
    show blaze 3seria2
    $ normal("blaze")
    "Dice eso último como si intentara convencerse a sí misma también."
    l_thought "Esa pequeña duda. Esa es la que me mata. Ni siquiera ella está segura. Porque nosotros sabemos cómo es papá con sus silencios."
    l_thought "Eso es lo peor. Preferiría mil veces que gritara. Que me gritara, que se enojara, algo. Pero no. Él no hace eso."
    l_thought "Solo se queda quieto, leyendo, con esa expresión... esa expresión de una decepción tan profunda y silenciosa que te hace desear haberle dado un golpe en su lugar."
    l_thought "Porque la decepción duele más que la ira. La ira estalla y se va. La decepción se instala, se enraíza y se pudre todo a su alrededor."
    l_thought "Y yo, al parecer, soy su principal proveedora."
    play audio car_horn volume 0.3
    stop music
    show blaze 1neutral at boo
    "Un claxon familiar suena a lo lejos, haciendo que ambas nos sobresaltemos.{w} Papá ya llegó."
    show blaze 1sonriente
    "Blaze me mira, y en sus ojos ya no solo hay preocupación por mí, sino una complicidad compartida, un “estamos en esto juntas”. Después de ese error monumental que cometí."
    "Eso me reconforta un poco."
    "El carro se estaciona frente de nosotros y baja la ventana del copiloto."
    show counter 1feliz with dissolve:
        night_urban
        right
        flip
    show blaze 1sonriente at center_flip
    show counter 1felizt
    $ enfocar("counter")
    dad "Hola, niñas. ¿Cómo estuvo el día?"
    show counter 1feliz
    $ normal("counter")
    "Yo me retuerzo un poco al escuchar eso. Blaze lo nota y responde primero sonriendo."
    show blaze 1felizt at center_flip
    $ enfocar_flip("blaze")
    b "¡Bastante bien!"
    show blaze 1feliz at flip
    $ normal_flip("blaze")
    "Yo sigo sin soltar ninguna palabra, solo espero que Blaze resuelva un poco."
    show blaze 1juzga2t at flip
    $ enfocar_flip("blaze")
    b "Y a ti, papá, ¿cómo te fue?{w} Te ves cansado. ¿El trabajo estuvo pesado?"
    show blaze 1juzga2 at flip
    $ normal_flip("blaze")
    show counter 1nosurpriset
    $ enfocar("counter")
    dad "Pesado, sí... pero nada nuevo.{w} Lo importante es que ya estoy aquí."
    show counter 1feliz
    $ normal("counter")
    "Mi padre me mira un segundo. Yo evito su mirada. Simplemente intento modular un “Bien” y él asiente."
    show counter 1seriot
    $ enfocar("counter")
    dad "Bien. Súbanse, que quiero llegar a casa"
    show counter 1serio
    $ normal("counter")
    l_thought "Su mirada se posó en mí un segundo de más."
    l_thought "¿Lo notó? ¿Notó lo raro que soné? ¿O solo estoy paranoica y proyectando mi culpa sobre cada uno de sus gestos?"
    play audio open_car_door
    "Blaze abre la puerta trasera y nos montamos en el auto, las dos en los asientos de atrás, ya que papá tiene un extraño bolso en el asiento del copiloto{w}, que por cierto, donde Blaze se suele sentar."
    hide counter with dissolve
    hide blaze with dissolve
    stop ambient fadeout(1.5)
    scene black with Fade(0.3, 0.3, 0.3)
    play audio close_car_door
    play ambient bus fadein(2.0)
    $ renpy.pause(6.5, hard=True)
    "En el auto simplemente hay un silencio, no incomodo, pero sí tenso."
    $ renpy.pause(6.0, hard=True)
    b "¿Psss… Laila? ¿Y cómo planeas decirle?"
    "Blaze rompe ese silencio. Susurrandome."
    "Me sobresalto, ya que estaba con mis pensamientos."
    l "P-Pues... Supongo que le diré cuando lleguemos a casa... Aquí no puedo."
    l_thought "Realmente no quiero hacerlo, afrontarlo me da miedo. No quiero mirar a sus ojos cuando le entregue el reporte."
    l_thought "Pero es eso o que el director lo llame apenas le diga que no tengo el reporte..."
    "Ella asiente."
    b "Bueno... cuando lo hagas, yo estaré ahí contigo. No tienes que hacerlo sola."
    "Volteo a verla sorprendida y para ser sincera, algo de alivio."
    l "..."
    l "¿En serio?"
    b "Claro. No es justo que te comas sola ese regaño."
    b "Además, tal vez sí estamos las dos, se le pasa más rápido el enfado."
    "Dice eso con una sonrisa genuina que casi parece real, y me guiña un ojo."
    "Por un segundo, un segundo estúpidamente frágil, casi le creo."
    l_thought "En verdad... No te merezco, Blaze."

    if (rutaCanon-rutaSuicida)<=-1:
        "Su sonrisa parece forzada, como si estuviera siguiendo un guión. Sus ojos no se sonríen como antes."
        l_thought '¿Es en serio?{w} ¿O solo quieres asegurarte de que papá vea que la "hermana buena" está haciendo su parte?'

    show screen red_effect
    nobody "{sc=3}¿Crees que es así de simple?{/sc}"
    nobody "{sc=3}¿Que un guiño y una sonrisa borran lo que hiciste?{/sc}"
    nobody "{sc=3}Es más fácil soportar la decepción de dos que la de una.{/sc}"
    nobody "{sc=3}No es lealtad, es pragmatismo.{/sc}"
    nobody "{sc=3}Ella solo quiere que esto termine rápido.{/sc}"
    nobody "{sc=3}Te está usando para su propia paz mental.{/sc}"
    nobody "{sc=3}Para quedar como la hermana buena ante tu padre.{/sc}"
    nobody "{sc=5}¿No lo ves?{/sc}"
    nobody "{sc=3}La buena hermana consolando a la rota, la problemática. Así queda mejor.{/sc}"
    nobody "{sc=3}¿Crees que de verdad le importas?{/sc}"
    l_thought "..."
    "Evito ponerme a llorar aquí mismo. Siento como si me estuvieran golpeando la cabeza contra el concreto."
    nobody "{sc=3}Ella te odia. En el fondo, te odia por obligarla a ser esto.{/sc}"
    nobody "{sc=5}Tenlo por seguro.{/sc}"
    nobody "{sc=3}Esto solo es... el calmante antes de que te saquen del juego.{/sc}"
    hide screen red_effect with Dissolve(1.0)
    "Un frío recorre mi espalda. La voz no suena a rabia, suena a lógica fría y devastadora. Y es tan, tan fácil de creer."
    "La sonrisa de Blaze sigue ahí, pero ahora la miro buscando grietas, buscando el destello de falsedad que la voz me promete que está allí."
    l_thought "..."
    l_thought "¿P-Por qué no puedo simplemente aceptarlo?"
    $ quick_menu = False

return