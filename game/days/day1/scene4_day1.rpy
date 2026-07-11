label scene4_day1:
     
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
    $ quick_menu = False

return