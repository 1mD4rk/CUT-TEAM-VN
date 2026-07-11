# Estilo para los susurros
style susurro_style:
    color "#b0b0b0"
    italic True
    size 24
    outlines [(1, "#000000", 0, 0)]

transform susurro1():
    xpos 0.9 ypos 0.8
    xanchor 0.5 yanchor 0.5
    alpha 0.0
    linear 0.5 alpha 0.6
    pause 3.0
    linear 0.5 alpha 0.0
    repeat

transform susurro2():
    xpos 0.7 ypos 0.3
    xanchor 0.5 yanchor 0.5
    alpha 0.0
    pause 0.8
    linear 0.5 alpha 0.7
    pause 2.5
    linear 0.5 alpha 0.0
    repeat

transform susurro3():
    xpos 0.1 ypos 0.75
    xanchor 0.5 yanchor 0.5
    alpha 0.0
    pause 1.6
    linear 0.4 alpha 0.5
    pause 3.0
    linear 0.4 alpha 0.0
    repeat

transform susurro4():
    xpos 0.8 ypos 0.12
    xanchor 0.5 yanchor 0.5
    alpha 0.0
    pause 2.2
    linear 0.5 alpha 0.6
    pause 2.0
    linear 0.5 alpha 0.0
    repeat

transform susurro5():
    xpos 0.15 ypos 0.45
    xanchor 0.5 yanchor 0.5
    alpha 0.0
    pause 3.0
    linear 0.4 alpha 0.5
    pause 2.5
    linear 0.4 alpha 0.0
    repeat

transform susurro6():
    xpos 0.3 ypos 0.15
    xanchor 0.5 yanchor 0.5
    alpha 0.0
    pause 0.5
    linear 0.4 alpha 0.5
    pause 2.0
    linear 0.4 alpha 0.0
    repeat

transform susurro7():
    xpos 0.6 ypos 0.6
    xanchor 0.5 yanchor 0.5
    alpha 0.0
    pause 1.2
    linear 0.5 alpha 0.6
    pause 3.5
    linear 0.5 alpha 0.0
    repeat

transform susurro8():
    xpos 0.9 ypos 0.5
    xanchor 0.5 yanchor 0.5
    alpha 0.0
    pause 2.5
    linear 0.3 alpha 0.4
    pause 2.8
    linear 0.3 alpha 0.0
    repeat

transform susurro10():
    xpos 0.4 ypos 0.9
    xanchor 0.5 yanchor 0.5
    alpha 0.0
    pause 3.8
    linear 0.4 alpha 0.5
    pause 2.2
    linear 0.4 alpha 0.0
    repeat

transform susurro11():
    xpos 0.2 ypos 0.3
    xanchor 0.5 yanchor 0.5
    alpha 0.0
    pause 1.8
    linear 0.5 alpha 0.6
    pause 3.0
    linear 0.5 alpha 0.0
    repeat

transform susurro12():
    xpos 0.75 ypos 0.08
    xanchor 0.5 yanchor 0.5
    alpha 0.0
    pause 4.2
    linear 0.3 alpha 0.4
    pause 2.5
    linear 0.3 alpha 0.0
    repeat

transform susurro13():
    xpos 0.5 ypos 0.4
    xanchor 0.5 yanchor 0.5
    alpha 0.0
    pause 0.9
    linear 0.5 alpha 0.7
    pause 1.5
    linear 0.5 alpha 0.0
    repeat

transform susurro15():
    xpos 0.05 ypos 0.95
    xanchor 0.5 yanchor 0.5
    alpha 0.0
    pause 3.5
    linear 0.5 alpha 0.4
    pause 2.0
    linear 0.5 alpha 0.0
    repeat

image poem_special = "images/poem_special.png"

screen poem_display():
    button:
        xfill True yfill True
        action Return()
        background None
    
    add "poem_special" at truecenter

image dream_rs = "images/dream_rs.png"

# Pantalla de susurros
screen susurros():
    modal False
    # Susurros originales
    text "{sc=5}No deberías estar aquí{/sc}" at susurro1 style "susurro_style"
    text "{sc=5}¿Crees que ella sabe lo que hizo?{/sc}" at susurro2 style "susurro_style"
    text "{sc=5}Yo no la culparía.{/sc}" at susurro3 style "susurro_style"
    text "{sc=5}Si supiera la verdad...{/sc}" at susurro4 style "susurro_style"
    text "{sc=5}No eres como ella...{/sc}" at susurro5 style "susurro_style"
    text "{sc=5}Te mereces esto.{/sc}" at susurro6 style "susurro_style"
    text "{sc=5}Ella te está mirando.{/sc}" at susurro7 style "susurro_style"
    text "{sc=5}No puedes escapar.{/sc}" at susurro8 style "susurro_style"
    text "{sc=5}¿Por qué no te fuiste?{/sc}" at susurro10 style "susurro_style"
    text "{sc=5}Mentirosa.{/sc}" at susurro11 style "susurro_style"
    text "{sc=5}Es tu culpa.{/sc}" at susurro13 style "susurro_style"
    text "{sc=5}Despierta...{/sc}" at susurro15 style "susurro_style"

