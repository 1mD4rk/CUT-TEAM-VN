label day1: 
    $ discord.set(details="Monday - (15/02/2066)", state="Day 1")
    $ phone.system.battery_level = 100
    #$ phone.system.date = datetime.date(2066, 2, 15)

    $ contador = 0

    play music classroom fadeout 1.0 fadein 3.5
    pause 4.0 
    $ persistent.quick_menu_visible = True 
    with Dissolve(0.5)
    show screen phone_button with Dissolve(0.5)
    idk1 "Se... Jac..."

    pause 3.0 
    "Oigo a alguien decir algo...{w} No lo entiendo."

    pause 3.0
    scene class3A-blur1 with Dissolve(2.0)
    pause 1.0

    scene black with dissolve 
    idk1 "Seño.. Jacks..."

    pause 3.0 
    l_thought "Déjame{w}, solamente quiero dormir..."

    pause 3.0 
    idk1 "Ultimo llamado, Señorita Jackson."

    scene class3A-blur with Dissolve(2.0)
    show ptod cruzado at center, fade_in
    "Una vez escuché esa advertencia... me levanto de mi dulce y reparador sueño."
    "Nótese el sarcasmo."
    "Levanto a mis músculos que protestaron al empujar mi cuerpo hacia arriba. El mundo giró levemente, una náusea familiar se instaló en mi estómago vacío."

    l_thought "Al parecer, lo primero que veo al despertar es algo horrible{w}, feo{w} y horripilante..."
    l_thought "Al profesor de biologia... Todd."

    "Tomo un bostezo."

    $ enfocar("ptod")
    ptod ".  {w=0.8}.  {w=0.8}."

    $ normal("ptod")
    "Lo miro con indiferencia, no sé que estará esperando."

    $ enfocar("ptod")
    ptod "Estoy esperando su tarea."

    $ normal("ptod")
    l "¿Tarea?"
    show ptod cruzado at sigh_animation
    "Él suspira."

    $ enfocar("ptod")
    ptod "Usted ya debería saber.{w=0.5} ¿El informe sobre las celulas eucariotas?"

    $ normal("ptod")
    l "..."
    "Decido quedarme en silencio, por obvias razones."

    pause 3.5
    
    show ptod tieso at center
    $ enfocar("ptod")
    ptod "Espero que su 'perro' no se haya comido {i}convenientemente{/i} su tarea."
    ptod "Como al tan conocido {i}{outlinecolor=#039dda}Presidente del Consejo Estudiantil{/outlinecolor}{/i}. Esa vez dando el ejemplo."

    $ normal("ptod")
    play sound teens_laugh volume 0.5
    pause 0.5

    l_thought "No desaprovechó la oportunidad de hacer un chiste tan malo."
    "Toda el aula se rie, obviamente él lo dijo con esa intención."

    show blaze 1neutral at right2, fade_in
    "Trato de mirar a otro lado, evitando molestarme más."
    "Pero en mi visión aparece mi hermanastra, Blaze, se le nota la preocupación en el rostro."
    $ inac("ptod")
    $ inac("blaze")
    

    "Volteo hacia el otro lado, tratando de evitar la mirada de los dos."
    "Algunos se siguen riendo del mal chiste de Todd. Las risas poco a poco me están empezando a irritar."
    pause 1.0
    "Intento tomar aire para tranquilizarme."
    
    $ enfocar("ptod")
    ptod "En fin...{w} ¿Y el informe, Señorita Jackson?"

    $ normal("ptod")
    "Suelto un suspiro agotado, ya harta de toda la situación."

    l "JA{w=0.5} JA{w=0.5} JA."
    "Solté una risa hueca, más por costumbre que por gracia."
    pause 0.5
    "Mi mirada se encuentra nuevamente con la del profesor, sus ojos ya mostrando algo de duda ante la risa que solté."

    l "Yo le pregunto...{w} ¡¿QUÉ MIERDA ME GANARÍA YO AL HACER ESE INFORME?!"
    stop music
    show blaze 1desinteresada2

    "Un silencio repentino ahoga el salón. Empiezo a sentir como la mirada de todos posándose sobre mí."

    window hide 
    pause 4.0    
    window show 

    $ enfocar("ptod")
    ptod "¿He oído eso bien?"
    $ normal("ptod")

    l "En tal caso de ser sordo, puede ser que no."

    $ enfocar("ptod")
    ptod "Jackson, cambie el rumbo de esa actitud. Ahora."
    $ normal("ptod")

    "Su voz empezó a tomar un tono más fuerte, más autoritario."
    "La discusión parece estar escalando hacia un punto sin retorno. La tensión en la habitación era tan densa que se podía cortar con un cuchillo."

    l "Disculpe, {i}su majestad{/i}, pero me despertó de mi sueño tan profundo, ¿qué esperaba? ¿flores y rosas?"
    l_thought "Me siento tan agotada que es como si me hubiera atropellado un camión. No estoy para discutir con un profesor a esta hora."

    $ enfocar("ptod")
    ptod "Se nota que alguien está ansiosa por llegar a la dirección hoy."
    $ normal("ptod")

    l "Depende. ¿Es opcional?"
    "Abre la boca para soltar una respuesta, pero mi voz le arrebata su turno."
    l "Si es así, un {i}NO{/i} será mi respuesta."

    "Deja escapar un suspiro profundo, una señal clara de que su paciencia se agota."

    show ptod cruzado
    $ enfocar("ptod")
    ptod "Entonces, ¿me va a entregar la tarea... o directamente la repruebo?"

    $ normal("ptod")
    l "Repr-{nw=0.2}"
    $ enfocar("ptod")
    ptod "Tranquila, ya sé la respuesta."

    $ normal("ptod")
    l "..."
    l "Jodase."

    show blaze 1enojadat
    $ enfocar("blaze")
    b "¡LAILA!"
    show blaze 1enojada2t
    extend " ¡BASTA!"
    show blaze 1enojada2
    $ normal("blaze")

    l_thought "Oh no. Por favor tú no."
    l_thought "¿Por qué todos quieren estar en mi contra hoy?"
    l_thought "No he hecho absolutamente nada."

    while contador < 15:
        pause 0.1
        l_thought "No he hecho nada.{nw}" 
        $ contador += 1

        # Cuando llega al latido 4, deja la viñeta fija
        if contador == 2: 
            show vignette at vineta_organico zorder 100
            $ renpy.music.play("heartbeat.ogg", channel="heartbeat")

    window hide       
    pause 3.0

    window show 
    show blaze 2nerviosa
    l "¡TU NO TE METAS, BLAZE!"
    "Las palabras salieron con una fuerza que no sabía que todavía tenía, pero en lugar de alivio, solo sentí el vacío expandirse en mi pecho."
    "El tono irritado con el que me dirigí a Blaze hizo que mis palabras resonaran por todo el salón."
    $ enfocar("blaze")
    show blaze 1desinteresada3t
    b "Igual yo no seré la que se lleve un reporte."
    show blaze 1desinteresada3
    $ normal("blaze")
    "Llamando aún más la atención de todos."
    show blaze 1seria
    "Ella solo me clava la mirada, enojada, y en sus ojos veo reflejado exactamente lo que temía: la confirmación de que soy todo lo que siempre creí ser."

    l_thought "Lo siento... Lo siento... Lo siento..."
    "Las palabras se repiten en mi mente pero no salen, atrapadas en esta garganta que se cierra."
    "Mientras, el resto, hambrientos de drama, observan al profesor, esperando mi regaño."

    pause 2.0

    $ enfocar("ptod")
    ptod "Disculpe..."

    "Deja escapar el evidente cansancio en su voz."

    ptod "¡CÓMO SE ATREVE HABLARME ASÍ Y A SU HERMA---{nw}"
    $ normal("ptod")

    l "¡ELLA NI SIQUIERA ES MI HERMANA!"
    show blaze 2desinteresada3
    "Las palabras salieron como cuchillas, y al instante de darme cuenta de lo que dije, me quedé callada." 
    $ inac("blaze")
    l_thought "¿QUÉ CARAJOS ESTOY DICIENDO?"
    show blaze 1desinteresada3
    "Vi cómo el rostro de Blaze de repente se quiebra un poco, esas palabras le dolieron. En lugar de contestar, simplemente aprieta los labios."

    "Al mirarla, mi propio corazón se encogió, y el vacío en mi estómago se transformó en una culpa tan pesada que casi me dobla por la mitad."

    l "Y con usted..."
    l "Lo que escuchó.{w} ¡¿QUÉ MIERDA ME GANARÍA YO AL HACER ESE INFORME?!"
    l "NO ME SERVIRÁ PARA NADA, NADIE EN ESTE MUNDO LO VA A USAR."

    $ enfocar("ptod")
    ptod "ESO ES TODO."
    ptod "A LA DIRECCIÓN, LAILA JACKSON."
    $ normal("ptod")
    l "¡BIEN POR MI!"

    "Mi cuerpo es un peso muerto anclado al asiento. Me levanto a la fuerza, el agotamiento grita en mis músculos, pero no escucho. Mochila al hombro, camino hacia la puerta."

    l_thought "Pendejos de mierda..."
    "Y salgo."

    window hide
    play sound closet_open
    pause 1.0
    scene black with fade 

    scene pasillo with dissolve
    show vignette at vineta_rapido zorder 100 
    play sound closet_close
    
    window show 
    l_thought "Necesito que este zumbido en mi cabeza se detenga. Necesito que el mundo deje de girar."
    "Pero no puedo. No puedo dejar de temblar. Cada músculo se rebela contra mí, recordando que estoy atrapada en este cuerpo que ya no reconozco."
    
    show pasillo-blur with dissolve
    hide pasillo
    "Mi vista se empaña de forma gradual, nublando mi visión como el cristal de una ventana bajo la lluvia."

    l_thought "No debí decir eso..."
    l_thought "Las palabras salieron tan rápido, tan afiladas, automáticas... Que cuando me di cuenta, ya era demasiado tarde."
    l_thought "Le grité que no era mi familia... y en el instante en que lo dije, supe que había cruzado una línea de la que no hay regreso."
    "Un vacío se abre en mi estómago, tan profundo que siento que podría caerme en él."
    "Cae una.{w} Luego dos.{w} Luego muchas lágrimas traicioneras empiezan a trazar caminos de culpa en mis mejillas."
    l_thought "Y ahora...{w} Estoy aquí, sola, con este nudo en la garganta."
    "Siento como si el aire se volviera más frío y denso."
    l_thought "¿Por qué siempre arruino todo?"
    l_thought "Quiero pedirle perdón{w}, correr a buscarla{w}, abrazarla.{w} Decirle que sí, que es mi familia, que me importa..."
    l_thought "Pero no quiero, me da pena afrontarla, pensar que si ya me odia..."

    window hide
    pause 1.0
    window show

    l_thought "Mejor no, prefiero escaparme que volverla a cagar."
    "Me ajusto las correas de la mochila que pesa como los errores que cargo dentro, y empiezo a caminar."
    "Cada paso que doy, siento que me agoto más y más. Pero mis pies se mueven por inercia, sin rumbo, sin destino."
    "Como si mi cuerpo supiera que cualquier dirección es igual de vacía que la otra."
    "Miro al suelo, para que nadie (si es que hay alguien) me vea llorar."
    l_thought "Por qué soy tan..."
    "Me detengo. El vacío que hay en mi estómago se expande, transformándose en un abismo frío y pesado."
    "Es como si mis entrañas se hubieran convertido en un pozo sin fondo donde caen todos mis pensamientos y emociones, ahogándose en la oscuridad."
    l_thought "Tan miserable, tan cobarde."
    "Un eco resuena en mi cabeza, una voz que no deja de repetirse, una y otra vez, como si quisiera aplastarme."
    l_thought "No quiero mentir, pero la verdad duele demasiado para compartirla."
    l_thought "No quiero ser otra carga para nadie... aunque sé que este silencio es la mentira más pesada que cargo."
    l_thought "No quiero preocupar a nadie más... aunque esta soledad se siente igual de falsa que cualquier sonrisa forzada."
    l_thought "¿O será que simplemente he olvidado cómo pedir ayuda después de tanto tiempo fingiendo que estoy bien?"
    "Tomo un poco de aire para calmar este torbellino  de emociones y pensamientos, que en cualquier momento, me van a romper."
    l_thought "Que llorona eres, Jackson."

    show pasillo with Dissolve(2.0)
    hide pasillo-blur
    hide vignette with Dissolve(2.0)
    $ renpy.music.stop(channel="heartbeat")
    "Me limpio las lágrimas que todavía quedan en mi rostro."
     
    l_thought "Tal vez si sigo caminando...{w} Desaparezca un poco el dolor."
    "Continuo."
    
    scene black with fade 
    pause 1.0
    jump dark_scene
    return

############## DARK MOMENT ##############
label dark_scene:

    scene pasillo2 with Dissolve(1.0)
    "Mientras caminaba distraída, arrastrando los pies como si llevara anclas atadas a los tobillos, noté que unos pasos se sincronizaban con los míos, acercándose poco a poco."
    "¿Íbamos en la misma dirección? No me importaba lo suficiente como para comprobarlo."
    play sound fall
    "Choco con esa persona, sacándome momentáneamente de mi niebla mental." with hpunch
    
    pause 1.0

    "Apenas logro estabilizarme, molesta volteo a ver quien fue el causante de que casi cayera———{w=0.5} Un chico."  

    l_thought "Realmente no caí en cuenta de su {i}magnífica{/i} presencia hasta este momento."
    l_thought "La verdad... Es que apenas registro lo que sucede a mi alrededor estos días."

    "Aparentemente él también caminaba distraído, no vió que íbamos por el mismo camino."
    show dark 2serio2 with Dissolve(0.2)
    "Sigue caminando como si nada y fingió sacudir el polvo en su chaqueta."
    pause 2.5

    show dark 2distraido2
    "En un momento se detiene y voltea a verme, al parecer sí recayó en mi presencia."

    pause 1.0
    show dark 2distraido2
    "Una vez terminado su falso desinterés, es el primero en hablar."

    show dark 2distraido2t
    $ enfocar("dark")
    d "Carajo{w=1.2}, no te ví" 
    show dark 2juzgat
    extend ", ¿Disculpa, sí?, ¿Te encuentras bien?"
    show dark 2desafiante
    $ normal("dark")

    "La pregunta simple me tomó por sorpresa. ¿Estoy bien? Ni siquiera sé qué significa eso ya."
    l "¡OUCH!"
    l "{sc=3}!¿No puedes ver por dónde diablos caminas,{/sc} {sc=6}idiota?!{/sc}"
    "La ira sale automáticamente, como un reflejo para mantener distanciada a la gente."
    "La adrenalina de la confrontación con Todd todavía recorre mis venas, mezclada con la vergüenza y la culpa. Este pobre idiota solo tuvo la mala suerte de cruzarse en mi camino."

    show dark 1distraido2
    $ normal("dark")
    play music bgm1

    "Al chico negr-{nw}"
    "El chico me mira curiosamente indiferente."
    l_thought "¿Por qué no reacciona como los demás? ¿Por qué no confirma lo que ya sé que soy?"
    
    "A simple vista simula ser egocéntrico. Realmente no me importa, solo quiero salir de aquí, volver a mi aislamiento."
    "Sin embargo, él me retiene."

    show dark 1juzga2t
    $ enfocar("dark")
    d "Eh..." 
    show dark 2distraido2t
    extend " Ya me disculpé."
    show dark 1serio2t
    $ normal("dark")
    $ _history = False
    d "{size=18}Dios, que chica tan sensible.{/size}"
    $ _history = True

    show dark 1serio2
    l_thought "Claro. Porque susurrar hace las palabras invisibles. Lógica impecable."
    l "Sensible mis bolas."

    show dark 2juzga2
    d "..."
    pause 1.5
    show dark 2juzga2t
    $ enfocar("dark")
    d "¿Siquiera tienes?"
    show dark 2juzga2
    $ normal("dark")
    pause 1.5

    l_thought "Ahora tenemos al don preguntas. Como si tuviera energía para esto."
    show dark 2distraido2
    l "{sc=4}!¿Qué mierda te importa?!{/sc}"
    pause 1.5
    l "Y bueno..."
    l "Tengo que irme a otra parte."
    "No tenía intención de sacarle una plática. Cada palabra me cuesta un esfuerzo monumental."
    "Intento seguir mi camino. Pero se interpone.{w} Otra vez."
    show dark 1incomodo
    "Pone una sonrisa algo forzada y habla."
    d "..."
    show dark 1incomodot
    $ enfocar("dark")
    d "¡Mi nombre es Dark!"
    show dark 2incomodot
    d "O así me suelen decir."
    show dark 2incomodo
    $ normal("dark")
    l_thought "¿Qué carajos es ese nombre? Suena como el personaje de manga barato."
    l_thought "Lo que sea...  Solo quiero que esto termine."
    "Debo admitir que su indiferencia calculada ante mi arrebato me tomó completamente por sorpresa."
    l_thought "¿No se espantó ante mi actitud?"
    l_thought "La mayoría de la gente se alejaría, me vería con miedo o desprecio.{w} Que extraño. Quizás está tan roto como yo."
    l "Ya que estamos diciendo nuestros nombres..."
    l 'El mío es...{w=0.5} "Tu puta madre", ¿Te parece?'
    show dark 1juzgat
    $ enfocar("dark")
    d "Creeme que el placer es mío…"
    show dark 2juzgat
    extend " ¡Y claramente el de tu mamá también!"
    show dark 2juzga
    $ normal("dark")

    show vignette at vineta_organico zorder 100
    l "..."
    "Al escuchar eso, siento cómo algo se quiebra dentro de mí. Las lágrimas amenazan con salir pero las contengo con fuerza."
    l_thought "Mierda... Tocó una fibra sensible... Como si no tuviera suficiente con lo de Blaze."
    "Aprieto los puños hasta que las uñas se clavan en las palmas de mis manos, usando el dolor físico para ahogar el emocional."

    show dark 2seriot
    $ enfocar("dark")
    d "Y para dejar esto claro, hablarle así al Vicepresidente del Consejo Estudiantil es una acción algo cuestionable."
    show dark 2serio
    $ normal("dark")
    "Eso lo intenta decir con un tono de voz muy autoritario."

    l_thought "¿Vicepresidente? Genial. Justo lo que necesitaba: otro tipo con poder sobre mí."
    l "¿Qué mierda pasa contigo...?"

    "Suspiro, el peso de todo el día empezando a aplastarme."
    "Miro hacia otro lado para que no vea cómo mis ojos empiezan a vidriarse."

    show dark 2seriot
    $ enfocar("dark")
    d "Solo trato de calmar tus hormonas."
    d "Ya que observo que estás como muy agresiva."
    show dark 2serio
    $ normal("dark")

    l_thought "Agresiva. No. Esto no es agresividad. Esto es el miedo de que alguien más vea lo mierda que soy."
    l_thought "Por favor, no llores... No al frente de él...{w} No al frente de nadie."
    pause 1.5
    hide vignette with Dissolve(1.0)
    "Tomo un poco de aire intentando tranquilizarme, pero siento que estoy respirando a través de una pajilla."

    show dark 2incomodo
    l "Cuenteme... ¿Qué desea {i}el {outlinecolor=#da0303}Vicepresidente del Consejo Estudiantil{/outlinecolor}{/i}?"
    "La formalidad de mis palabras suena falsa incluso para mis propios oídos."

    show dark 1serio2t
    $ enfocar("dark")
    d "A ver, recapitulemos un poco..."
    show dark 1juzga2t
    extend " Chocamos, porque, según entiendo, los dos estábamos distraídos."
    show dark 2serio2t
    d "Te pido disculpas y procedes a hablarme de tus bolas, que quizás no tengas."
    l "Mir-{nw}"
    show dark 2juzga2t
    d "Porque, vamos, se nota a kilómetros que eres mujer."
    "Dice eso mientras me apunta con su dedo."
    show dark 2juzga2
    $ normal("dark")
    l ". . ."
    l "Entonc-{nw}"
    show dark 1incomodot
    $ enfocar("dark")
    d "Por formalidad, me presento, y me vuelves a insultar."
    show dark 1incomodo
    $ normal("dark")
    l "..."
    l "Ya puedo habl-{nw}"
    show dark 1incomodot
    $ enfocar("dark")
    d "Y por último, te devuelvo el sarcasmo{w=0.5} y pones esta cara."
    show dark 2incomodo2
    pause 1.1
    show dark 1incomodot
    d "O sea"
    show dark 2desafiantet
    extend ", que buenas agallas, para preguntar algo así después de todo eso."
    d "Ni yo he llegado a tanto."
    show dark 2desafiante
    $ normal("dark")

    l "..."
    l_thought "Si lo dices de esa manera...{w} Parezco que soy mala persona."
    l_thought "La cual seguramente soy. Es lo que todos piensan. Es lo que Blaze debe estar pensando ahora mismo."

    show dark 2seriot
    $ enfocar("dark")
    d "Y ahora procedo a preguntar..."
    show dark 2juzga2t
    d '¿Podríamos {i}TRATAR{/i} de hablar como dos personas "normales y decentes"?'
    "Lo último simula ponerlo entre comillas."
    show dark 1distraidot
    d "Sin la necesidad de insultarnos mutuamente, por favor."
    show dark 1juzga2
    $ normal("dark")

    l_thought 'Si este es el "Vicepresidente del Consejo", lo mejor sería comportarme. No quiero más problemas.'
    "Suspiro, el sonido sale tembloroso."
    l "Bien."
    "Respondo sin ganas de hablar, por si no fuera poco, me quiere sacar tema de conversación."
    l_thought "En estos momentos, cada sílaba es un esfuerzo."

    l "Pues hablemos."
    show dark 1feli
    l "En estos momentos, quiero estar {i}completamente{/i} sola."  
    l "Sola, solita{nw}"
    show dark 2serio
    extend ", {i}solísima...{/i}{w} ¿Me explico?"
    "Lo digo con evidente sarcasmo, pero por debajo late una verdad desesperada."

    show dark 1desafiantet
    $ enfocar("dark")
    d "Y yo, {i}en estos momentos, quiero{/i} tirarme de un edificio."
    "En algún punto quiso imitar mi voz.{w=0.5} Le salió terrible."

    l_thought "Yo también DESEO eso... Más de lo que podría admitir."
    l_thought "Pero... ¿Por qué dije eso? ¿La verdad se está empezando a filtrar?"

    d "Entonces... ¿Estamos igual, no?"
    show dark 1desafiante
    $ normal("dark")

    l_thought "No, {i}PARA NADA{/i} estamos igual."
    l_thought "Tu tienes {i}casi{/i} el mejor puesto de toda esta preparatoria. A mi directamente nadie me conoce."
    l_thought "Quizás simplemente me conozcan como la chica rota, la perra problemática."

    $ renpy.music.set_audio_filter("music", [af.Reverb(0.0), af.Lowpass(22000)], replace=True)
    $ apply_filter_with_fade("music", [af.Reverb(0.5), af.Lowpass(440)], duration=1.5)

    show vignette at vineta_organico zorder 100
    l_thought "Te ves más presentable que yo. Yo parezco una vagabunda, una muy mala."
    show dark 1juzga2
    l_thought "Con este suéter que es lo último que tengo de ella... Este pelo sin lavar, y paremos de contar."
    l_thought "Entonces, hablas de mí como una mala persona... La cual verdaderamente soy."
    l_thought "Comparado a ti, yo soy una mier-{nw}"
    show dark 2distraido2
    $ enfocar("dark")
    d "¿Mhmp?"
    $ normal("dark")

    l "¿...?"
    $ renpy.music.set_audio_filter("music", None, replace=True)
    hide vignette with Dissolve(1.5)
    "Su sonido en busca de una respuesta hace que salga de mi tren del pensamiento. Por un momento, me había olvidado de que estaba allí."

    l "Sí, sí, lo que digas."
    "Le respondo con algo de irritación, pero ya sin fuerza."

    l_thought"{i}La insultaste{/i} porque sí..."
    l_thought "Aunque, yo insulte a la suya... Eso no me hace ver como un angelito."

    show dark 2distraidot
    $ enfocar("dark")
    d "De todas formas..."
    show dark 1juzga2t
    d "¿Tú nombre es Laila, verdad?"
    show dark 1juzga2
    $ normal("dark")

    "Lo pregunta con una familiaridad que me toma por sorpresa, como si mi nombre hubiera estado rondando en su cabeza durante este incómodo encuentro."
    l "Eh... ¿Qué?"
    l "Ah... S-Sí. Esa soy yo."
    "La confirmación sale casi en un susurro."
    l_thought "¿Cómo sabe mi nombre? ¿Me conoce de algún lado? ¿Escuchó algo sobre mí?"

    show dark 1felit
    $ enfocar("dark")
    d "¡Excelente! Entonces no me equivoque."
    d "Ya vamos bien."
    l_thought "¿Eso qué significa? ¿Me estaba buscando?"
    show dark 1juzga2
    $ normal("dark")
    l "¿Y Cómo sabes mi nombre?"
    extend " ¿Eres adivino o solo otro espeluznante periodista?"
    "Su rostro ahora expresa duda al decir esto último."
    show dark 1juzga2t
    $ enfocar("dark")
    d "O sea..."
    show dark 1incomodot
    extend " Soy el Vice-Presidente del consejo... Debería saber quien es cada quien."
    l_thought "¿Vicepresidente? Más bien pareces vice-pendejo, si me lo preguntas."
    l_thought "..."
    l_thought "¿Qué digo yo? Todos aquí tienen un propósito claro... Menos yo, aparentemente."
    d "Y precisamente, estamos en la misma aula de clases."
    show dark 2distraido2t
    d "Si no lo recuerdas{w}, Salon 3-A... ¿Sabes?" 
    show dark 2distraido2
    $ normal("dark")
    "Entrecierro los ojos y lo miro, tratando de encontrar en mi memoria algún recuerdo de él."
    extend " Simplemente, nada."
    l "Sinceramente... Si tuviera algún recuerdo de ti en esa clase, lo sabría."
    l_thought "La verdad es que apenas registro quién está en el salón estos días."
    show dark 2incomodot
    $ enfocar("dark")
    d "Para hacertela facil. Soy unos de los tipos que se sienta detrás de ti."
    show dark 2incomodo
    $ normal("dark")
    l_thought "Creo tener en mi mente unas voces MUY tediosas que no saben que es el silencio."
    show dark 2incomodot
    $ enfocar("dark")
    d 'Y... soy uno de los {i}"amigos"{/i} de tu hermana, Blaze.'
    show dark 2incomodo
    $ normal("dark")
    l "..." 
    "El nombre de Blaze me golpea como un puño en el estómago, reviviendo toda la culpa que acababa de enterrar momentáneamente."
    l "Ah, mi hermana..."
    "Las palabras salen vacías, sin aire."
    l_thought "Me había olvidado de eso... O más bien, había intentado bloquearlo."
    l_thought "¿Alguna otra señal divina que quieras mandarme, oh Señor Todopoderoso?"
    l_thought "¿Quieres añadir un letrero luminoso en el cielo que diga: 'Lo estás haciendo todo mal'?"
    l_thought "No, mejor un tsunami de mierda. Así no hay duda."
    l '¿"Amigos"?'
    show dark 1incomodot
    $ enfocar("dark")
    d 'Digamos que es algo parecido a lo que denominas "amigo".'
    d "Puede que cumpla con ese requisito básico."
    show dark 2incomodo
    $ normal("dark")
    l "Ya veo..."
    "Decido dejar de preguntar, no entiendo su lógica. No tengo energía para esto."
    pause 1.0

    show dark 2enojao
    "La mueca burlona se esfuma, reemplazada por una expresión algo más seria."
    show dark 2seriot
    $ enfocar("dark")
    d "Ahora explicame... ¿Qué haces por los pasillos en horas académicas?"
    show dark 2enojao
    $ normal("dark")

    l_thought "..."
    l_thought "Debería decirle...? Tipo, es el Vicepresidente del Consejo y..."

    menu (time=5, timeout='rutasuicida_nochoice1'):
        l_thought "¿Debería decirle?"

        "Decirle.":
            $ rutaCanon += 1
            l_thought "Mejor... le digo, así tengo alguna garantía de no tener otro problema."
            l_thought "Aunque, la verdad, un problema más o menos ya no parece importar mucho."

        "No decirle.":
            $ rutaSuicida += 1
            l_thought "No es problema suyo. Créete que te lo voy a decir."
            l_thought "Nada es realmente problema de nadie excepto mío."

    if rutaCanon == 1:
        call rutacanon_choice1 from _call_rutacanon_choice1

    if rutaSuicida == 1:
        call rutasuicida_choice1 from _call_rutasuicida_choice1

    jump dark_scene_afterchoice1
    return   

    ############## DARK AFTERCHOICES ##############
