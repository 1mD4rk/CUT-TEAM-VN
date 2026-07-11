label scene8_day3:

    if (rutaCanon-rutaSuicida)>=0:
        "El auto se detiene frente a casa. Las luces de la sala están encendidas, cálidas, como un faro en la niebla de esta noche que no termina de decidirse si quiere ser oscura o permitir que las estrellas falsas del domo la iluminen."
        "Papá apaga el motor. Por un momento, ninguno se mueve."
        $ renpy.pause(4.0, hard=True)
        "El silencio no es incómodo.{w} Es...{w} diferente."
        "Como si el parque, el banco, las palabras que no dijimos pero sentimos, hubieran construido algo frágil entre nosotros. Algo que ninguno quiere romper con un movimiento brusco."
        $ renpy.pause(4.0, hard=True)
        dad "Laila..."
        "Su voz suena distinta. Menos militar.{w} Más papá."
        l "¿Sí?"
        "Papá mira al frente. Sus manos aún en el volante, pero no tensas. Descansan."
        dad "Me alegro de que hayas venido."
        l_thought "¿Se alegra? ¿De verdad?"
        extend " ¿O solo es otra frase de manual?"
        "Pero algo en su tono me hace guardar el sarcasmo.{w} Por una vez, no quiero apuñalar sus palabras con mi cinismo."
        l "Yo...{w} también."
        "La frase sale torpe, mal ensamblada. Pero es verdad.{w} Y eso es lo que más duele."
        "Papá asiente. Baja del auto.{w} Yo lo imito."
        play audio open_car_door
        $ renpy.pause(1.9, hard=True)
        play audio close_car_door
        $ renpy.pause(1.9, hard=True)
        play audio closet_open
        "La puerta de casa se abre antes de que lleguemos a la puerta."
        "Blaze está ahí, con su sonrisa de siempre, pero sus ojos recorren nuestros rostros buscando pistas, buscando heridas, buscando algo que le diga cómo actuar."
        play ambient int_night fadein(2.0)
        scene livingroom_l
        show blaze 1sonriente:
            center
        show counter 1serio:
            left
        with Fade(0.5, 0.5, 0.5)    
        play audio closet_close
        $ renpy.pause(1.9, hard=True)
        show blaze 1sonrientet
        $ enfocar("blaze")
        b "¿Cómo les fue?"
        show blaze 1sonriente
        $ normal("blaze")
        "No es una pregunta casual.{w} Es una evaluación."
        "Es ella tomando la temperatura de la casa, de nosotros, de lo que pasó mientras ella no estaba."
        show counter 1distraido
        "Papá la mira."
        show counter 1serio
        extend " Después me mira a mí."
        show counter 1distraido
        extend " Después vuelve a ella."
        show counter 1distraidot
        $ enfocar("counter")
        dad "Bien."
        show counter 1serio
        $ normal("counter")
        "Una sola palabra. Pero dicha de una forma que no es un muro. Es un resumen. Es todo lo que puede decir ahora."
        show blaze 1feliz:
            asentir
        "Blaze asiente. No presiona. Sabe cuándo hacerlo y cuándo no.{w} Eso es lo que la hace ella."
        show blaze 1felizt
        $ enfocar("blaze")
        b "¿Comieron? Puedo calentar algo."
        show blaze 1feliz
        $ normal("blaze")
        "Papá niega con la cabeza."
        show counter 1distraido2t
        $ enfocar("counter")
        dad "Después. Ahora necesito... descansar un poco."
        show counter 1distraido2
        $ normal("counter")
        $ renpy.pause(1.2, hard=True)
        show counter 1distraido2:
            xanchor 0.5 yanchor 1.0
            parallel:
                ease 6.5 xpos 2500
            parallel:
                block:
                    ease 0.5 yoffset 15
                    ease 0.21 yoffset 0
                    repeat 11
                yoffset 0
        "Sube las escaleras. Sus pasos son pesados, pero no arrastrados.{w} Es el cansancio de quien soltó algo que llevaba cargando demasiado tiempo."
        $ renpy.pause(1.2, hard=True)
        show blaze 1sonriente
        "Blaze se acerca a mí. No habla. Solo me mira. Espera."
        l_thought "¿Qué espera? ¿Que le cuente todo?"
        l_thought "¿Que le diga que papá habló de mamá, que fuimos al parque, que el banco sigue ahí, que el sensor se encendió como quejándose de seguir viva?"
        "Pero no digo nada.{w} Solo me encojo de hombros."
        l "Normal.{w} Fue...{w} normal."
        "Blaze sonríe.{w} No es una sonrisa de alivio. Es una sonrisa de “ya hablaremos cuando puedas”."
        show blaze 1felizt
        $ enfocar("blaze")
        b "Bien. Me alegro."
        hide counter
        show blaze 1feliz
        $ normal("blaze")
        "Me da un pequeño golpecito en el brazo.{w} Su mano está cálida."
        show blaze 1compadecert
        $ enfocar("blaze")
        b "Hay galletas en la cocina. Por si quieres."
        show blaze 1compadecer
        $ normal("blaze")
        l_thought "Las galletas. Siempre las galletas."
        "Siento el peso de las galletas en mi mochila.{w} Las galletas que aún no he comido y que ella me dio antes de irme."
        l_thought "Como si pudieran reparar lo que está roto."
        extend " O tal vez... como si supiera que a veces lo único que puedes hacer es ofrecer algo dulce en medio de lo amargo."
        "Asiento. Pero no voy a la cocina."
        hide blaze with Dissolve(0.3)
        "Subo las escaleras.{w} Cada escalón es un compás de espera.{w} Un segundo entre lo que fui y lo que estoy siendo."
        $ renpy.pause(1.2, hard=True)
        play audio closet_open
        scene lailaroom_n with Fade(0.8, 0.5, 0.8)
        play audio closet_close
        "Llego a mi habitación. Cierro la puerta con suavidad. No quiero que el ruido rompa algo que todavía no sé nombrar. Tiro mi mochila al lado de esta."
        "La oscuridad me recibe. No enciendo la luz.{w} Prefiero la penumbra. Prefiero que las sombras me acompañen mientras decido quién quiero ser esta noche."
        "Me siento en la cama. El colchón cede bajo mi peso. Es el mismo de siempre, pero todo se siente distinto."
        window hide
        $ renpy.pause(5.0, hard=True)
        window show
        "Mi mesita de noche. Allí está. Y sobre ella, el cuadro."
        "La foto."
        "{i}Ella{/i} sonriendo.{w} Blaze pequeña, con su uniforme del colegio, los dientes de leche mostrando una sonrisa desordenada."
        "Counter, mi padre, con el brazo alrededor de las dos, serio pero no duro. Serio de esa forma que ahora entiendo: era su manera de decir “esto es mío, esto es importante, esto no lo cambio por nada”."
        l_thought "Míralos. Felices."
        extend " Completos."
        show screen red_effect2
        nobody "{sc=5}Felices.{w} Sin ti.{/sc}"
        nobody "{sc=7}¿Crees que volverán a ser así?{/sc}"
        "La voz.{w} Otra vez la voz. Pero hoy no suena a cuchillo. Suena a...{w} advertencia.{w} Como si alguien dentro de mí tuviera miedo de que me permita creer."
        l_thought "No lo sé."
        nobody "{sc=7}¿No lo sabes o no quieres admitirlo?{/sc}"
        l_thought "Las dos cosas."
        hide screen red_effect2 with Dissolve(0.5)
        "La voz se calla.{w} No porque haya ganado. Sino porque, por primera vez, no tengo una respuesta automática."
        "Y el silencio, a veces, es más honesto que cualquier palabra."
        window hide
        $ renpy.pause(4.0, hard=True)
        window show
        "Miro la foto un largo rato.{w} Los detalles. La forma en que {i}ella{/i} inclina la cabeza."
        "La manera en que Blaze aprieta los ojos al reír."
        "La postura de papá, como si el mundo no existiera fuera de ese cuadrado de vidrio y madera."
        l_thought "Ese día... ¿qué pasó después?"
        l_thought "¿Quién sacó la foto?"
        l_thought "¿Dónde estaba yo?"
        "No lo recuerdo.{w} O tal vez no estaba.{w} Tal vez esa foto es de cuando el mundo aún tenía forma de familia completa."
        window hide
        $ renpy.pause(3.0, hard=True)
        window show
        "Saco mi teléfono. La pantalla se enciende. La luz me lastima un segundo, hasta que mis ojos se acostumbran."
        "Abro el chat con papá."
        "El último mensaje es de esta tarde. “Saliendo del trabajo. 10 minutos. Ahí te recojo”."
        "Mis dedos flotan sobre el teclado.{w} Tiemblan.{w} O no.{w} Ya no sé distinguir."
        "Escribo:"
        "“Hoy papá... hoy olí”"
        "..."
        "Pausa. Borro “olí”.{w} Vuelvo a escribir."
        "“Hoy papá... hoy en el auto”'"
        "..."
        "Pausa.{w} Borro.{w} Otra vez."
        "“Hoy papá... hoy me sentí”"
        "..."
        "Mis dedos se detienen."
        l_thought "¿Qué quiero decir? ¿Que me sentí viva? ¿Que me sentí rota?"
        l_thought "¿Que me sentí como si ella estuviera ahí, en el asiento de atrás, oliendo el café que él no bebe?"
        "Escribo, finalmente:"
        "“Hoy papá... hoy olí y me sentí... no sé. Casi humana.”"
        "Leo las palabras. Las veo brillar en la pantalla.{w} Tan pequeñas.{w} Tan insuficientes."
        l_thought "“Casi humana”."
        extend "Qué estupidez."
        l_thought "¿Desde cuándo no soy humana? ¿Desde cuándo soy esto que camina, que respira, que finge?"
        "Mi dedo se posa sobre el botón de enviar."
        "..."
        l_thought "No."
        "Borro el mensaje."
        "La pantalla se queda en blanco.{w} El chat está como si nada hubiera pasado."
        "Como si no hubiera estado a punto de decirle algo que no sé si estoy lista para que sepa."
        l_thought "No es el momento. O tal vez nunca lo es."
        l_thought "O tal vez soy una cobarde. O tal vez solo quiero guardar esto para mí. Este momento."
        l_thought "Esta sensación de que algo cambió, aunque no sepa qué."
        "Apoyo el teléfono en la mesita.{w} Queda al lado de la foto.{w} Madre e hija. Pasado y presente.{w} Lo que fui y lo que estoy dejando de ser."
        $ renpy.pause(3.0, hard=True)
        "Abro el cajón.{w} El segundo cajón.{w} El de las cosas que no quiero que nadie vea."
        "Allí están.{w} Las pastillas."
        "No muchas.{w} Las justas."
        "Las que la psicóloga me recetó y que nunca terminé. Las que se suponia que tenia que tomar cuando el ruido es demasiado fuerte. Las que a veces miro y pienso '¿y si…?'."
        "Las que a veces miro y pienso “¿y si…?”."
        "Las saco.{w} Una por una."
        "Las coloco en fila sobre la mesita."
        "1...{w} 2...{w} 3...{w}"
        "La luz de la calle entra por la ventana. Tiembla sobre los comprimidos blancos."
        "4...{w} 5...{w} 6...{w}"
        l_thought "Doce. Siempre doce."
        l_thought "Como las horas del reloj. Como los meses del año."
        l_thought "Como las veces que he querido desaparecer y no lo he hecho."
        "7...{w} 8...{w} 9...{w}"
        "Las miro. Son pequeñas.{w} Inocentes.{w} Parecen inofensivas."
        "10...{w} 11...{w} 12."
        "..."
        "Las guardo.{w} Una por una. De vuelta al frasco.{w} De vuelta al cajón. De vuelta al lugar donde esperan."
        l_thought "Otro día. Otra noche. Otra vez que elijo quedarme."
        "Cierro el cajón.{w} El ruido es seco.{w} Final."
        "Me acuesto. La almohada está fría. Las sábanas huelen a suavizante, a limpio, a algo que intenta ser hogar."
        "La oscuridad me abraza.{w} No es un abrazo asfixiante.{w} Es uno cansado."
        "Como si la noche también estuviera agotada de cargar conmigo."
        "..."
        show parpadeo_on
        l_thought "Casi humana. Eso escribí."
        extend " Y lo borré."
        "Las palabras flotan detrás de mis ojos cerrados."
        l_thought "Pero las sentí. Por un momento, las sentí."
        "Un sollozo.{w} Pequeño.{w} Ahogado."
        "No es de tristeza.{w} No es de rabia.{w} Es de algo que no sé nombrar."
        "Alivio, tal vez."
        "O miedo."
        "O esperanza."
        "Esa cosa frágil que no me atrevo a tocar porque sé que se rompe."
        "..."
        "La lágrima resbala por mi sien.{w} Se pierde en la almohada."
        l_thought "No soy humana. No del todo."
        l_thought "Pero esta noche, por primera vez en mucho tiempo, creo que podría estar aprendiendo."
        $ renpy.pause(6.0, hard=True)
        "La foto en la mesita.{w} Las pastillas guardadas.{w} El mensaje borrado."
        "Pequeñas decisiones.{w} Pequeñas victorias."
        "O pequeñas derrotas."
        "Ya no sé distinguir."
        "Pero sigo aquí."
        "Y esta noche, eso es suficiente."

    else:
        stop ambient fadeout(0.5)
        "El auto se detiene frente a casa. Las luces de la sala están encendidas, pero se ven frías.{w} O tal vez soy yo, que todo lo veo frío desde hace rato."
        "Papá no se mueve.{w} No me mira."
        "El silencio es una losa. Este es diferente.{w} Este es el silencio de dos personas que estuvieron juntas todo el rato y no se encontraron."
        dad "Laila..."
        "Su voz suena cansada. No del trabajo. De mí."
        l "¿Qué?"
        "Papá aprieta la mandíbula. Piensa en algo. Lo descarta."
        dad "Nada. Ya estamos."
        l_thought "“Nada”. Siempre “nada”. Como si todo lo que no se dice cupiera en esa palabra."
        "Papá no baja del auto. Se queda ahí, con las manos en el volante, mirando al frente. Como si la casa no fuera suya."
        "Como si entrar fuera un esfuerzo que ya no tiene fuerzas para hacer."
        "El motor sigue encendido. Un ronroneo bajo, constante.{w} Como un reloj que cuenta los segundos hasta que se vaya."
        l_thought "¿No va a bajar? ¿No va a entrar? ¿No va a...?"
        "Pero no pregunto. Porque ya sé la respuesta."
        dad "Bájate.{w} Tengo que volver al trabajo."
        "Su voz es plana. Un comunicado.{w} No una explicación."
        l_thought "Trabajo. A estas horas. Claro."
        "No lo creo. Él tampoco."
        "Pero ninguno de los dos dice nada."
        play audio open_car_door
        "Bajo del auto. La mochila pesa. Pesan los libros. Pesan las palabras no dichas.{w} Pesan los silencios."
        play audio close_car_door
        "Cierro la puerta. El golpe es sordo, definitivo."
        "El auto no se va de inmediato.{w} Papá se queda ahí un momento más.{w} Sus manos aún en el volante. Su mirada aún al frente."
        l_thought "¿Qué espera? ¿Que me dé la vuelta?"
        l_thought "¿Que le diga algo? ¿Que le ruegue que se quede?"
        "No me doy la vuelta."
        "Camino hacia la puerta de casa. Siento su mirada en mi espalda. O tal vez no.{w} Tal vez ya ni eso."
        "El motor ruge.{w} El auto se aleja."
        "No miro atrás."
        play audio closet_open
        "La puerta de casa se abre.{w} Blaze está en la entrada.{w} Su sonrisa se enciende cuando me ve, pero se apaga igual de rápido cuando nota que estoy sola."
        play ambient int_night fadein(2.0)
        scene livingroom_l
        show blaze 1preocupada:
            center
        with Fade(0.5, 0.5, 0.5)    
        play audio closet_close
        $ renpy.pause(1.9, hard=True)
        show blaze 1preocupadat
        $ enfocar("blaze")
        b "Laila ¿y Papá...?"
        show blaze 1preocupada
        $ normal("blaze")
        l "Se fue."
        "Mi voz es plana. Muerta. Como yo por dentro."
        show blaze 1seria2
        "Blaze mira hacia la calle vacía. Hacia el lugar donde el auto desapareció. Su rostro se tensa."
        show blaze 1seria2t
        $ enfocar("blaze")
        b "¿A dónde?"
        show blaze 1seria2
        $ normal("blaze")
        l "Supuestamente, al trabajo."
        "Una sola verdad."
        show blaze 1compadecer
        "Blaze da un paso hacia mí. Su mano se levanta, como si fuera a tocarme el hombro."
        show blaze 1compadecert
        $ enfocar("blaze")
        b "Laila..."
        show blaze 1preocupada
        $ normal("blaze")
        l "Estoy cansada."
        "No es una excusa. Es la verdad.{w} Estoy tan cansada que las palabras se me quedan en la garganta."
        show blaze 1preocupada:
            asentir
        "Blaze baja la mano. Asiente.{w} Su expresión es la de alguien que quiere ayudar y no sabe cómo."
        show blaze 2preocupadat
        $ enfocar("blaze")
        b "Está bien... si necesitas algo, ya sabes."
        show blaze 2preocupada
        $ normal("blaze")
        l_thought "“Si necesitas algo”. Como si pudiera pedir. Como si supiera cómo."
        "Asiento. No digo nada."
        "Entro.{w} Paso junto a ella sin mirarla.{w} Las escaleras me esperan."
        hide blaze with Dissolve(0.3)
        "Cada escalón es un peso. Un recordatorio de que sigo aquí, en este cuerpo que no me pertenece, en esta casa que ya no es hogar sin él.{w} Sin {i}ella{/i}.{w} Sin nada."
        $ renpy.pause(1.2, hard=True)
        play audio closet_open
        scene lailaroom_n with Fade(0.8, 0.5, 0.8)
        play audio closet_close
        "Llego a mi habitación. Cierro la puerta. Con fuerza. Quiero que el ruido ahogue algo.{w} No sé qué."
        "El golpe resuena en el pasillo. No me importa."
        "Arrojo la mochila al suelo. Golpea la pared con un sonido sordo."
        l_thought "Nada que guardar. Nada que proteger."
        l_thought "Solo el peso de otro día que sobreviví sin saber por qué."
        window hide
        $ renpy.pause(3.0, hard=True)
        window show
        "Busco en el fondo de la mochila.{w} Entre libros, papeles, restos de días que no quiero recordar."
        "Mis dedos encuentran el borde arrugado.{w} Lo saco."
        "La foto."
        "Ella y yo.{w} Madre e hija.{w} Rasgada por la mitad."
        "Falta él.{w} Falta Blaze.{w} Falta todo lo que pudo ser y no fue."
        "La miro.{w} La sostengo con manos que tiemblan."
        l_thought "¿Cuándo la rompí?"
        extend " ¿Ayer?"
        extend " ¿Hace un mes?"
        extend " ¿El día que se fue?"
        extend " No recuerdo. O tal vez sí, pero duele recordar."
        show screen red_effect2
        nobody "{sc=5}Ella se fue.{/sc}"
        nobody "{sc=5}Tú deberías seguirla.{w} Es lo lógico.{/sc}"
        "La voz vuelve. No es una advertencia.{w} Es una orden. Es la única certeza en medio de este caos."
        l_thought "Lo lógico. ¿Qué es lo lógico?"
        l_thought "¿Sobrevivir? ¿Morir? ¿Seguir aquí, respirando, comiendo, fingiendo que todo está bien?"
        "La foto se arruga entre mis dedos.{w} No me importa.{w} Ya está rota."
        hide screen red_effect2 with Dissolve(0.5)
        "Tiro la foto a un lado."
        "Busco papel. Bolígrafo."
        "Los encuentro en el cajón.{w} El mismo cajón donde guardo las pastillas. Donde guardo todo lo que no quiero que nadie vea."
        "Me siento en la cama.{w} Apoyo el papel en la mesita.{w} Escribo."
        l_thought "“Papá, Blaze:”"
        "Mis dedos tiemblan.{w} La letra es torcida, apenas legible."
        l_thought "“Cuando lean esto, ya habré tomado una decisión.”"
        "Pausa.{w} Respiro.{w} El aire entra, pero no llena. Nunca llena."
        l_thought "“No es culpa de nadie.{w} O tal vez sí.{w} Ya no sé.”"
        "Sigo escribiendo. Las palabras salen solas. Como si alguien las dictara."
        " Como si mi mano solo fuera un conducto para algo que llevo dentro desde antes de nacer."
        l_thought "“No quiero que me busquen.{w} No quiero que me recuerden.{w} Solo quiero que me dejen ir.”"
        "Tres párrafos.{w} Los releo."
        "..."
        "Las palabras bailan frente a mis ojos.{w} Son mías.{w} Pero no me pertenecen."
        l_thought "¿Es esto lo que quiero decir? ¿Es esto lo que siento?"
        l_thought "¿O solo es la voz, hablando a través de mí?"
        l_thought "No lo sé."
        "Pero no rompo la hoja."
        "La dejo sobre la mesita.{w} Al lado de la foto rota.{w} Al lado de todo lo que fui."
        window hide
        $ renpy.pause(6.0, hard=True)
        window show
        "Me levanto. Camino hacia la ventana."
        stop ambient fadeout(1.0)
        play ambient ext_night fadein(2.0)
        "La abro. El aire entra, frío, cortante.{w} Huele a ciudad, a domo, a nada."
        "Me asomo."
        "El vacío me mira.{w} No es aterrador. Es...{w} familiar."
        l_thought "¿Cuánto? ¿Cuántos metros? ¿Cuántos segundos de caída?"
        "Cálculo.{w} No con miedo.{w} Con curiosidad."
        "Como quien mira el menú de un restaurante y piensa “qué pediré”."
        show screen red_effect2
        nobody "{sc=6}Solo un paso.{/sc}"
        nobody "{sc=7}Un paso y termina.{/sc}"
        nobody "{sc=8}El ruido.{w} El dolor.{w} La culpa.{w} Todo.{/sc}"
        l_thought "Un paso."
        hide screen red_effect2 with Dissolve(0.5)
        "Mis manos se aferran al marco.{w} Los nudillos blancos.{w} Las uñas clavándose en la madera."
        "Un paso."
        window hide
        $ renpy.pause(6.0, hard=True)
        window show
        "Retrocedo."
        "No porque tenga miedo.{w} No porque quiera vivir."
        "Porque todavía no es el momento."
        "O porque soy una cobarde."
        "Ya no sé distinguir."
        window hide
        $ renpy.pause(6.0, hard=True)
        window show
        stop ambient fadeout(1.0)
        play ambient  int_night fadein(2.0)
        "Cierro la ventana.{w} El ruido del marco encajando es seco.{w} Final."
        "Me acuesto en la cama.{w} Vestida.{w} Sin fuerzas ni para cambiarme."
        "Miro el techo."
        "Las grietas.{w} Las manchas de humedad.{w} Las formas que de niño imaginabas que eran animales y que ahora solo son marcas de que todo se deteriora."
        l_thought "Como yo. Deteriorándome."
        l_thought "Día tras día."
        window hide
        $ renpy.pause(6.0, hard=True)
        window show
        "No lloro."
        "Las lágrimas no vienen.{w} O tal vez se secaron hace tiempo."
        "Solo miro el techo.{w} Y respiro.{w} Y espero."
        "No sé qué."
        "El fin, tal vez."
        "O un milagro."
        "O nada."
        window hide
        $ renpy.pause(6.0, hard=True)
        window show
        "La foto rota y carta escrita sobre la mesita."
        "La ventana cerrada."
        "Yo aquí."
        "Todavía."
        l_thought "Otro día. Otra noche."
        l_thought "Otra vez que no lo hago."
        show screen red_effect2
        nobody "{sc=6}{b}Pero lo harás.{w} Es cuestión de tiempo.{/b}{/sc}"
        l_thought "Lo sé."
        nobody "{sc=8}{b}Y cuando llegue el momento, no dudarás.{/b}{/sc}"
        l_thought "Lo sé."
        hide screen red_effect2 with Dissolve(0.5)
        "La oscuridad me traga."
        "No es un abrazo. Es un pozo."
        "Y yo, en el fondo."
        "Sola."
        "Como siempre."
        "Como siempre será."

    window hide
    stop ambient fadeout(4.5)
    scene black
    $ quick_menu = False
    with dissolve_scene_full3

return