label scene1_day3:
    if (rutaCanon-rutaSuicida)>=0:
        $ quick_menu = False
        hide screen phone_button
        scene black
        "Un silencio, es todo lo que escucho y es todo lo que hay."
        $ renpy.pause(6.0, hard=True)
        extend " Sin ninguna iluminación, sin ninguna forma extraña saliendo de mi puerta o de mi ventana que solo es una alucinación."
        $ renpy.pause(6.0, hard=True)
        "De pronto empiezo a escuchar una risa, una suave que se escuchaba a la lejanía, como si el sonido proviniera debajo del mar, no podía distinguirla, pero tampoco sonaba amenazante."
        "Era una risa familiar...{w} Bastante familiar."
        "Mi curiosidad me decía que abriera los ojos, pero me aterraba que fuera otra..."
        "Una pesadilla más del montón, me sentía algo nerviosa por saber que era esta risa...{w} De repente escucho un sonido crujir."
        "No es el sonido de madera que tiene el suelo de mi habitación, pero tampoco era de alguien caminando sobre ella.{w} Sentí como mi cuerpo se levantaba lentamente, de algún modo ya estaba de pie sin darme cuenta."
        "Pude escuchar lo que parecía estar pisando, pero me negaba a abrir los ojos aun, después llegó un olor, a tierra mojada, a pasto recién cortado..."
        "Veo que de repente que la oscuridad empieza a desaparecer, aclarando mi vista lentamente, como si alguien estuviera limpiando el vidrio sucio del otro lado, obligándome a observar ahora."
        window hide
        play ambient ext_day fadein(1.5)
        scene garden with Dissolve(3.0)
        window show
        "Primero aparecieron colores sin forma.{w} Verdes.{w} Amarillos.{w} Manchas de luz."
        "Después, los sonidos empezaron a aclarar, el canto de ciertas aves, el viento mover las hojas, estaba claro que ya no estaba en mi habitación."
        l "¿Q-que hago—{nw=0.2}"
        "Antes de que pudiera terminar mi frase, una voz empezó a resaltar, captando mi mirada instantáneamente, mirando a una niña."
        "A mi misma."
        l_child "¡Mamá! ¡Mira! Encontré estas flores en el jardín."
        "Ella se rie suave, cálida."
        mom "¿En serio? Me alegro mucho, mi amor...{w} ¡Deberíamos ponerlas en agua antes de que se m{size=30}a{/size}{size=27}r{/size}{size=24}c{/size}{size=21}h{/size}{size=18}i{/size}{size=15}t{/size}{size=12}e{/size}{size=9}n{/size}"
        "La voz se estira.{w} Se vuelve elástica.{w} Las últimas sílabas se deforman, como si pasaran por un aparato mal sintonizado."
        l "¿Antes de que...?"
        show garden:
            matrixcolor SaturationMatrix(0.0)
        with Dissolve(0.5)
        "El jardín pierde color de golpe."
        "Los verdes se apagan como luces viejas, los pétalos se desprenden y caen... pero no llegan al suelo. Se deshacen en polvo antes de tocarlo."    
        scene black
        stop ambient 
        $ renpy.pause(6.0, hard=True)
        scene house_dream with Dissolve(3.0)
        play ambient int_night fadein(1.5)
        window show
        "Ahora estoy dentro de una casa.{w} La reconozco al instante."
        "Y, al mismo tiempo, no recuerdo haber estado aquí nunca. La sala de—{nw=0.3}"
        l "¿Qué...?{w} ¿Qué hago aquí?"
        "Al fondo del pasillo, una puerta entreabierta."
        show screen susurros
        with Dissolve(0.3)
        "De su interior se filtran murmullos, frases incompletas, palabras sin principio ni final."
        "No las entiendo. Pero sé que hablan de mí."
        window hide
        $ renpy.pause(6.0, hard=True)
        window show
        "Sin tener muchas opciones, empiezo a caminar, mis pies no hacen ruido sobre las tablas de madera."
        "El silencio es total, salvo por un zumbido lejano, constante, como estática de radio metida dentro del cráneo."
        hide screen susurros
        with Dissolve(0.3)
        scene black with Dissolve(1.5)
        "La puerta cede con un chirrido apenas audible."
        "Una figura está sentada de espaldas, inclinada sobre un escritorio mientras escribía.{w} La postura es familiar.{w} Demasiado familiar."
        "Pero algo está... mal alineado.{w} Como una imagen desplazada unos centímetros fuera de su lugar."
        l_child "¡Mami! ¿Qué estás escribiendo? ¡Estás muy concentrada!"
        mother "Oh... Nada especial, hija mía.{w} Solo es un poema..."
        "Es su voz.{w} Pero no suena como ella."
        "No tiene ese ritmo, ese calor, solo es una grabación que aprendió a hablar idéntica a ella."
        l_child "¿Y eso es algo malo?"
        mother "Oh... C-Claro que no.{w} Solo... Me dio nostalgia."
        l_child "¿¡Lo puedo leer?!"
        "La niña en mi memoria salta, pero nunca se completa.{w} su cuerpo queda suspendido en el aire, congelado a mitad del impulso, no cae, ni se mueve."
        "La figura se levanta.{w} Gira lentamente.{w} No hay rostro, solo un borrón inestable donde deberían estar sus ojos, la boca, la sonrisa."
        "Se acerca.{w} No camina, se desliza.{w} Se detiene frente a mí, no frente a la niña. A mí."
        "Extiende una mano. En ella, una hoja de papel doblada."
        mom "C-Claro...{w} Ten..."
        "Intento mover mis brazos.{w} Pesan como plomo.{w} Mis dedos se niegan a extenderse."
        l "¿Q-Qué?{w} ¿Por qué tengo que leerlo yo?"
        play audio pageflip
        window hide
        show poem_special at truecenter with Dissolve(0.3)
        call screen poem_display 
        hide poem_special with Dissolve(0.3)
        window show
        mom "¿Por qué...{w} no...{w} me...{w} protegiste?"
        "La voz ya no sale de la figura, de las paredes, del techo, dentro de mi pecho."
        mom "Confié en ti."
        "La palabra se multiplica.{w} Rebota.{w} Se superpone."
        
        while contador < 30:
            pause 0.1
            centered "{sc=7}{b}FALLASTE.{/b}{sc}{nw}" 
            $ contador += 1

            # Cuando llega al latido 4, deja la viñeta fija
            if contador == 2: 
                show vignette at vineta_organico zorder 100
                $ renpy.music.play("heartbeat.ogg", channel="heartbeat")

        $ renpy.music.stop(channel="heartbeat")
        stop ambient
        scene lailaroom_d
        $ quick_menu = True
        show screen phone_button
        play ambient int_day fadein(2.0)
        "—Me despierto con un sollozo ahogado."
        "No es un sobresalto violento.{w} Es una ruptura suave."
        "Cómo emerger a la superficie después de haber contenido la respiración demasiado tiempo."
        "Lágrimas.{w} Calientes, silenciosas, recorren mis sienes y se pierden en la almohada."
        "Temblor.{w} Un estremecimiento leve recorre mis brazos."
        "Vacío.{w} Un hueco familiar y pesado en el pecho."
        "Mi mano derecha está extendida hacia el costado de la cama, como si hubiera estado buscando a alguien en el sueño."
        $ renpy.pause(2.0, hard=True)
        "Me siento lentamente. La habitación está en penumbra, la luz del amanecer pintando las paredes."
        "Toco mi garganta. No hay marcas.{w} Solo piel intacta, fría."
        l_thought "Solo un sueño..."
        "Pero las palabras PERDÓN-CULPA-ADIÓS flotan detrás de mis ojos, nítidas, escritas con esa caligrafía torcida que reconocería en cualquier lugar."
        "Respiro hondo.{w} El aire entra fresco, limpio. Demasiado puro para cómo me siento por dentro."
        "Miro el reloj: 6:42. La mañana ha llegado puntual, indiferente a mis fantasmas."
        "Suspiro.{w} Un sonido cansado pero resignado.{w} No es el primer sueño así.{w} No será el último."
        l_thought "Fallaste..."
        "La palabra resuena, pero hoy no duele como un cuchillo.{w} Duele como un moretón antiguo, algo que ya conozco, algo que ya acepté como parte de mí."
        "Me levanto. El suelo está frío, pero no helado. Solo madera de mañana."
        "Voy hacia el espejo del armario. No me molesto en encender la luz."
        "Me veo. Ojeras, sí.{w} Pelo revuelto, sí."
        "Pero hoy no pregunto “¿quién eres?”.{w} Hoy solo asiento."
        "Esta soy yo.{w} La que sobrevivió otra noche. La que cargó el sueño y despertó igual."
        l_thought "Ella... ¿Qué quería que entendiera? ¿Tengo que entender algo?"
        "No hay respuesta.{w} Solo mi reflejo, y la certeza de que hoy tendré que seguir adelante, con o sin respuestas."

    else:
        window hide
        $ quick_menu = False
        hide screen phone_button
        scene black
        $ renpy.pause(6.0, hard=True)
        scene lailaroom_dream with Dissolve(3.0)
        play ambient int_night fadein(1.5)
        window show
        "No despierto. O sí. No sé."
        "Mi pecho sube. Pero no lo siento. Estoy en mi habitación. Creo."
        "La cama está donde debería. La ventana también. Pero todo está… ligeramente corrido. Como si alguien hubiera armado este lugar sin haber estado nunca aquí."
        l_thought "¿Q-Qué hora es?"
        $ renpy.music.play("heartbeat.ogg", channel="heartbeat")
        "El reloj. {b}3:07 AM{/b}."
        "No hay segundero. No hay tiempo.{w} Solo esa hora."
        "Clavada eternamente..."
        play audio toc1
        "No vino de la puerta.{w} Vino de..."
        "Atrás."
        "Pero no hay nada atrás. Solo mi pared."
        "Mi cuerpo no se mueve.{w} No es porque no quiera sino porque ya no responde igual."
        "Trato de tragar saliva pero no puedo, algo aprieta desde adentro de mi cuerpo, impidiendo que lo pueda hacer."
        play audio toc2
        "Ahora el sonido viene de la puerta.{w} MI puerta, pero el sonido viene con retraso. Primero lo siento y Luego lo escucho."
        l_thought "..."
        l_thought "No abras."
        "No lo dije. Pero algo en mí lo pensó antes que yo."
        play audio flesh_background volume 0.4 fadein(1.5) loop
        "Mi mirada se clavó a la ventana y lo único que podía observar era un cielo negro, no el de un vacío, el de una gran densidad como de carne sin forma."
        "Podía escuchar un latido... un latido muy leve de alguna parte de la habitación, no podía distinguir si se trataba del mío o del sueño en sí."
        "Ahora lo que escuchaba no es un golpe, son uñas.{w} Arrastrándose."
        "Pero no sobre madera. Sobre algo...{w} más blando."
        l_thought "..."
        l_thought "No es la puerta."
        "No... No es. Es más cerca...{w} Mucho más cerca."
        show vignette at vineta_organico zorder 100
        "Mi respiración empieza a fallar no porque tuviera miedo, sino porque alguien más está usando mi ritmo, está imitándome."
        "La manija gira.{w} Escucho el metal.{w} Pero lo siento en los dientes."
        "La puerta se abre y miraba lo mismo que en mi ventana, Oscuridad."
        "No... no era solo eso..."
        "Algo está ocupando la oscuridad...{w} Demasiado grande y no cabe ahí.{w} Y aun así está."
        $ renpy.pause(6.0, hard=True)

        menu:
            "Despertar":
                pass 

        show parpadeo_on
        "Me obligo a cerrar los ojos."
        "Si no veo, no existe."
        "Si no escucho, no es real."
        "Pero detrás de mis párpados, las sombras se mueven, pero mi curiosidad hace que las abra de nuevo..."
        "Mi cuerpo reacciona, antes que mi mente, dándome un tirón.{w} Un microespasmo en el cuello.{w} Es como si— reconociera algo."
        $ renpy.pause(6.0, hard=True)
        mother "Laila..."
        "No. No. Esa voz—{w} No es ella. Pero—{nw=0.2}"
        "Mi estómago se hunde igual."
        mother "Mirame..."
        "No quiero.{w} No puedo...{w} Mis ojos... se mueven solos hacia la puerta."
        show dream_rs with dissolve
        hide parpadeo_on
        "Ni siquiera soy capaz de reconocer lo que veo, ni una cara."
        hide parpadeo_off
        "Mi cerebro en serio intenta construirla. Una y otra vez como si buscara en una base de datos al fugitivo más buscado de la historia pero falla sin parar."
        "Pero solo puedo ver qué tiene Ojos en lugares incorrectos, una boca que no coincide en absoluto con algo común, y su piel...{w} que está abierta."
        "No. ¡NO! No la estoy viendo.{w} Estoy recordando mal."
        l_thought "¡YO SÉ QUE ELLA NO ES ASÍ!"
        l_thought "ENTONCES ¿POR QUÉ NO PUEDO—{nw=0.3}"
        mother "Tanto tiempo..."
        "La voz de esa cosa se quiebra constantemente. No emocional, sino estructural.{w} Como si no supiera mantenerse estable."
        mother "Y...{w} Sigues igual de..."
        "Mi brazo tiembla."
        "Trato de levantarlo con mucho esfuerzo pero mi cuerpo no es capaz de poder coordinarlo correctamente, estoy inmóvil por completo a lo que creí tener movilidad."
        "Una mano emerge de la oscuridad."
        "Una mano pálida, sin carne y con un movimiento antinatural y torpe se acercaba a mi rostro, posándose suavemente en mi mejilla."
        "Y mi cuerpo entra en alerta máxima pero se congela aún más de lo debido."
        "Es como si ya hubiera aprendido la lección...{w} De que no tiene caso tratar de luchar."
        mother "Cansada."
        "La palabra se alarga demasiado como si disfrutara."
        mother "Yo también..."
        "Algo se mueve dentro de la oscuridad."
        "No sale, solo se reacomoda, y se escuchaban los crujidos de algo ajustándose, algo que tronaban de manera visceral, podía intuir que eran huesos..."
        "Huesos que no encajan en ese cuerpo que apenas podía visualizar..."
        "Sale de la propia oscuridad un brazo y uno demasiado largo, se despliega mal.{w} Luego se corrige."
        "Esa cosa quiere parecer humano y fallaba estrepitosamente... pero aun así—"
        "Mi cuerpo lo reconoce y por instinto mi garganta se cierra por respuesta."
        mother "Ven."
        "Veo mi mano moverse, pero no por mi acción, sino que algo lo levanta por mí."
        "Mis dedos tiemblan frenéticamente, no sabía lo que estaba por suceder, solo estaba rezando que esto acabara pronto, que ese sueño estaba convirtiéndose en una verdadera pesadilla."
        "Mis dedos se abren y se colocan—{w} en mi cuello."
        mother "Asi."
        "La voz que me hablaba con ese tono cariñoso se acercaba lentamente desde dentro, siendo igual como si fuera esa voz que escucho todos los días hecha en esa forma."
        mother "No duele."
        show black with Dissolve(0.3):
            alpha 0.5
        "Siento que ejerce una presión, una ligera que apretaba mi garganta"
        show black:
            alpha 0.6
        mother "No pesa."
        show black:
            alpha 0.7
        "Que poco a poco se hacía más fuerte, empezando a cortar un poco mi oxígeno, mis uñas se clavan conforme a la presión que ejercía sintiendo como la piel ya empezó a ceder."
        show black:
            alpha 0.8
        mother "No tienes que seguir."
        "Mi cuerpo ahora tiembla sin parar, no resisto."
        "No quiero resistirme a esto, porque ya dentro, siento que ese deseo me carcome por dentro cada vez más, el acabarlo, pero no es por eso simplemente, sino porque se siente familiar."
        "Demasiado familiar."
        show black:
            alpha 0.9
        mother "Déjame ayudarte."
        "Mi otra mano sube, no debería hacerlo pero lo hace y lo hace uniéndose a mis dos manos, apretando con mucha fuerza, mi visión se rompe..."
        show black:
            alpha 1.0
        "Fragmentándose y oscureciéndose rápidamente, solo sé que lo último que estaba por ver era la habitación, la puerta y por un segundo— veo algo inclinado encima de mí"
        "Demasiado cerca, observándome detalladamente, aprendiendo cómo mi cuerpo está cediendo a suicidarme con sus propias palabras, solo antes de que perdiera la propia consciencia, lo veo..."
        "Sonriendo de punta a punta...{w} mientras me dice algo que no logro escuchar por completo..."
        $ renpy.pause(6.0, hard=True)
        "¡NO!"
        $ renpy.music.stop(channel="heartbeat")
        stop audio
        stop ambient
        scene lailaroom_d
        $ quick_menu = True
        show screen phone_button
        play ambient int_day fadein(2.0)
        "El aire no entra, ni tampoco salí del sueño, el sueño realmente nunca acabó, solo me veo a mí misma sentada, en mi cama JADEANDO mientras siento mis manos"
        "{b}SIGUEN{/b} en mi cuello."
        "{b}APRETANDO{/b} cada vez más."
        "ARRANCO los dedos tarde.{w} Muy tarde, por fin recuperando el aire que se estaba perdiendo por completo."
        "El dolor llega después, de forma violenta y sin espera, dejándome marcas… profundas e irregulares, y empiezo a sentir algo que recorre mi cuello..."
        "Sangre.{w} es sangre {b}REAL{/b}."
        "Se escurre y baja por mi piel lentamente, sintiendo un ardor increíble que jamás llegué a imaginar sentir, solo me limito a voltearme y ver mi propio reflejo en el espejo."
        "Simplemente no quiero mirarme, pero ya estoy ahí... Pero veo algo en mi reflejo, medio segundo fue suficiente para verlo."
        "Algo estaba detrás de mí, demasiado cerca... Parpadeo varias veces para ver si lo que veo no es una alucinación, pero ya no hay nada..."
        l_thought "¿Mamá...?"
        window hide
        $ renpy.pause(6.0, hard=True)
        window show
        "Silencio...{w} Esa palabra— Ya no se siente correcta, ya dejó de no encajar aquí."
        "Miro el reloj de mi mesa de noche y veo: {b}6:42 AM{/b}."
        "Por un momento me emocioné, creí que realmente sí fue un mal sueño...{w} Pero no."
        "Las {b}3:07 AM{/b} siguen aquí."
        "Mi mano toca el cuello y siento dolor, solo por un segundo, me calmo."
        $ renpy.pause(3.0, hard=True)
        l_thought "Porque significa que aún sigo siendo yo."
        $ renpy.pause(3.0, hard=True)
        l_thought "¿Verdad?"
        $ renpy.pause(3.0, hard=True)
        "Para cuando volteo realmente el reloj dice 6:42 AM.{w} Ya estaba despierta por completo..."
        "No podía volver a dormirme porque si lo hacía, tendría que verme obligada a obedecer a mi padre a madrugar nuevamente."
    
    "Suspiro.{w} Ya agotada apenas me despierto."
    l "Espero..."
    extend " Espero que no sea nada malo lo que haya soñado."
    "Digo eso con un murmullo áspero, sin esperanza. Sin aferrarme a nada."
    "Pero es mentira. {b}Sé{/b} con quién soñé. Y lo peor no es que fuera malo."
    "Lo peor es que, en algún rincón retorcido, {b}no estoy segura de querer que fuera solo un sueño.{/b}"
    "Siento un escalofrío recorrer mi espalda."
    $ renpy.pause(6.0, hard=True)
    "Me levanto.{w} Tambaleo un poco pero me logro equilibrar."
    "La madera del piso está fría, demasiado fría para una mañana cualquiera."
    extend " O tal vez solo soy yo, todavía helada por dentro."
    "Salgo de mi habitación"
    stop ambient fadeout(0.2)
    scene black with Fade(0.3, 0.3, 0.3)
    $ renpy.pause(0.9, hard=True)
    extend " y me dirijo hacia el baño.{w} Específicamente hacia el espejo."
    play audio closet_open
    scene bathroom with Fade(0.3, 0.3, 0.3)
    "Entro, no me molesto en encender la luz. Voy hacia el espejo."
    "Prefiero la penumbra de la mañana a la crudeza de los focos."
    $ renpy.pause(0.9, hard=True)
    "Me miro."
    "Ojeras moradas como moretones.{w} Pelo revuelto, enredado en sí mismo."
    "Labios partidos.{w} Ojos rojos, no de llanto, sino de no haber dormido en realidad."
    l_thought "¿Quién mierda eres?"
    "La pregunta no es retórica. La pregunto en serio."
    "La persona en el reflejo parece un extraño.{w} Una versión gastada, desteñida de alguien que alguna vez fui."

    if (rutaCanon-rutaSuicida)>=0:
        "Mis dedos tocan el vidrio frío.{w} Sigo las líneas de mis ojos, la curva de mi boca."
        $ renpy.pause(1.0, hard=True)
        "La recuerdo, con nostalgia."
        l_thought "¿Esta es la persona que dejaste atrás?"
    else:
        "Mis dedos tocan el vidrio frío.{w} Presionan el vidrio hasta que duele.{w} Quiero romperlo."
        "Quiero romper este reflejo falso, esta imitación patética."
        l_thought "Deberías haberte ido con ella. Al menos allí serías útil."

    $ renpy.pause(1.0, hard=True)
    "Un sonido abajo. Platos. Huele a café."
    "Papá está en la cocina."

    if (rutaCanon-rutaSuicida)>=0:
        "Trago saliva."
    else:
        "Trago saliva. La garganta aún duele por el jadeo, por las marcas."

    "Me lavo la cara rápidamente"
    scene black with Fade(0.3, 0.3, 0.3)
    extend " y salgo del baño y bajo las escaleras lentamente, como si cada escalón fuera un obstáculo."

    $ renpy.pause(1.0, hard=True)
    play ambient int_day fadein(2.0)
    scene kitchen with Fade(0.5, 0.5, 0.5)
    show counter 1distraido with dissolve:
        center
    $ renpy.pause(0.8, hard=True)
    show counter 1surprise:
        boo
    "Al verme, asiente brevemente. No sonríe, pero su mirada es menos dura que de costumbre."
    show counter 1surpriset
    $ enfocar("counter")
    dad "Laila. Buenos días."
    show counter 1surprise
    $ normal("counter")
    "Asiento, pero no confío en su voz."
    show counter 1surpriset
    $ enfocar("counter")
    dad "Hay café."
    show counter 1distraido
    $ normal("counter")
    $ renpy.pause(1.5, hard=True)
    show counter 1surpriset
    $ enfocar("counter")
    dad "Tu madre...{w} siempre decía que un día difícil empieza mejor con las manos calientes."
    show counter 1compadecer
    $ normal("counter")
    "Empuja la otra taza hacia el espacio vacío. Un gesto incómodo, pero genuino."

    menu (time=5, timeout='rutasuicida_nochoice3'):
        l_thought "Tomar la taza..."

        "Aceptar la taza de café.":
            $ rutaCanon += 4
            "Mis dedos dudan. La taza está ahí. Caliente. Esperando."
            "Un segundo pasa.{w} Dos.{w} Tres."

        "No la aceptaré.":
            $ rutaSuicida += 7
            "Mis dedos no se mueven hacia la taza. Flotan en el aire, indecisos."
            "Hasta que finalmente aparto la taza con un movimiento brusco."

    if (rutaCanon-rutaSuicida)>=0:
        call rutacanon_choice3 from _call_rutacanon_choice3
    else:
        call rutasuicida_choice3 from _call_rutasuicida_choice3

    jump afterchoice_day3
    return

    label afterchoice_day3:
        "Me quedo en la cocina, la taza como testigo mudo entre nosotros."
        l_thought "Blaze..."
        extend " ¿Ya se habrá ido?"
        scene black with fade
        "Subo las escaleras, cada escalón un esfuerzo."
        $ renpy.pause(1.0, hard=True)
        "Su puerta está cerrada. La mía, abierta, mostrando el desorden de mi sueño interrumpido."
        $ renpy.pause(2.0, hard=True)
        "Me visto con movimientos automáticos.{w} Jeans, camiseta, suéter—el mismo de ayer, y anteayer."
        "No importa. Nada importa realmente.{w} Lo que hice fue solo ponerme una muda nueva de ropa. Ya que dormí con esa."
        $ renpy.pause(3.0, hard=True)
        "Al salir de mi habitación, la puerta de Blaze se abre."
        "Aparece, ya lista, con una mochila al hombro y una expresión que no logro descifrar."
        b "¿Lista?"

        if (rutaCanon-rutaSuicida)>=0:
            "Sus ojos buscan los míos y encuentran algo—no fuerza, pero sí una ausencia de la habitual resistencia.{w} Es suficiente."
            "Asiento. Un movimiento pequeño pero que se siente como el primer paso consciente que doy hoy.{w} Mis dedos se ajustan a la correa de la mochila."
            "La casa huele a café y a promesas rotas. Y salimos."

        else:
            "Ella mira mi cuello donde las marcas deberían estar, pero no pregunta. Su silencio es otra forma de cuidado, o de rendición."
            "Su mirada es un escáner:"
            "Pasa de mis ojos hundidos a mis manos temblorosas, se detiene en mi cuello, calcula el daño, y decide que el costo de preguntar es demasiado alto."
            "Asiento.{w} Un movimiento mecánico de alguien que sigue programado para funcionar."
            "Ella da media vuelta sin esperar confirmación. Baja el primer escalón."
            "Bajamos en silencio. Evito mirar la cocina. Hacia el desastre que hice..."
            "La casa huele a café y a promesas rotas.{w} Y salimos."
        
        play audio closet_open
        stop ambient fadeout(1.5)
        $ renpy.pause(1.7, hard=True)
        play ambient ext_day fadein(2.0)
        show out_house_d
        show blaze 1desinteresada3:
            flip
            center
        with fade
        play audio closet_close
        "Las aceras están casi vacías a esta hora. Solo algunos vecinos apresurados, carteros con sus mochilas brillantes, y el ocasional corredor matutino que pasa como un fantasma entre la niebla baja."
        "Empezamos a caminar hacia la parada del bus."
        show blaze 1desinteresada3: 
            walking_ab_normal

        if (rutaCanon-rutaSuicida)>=0:
            l_thought "Quince minutos."
            extend " Quince minutos donde lo único que tengo que hacer es poner un pie delante del otro."
            "Blaze mira hacia adelante, pero de vez en cuando su mirada se desliza hacia mí."
            "No con esa intensidad ansiosa de otros días.{w} Hoy es más...{w} observadora.{w} Como si estuviera midiendo algo."
            $ renpy.pause(4.0, hard=True)
            show blaze 1desinteresada3:
                flip
                center
            "Llegamos a la parada.{w} El banco de metal está húmedo."
            "Ella es la primera en sentarse. Me siento a su lado.{w} El frío del metal, se siente real, no metafórico."
            l_thought "Normal. Esto es lo más cerca de normal que he estado en semanas."
            l_thought "Sentarme en una parada de bus, esperando. Respirar. Existir sin que duela cada célula."
            "Un pájaro se posa en el cable de enfrente.{w} Canta algo corto, desafinado."
            show blaze 1sonriente
            extend " Blaze sonríe un poco, sin mirarme."
            show blaze 1sonrientet
            $ enfocar("blaze")
            b "¿No te sorprende que hayan pájaros en un domo?"
            show blaze 1sonriente
            $ normal("blaze")
            l "Es raro."
            show blaze 1sonrientet
            $ enfocar("blaze")
            b "Es realmente sorprendente.{w} A veces."
            show blaze 1sonriente
            $ normal("blaze")
            $ renpy.pause(1.8, hard=True)
            show blaze 1neutralt
            $ enfocar("blaze")
            b "Los días siempre empiezan..."
            extend " Igual. Por así decirlo."
            show blaze 1neutral
            $ normal("blaze")
            l "Sí...{w} Supongo que sí."
            $ renpy.pause(1.8, hard=True)
            show blaze 1sonrientet
            $ enfocar("blaze")
            b "Pero terminan siendo diferentes.{w} A veces."
            show blaze 1sonriente
            $ normal("blaze")
            "No es una afirmación. Es una posibilidad."
            "La deja flotando en el aire entre nosotros, como el vapor de nuestro aliento en el frío."
            "A lo lejos, se ve el bus acercarse. Las luces amarillas parpadean sin nada especial."
            "{b}“Fallaste.”{/b}"
            "La palabra del sueño vuelve, pero hoy no es un martillo.{w} Es un eco lejano. Como algo que ya pasó, no algo que esté por venir."

        else:
            "Mis pies arrastran por la acera. Cada paso es un esfuerzo consciente.{w} La mochila pesa el doble hoy. O quizás soy yo la que pesa la mitad."
            l_thought "Quince minutos."
            extend " Quince minutos de prueba de que sigo respirando. Quince minutos donde cada inhalación es un recordatorio:"
            extend "  todavía estoy aquí. Todavía."
            "Pasamos frente a una cafetería. La gente dentro se ríe, sostiene tazas humeantes, vive vidas completas y ajenas.{w} Una mujer mira por la ventana y nuestros ojos se encuentran un instante. Ella aparta la vista primero."
            l_thought "Incluso los extraños saben que sobro."
            $ renpy.pause(4.0, hard=True)
            show blaze 1desinteresada3:
                flip
                center
            "Llegamos a la parada. El banco tiene graffiti—nombres tachados, declaraciones de amor que se descascaran, un dibujo torpe de un pájaro con las alas rotas."
            "Me siento directamente sobre el concreto frío, apoyando la espalda contra el poste de metal."
            "Blaze se queda de pie. No se sienta."
            "Mira hacia la dirección de donde vendrá el bus como si pudiera acelerarlo con la fuerza de su deseo de no estar aquí."
            l_thought "Normal. Qué palabra tan vacía. Qué concepto tan ajeno. Yo no soy normal."
            l_thought "Soy el error en el sistema, el glitch en la matriz, la sombra que se niega a desaparecer cuando encienden la luz."
            "Un auto pasa a toda velocidad, salpicando agua sucia de la acera.{w} Ni siquiera me muevo. Deja que me moje los zapatos. Deja que el frío penetre.{w} Es lo que merezco."
            show blaze 1desinteresada3t
            $ enfocar("blaze")
            b "Va tarde."
            show blaze 1desinteresada3
            $ normal("blaze")
            l "Como siempre."
            "Mi voz es un susurro áspero."
            show blaze 1desinteresada3t
            $ enfocar("blaze")
            b "Sí.{w} Como siempre."
            show blaze 1desinteresada3
            $ normal("blaze")
            window hide
            $ renpy.pause(4.0, hard=True)
            window show
            "El “como siempre” cuelga entre nosotros, cargado de todos los “siempre” que nos han traído hasta aquí."
            "Los desayunos en silencio.{w} Las puertas cerradas.{w} Las promesas rotas antes de hacerse."
            "A lo lejos, las luces del bus son dos ojos amarillos y enfermos que se abren paso a través de la niebla."
            l_thought "“Ven.” La invitación del sueño es un zumbido en mis huesos."
            l_thought "No es una voz ahora. Es un impulso. Un tirón hacia el borde de la acera cada vez que un auto pasa."
            show screen red_effect2
            nobody "{sc=4}Solo un paso.{w} Solo un empujón.{w} Solo un descuido.{/sc}"
            hide screen red_effect2 with Dissolve(0.5)
            $ renpy.pause(0.8, hard=True)
            show parpadeo_on
            "Cierro los ojos."
            $ renpy.pause(4.0, hard=True)
            show blaze 1seria
            show parpadeo_off
            hide parpadeo_on
            "Cuando los abro, Blaze está mirándome. No mi cuello esta vez. Mis ojos."
            show blaze 1seriat
            $ enfocar("blaze")
            b "El bus."
            show blaze 1seria
            $ normal("blaze")
            "Subimos. Ella primero. Yo después.{w} Como siempre." 
return