label dark_scene_afterchoice1:
    show dark 2serio2 at sigh_animation
    "Él suspira. Parece que tiene una lucha interna en su mente."
    show dark 2seriot
    $ enfocar("dark")
    d "Puedes irte."
    show dark 2serio
    $ normal("dark")
    l "¿E-Eh...?"
    l_thought "¿Puedo irme? ¿Así como si nada? Después de todo esto..."
    "La simpleza de la solución me desconcierta. Esperaba más consecuencias."
    show dark 2seriot
    $ enfocar("dark")
    d "¿Eres sorda o es que hablo en otro idioma?"
    show dark 2incomodo
    $ normal("dark")
    l "No, no soy sorda, solo estoy practicando mi habilidad para filtrar tonterías. ¿Lo notas?"
    "El sarcasmo sale automáticamente, un escudo gastado pero familiar."
    show dark 2incomodot
    $ enfocar("dark")
    d "Buena esa, eh. Me gustó."
    show dark 2distraidot
    d "Volviendo al tema..."
    show dark 2seriot
    d "Puedes irte, te lo dejaré pasar por esta vez."
    show dark 1neutralt
    d "Solo por ser hermanastra de Blaze."
    show dark 1incomodo
    $ normal("dark")
    l "¿Te pregunté?"
    "Evita responder a mi provocación."
    show dark 1desafiantet
    $ enfocar("dark")
    d "Fue un placer hablar contigo..."
    show dark 1distraidot
    d "Eh..."
    show dark 1desafiantet
    extend " ¿Laira?"
    show dark 1desafiante
    $ normal("dark")
    l_thought "Sé que lo hace a propósito..."
    l_thought "¿Pero tan olvidadizo es mi nombre? O quizás simplemente no le importo lo suficiente como para recordarlo."
    l "Laila. Es Laila."
    l "Si no hay nada más que decir, adiós."
    l_thought "Prefiero retirarme que seguir sacando conversación. Cada interacción me agota un poco más."
    show dark 1distraido
    hide dark with Dissolve(0.2)
    "Doy el primer paso, dejando a Dark atrás mientras continúo mi rumbo con mis pensamientos."
    "Solamente oigo sus pasos siguiendo su camino, le escucho decir algo, pero lo ignoro."
    
    l_thought "Por fin... Silencio."
    pause 1.0
    l_thought "He de admitir que la ropa de Dark era algo llamativa..."
    l_thought "Aunque debo admitir que su estilo era... peculiar. Esa chaqueta negra con el 15. Un pantalon negro."
    l_thought "..."
    l_thought "Ese collar con forma de corazón... Raro."
    pause 1.0
    "Suspiro para mis adentros. Ya agotada."
    l_thought "¿Pero qué puedo decir yo?"
    l_thought "Como si el mío fuera mejor."
    l_thought "Claramente no lo es."
    l_thought "..."
    pause 1.0
    "Una idea cruza por mi mente, y es la primera que elijo."
    l_thought "Ya sé hacia donde puedo ir..."
    "Siento como mi pecho se aprieta, solo por no cumplir el castigo el cual merezco. "
    "Ignoro el dolor y aumento la velocidad de mis pasos, avanzando hacia mi destino. Mientras continuó la charla en mis pensamientos."
    stop music fadeout 1.8
    $ persistent.quick_menu_visible = False
    scene black with Fade(1.0, 1.0, 1.0)
    pause 2.0
    jump azotea
    return

