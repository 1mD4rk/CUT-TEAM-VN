label scene6_day1:
     
    $ quick_menu = True
    "Volteo mi mirada hacia la ventana y empiezo a observar que llegamos a un vecindario reconocido."
    stop ambient fadeout(0.5)
    $ renpy.pause(5.0, hard=True)
    play audio open_car_door
    "Papá por fin estaciona. Blaze y yo nos bajamos."
    play ambient int_night fadein(2.0)
    play audio close_car_door
    "El silencio del auto se traslada a la puerta."
    "Blaze me pone la mano en el hombro y entra primero y yo la sigo."
    play audio closet_open
    scene livingroom_n with fade
    "La casa está a oscuras, voy al encendedor y enciendo las luces de la sala."
    play audio light_switch
    scene livingroom_l
    play audio closet_close
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
    play audio closet_open
    scene lailaroom_n with Fade(0.3, 0.3, 0.3)
    "Llego a mi habitación, mi supuesto refugio."
    play audio closet_close
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
    play audio door_knock
    "Escucho que alguien toca la puerta..."
    "Me quedo en silencio. No me quiero levantar."
    play audio closet_open
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
    play audio closet_close
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
    play audio closet_open
    show counter 1compadecert
    $ enfocar("counter")
    dad "Descansa, Laila."
    show counter 1compadecer
    $ normal("counter")
    play audio closet_close
    hide counter with Dissolve(0.5)
    "Cierra la puerta de mi habitación lentamente."
    "Veo como la iluminación del pasillo se desvanecía por completo, llenando mi habitación de oscuridad total."
    "Un pequeño escalofrío me invade por mi cuerpo al sentir está emoción..."
    "Pero no es de frío o de miedo. Es... diferente."
    "Una sensación extraña, casi olvidada. ¿Será... esperanza? ¿O solo el susto de que algo finalmente haya salido bien?"
    "¿Eso es normal?"
    show parpadeo_on
    "Una vez esa charla, intento dormir, esperando al siguiente día."
    $ quick_menu = False
    hide screen phone_button
    with Dissolve(5.0)
    stop ambient fadeout(1.5)
    scene black with Fade(1.0, 1.0, 1.0)

    # $ renpy.pause(3.0, hard=True)
    # if(rutaCanon-rutaSuicida)==1:
    #     call unlock_paralela1

return

# label unlock_paralela1:

#     $ persistent.unlocked_paralela1 = True  
#     show screen unlock_notification("¡Has desbloqueado la ruta Azul Paralela!\n\nAhora puedes acceder a este contenido desde el menú Extras.")
#     $ renpy.pause()
    
#     return


    #if persistent.day < 1:
    #    $ persistent.day = 1
    #   $ renpy.save_persistent()

    # Finaliza el juego: