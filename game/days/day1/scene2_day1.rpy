label scene2_day1:
     
    scene pasillo2 with Dissolve(1.0)
    "Mientras caminaba distraída, arrastrando los pies como si llevara anclas atadas a los tobillos, noté que unos pasos se sincronizaban con los míos, acercándose poco a poco."
    "¿Íbamos en la misma dirección? No me importaba lo suficiente como para comprobarlo."
    play audio fall
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
            $ rutaSuicida += 2
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
    $ quick_menu = False
    scene black with Fade(1.0, 1.0, 1.0)

return