############## AZOTEA MOMENT ##############
label azotea:

    play audio bell
    $ renpy.pause(3.0, hard=True)
    $ persistent.quick_menu_visible = True 
    with Dissolve(0.5)
    "Después de ese encuentro... inesperado, con al parecer el {i}{outlinecolor=#da0303}Vicepresidente del Consejo Estudiantil{/outlinecolor}{/i}. El receso empezó.{w} Me salvé por ahora."
    "Decidí irme a la azotea... un lugar donde al menos nadie viene y casi siempre está solo."

    l_thought "Por fin algo de paz me vendría bien después de eso."
    "Digo en mi propia mente para convencerme que lo que acabo de hacer no me llena de culpa."
    "Pero incluso en el silencio, mis pensamientos gritan más fuerte."

    play sound closet_open
    $ renpy.pause(1.0, hard=True)
    scene azotea with fade
    play ambient ext_day fadein(2.0)
    play sound closet_close

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
    play sound pushing_a_metal1
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
    play sound ear_ringing volume 0.5 
    "Y como si alguien estuviera hablando frente mio, escucho alguien decir algo... Mientras escucho como un pitido resuena en mi oído, incrementando."
    pause 1.0
    nobody "{sc=3}¿Crees que no es tu culpa? Aw, ternura.{/sc}"
    nobody "{sc=4}Eso mismo dirán cuando encuentren tu cuerpo sin vida:{/sc}"
    nobody "{sc=6}“Ahora tiene lo que se merecía”{/sc}"
    pause 1.5
    stop sound fadeout 1.8
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

    play sound closet_open
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
    play sound closet_close
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
    play sound closet_open
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
    play sound closet_open
    pause 1.0
    stop ambient fadeout(1.5)
    scene black with Fade(1.0, 1.0, 1.0)
    play sound closet_close
    l_thought "Ya no quiero oír nada de ese estúpido furro. Tal vez de Steve pero no de su amigo."
    jump director
    return

