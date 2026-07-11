image blaze_parpadeo:
    "blaze 3blink"
    pause 0.08
    "blaze 3preocupada"
    pause 0.08
    "blaze 3blink"
    pause 0.08
    "blaze 3preocupada"

label scene6_day3:
 
    $ quick_menu = True
    window show

    if (rutaCanon-rutaSuicida)>=0:
        "Las últimas horas se arrastraron como si el tiempo estuviera tan cansado como yo."
        "Clases que entraban por un oído y salían por el otro{w} Profesores que ya ni me pedían participar, habían aprendido que mi silencio era más estable que mis respuestas."
        play audio bell
        "Una vez suena la última campana del día, veo cómo mis “compañeros” empiezan a irse. Pero estos tres no. Se quedan, como si esperaran algo. O a alguien."
        l_thought "Otra vez ellos. Otra vez el mismo ritual."
        play music bgm15
        scene class3A at afternoon_filter
        show dark 1distraido:
            left
            afternoon_character
        show blaze 1seria:
            center2
            afternoon_character
        show jeremy 1serio:
            flip
            right5
            afternoon_character
        with dissolve_scene_full2
        "Cada uno guarda sus cosas con calma, sin prisas.{w} Como si el tiempo no fuera un lujo que otros no pueden permitirse."
        $ renpy.pause(4.0, hard=True)
        show dark 1feli:
            boo3
        "Dark es el primero en levantarse.{w} Se estira con un ruido exagerado, como un gato viejo después de una siesta."
        show blaze 1juzga
        show jeremy 1juzga
        show dark 1felit
        $ enfocar("dark")
        d "Bueno, otro día, otro aburrimiento superado con éxito."
        show dark 1desafiantet
        extend " ¿Alguien me da una medalla?"
        show dark 1desafiante
        $ normal("dark")
        show jeremy 1seriot
        $ enfocar("jeremy")
        je "Tu medalla sería aprender a estar cinco minutos sin abrir la boca."
        show jeremy 1serio
        $ normal("jeremy")
        show dark 1sarcasmot
        $ enfocar("dark")
        d "Imposible.{w} Moriría de abstinencia."
        show dark 1sarcasmo
        $ normal("dark")
        show jeremy 1neutral2
        "Jeremy niega con la cabeza, pero no hay veneno en su gesto.{w} Solo costumbre."
        show blaze 1seria2
        "Blaze también se levanta, ajustándose la mochila con un suspiro que arrastra todo el cansancio del día."
        show blaze 1seria3t
        $ enfocar("blaze")
        b "Ojalá pudiera quedarme dormida aquí mismo. Pero no. Hay papeleo."
        show blaze 1seria2
        $ normal("blaze")
        l_thought "¿Papeleo? ¿De qué habla?"
        show blaze 1neutral
        l "Eh... Blaze, ¿otra vez te quedas?"
        show blaze 1seria2t
        $ enfocar("blaze")
        b "Sí. El director nos tiene hasta tarde con eso de la secretaría y lo clubes.{w} No me preguntes por qué."
        show blaze 1seria2
        $ normal("blaze")
        "Lo dice con fastidio, como si la hubieran arrastrado a algo que no pidió."
        show jeremy 1serio2
        extend " Jeremy desvía la mirada."
        show dark 1metiche
        extend " Dark sonríe, claramente responsable de algo."
        l_thought "Secretaria del consejo. Mi hermana la responsable, la útil, la que todos quieren cerca."
        show blaze 1seria
        l "Ah. Qué divertido."
        show blaze 1preocupada
        "Mi voz suena más seca de lo que quería.{w} Blaze me mira con esa expresión que conozco demasiado: preocupación mezclada con culpa."
        "Me levanto.{w} Los huesos me crujen, como si hubiera envejecido diez años en un solo día."
        show blaze 1preocupadat
        $ enfocar("blaze")
        b "Oye... ¿Y papá? ¿Ya te dijo algo de hoy? ¿Van a salir?"
        show blaze 1preocupada
        $ normal("blaze")
        l_thought "Ahí está. La pregunta que no quería escuchar."
        l "Ni idea.{w} Supongo que ya me avisará."
        "Miento. O no.{w} Todavía no sé.{w} El teléfono sigue mudo en mi bolsillo."
        "Dark se reclina en su pupitre, observándonos como si fuéramos su serie favorita."
        show dark 1felit
        $ enfocar("dark")
        d "Qué emocionante."
        show dark 2juzgat
        extend " ¿Alguien quiere palomitas?"
        show dark 1feli
        $ normal("dark")
        show jeremy 1seriot
        $ enfocar("jeremy")
        je "Dark, cállate."
        show jeremy 1serio
        $ normal("jeremy")
        show blaze 1seriat
        $ enfocar("blaze")
        b "Estoy de acuerdo con Jeremy. Cállate."
        show blaze 1seria2
        $ normal("blaze")
        show dark 2sarcasmot
        $ enfocar("dark")
        d "Qué bonito. Se alían contra mí.{w} Me siento especial."
        show dark 2sarcasmo
        $ normal("dark")
        l_thought "Ese idiota. Siempre convirtiendo todo en un espectáculo."
        "Saco el teléfono del bolsillo.{w} La pantalla me devuelve un reflejo pálido, ojeroso. Sin notificaciones."
        l_thought "Claro. ¿Por qué iba a contestar?"
        show dark 1desafiantet
        $ enfocar("dark")
        d "¿Qué?{w} ¿El señor puntual otra vez desaparecido?"
        show dark 1desafiante
        $ normal("dark")
        "Lo fulmino con la mirada, pero no tengo energía para responder."
        show blaze 1preocupadat
        $ enfocar("blaze")
        b "Laila...{w} ¿Quieres escribirle?"
        show blaze 1preocupada
        $ normal("blaze")
        "Asiento.{w} Mis dedos tiemblan sobre la pantalla."
        show jeremy 1juzga
        show dark 2juzga2
        $ inac("dark")
        $ inac("jeremy")
        "Blaze se acerca un poco y empieza a hablar susurrado."
        show blaze 3preocupadat
        $ enfocar("blaze")
        b "¿Necesitas que vaya contigo? Puedo decir que me siento mal o algo..."
        show blaze 3preocupada
        $ normal("blaze")
        l_thought "No. No quiero que me vean así."
        extend " No quiero que nadie me vea así."
        "..."
        l_thought "Mentira. Lo que tengo que hacer es huir, esconderme, desaparecer..."
        l_thought "Pero tengo que hacer esto..."
        "Doy un largo suspiro e intento hablar."
        l "No hace falta.{w} Ve a lo tuyo, no me hace falta una niñera"
        show dark 1distraido
        show jeremy 1serio3
        show blaze_parpadeo:
            center2
            afternoon_character
        "El chiste duele.{w} Lo noto en la forma en que Blaze parpadea, como si le hubiera escupido. Pero no me retracto."
        hide blaze_parpadeo
        l "Además, a ti te necesitan más que a mí.{w} Siempre."
        l_thought "Y tengo mi justificación al pensar así, al mal traducido (Jeremy) no parece que le caiga bien, ni tampoco pienso escuchar a este..."
        extend " pendejo (Dark)."
        l_thought "Además, como debería de ayudar con algo que se supone que “es sencillo”."
        extend " Qué más da."
        show blaze 1compadecert
        $ enfocar("blaze")
        b "¿Estás realmente segura de esto, Laila?"
        show blaze 1compadecer
        $ normal("blaze")
        l "¿Mi cara te parece la de alguien que duda? Porque no lo estoy."
        show blaze 3preocupada
        "Respondo con algo de enojo a su persistencia.{w} Demasiado rápido{w}. Demasiado filoso."
        l_thought "En serio ya le dije que no quiero estar con alguien, esto tengo que solucionarlo solo."
        extend " Si ella va..."
        l_thought "Ugh... No sé qué voy a sentir en ese momento."
        l "Nos vemos, Blaze."
        "Me retiro por fin del salón sin dejar contestar a Blaze, intentando no pensar que esto es una mala idea."
        scene pasillo at afternoon_filter with Fade(1.0, 0.5, 1.0)
        stop music fadeout 1.5
        l_thought "La caminata la siento cada vez más sofocante..."
        "Mis pasos resuenan huecos en el pasillo vacío. Cada eco suena como un reproche."
        show black with Dissolve(0.3):
            alpha 0.8
        centered "{sc=4}{b}Egoísta.{/b}{/sc}"
        centered "{sc=4}{b}Ingrata.{/b}{/sc}"
        centered "{sc=4}{b}Cobarde.{/b}{/sc}"
        hide black with Dissolve(0.3)
        l_thought "¿Por qué dije eso? “¿Mi cara te parece la de alguien que duda?” Qué estúpida. Claro que dudo. Dudo de cada maldito paso que doy."
        l_thought "“¿Mi cara te parece la de alguien que duda?”"
        l_thought "Qué estúpida. Claro que dudo. Dudo de cada maldito paso que doy."
        l_thought "“No me hace falta una niñera”..."
        l_thought "Quiero marcar un poco ese límite, no quiero sentir que soy una carga..."
        extend " Realmente no quiero."
        show screen red_effect2
        nobody "{sc=5}¿En serio?{/sc}"
        nobody "{sc=5}¿Te quieres seguir mintiendo a ti misma?{/sc}"
        nobody "{sc=7}¿No te han dejado claro que eres una carga para todos?{/sc}"
        l_thought "Cállate. Por una maldita vez, cállate de verdad."
        hide screen red_effect2 with Dissolve(0.5)
        scene pasillo2 at afternoon_filter with Fade(1.0, 0.5, 1.0)
        show vignette at vineta_organico zorder 100
        "Mis pasos se frenan en seco a mitad del pasillo.{w} Me apoyo contra los casilleros, sintiendo el metal frío a través de mi ropa.{w} La respiración se me entrecorta."
        hide vignette
        "De pronto, un sonido me saca de mi espiral. Pasos. Rápidos.{w} Conocidos."
        b "Laila, ¡espera!"
        "Dice jadeando."
        l_thought "No... ¿Por qué vino? ¿No le quedó claro que quiero estar sola?"
        extend " ¿No le quedó claro que quiero estar sola?"
        play music bgm4
        show blaze 1blink:
            flip
            afternoon_character
            slide_in_left_fast_to_center
        "Me giro y veo a Blaze al final del pasillo, deteniéndose con el rostro ligeramente enrojecido, como si hubiera corrido."
        show blaze 1compadecert
        $ enfocar("blaze")
        b "Olvidé darte esto. Por si...{w} Te da hambre en el camino."
        show blaze 1compadecer
        $ normal("blaze")
        "Saca de su mochila una pequeña bolsa de galletas.{w} No son las industriales de la tienda."
        show blaze 1compadecert:
            flip
            afternoon_character
            center
        "Están envueltas en papel encerado, cerrado con una pegatina de corazón.{w} Las hizo ella."
        l_thought "No son galletas. Es una excusa."
        extend " Es su manera de decir “sigo aquí” sin tener que decirlo."
        "Mis dedos tiemblan al tomar la bolsa.{w} La voz en mi cabeza se calla por un instante, ahogada por este simple acto de bondad obstinada."
        l "No tenías que..."
        show blaze 1compadecert
        $ enfocar("blaze")
        b "Lo sé."
        show blaze 1felizt:
            boo2
        extend " Pero quería."
        show blaze 1feliz
        $ normal("blaze")
        "Pausa.{w} Su pecho aún sube y baja por la carrera, pero sus ojos están fijos en los míos, buscando algo que no sé si puedo darle."
        show blaze 1compadecert
        $ enfocar("blaze")
        b "No es porque crea que no puedes sola, Laila.{w} Es porque no quiero que tengas que hacerlo."
        show blaze 1compadecer
        $ normal("blaze")
        "La frase me golpea justo donde más duele. No es lástima. No es control. Es...{w} compañía.{w} Ofrecida, no impuesta."
        show blaze 1sonrientet
        $ enfocar("blaze")
        b "Además, Jeremy puede esperar cinco minutos... ¡Dark también!"
        show blaze 1sonriente
        $ normal("blaze")
        $ renpy.pause(0.6, hard=True)
        show blaze 1feliz:
            boo3
            flip_off
            outwalk_left_fast
        "Se da la vuelta antes de que pueda responder.{w} Camina de regreso hacia el aula, pero se detiene a medio camino."
        b "¡Ah! Y dile a papá que no me espere. Ya cenaré algo por aquí."
        show blaze 1sonriente
        "Y se va.{w} Dejándome sola en el pasillo con una bolsa de galletas hechas a mano y un nudo en la garganta que no sé si es tristeza o algo más."
        hide blaze
        "Miro la bolsa.{w} El papel encerado cruje bajo mis dedos."
        l_thought "Maldita sea, Blaze."
        extend " Siempre sabiendo exactamente cómo..."
        extend " Romperme."
        "Aprieto la bolsa de galletas.{w} Saben a elección.{w} A que alguien eligió volver a intentarlo, incluso después de que yo le cerrara la puerta en la cara."
        "Me quedo sola con las galletas.{w} El pasillo está vacío."
        "Silencio."
        $ renpy.pause(3.5, hard=True)
        stop music fadeout 1.5
        play audio phone_quiet
        "El teléfono vibra.{w} Casi se me caen las galletas de las manos."
        "MENSAJE DE:{w} PAPÁ."
        call chat_dad_day3
        "Guardo el teléfono. Aprieto las galletas contra mi pecho un segundo, como si pudiera absorber ese gesto, hacerlo parte de mí."
        "Camino hacia la salida.{w} Mis pasos ya no resuenan huecos."
        "Ahora tienen compañía: el leve crujido de una bolsa de galletas que prueba, contra toda lógica, que tal vez no soy completamente indigna de cuidado."
        scene school_entrance_afternoon with Fade(1.0, 2.5, 1.0)
        play ambient ext_day fadein(2.0)
        "Llego a la puerta principal de la escuela. El sol de la tarde se filtra por los ventanales, pintando el piso de rayas doradas."
        "Salgo. El aire afuera es fresco, casi amable. Me tomo mi tiempo para ajustarme al brillo."
        l_thought "¿Por qué mierda, aun así estemos en un domo flotante, el sol pega tanto? Dios."
        "Una vez me adapto a la iluminación, empiezo a caminar hacia donde papá nos suele recoger."
        scene intersection_afternoon with Fade(0.8, 1.5, 0.8)
        "Llego al punto de encuentro.{w} Miro hacia ambos lados de la calle.{w} Nada."
        l_thought "No..."
        extend " No ha llegado todavía."
        "Miro a mi mano, mirando las galletas...{w} No con odio{w}, sino con un sentimiento extraño..."
        l_thought "Mejor..."
        extend " Las guardo, no quiero que les pase algo."
        "Me acomodo mi mochila y las guardo. El corazón me da un vuelco. Un vuelco estúpido, infantil, que odio reconocer."
        $ renpy.pause(3.5, hard=True)
        "Pasan dos minutos.{w} Tres.{w} Cuatro."
        l_thought "Otra vez no..."
        extend " Por favor, otra vez no."
        $ renpy.pause(3.5, hard=True)
        play audio car_horn volume 0.3
        "Y entonces, a lo lejos, el claxon. Ese sonido áspero, metálico, que siempre me hacía quejarme cuando era pequeña."
        "“Papá, ¿por qué no usas el claxon normal?” Y él respondía, serio: “Porque este se oye mejor.”"
        "Pero...{w} Hoy no me quejo."
        "El coche se acerca lentamente y se detiene frente a mí.{w} El motor ronronea, cansado pero fiel."
        "El coche se estaciona frente a mí, y escucho el reconocible “click” de cuando se bajan los seguros, dándome a entender que entre."
        "Me dirijo al asiento trasero, pero mi padre baja la ventanilla."
        show counter 1seriot:
            afternoon_character2
            center 
        with Dissolve(0.3)
        $ enfocar("counter")
        dad "¿Y por qué te subes atrás? Ven adelante conmigo. Vamos."
        show counter 1serio
        $ normal("counter")
        l_thought "¿El asiento delantero? Pero... siempre me montó atrás."
        extend " Es como un acuerdo... La distancia segura."
        "Me quedo paralizada, la mano aún en el tirador de la puerta trasera.{w} Esto ya no es solo llegar tarde.{w} Esto es romper el protocolo no escrito"
        "Mi papa suspira al ver un poco, hablando con un tono firme un poco cansado de mis… actos."
        show counter 1compadecert
        $ enfocar("counter")
        dad "Laila, por favor."
        show counter 1compadecer
        $ normal("counter")
        l_thought "“Por favor”. Otra palabra que no usa conmigo. Primero Blaze, ahora él."
        extend " ¿Qué está pasando hoy?"
        l_thought "Su voz suena... Diferente. No más fuerte, pero más presente."
        "Dudo un instante más antes de caminar lentamente hacia el otro lado del auto."
        play audio open_car_door
        extend " Abro la puerta del copiloto y me siento, sintiéndome como un intruso en un espacio que no me pertenece. El asiento está ajustado a su altura."
        "Este era el territorio de {i}ella{/i}."
        hide counter with Dissolve(0.3)
        stop ambient fadeout(1.5)
        scene black with Fade(0.3, 0.3, 0.3)
        play audio close_car_door
        play ambient bus fadein(2.0)

    else:
        "Las últimas horas se arrastraron como si el tiempo estuviera tan cansado como yo."
        "Clases que entraban por un oído y salían por el otro.{w} Profesores que ya ni me pedían participar, habían aprendido que mi silencio era más estable que mis respuestas."
        play audio bell
        "Una vez suena la última campana del día, veo como mis “compañeros” empiezan a irse.{w} Pero veo cómo estos 3 se quedan aquí."
        play music bgm6
        scene class3A at afternoon_filter
        show dark 1distraido3:
            left
            afternoon_character
        show blaze 1seria3:
            center2
            afternoon_character
        show jeremy 1serio2:
            flip
            right5
            afternoon_character
        with dissolve_scene_full2
        l_thought "..."
        l_thought "¿Por qué no se van? ¿Qué esperan?"
        extend " ¿No tienen nada mejor para hacer?"
        "Cada uno guarda sus cosas rápidamente, esperando que hasta la última alma de aquí se vaya."
        $ renpy.pause(4.0, hard=True)
        show dark 1serio:
            boo2
        "Dark es el primero en levantarse y estirarse."
        show dark 1sarcasmot
        $ enfocar("dark")
        d "Bueno, yo los espero afuera, sinceramente no quiero estar aquí con ella."
        show dark 2incomodot
        d "Sale mejor estar en un campo de guerra."
        show dark 2incomodo
        $ normal("dark")
        show blaze 3seria
        show jeremy 1serio3
        l_thought "Por fin. Un poco de sinceridad en esta prisión."
        extend " Agradezco mucho que no disfrute su desprecio."
        "No me molesto en responder. No le veo sentido y no tengo ganas de discutir.{w} Suspiro de forma dramática."
        show dark 1distraido:
            flip
            xanchor 0.5 yanchor 1.0
            parallel:
                ease 5.5 xpos -400
            parallel:
                block:
                    ease 0.5 yoffset 15
                    ease 0.21 yoffset 0
                    repeat 11
                yoffset 0
        "Es el primero de los 3 en salir.{w} Sin mirar atrás.{w} Dejando el mensaje claro."
        "Jeremy termina de cerrar su mochila.{w} Dejando el sonido del cierre en seco."
        show jeremy 1serio
        hide dark
        "Me mira de arriba abajo, analizándome."
        $ renpy.pause(3.0, hard=True)
        l "¿Acaso tengo algo en la cara o qué?"
        l_thought "Que molesto..."
        extend " Ya sé que estoy como un desastre natural, pero tampoco para que me analices como si fuera un maldito experimento."
        $ renpy.pause(3.0, hard=True)
        show blaze 1preocupada
        "Blaze me mira.{w} Se acerca con una mirada preocupada y mordiéndose el labio.{w} Como si midiera sus palabras antes de decirlas."
        show blaze 1compadecert
        $ enfocar("blaze")
        b "Laila...{w} ¿Quieres hablar o...?"
        show blaze 1compadecer
        $ normal("blaze")
        l_thought "Sí. Puedes dejarme sola."
        l_thought "Puedes admitir que esto es un juego donde tú eres la santa y yo la pecadora que necesita redención."
        l_thought "Puedes irte con tus amigos perfectos y dejar que me pudra en paz con mi miseria, que por lo menos es mía."
        "La miro directamente, con una sonrisa vacía."
        l "No.{w} Mi personalidad dice que no debo hablar contigo, solo requiero una habitación sola en estos momentos."
        l " O mejor, un extintor para apagar el circo en el que se ha convertido mi vida."
        hide blaze
        show blaze_parpadeo:
            center2
            afternoon_character
        "Ella parpadea, herida."
        hide blaze_parpadeo
        show blaze 3preocupada:
            center2
            afternoon_character
        l_thought "Es mejor que esté así que la falsa preocupación."
        "Blaze mira a Jeremy, buscando refuerzos."
        show jeremy 1serio:
            asentir
        extend " Él asiente levemente, como un director dando la señal para el siguiente acto."
        l_thought "No. Hoy no."
        l_thought "Hoy no me voy a dejar arrastrar a su obra de teatro donde todos tienen un guión excepto yo."
        "Me levanto, agarro mi mochila y camino hacia la puerta sin mirarlos.{w} Paso junto a ellos."
        l "No molesten.{w} El proyecto de rehabilitación de Laila está cancelado por hoy."
        "Hago una pausa en la puerta, sin voltear."
        show jeremy 1juzga
        show blaze 2desinteresada3
        l "Vayan a salvar a alguien que al menos les vaya a dar las gracias."
        scene pasillo at afternoon_filter
        show dark 1distraido:
            left
            afternoon_character
        with Fade(1.0, 0.5, 1.0)
        stop music fadeout 1.5
        "Salgo al pasillo, dejando atrás su silencio cargado de decepción."
        extend " Dark está apoyado en la pared frente a la puerta, como un guardián aburrido."
        show dark 1sarcasmot
        $ enfocar("dark")
        d "¿Ya terminó el episodio de hoy?"
        show dark 1sarcasmo
        $ normal("dark")
        "Sigo caminando sin detenerme. Haciendo que mis palabras resuenen en el pasillo."
        l "Sí.{w} Spoiler: la protagonista sigue sin querer ser salvada.{w} Qué aburrido, ¿no?"
        hide dark with Dissolve(0.2)
        "Camino hacia la salida, sintiendo sus miradas en mi espalda como dagas sin filo."
        l_thought "Esta es la única verdad que me queda: el deseo de que todos se vayan a la mierda. Es frío, es feo, pero es mío. Y por ahora, es lo único a lo que me puedo agarrar."
        "El pasillo, que antes me parecía una cloaca opresiva, ahora se siente como un túnel de escape.{w} Pero es un escape hacia la nada."
        "No tengo destino.{w} Mis pies simplemente se mueven, alejándose del aula, de ellos, de todo."
        "Giro en una esquina, luego en otra, sin un plan más allá de poner la mayor distancia posible entre yo y el escenario de esa incomodidad ensayada."
        l_thought "¿A dónde se supone que debo ir? ¿A la biblioteca? ¿A esconderme en un baño? ¿A casa? Como si “casa” fuera un refugio y no otra habitación con cuatro paredes que esperan que me componga."
        l_thought "Todos los caminos parecen llevar a otro tipo de prisión, a otra versión de la misma expectativa: que en algún momento deje de ser esto."
        "Mis pasos se hacen más lentos sin que yo me dé cuenta.{w} La adrenalina del escape se disipa, dejando un vacío pesado y familiar en el pecho.{w} El sonido de mis zapatos ya no es un martilleo desafiante, sino un arrastre cansado."
        scene pasillo2 at afternoon_filter with Fade(1.0, 0.5, 1.0)
        "Me detengo frente a una ventana grande que da al patio vacío.{w} El sol de la tarde proyecta largas sombras, pintando el asfalto de un naranja enfermizo."
        "Ahí fuera hay espacio, aire, pero parece tan falso e inalcanzable como el interés de Blaze y sus amigos."
        "Apoyo la frente contra el cristal frío. El vidrio absorbe un poco del calor de mi piel, un pequeño alivio insignificante."
        l_thought "Vayan a salvar a alguien que al menos les vaya a dar las gracias. Quizás tenía razón."
        l_thought "Quizás el problema es que soy una ingrata. Una ingrata por no querer su caridad, su obra de teatro benéfica."
        l_thought "¿Cuándo se convirtió el simple hecho de existir en un proyecto de rehabilitación para que otros se sientan bien consigo mismos?"
        show parpadeo_on
        "Cierro los ojos y respiro hondo.{w} El único sonido ahora es el leve zumbido de los fluorescentes sobre mi cabeza."
        l_thought "Estoy completamente sola."
        extend " Lo conseguí."
        l_thought "Y es tan desolador y frío como pensé que sería, pero al menos esta desolación es mía."
        extend " No está decorada con su falsa compasión."
        show screen red_effect2
        nobody "{sc=5}¿O será que finalmente te rendiste?{/sc}"
        nobody "{sc=5}Que aceptaste lo que siempre supiste.{/sc}"
        nobody "{sc=7}{b}Que el mundo está mejor sin tu drama constante{b}.{/sc}"
        hide parpadeo_on
        show parpadeo_off
        "Camino, intento caminar para alejar estos malos pensamientos.{w} La mochila, pesada como un ladrillo de desprecio.{w} Desde aquí, el pasillo parece aún más largo y vacío."
        hide parpadeo_off
        l_thought "No sé cuánto tiempo me quedé aquí. No importa."
        l_thought "El tiempo es solo otra cosa que debo esperar a que pase."
        nobody "{sc=5}Cada segundo que pasa es otro segundo que tienen que aguantarte.{/sc}"
        nobody "{sc=5}Otro segundo que les robas con tu mera existencia.{/sc}"
        l_thought "Que se cansen. Que se rindan."
        l_thought "Que me dejen por fin en paz con mi miseria... Esta amargura... Está fría, fea y familiar amargura..."
        extend " Es el único hogar que no me pide que cambie."
        nobody "{sc=7}{b}Mentira{/b}.{/sc}"
        nobody "{sc=5}Ni siquiera esta amargura te quiere.{/sc}"
        nobody "{sc=5}Solo es lo único lo suficientemente patético para quedarse contigo.{/sc}"
        nobody "{sc=5}Es el refugio de los que no tienen a dónde más huir.{/sc}"
        "Y en el silencio que llena el pasillo, el eco de mis propios pasos ya se ha desvanecido, reemplazado por el latido sordo de un resentimiento que se ha convertido en mi único hogar."
        "De la nada escucho unos pasos corriendo hacia mi dirección.{w} Volteo, esperando que sea alguno de los que dejé atrás pero..."
        show mani 1nervioso:
            flip
            afternoon_character
            slide_in_left_fast_to_center
        play audio fall
        hide screen red_effect2
        "¿Es Mani? Choca conmigo, rebotando casi inmediatamente." with hpunch
        show mani 1nerviosot
        $ enfocar("mani")
        ma "¡Uy! ¡Perdón! ¡Lo siento, lo siento! Iba pensando en..."
        show mani 2felizt
        extend " ¡en la cena que me espera!"
        show mani 2feliz
        $ normal("mani")
        pause 0.6
        show mani 2feliz:
            flip
            afternoon_character
            center
        "Estaba esperando el más mínimo gesto para explotar. Esta vez no me contengo."
        l "¡¿Eres puto ciego o qué, imbécil?! ¡Fíjate por dónde vas, maldita sea!"
        show screen red_effect2
        nobody "{sc=5}Mira, hasta para gritar eres predecible.{/sc}"
        nobody "{sc=5}Las mismas malditas palabras, el mismo show.{/sc}"
        nobody "{sc=5}Ni siquiera tu ira es original.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
        "Mis uñas se clavan en las palmas de mis manos, un dolor pequeño y controlable con la rabia que tengo en estos momentos."
        show mani 3pinguino
        "Él en vez de devolverme el insulto o algo, me mira con curiosidad."
        show mani 1felizt
        $ enfocar("mani")
        ma "¡Laila! Con que eras tú... ¡Qué interesante!"
        show mani 1feliz
        $ normal("mani")
        "Me quedo en silencio un momento.{w} El sobrepensamiento lucha con la confusión. Él no está reaccionando como yo esperaba."
        l_thought "¿Es puta broma? ¿Por qué mi ira no le afecta? Es demasiado despistado para captar que no quiero hablar con él."
        l_thought "Es demasiado despistado para captar que no quiero hablar con él."
        extend " Es un puto niño."
        show screen red_effect2
        nobody "{sc=5}Claro, porque hasta para ser odiosa eres incompetente.{/sc}"
        nobody "{sc=5}Ni siquiera puedes asustar a un niño hiperactivo.{/sc}"
        nobody "{sc=5}¿En qué clase de fracaso te has convertido?{/sc}"
        hide screen red_effect2 with Dissolve(0.3)
        l "Oh, qué honor ser tu fuente de tus análisis.{w} Ahora lárgate, antes de que te use de abono."
        "Digo con un tono sarcástico, pero ya agobiada de todo."
        show mani 3juzgat
        $ enfocar("mani")
        ma "¿Abono? ¿Para qué? ¿Para que crezca una planta carnívora?"
        show mani 2felizt
        ma "¡Me recuerdas a un personaje de un anime donde nadie la quiere, ¡pero es solo porque necesita un abrazo de gato!"
        show mani 1feliz
        $ normal("mani")
        "Me lo dice con un tono inocente, sin saber lo que está pasando."
        l_thought "Parece que Mani no tiene la “falsa compasión” que odio; es simplemente un “Catalizador de Conflictos”."
        l_thought "Ni siquiera me está tomando en serio."
        show screen red_effect2
        nobody "{sc=5}¿Y por qué lo haría?{/sc}"
        nobody "{sc=5}Eres una niña berrinchuda haciendo escándalo en un pasillo.{/sc}"
        nobody "{sc=5}Ni tú misma te tomas en serio.{/sc}"
        hide screen red_effect2 with Dissolve(0.3)
        "..."
        "Suspiro.{w} Ya agotada con esta interacción."
        l "Eres un puto imbécil."
        show mani 1felizt
        $ enfocar("mani")
        ma "¡Gracias! ¡Me lo dicen mucho! ¡Adiós!"
        show mani 1feliz
        $ normal("mani")
        $ renpy.pause(0.6, hard=True)
        show mani 2feliz:
            flip_off
            pause 0.5
            boo3
            pause 0.2
            xanchor 0.5 yanchor 1.0
            easein 0.3 xpos 2500
        "Mani se va corriendo por el pasillo.{w} Me quedo sola. La rabia se esfuma, dejando un vacío helado."
        show screen red_effect2
        nobody "{sc=5}Y ahí lo tienes.{/sc}"
        hide mani
        nobody "{sc=5}Ahuyentaste hasta al único ser que era demasiado estúpido para odiarte.{/sc}"
        nobody "{sc=8}Bravo, Laila.{/sc}"
        nobody "{sc=5}Un nuevo récord en tu colección de fracasos.{/sc}"
        hide screen red_effect2 with Dissolve(0.3)
        "..."
        "Aflojo los puños.{w} Observo las pequeñas marcas rojas en mis palmas."
        l_thought "Ni siquiera puedo tener una puta discusión decente. Esta amargura es lo único que no me ha fallado."
        l_thought "Esta es la única verdad que me queda: el deseo de que todos se vayan a la mierda."
        l_thought "Es frío, es feo, pero es mío. Y en esta ruta, es el único camino que puedo tomar."
        show screen red_effect2
        nobody "{sc=5}Camino... ¿a dónde?{w} ¿A más de lo mismo?{/sc}"
        nobody "{sc=5}¿A otro día de fingir que no quieres exactamente lo que mereces?{/sc}"
        nobody "{sc=7}Sigue caminando, Laila.{/sc}"
        nobody "{sc=8}{b}A ver qué tan lejos llegas antes de darte cuenta de que no hay escapatoria{/b}.{/sc}"
        "..."
        hide screen red_effect2
        play audio phone_quiet loop
        "En medio del silencio, una vibración inesperada en mi bolsillo me saca de mis pensamientos. Agotada, lo tomo, veo a la pantalla y veo quien es…"
        l "P-papá..."
        show vignette at vineta_organico zorder 100
        "Siento como el color se va de mi piel y como se instala en mi pecho."
        $ renpy.pause(2.0, hard=True)
        l_thought "¿Por qué llama? ¿Para checar? ¿Para confirmar lo que ya sabe? ¿Para darme otra oportunidad de decepcionarlo en tiempo real?"
        hide vignette
        "El teléfono sigue vibrando.{w} Insistente.{w} Como si supiera que no puedo ignorarlo."
        $ renpy.pause(2.0, hard=True)
        "Lo contesto."
        stop audio
        call call_dad_day3_rutasuicida
        "Click."
        "Cuelga sin esperar respuesta.{w} Sin un “te espero”.{w} Sin un “cuidado”.{w} Solo el vacío de la llamada terminada."
        l_thought "Ahí está. La prueba número mil de que soy una carga."
        l_thought "De que ni siquiera puedo hacer algo tan simple como estar en el puto lugar a la puta hora."
        "Me quedo mirando el teléfono, los tres minutos empezando a contar en mi cabeza como una bomba de tiempo."
        $ renpy.pause(2.0, hard=True)
        "Guardo el teléfono.{w} Mis dedos aún presionan la pantalla como si pudieran extraer algo más de esa conversación de diez segundos."
        show screen red_effect2
        nobody "{sc=5}Corre, pequeña fracasada.{/sc}"
        nobody "{sc=5}Corre a demostrar una vez más que no puedes ni siquiera ser puntual.{/sc}"
        hide screen red_effect2
        "Empiezo a caminar. Mis pies se mueven solos, arrastrándose hacia la salida.{w} El pasillo se estira interminable, cada paso un recordatorio de mi propia incompetencia."
        l_thought "Quince minutos. No es mucho."
        extend " Para cualquiera no es mucho."
        l_thought "Pero para él, para papá, quince minutos son una eternidad de esperar a que su hija deje de ser quien es."
        $ renpy.pause(2.0, hard=True)
        show screen red_effect2
        nobody "{sc=5}Claro.{/sc}"
        nobody "{sc=5}Porque cualquier padre esperaría a su hija con paciencia.{/sc}"
        nobody "{sc=5}Pero tú te las arreglas para convertir quince minutos en un acta de acusación.{/sc}"
        nobody "{sc=5}Es un talento, en realidad.{/sc}"
        l "Cállate."
        "Las palabras escapan de mis labios en un susurro áspero, pero la voz en mi cabeza no necesita oír para continuar."
        nobody "{sc=5}Mira el lado bueno:{/sc}"
        nobody "{sc=5}Al menos hoy no tendrás que fingir que querías estar con él.{/sc}"
        nobody "{sc=5}Ya empezaste con el pie izquierdo.{w} Como siempre.{/sc}"
        l_thought "Como siempre..."
        hide screen red_effect2 with Dissolve(0.3)
        "Sigo caminando.{w} La mochila pesa el doble ahora, cargada con el peso de la llamada, del encuentro con Mani, de todo el día."
        "Llego a la puerta principal de la escuela. El sol de la tarde se filtra por los ventanales, pintando el piso de rayas doradas que parecen barreras que debo cruzar."
        "Mi mano tiembla al empujar la puerta."
        scene school_entrance_afternoon with Fade(1.0, 2.5, 1.0)
        play ambient ext_day fadein(2.0)
        "Salgo.{w} Con miedo."
        "Sin saber qué esperar. El sol me pega en la cara. Me tomo mi tiempo para ajustarme al brillo."
        l_thought "¿Por qué mierda, aun así estemos en un domo flotante, el sol pega tanto? Dios."
        "Una vez me adapto a la iluminación, empiezo a caminar hacia donde papá nos suele recoger."
        "Cada paso es una batalla.{w} Mis pies parecen querer clavarse en el concreto, rebelándose contra el destino que me espera."
        l_thought "¿Y si me doy la vuelta? ¿Y si simplemente sigo caminando en otra dirección?"
        l_thought "Pero ¿a dónde iría? Todos los caminos llevan a la misma decepción."
        scene intersection_afternoon with Fade(0.8, 1.5, 0.8)
        "A lo lejos, distingo su auto estacionado con precisión militar en el lugar exacto de siempre. Negro, impoluto, reflejando la luz del atardecer como un espejo que devuelve una imagen que no quiero ver."
        show screen red_effect2
        nobody "{sc=6}Ahí está. Tu juez y tu verdugo.{/sc}"
        nobody "{sc=6}Esperando para el veredicto diario.{/sc}"
        hide screen red_effect2 with Dissolve(0.3)
        "Me acerco lentamente, sintiendo cómo la distancia se reduce como una cuenta regresiva hacia mi ejecución."
        "Escucho el reconocible “click” de cuando se bajan los seguros, dándome a entender que entre."
        "Me dirijo al asiento trasero, pero mi padre baja la ventanilla."
        show counter 1seriot:
            afternoon_character2
            center 
        with Dissolve(0.3)
        $ enfocar("counter")
        dad "Adelante."
        show counter 1serio
        $ normal("counter")
        "No es una invitación.{w} Es una orden disfrazada."
        l_thought "¿El asiento delantero? Pero..."
        extend " siempre me montó atrás."
        l_thought " Es como un acuerdo... La distancia segura."
        "Me quedo paralizada, la mano aún en el tirador de la puerta trasera.{w} Esto ya no es solo llegar tarde.{w} Esto es romper el protocolo no escrito."
        show counter 1serio:
            sigh_animation
        "Mi papá suspira al verme un poco, hablando con un tono firme un poco cansado de mis...{w} actos."
        show counter 1seriot
        $ enfocar("counter")
        dad "Laila, por favor."
        show counter 1serio
        $ normal("counter")
        l_thought "“Por favor”. Otra palabra que no usa conmigo. Primero Blaze, ahora él."
        extend " ¿Qué está pasando hoy?"
        play audio open_car_door
        "Me siento en el asiento del copiloto."
        scene black with Fade(0.3, 0.3, 0.3)
        stop ambient fadeout(1.5)
        extend " El auto huele a desinfectante, a limpio, a nada."
        "No hay aroma de café. No hay rastro de ella."
        play audio close_car_door
        play ambient bus fadein(2.0)
        "Papá arranca sin mirarme.{w} La radio está apagada.{w} El silencio es una losa."
        l_thought "Esto es peor que si me gritara."
        extend " Prefiero que me grite."
        l_thought "Pero no lo hace."
return