label director:
    scene azotea_stairs with fade
    l_thought "Este fue el momento MÁS incómodo que he vivido en mi vid-{nw=0.1}"
    play audio bell
    $ renpy.pause(3.0, hard=True)
    l_thought "¿¡Es en serio!? Que maldita suerte la mía..."
    "Bajo las escaleras a un paso lento sabiendo que no pienso llegar al salón lo más rápido posible."
    "Siento el sol como pega cálidamente a mi piel, como si me estuviera dando un abrazo consolador mientras llegó al 2do piso de la escuela, un piso el cual casi no suelo llegar seguido"
    scene pasillo_2dopiso with fade
    "Doy vueltas por los pasillos de este piso, siento lo reconfortante lo solitario que se siente."
    extend " Cada pisada que doy un eco tan ahogador resuena mientras cada quien está en sus salones. Era de esperarse, acabó el receso."
    l_thought "Tal vez debería quedarme en la azotea un rato más. No tengo energía para esquivar miradas de desprecio ni sonrisas falsas."
    l_thought "Prefiero el silencio aplastante de esta azotea a los pasillos llenos de gente que solo ve lo que quiere ver... Nunca a la persona detrás del chisme."
    l_thought "Por lo menos aquí estoy sola."
    show dirc tieso with Dissolve(0.2)
    "Al dar la vuelta para seguir caminando, me encuentro inesperadamente con el director de la escuela..."
    extend " {i}JUSTO{/i} cuando dije esa maldita palabra."
    show dirc cintura
    $ enfocar("dirc")
    dirc "Señorita Jackson. Nos volvemos a encontrar. ¿Desobedeciendo órdenes del profesor otra vez?"
    $ normal("dirc")
    l_thought "¿En serio? ¿Tienen un sensor que se activa cada vez que pronuncio “soledad”? ¿O es solo mi maldita mala suerte?"
    l "¿Desobedecer? Yo solo... Disfrutaba del tour arquitectónico de los pasillos. Muy educativo, por cierto."
    l "Además, estaba regresando a mi salón. ¿Acaso necesita lentes nuevos?"
    $ enfocar("dirc")
    dirc "¿Me está tomando por idiota? En esta institución no toleramos—{nw=0.1}"
    l_thought "—esta clase de comportamientos, sí, sí. Lo sé. El mismo disco rayado que repiten todos. Hasta mi padre usa las mismas palabras gastadas."
    $ normal("dirc")
    l_thought "¿Todos leen el mismo guión? ¿O hay un curso de “cómo ser un cliché viviente”?"
    l "No estoy mintiendo. ¿Acaso necesito un testigo que confirme que puedo caminar sola?"
    show dirc hand_corbata
    $ enfocar("dirc")
    dirc "¿Entonces cómo explica los reportes del profesor Todd y de otro estudiante sobre lo sucedido en la clase de Biología?"
    $ normal("dirc")
    l_thought "Puta madre... {outlinecolor=#da7603}Blaze{/outlinecolor} tuvo que haber dicho algo o fue ese {outlinecolor=#da0303}tipo{/outlinecolor} raro del pasillo. Maravilloso."
    l_thought "¿Por qué nunca puedo simplemente... desaparecer?"
    show dirc tieso
    $ enfocar("dirc")
    dirc "Necesito que me acompañe a mi oficina. Y no intente nada inteligente."
    $ normal("dirc")
    l "¿Es obligación?"
    "Solo siento la mirada del director como me atraviesa el alma. Ahogando cualquier protesta antes de que nazca."
    scene black with Fade(1.0, 1.0, 1.0)
    hide dirc
    "En el camino me pregunto qué clase de sermón me dirá esta vez mientras cada paso hacia su oficina es una losa más sobre mí."
    $ renpy.pause(2.0, hard=True)
    show screen vignette_screen2
    scene despacho_dirc 
    show dirc tieso
    $ inac("dirc")
    with fade
    $ renpy.pause(1.0, hard=True)
    "Resumidamente: sí, me dieron un reporte por mi “comportamiento”. Y además tuve que tragarme el sermón del director."
    "¿Quieren saber cómo suena? Es siempre lo mismo, un discurso reciclado, palabras que ya tienen polvo de tanto usarlas."
    show dirc cintura
    $ enfocar("dirc")
    dirc "“Debes aprender a comportarte... piensa en tu futuro... no puedes seguir siendo un ejemplo negativo para los demás...”"
    show dirc tieso
    $ inac("dirc")
    "Ya ni siquiera me sorprende. Ni siquiera debería recordarlo con tanta claridad, pero ahí está, repitiéndose como un cassette roto."
    "Ni siquiera me molesto en escuchar. Son palabras vacías que flotan en el aire hasta que las barro mentalmente."
    "Intento convencerme:"
    l_thought "Es una puta hoja de papel. ¿Por qué entonces siento que me estoy desangrando por dentro?"
    l_thought "¿Por qué esta culpa se adhiere a mi piel como una segunda capa más sucia que la primera?"
    "Mi cuerpo se siente pesado, como si alguien lo sujetara desde dentro. Tengo ganas de gritar, de llorar, de romper esta máscara que llevo pegada al rostro… Pero me repito:"
    l_thought "Es solo una hoja de papel."
    l_thought "Entonces, ¿por qué me siento así? ¿me merezco sentirme así?"
    l_thought "¿Por qué esta sensación de hundirme en algo más grande que yo?"
    l_thought "Esta sensación me hace sentirme agotada cada vez más..."
    "Y aunque lo niegue a gritos, en el fondo sé que es inútil: soy mi peor enemiga, mi propia torturadora."
    "Me insulto, me despedazo, me aniquilo con cada pensamiento. Me repito obsesivamente que debo cambiar, que necesito mejorar... Pero la farsa es tan obvia que me avergüenza."
    "Porque la promesa se rompe antes de nacer."
    extend " Porque yo misma la arruino."
    "Y ahí, en medio del silencio que ni el director llena, escucho esa voz. Esa que me desgasta, esa que se clava con palabras que duelen más que cualquier castigo."
    $ renpy.music.set_audio_filter("music", [af.Reverb(0.0), af.Lowpass(22000)], replace=True)
    $ apply_filter_with_fade("music", [af.Reverb(0.5), af.Lowpass(440)], duration=1.5)
    show screen red_effect2
    nobody "{sc=3}Eres una basura humana. El pedazo que nadie quiere, que nadie usa.{/sc}"
    nobody "{sc=3}Lo que queda después de que todos ya eligieron lo bueno.{/sc}"
    nobody "{sc=3}Te pones tu máscara dura, pero en el fondo lo sabes:{/sc}"
    nobody "{sc=3}¿Para qué carajos sigues acá?{/sc}"
    nobody "{sc=3}Nadie te aguanta. Nadie te quiere. TODOS te desprecian.{/sc}"
    nobody "{sc=3}Cheryl, Blaze, tu vieja amiga Arain...{/sc}"
    nobody "{sc=3}Todas ellas lo piensan.{/sc}"
    nobody "{sc=6}Y tu padre... Tu padre está decepcionado. Siempre lo estuvo.{/sc}"
    nobody "{sc=6}Siempre lo estará.{/sc}"
    nobody "{sc=3}Nada de lo que perdiste va a volver.{/sc}"
    nobody "{sc=4}¿Sabés por qué? Porque tu vida es una maldición.{/sc}"
    nobody "{sc=4}Porque naciste para ser esto: un error, un 'qué pena'. Nada más.{/sc}"
    "Las oigo."
    "Las palabras me atraviesan, y cada palabra arde como si me grabaran en la piel con hierro caliente."
    extend " No puedo tapar mis oídos porque no vienen de afuera, vienen de mí misma. Es mi propia voz disfrazada, escupiendo lo que más temo."
    "Un nudo de angustia y asco se forma en mi garganta, tan denso que siento que voy a vomitar mi propio odio."
    "Mis manos tiemblan incontrolablemente, no por el miedo a la voz, sino porque en el fondo..."
    extend" Le creo. Me aplastan. Me quiebran. Me reducen a pedazos."
    "Y lo más devastador es que duele precisamente porque sé que es verdad."
    extend " O al menos... eso es lo que siento."
    nobody "{sc=3}¿Sabes? No debería de contártelo nuevamente...{/sc}"
    nobody "{sc=3}Tú misma ya lo sabes. Solo quiero que recuerdes algo.{/sc}"
    nobody "{sc=6}Siempre voy a estar ahí.{/sc}"
    $ renpy.pause(1.3, hard=True)
    $ renpy.music.set_audio_filter("music", None, replace=True)
    hide screen red_effect2
    hide screen semiblack
    hide screen vignette_screen2
    with Dissolve(0.8)
    "De repente, la voz se corta como si alguien hubiera desconectado un cable en mi cerebro, y la reemplaza la del director."
    "Recién entonces me doy cuenta de que las lágrimas han estado cayendo sin parar, dibujando caminos salados en mis mejillas."
    "Él coloca una hoja sobre la mesa, junto con una pluma."
    show dirc cintura
    $ enfocar("dirc")
    dirc "Tome. Necesito que me la traiga firmada por su padre. O si lo prefiere, puedo hacer un citatorio para hablar seriamente de su comportamiento."
    $ normal("dirc")
    "Lo miro confundida. Apenas logro decir algo, como si quisiera confirmar lo que apenas entendí."
    l "¿P-para mañana?"
    show dirc tieso at sigh_animation
    $ enfocar("dirc")
    dirc "Sí, Laila. Para mañana."
    dirc "Mire... sé que tanto usted como yo estamos hartos de repetir lo mismo. Una y otra vez. Ya ni siquiera me escucha cuando hablo, ¿verdad?"
    "No le respondo. Porque sé que tiene razón."
    show dirc hand_corbata
    dirc "Pero hay algo que quiero dejar claro."
    dirc "¿Qué pensaría su madre si la viera ahora... Así, en este estado?"
    "Me muerdo el labio ante su mencion. Sintiendo una punzada que taladra mi cabeza."
    dirc "Yo sé que usted es talentosa, que es inteligente. Este incidente no es todo lo que usted es..."
    show dirc tieso
    dirc "Pero está marcando quién está eligiendo ser después."
    $ normal("dirc")
    l_thought "¿Y qué? ¿Qué te hace pensar que ahora sí voy a escucharte? No eres la primera persona que me lo dice y no serás la última."
    $ enfocar("dirc")
    dirc "Me preocupa que su actitud de “chica dura” la lleve a puntos extremos."
    dirc "Usted no es esa caricatura de señorita Jackson que intenta aparentar."
    dirc "Dígame algo:{nw}"
    show dirc cintura
    extend " ¿no tiene personas cercanas con las que pueda hablar?"
    $ normal("dirc")
    "La pregunta aterriza como un golpe sordo en el pecho. Justo lo que no quiero oír."
    l "Tengo... Algunas amigas, supongo."
    "Digo eso apretando los labios, con la voz apenas audible."
    dirc "Eso es lo que me importa. No se quede callada, Laila."
    show dirc tieso
    dirc "No se aísle. Créame: ellas no van a rendirse con usted."
    "Silencio."
    "El aire se siente pesado y algo incómodo. Yo bajo la mirada. No sé qué decirle. No me salen las palabras, ni siquiera las falsas."
    "El director me observa un momento más y{nw}"
    show dirc tieso at sigh_animation
    extend " finalmente suspira, resignado."
    $ enfocar("dirc")
    dirc "Está bien. Ya puede volver a clase."
    $ normal("dirc")
    "Recojo la hoja con la firma pendiente y me levanto sin mirarlo a los ojos."
    hide dirc with Dissolve(0.2)
    "Camino hacia la puerta con las piernas pesadas, como si arrastrara el eco de todo lo que no quise contestar."
    "No soy capaz de agradecer lo que me dijo. Al menos en ese aspecto fue el único que me “intentó” ayudar...{w} Le doy algo de mérito por su acto."
    scene black with Fade(1.0, 1.0, 1.0)
    "Salgo del despacho, sin palabras sarcásticas ni insultos en mi garganta, como si está “plática” con el director fuera capaz de arrebatar lo que estaría por decir al salir de ahí."
    "Camino con la cabeza agachada al suelo hacia mi salón, el 3-A, sus palabras se me grabaron como pelota rebotando infinitamente en mi cabeza."
    "No me gustaría pensar más en esto.{w} Pero inconscientemente lo hago..."
    $ renpy.pause(2.0, hard=True)
    scene class3A with Fade(1.0, 1.0, 1.0)
    "Entro al aula sintiendo el peso de cada mirada sobre mí… Incluso siento la de Blaze como una daga de preocupación que atraviesa mis huesos."
    "Solo logro escuchar vagamente al profesor de Física dándome un sermón por llegar tarde al salón."
    "Solo le doy un asiento robótico. Mis piernas se mueven en automático y me llevan hasta mi mesa."
    "Me siento y dejo mis cosas aun lado."
    scene black with dissolve
    "Me acuesto en mis brazos, como cuando inicio el día. E intento dormirme creyendo que este día fue un mal sueño."
    stop music fadeout 1.8
    $ persistent.quick_menu_visible = False
    jump whatremainsofday1
    return

label whatremainsofday1:
    $ renpy.pause(6.0, hard=True)
    $ persistent.quick_menu_visible = True
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
    #play sound miedomujere

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
    play sound car_horn volume 0.3
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
    play sound open_car_door
    "Blaze abre la puerta trasera y nos montamos en el auto, las dos en los asientos de atrás, ya que papá tiene un extraño bolso en el asiento del copiloto{w}, que por cierto, donde Blaze se suele sentar."
    hide counter with dissolve
    hide blaze with dissolve
    stop ambient fadeout(1.5)
    scene black with Fade(0.3, 0.3, 0.3)
    play sound close_car_door
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
    $ persistent.quick_menu_visible = False
    jump final_day1
    return

label final_day1:
    $ renpy.pause(4.0, hard=True)
    $ persistent.quick_menu_visible = True
    "Volteo mi mirada hacia la ventana y empiezo a observar que llegamos a un vecindario reconocido."
    stop ambient fadeout(0.5)
    $ renpy.pause(5.0, hard=True)
    play sound open_car_door
    "Papá por fin estaciona. Blaze y yo nos bajamos."
    play ambient int_night fadein(2.0)
    play sound close_car_door
    "El silencio del auto se traslada a la puerta."
    "Blaze me pone la mano en el hombro y entra primero y yo la sigo."
    play sound closet_open
    scene livingroom_n with fade
    "La casa está a oscuras, voy al encendedor y enciendo las luces de la sala."
    play sound light_switch
    scene livingroom_l
    play sound closet_close
    "Él deja las llaves sobre la mesa. El sonido seco resuena como un martillazo en mi pecho."
    show counter 1serio with dissolve:
        center
    show counter 1seriot
    $ enfocar("counter")
    dad "Bien. Ahora, ¿qué es lo que tienen que decirme?"
    show counter 1serio
    $ normal("counter")
    "Me tenso al escuchar su voz. Haciendo que me voltee a donde está él."
    show blaze 1sonriente with dissolve:
        right4
    "Noto que Blaze está a mi lado. Solo me sonríe para que pueda agarrar agarrar un poco de valor para decirle..."
    l_thought "Si supiera con quién estaría hablando tal vez entendería mi miedo del porque no quiero decirle..."
    "Saco el reporte de mi mochila, lentamente, sintiendo como mi cuerpo se tensa poco a poco."
    l "Y-yo... tengo que darte esto papá..."
    "Extiendo mi brazo algo nervioso, se que no puede parecer la gran cosa pero... No lo sé, me da miedo que vaya a reaccionar."
    show counter 1nosurprise
    "Él toma la hoja que tengo entre mis manos sin prisa alguna, para después leerlo con atención."
    show blaze 1feliz
    "Volteo a ver a Blaze un poco nerviosa, me devuelve la sonrisa queriendo decirme: “Todo estará bien hermana no es para tanto”."
    "Mi padre no levanta la voz, no lo necesita y habla:"
    show blaze 1neutral
    show counter 1nosurpriset
    $ enfocar("counter")
    dad "¿Ahora que hiciste, Laila?"
    show counter 1nosurprise
    $ normal("counter")
    "Bajo la cabeza bastante apenada. Mi garganta arde al ver la reacción de él al ver este papel. Ya parece que ver este papel es costumbre y ahora sí siento que la he cagado..."
    "Antes de que pueda decir una palabra, Blaze me cubre."
    show blaze 1neutralt
    $ enfocar("blaze")
    b "Papá, fue un error. No la juzgues tan duro, recuerda que también tuve mis problemas cuando entré."
    show blaze 1neutral
    $ normal("blaze")
    "El me mira por un momento, solo negando la cabeza, como si ya supiera lo que quiere decirme esta vez."
    show blaze 2seria2
    show counter 1nosurpriset
    $ enfocar("counter")
    dad "Aprecio que defiendas a tu hermana, pero el error fue de ella y tiene que aprender a sostenerlo."
    show counter 1seriot
    dad "Ella debería de entender que si vuelve a hacer esta clase de incidentes, no pienso yo a-{nw=0.3}"
    show counter 1serio
    $ normal("counter")
    "Me siento como me hago más pequeña con cada palabra que decía..."
    "Y justo antes de que pueda decir algo más hiriente, cambia sus palabras para decirme de una manera {i}sutil{/i} que la he cagado bastante..."
    "Suavizando el tono y sin perder esa firmeza que tanto lo caracteriza."
    show counter 1nosurpriset
    $ enfocar("counter")
    dad "Mira, Laila, no estoy enojado contigo, pero sí decepcionado."
    show counter 1nosurprise
    $ normal("counter")
    $ renpy.pause(1.5, hard=True)
    "Toma unos segundos para decir lo siguiente."
    show counter 1nosurpriset
    $ enfocar("counter")
    dad "Y me duele mucho verte así todo el tiempo."
    show blaze 2neutral2
    show counter 1seriot
    dad "Pero, debes entender que cuando pasen estos tipos de cosas, tendrás que enfrentar las consecuencias sola. Yo no voy a interferir."
    show counter 1serio
    $ normal("counter")
    "Sus palabras no son un golpe; es una caída libre."
    "El suelo parece ceder bajo mis pies. Levanté la vista, sorprendida y aterrada por esa última frase."
    "Sus ojos no son fríos, pero sí pesados, como si cargaran con algo que yo misma puse ahí."
    l_thought "Sola..."
    "La palabra resuena en mi cabeza, vacía y enorme. “No voy a interferir. No... No va a ayudarme”."
    l_thought "¿Y si el director me expulsa? ¿Y si Todd insiste en suspender? ¿Y si...?"

    if (rutaCanon-rutaSuicida)<=-1:
        show screen red_effect2
        nobody "{sc=3}Es lo que mereces. Un ensayo para el abandono final.{/sc}"
        nobody "{sc=3}¿Crees que se quedará cuando vea lo rota que estás por dentro?{/sc}"
        hide screen red_effect2 with Dissolve(1.0)

    l_thought "Me va a dejar ahogarme. Él, que es el único que... que..."
    "Sacudo mi cabeza, echando para atrás cualquier pensamiento intrusivo. Y le presto atención a papá."
    show counter 1seriot
    $ enfocar("counter")
    dad "Ahora quiero que hagas lo siguiente."
    dad "Quiero que le entregues esto al director para mañana."
    dad "No podré ir a su “citatorio” por trabajo, y quiero que me digas al salir que vas a hacer para evitar estos incidentes nuevamente."
    show blaze 2sonriente
    show counter 1nosurpriset
    dad "¿De acuerdo?"
    show counter 1nosurprise
    $ normal("counter")
    "Mi padre solo me entrega una hoja con algo ya escrito, parecía que ya anticipa esta clase de situaciones, no me sorprende que no haya cambiado después... de eso."
    "Solo agacho la cabeza sin decirle absolutamente nada y respondo casi como un susurro."
    l "S-Sí, papá..."
    show counter 1nosurpriset
    $ enfocar("counter")
    dad "De acuerdo, Ahora vamos a cenar, se acabó el tema por hoy."
    show counter 1nosurprise
    $ normal("counter")
    show counter at outwalk_right4
    "Solo veo cómo se va a la cocina a prepararnos algo, mientras Blaze solo me toma del hombro para darme un confort después de esta breve plática. "
    show blaze 1sonrientet
    $ enfocar("blaze")
    b "¿Ves? No estuvo nada mal como pensabas."
    show blaze 1sonriente
    $ normal("blaze")
    hide counter
    l "Lo dices como si no lo conocieras."
    "Respondo soltando un suspiro de alivio al estar las 2 en la sala."
    l "Sabes cómo es él."
    show blaze 1juzga2t
    $ enfocar("blaze")
    b "Será serio y todo pero, se preocupa por ti. Solo que jamás lo has visto como es en realidad."
    show blaze 1juzga2
    $ normal("blaze")
    "Sus palabras por algún motivo no me las creo, siento que lo que me dice es una mentira disfrazada de una verdad."
    "Como si su voz y ese rostro de él fuera a tener algo dulce y agradable en la cual sentir."
    scene black with Fade(1.0, 0.5, 1.0)
    $ renpy.pause(5.0, hard=True)
    "Me voy a mi habitación. Volteo a ver a Blaze, apenas y logro escuchar un “Buenas noches”."
    "Siento como mi estómago se retuerce del hambre por no comer. Pero no le presto atención."
    "Subo las escaleras paso a paso, cada peldaño parece demandar el doble de esfuerzo."
    $ renpy.pause(2.5, hard=True)
    play sound closet_open
    scene lailaroom_n with Fade(0.3, 0.3, 0.3)
    "Llego a mi habitación, mi supuesto refugio."
    play sound closet_close
    "Y cierro la puerta tras de mí, apoyando toda mi espalda contra la madera como si intentara bloquear el mundo exterior."
    $ renpy.pause(4.0, hard=True)
    l_thought "Que dia..."
    "Me enderezo y voy a ponerme mi pijama. Una ropa más cómoda."
    "Me cambio con movimientos lentos y automáticos, arrastrando los pies."
    "La comodidad del pijama es un alivio mínimo, casi imperceptible contra el peso que llevo dentro."
    "Me dejo caer sobre la cama, no con el propósito de dormir, sino de desaparecer." 
    "El colchón cede bajo mi peso, pero la presión en el pecho no se alivia."
    show layer master: 
        function apply_blur_gradually2  
    l "Por fin... silencio. Soledad. Las únicas cosas que no me piden nada a cambio."
    l "Estoy tan, tan cansada. No es solo el cuerpo... es todo."
    l "Como si alguien hubiera desconectado mis pilas y ahora todo es más pesado, más lento, más gris."
    l "Este día ha sido una locura. Presiento que me debo seguir preparando para más."
    $ renpy.pause(2.5, hard=True)
    l "Aun así, un día menos. Solo queda esperar a que llegue el siguiente. Y el siguiente. Y el siguiente."
    "Tomo mi teléfono. La luz de la pantalla ilumina mi rostro en la oscuridad, un brillo artificial e hiriente."
    show screen phone with dissolve
    "Pero antes de apagarlo, veo el fondo de pantalla."
    l "..."
    "La imagen está borrosa. O son mis ojos, o es el polvo en la pantalla. Ni siquiera tengo energía para limpiarlo."
    l "¿Qué desearías que hiciera, mamá?"
    $ renpy.pause(2.5, hard=True)
    l_thought "Sé que nadie me va a responder, es algo estupido..."
    l_thought "Aun así..."
    hide screen phone with dissolve
    "Apago el telefono y lo lanzo a la mesita de noche."
    "Tomo un largo bostezo, que desprende agotamiento tanto mental y físicamente."
    $ renpy.pause(1.5, hard=True)
    "Me acomodo y empiezo a cerrar los ojos poco a poco."
    $ renpy.pause(0.6, hard=True)
    show parpadeo_on
    $ renpy.pause(8.0, hard=True)
    play sound door_knock
    "Escucho que alguien toca la puerta..."
    "Me quedo en silencio. No me quiero levantar."
    play sound closet_open
    "Aun así, abren suavemente la puerta."
    l_thought "¿No conocen la privacidad?"
    "En eso, mi padre entra a mi habitación, sin preguntarme siquiera qué podía pasar o si estaba dormida. "
    l_thought "Claramente se que se viene un sermón... muy largo..."
    l_thought "¿Qué parte de no quiero hablar con nadie, no entienden? Claro que nadie lo sabe si no lo digo."
    dad "Sé que estás despierta, Laila. No finjas que estás dormida."
    show parpadeo_off
    hide parpadeo_on
    $ renpy.pause(1.5, hard=True)
    show counter 1serio with dissolve:
        center
        night_urban
    show counter 1seriot
    dad "Necesito hablar contigo. ¿Te parece?"
    show counter 1serio
    show layer master:
        matrixcolor IdentityMatrix()
    with dissolve
    l_thought "Por supuesto que no... ¿Puedes dejarme sola?"
    play sound closet_close
    "Mi padre entra a mi habitación, cerrando la puerta para poder hablar a solas."
    "Aunque me temo que será está clase de pláticas incómodas como las ventas de multinivel que hay en internet."
    "Se sienta en mi cama y me mira un poco serio, esperando a que le responda algo, pero no tengo ni siquiera el valor de mirarle, ni de contestar a su pregunta."
    $ renpy.pause(3.0, hard=True)
    "El silencio y la incomodidad que hay mutuamente logran invadir mi habitación."
    "Mi padre es alguien de pocas palabras, es MUY directo..."
    l_thought "¿Qué pensará a que no le estoy diciendo nada?"
    $ renpy.pause(3.0, hard=True)
    "Por fin se agarra de valor al no responderle nada y habla."
    show counter 1seriot
    $ enfocar("counter")
    dad "Seré breve Laila, tu comportamiento me preocupa demasiado."
    l_thought "Aquí vamos..."
    dad "No es la 1ra vez que te llevó a psicólogos por tu “situación”. Te niegas a todo tipo de ayuda que te ofrezcan.{w} Incluso la mía."
    dad "Dejaste que tú amiga... la arin—{w=0.5} o como se haga llamar, lograste pelearte con ella, te peleaste con tu hermanastra, tanto Blaze como Cheryl."
    "Al mencionar a cada una de ellas, sentí un pinchazo de culpa en el estómago."
    dad "Incluso insultas a la maldita autoridad de la escuela.{w} ¿Qué más falta?{w} ¿¡Que te hagas anarquista por tu madre!?"
    show counter 1enojaot
    dad "O Peor aún.{w} ¿¡Que te vuelvas en contra de {i}Marno{/i}!?"
    show counter 1enojao
    $ normal("counter")
    "Solo vuelvo a ver incómodo a mi papá, ya queriendo que acabe enseguida está conversación..."
    "Aunque no entiendo a quien quiso decir con este último..."
    l_thought "¿Marno? ¿Quién es Marno?"
    show counter 1serio at sigh_animation
    $ renpy.pause(1.5, hard=True)
    show counter 1seriot
    $ enfocar("counter")
    dad "Mi punto es: que trato de ayudarte en lo que puedo.{w} Aún si no soy alguien expresivo."
    dad "Y creo, que te sientes bastante abrumada por la escuela..."
    l_thought "Por 1ra vez después de mucho tiempo,  estoy de acuerdo con lo que dices..."
    show counter 1nosurpriset
    dad "Ya que, si te pregunto qué es lo que sientes no me vas a responder de igual forma..."
    show counter 1seriot
    dad "Pero tengo una solución que tú abuela me dio hace mucho."
    dad "No será la mejor de todas"
    show counter 1compadecert
    extend ", pero podríamos pasar tiempo juntos.{w} Cómo antes.{w} Ya sea tu y yo o con Blaze."
    dad "Podemos caminar por el parque... o en las calles, comer algo en los puestos nocturnos... No lo sé.{w} La idea es salir."
    show counter 1compadecer
    $ normal("counter")
    l "..."
    show counter 1compadecert
    $ enfocar("counter")
    dad "Siento que es una forma de que tanto a mi, como a ti nos ayude a olvidar esta presión de todos lados."
    dad "¿Qué te parece, Laila?"
    show counter 1compadecer
    $ normal("counter")
    "Me agarro del cuello sin saber que responderle..."
    l_thought "Por una parte no quiero, ni siquiera salir..."
    l_thought "Pero por otra quiero aceptar la idea de mi padre, quiero desconectarme de todo...{w} de la escuela, de los problemas... aún si son muy insignificantes..."
    $ renpy.pause(3.0, hard=True)

    if (rutaCanon-rutaSuicida)<=-1:
        l_thought "¿Tiempo juntos? ¿Para qué?"
        l_thought "¿Para que vea de cerca lo defectuosa que estoy?{w} ¿Para que la decepción sea aún más palpable?"

    "Abrumada, asiento con la cabeza, incapaz de formar palabras. Es un movimiento pequeño, casi imperceptible, pero él lo ve."
    show counter 1nosurpriset
    $ enfocar("counter")
    dad "¿Eso es un sí, Laila? Recuerda que tienes que estar segura de tu decisión."
    dad "No puedo obligarte a hacer algo que no deseas. ¿Lo olvidas?"
    show counter 1nosurprise
    $ normal("counter")
    l "..."
    "Me la pienso mucho tras ver si realmente es una buena idea..."
    l_thought "¿Qué más puedo perder?"
    l "Si, papá...{w} me agrada la idea..."
    show counter 1compadecer
    "Veo a papá sonreír...{w} parece extraño verle así, parece algo surreal de alguien que se la pasa completamente serio todo el día."
    "Solo me da unas caricias en la cabeza, despeinando más mi cabello{w}, como si le hubiera alegrado oír esa respuesta después de demasiado tiempo."
    "Se levanta de mi cama satisfecho de mi respuesta, y se retira de mi habitación."
    play sound closet_open
    show counter 1compadecert
    $ enfocar("counter")
    dad "Descansa, Laila."
    show counter 1compadecer
    $ normal("counter")
    play sound closet_close
    hide counter with Dissolve(0.5)
    "Cierra la puerta de mi habitación lentamente."
    "Veo como la iluminación del pasillo se desvanecía por completo, llenando mi habitación de oscuridad total."
    "Un pequeño escalofrío me invade por mi cuerpo al sentir está emoción..."
    "Pero no es de frío o de miedo. Es... diferente."
    "Una sensación extraña, casi olvidada. ¿Será... esperanza? ¿O solo el susto de que algo finalmente haya salido bien?"
    "¿Eso es normal?"
    show parpadeo_on
    "Una vez esa charla, intento dormir, esperando al siguiente día."
    $ persistent.quick_menu_visible = False
    hide screen phone_button
    with Dissolve(5.0)
    stop ambient fadeout(1.5)
    scene black with Fade(1.0, 1.0, 1.0)
    return

    #if persistent.day < 1:
    #    $ persistent.day = 1
    #   $ renpy.save_persistent()

    # Finaliza el juego: