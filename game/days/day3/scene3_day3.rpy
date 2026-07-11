label scene3_day3:

    scene class3A with dissolve_scene_full2
    window show

    if (rutaCanon-rutaSuicida)>=0:
        "Estamos en clases, específicamente, {i}matemáticas{/i}."
        "Una de las clases más insufribles que hay en esta preparatoria... Quizás sea una opinión {i}muy{/i} popular."
        "Veo los clásicos pizarrones holográficos que parpadea de vez en cuando."
        "El profesor escribe “x² + y² = r²” por décima vez, como si esperara que la repetición creara comprensión por ósmosis."
        "Miro los números pero solo veo como bailan, se mezclan, forman patrones que no significan nada."
        l_thought "“x + y = z” podría ser “dolor + tiempo = olvido” e igual tendría sentido. Realmente ya no entiendo nada de lo que está allí."
        $ renpy.pause(3.0, hard=True)
        l_thought "Sólo agradezco que se escriba automáticamente en mi cuaderno..."
        extend " No tengo ni ganas de copiar toda esa mierda."
        $ renpy.pause(3.0, hard=True)
        play music bgm8
        queue music bgm82
        show dark 1distraido with Dissolve(0.5):
            left    
        $ renpy.pause(2.5, hard=True)
        show dark 1juzga2
        $ renpy.pause(2.0, hard=True)
        show dark 1metiche
        $ renpy.pause(1.5, hard=True)
        show dark 1juzgat
        $ enfocar("dark")
        d "¿Alguna vez te has preguntado si “x” y “y” están en una relación tóxica y “r” es el terapeuta que cobra por hora?"
        show dark 1desafiante
        $ normal("dark")
        "Lo dice susurrando desde el asiento de atrás, lo suficientemente bajo para que solo nosotros lo escuchemos."
        "No me volteo, pero un músculo de su mandíbula se tensa.{w} ¿Es enojo?{w} ¿O es el impulso de reírme de algo que no tiene gracia?"
        show blaze 1seria with Dissolve(0.5):
            center2
        "Blaze se voltea ligeramente, en su mirada mostrando advertencia."
        show blaze 1desinteresadat
        $ enfocar("blaze")
        b "Dark, cállate.{w} No quiero otro sermón sobre el “ejemplo del Vicepresidente”."
        $ normal("blaze")
        show blaze 1desinteresada
        "Eso último lo pone entre comillas."
        show jeremy 1serio with Dissolve(0.5):
            flip
            right5
        $ renpy.pause(1.5, hard=True)
        show jeremy 1seriot
        $ enfocar("jeremy")
        je "Silencio. No dramático."
        show jeremy 1serio
        $ normal("jeremy")
        "No levanta la vista de su cuaderno, su voz es baja pero clara."
        show dark 1metiche
        $ renpy.pause(2.5, hard=True)
        prandom "Señor Larssen, si tiene aportes sobre las relaciones entre variables, le invito a compartirlos con la clase."
        show dark 1juzga
        l_thought "¿Señor..."
        extend " {i}Larssen?{i}"
        "No termina de encajar con la imagen que tengo de él.{w} “Larssen” suena a herencia, a tradición, a algo que le queda grande.{w} O quizás solo es mi cabeza, buscando significados donde no los hay."
        "Al profesor el “Larssen” sale de su boca como una advertencia, no como un nombre."
        show dark 1sarcasmot
        $ enfocar("dark")
        d "Solo decía que la circunferencia es el círculo vicioso de la geometría, profesor."
        show dark 1sarcasmo
        $ normal("dark")
        "Su voz normal, fingiendo inocencia."
        show blaze 1preocupadat
        $ enfocar("blaze")
        b "Dark, por favor. No otra vez.{w} Ya tienes una advertencia esta semana."
        $ normal("blaze")
        show blaze 1preocupada
        show jeremy 2serio2t
        $ enfocar("jeremy")
        je "Dark, por favor callar. No queremos otro regaño. No hoy."
        show jeremy 2serio
        $ normal("jeremy")
        "Dark hace una mueca de derrota fingida."
        show dark 1sarcasmot
        $ enfocar("dark")
        d "Ustedes dos son el freno de mano de mi creatividad matemática."
        show dark 1sarcasmo
        $ normal("dark")
        prandom "Sus aportes filosóficos son tan recurrentes como las ecuaciones que no resuelve, Señor Larssen."
        prandom "Silencio o dirección. Elija."
        show dark 1juzga2
        show blaze 1desinteresada
        show jeremy 1serio2
        l_thought "Suponiendo que ese es su apellido... Es muy..."
        extend " Ni sé como describirlo."
        show dark 1sarcasmo:
            xpos 400 ypos 1080
            xanchor 0.5 yanchor 1.0
            yoffset 0
            easein 0.6 yoffset 8
            pause 0.3
            easeout 1.0 yoffset 0
            easein 0.1 yoffset 1
            easeout 0.1 yoffset 0
        "Dark asiente con solemnidad exagerada..."
        show dark 1neutral
        "Pero justo antes de bajar la cabeza, sus ojos encuentran los míos. No sonríe. No guiña." 
        "Solo sostiene la mirada un segundo de más, como diciendo “sé que estás aquí”.{w} Es un reconocimiento, no una broma."
        l_thought "Este idiota..."
        l_thought "No es que sus chistes sean buenos. Es que son... presentes."
        l_thought "Como si supiera que estoy ahogándome y me tirara un salvavidas de sarcasmo. Y lo peor es que funciona."
        show dark 1distraido
        show jeremy 2serio2
        show blaze 1seria2
        $ renpy.pause(4.0, hard=True)
        l_thought "A veces, cuando estás ahogándote, agarrarse a cualquier cosa—incluso al sarcasmo de un idiota—es lo único que te mantiene a flote."
        $ inac2("dark")
        $ inac2("jeremy")
        $ inac2("blaze")
        "Siento cómo los hombros, tensos como cuerdas de arco desde esta mañana, se relajan un milímetro.{w} Es casi imperceptible.{w} Pero está ahí."
        show screen red_effect2
        nobody "{sc=4}No es felicidad... Es distracción.{/sc}"
        nobody "{sc=5}Y a veces, la distracción es lo más cercano al alivio que puedes permitirte.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
        l_thought "..."
        "Pero mis hombros se vuelven a tensar."
        $ normal("blaze")
        show blaze 1enojada
        show dark 1desafiante
        "Blaze le lanza una mirada entre reproche y alivio a Dark"
        show blaze 1compadecer
        extend ", luego me mira.{w} Sus ojos dicen “lo siento” y “gracias a Dios no escaló” al mismo tiempo."
        show blaze 1seria2
        $ inac2("blaze")
        "La clase continúa. El profesor vuelve a... Lo que sea que esté dando."
        show dark 2distraido3
        "Pero el zumbido en mi cabeza no desaparece, pero ahora tiene un contrapunto:"
        "el leve rasgueo del lápiz de Jeremy, el susurro de Blaze volteando páginas, y desde atrás, el sonido casi inaudible de Dark tarareando esa tonadilla inexistente."
        "Es una cacofonía: ecuaciones, susurros, sarcasmo, el zumbido de mi propia cabeza."
        "Pero hoy, por primera vez, no soy un espectador aislado.{w} Soy parte del ruido.{w} Y el ruido, al menos, prueba que existo."
      
    else:
        "Estamos en clases, específicamente, {i}matemáticas{/i}."
        "Una de las clases más insufribles que hay en esta preparatoria... Quizás sea una opinión {i}muy{/i} popular."
        "Veo el pizarrón holográfico como un corazón moribundo."
        "“x² + y² = r²” — la ecuación del círculo perfecto. Perfecta, redonda, infinita.{w} Todo lo que yo no soy."
        l_thought "Un círculo no tiene principio ni fin. Yo tengo ambos, y ambos duelen igual."
        $ renpy.pause(4.0, hard=True)
        #show screen semiblack
        $ renpy.pause(1.5, hard=True)
        "Los números bailan. No son matemáticas, son jeroglíficos de una condena."

        show vignette at latido_con_aparicion zorder 100
                
        "El “+” ya no suma, conecta. Conecta {i}{b}“dolor”{/b}{/i} con {i}{b}“tiempo”{/b}{/i}, {i}{b}“culpa”{/b}{/i} con {i}{b}“memoria”{/b}{/i}, {i}{b}“ayer”{/b}{/i} con {i}{b}“hoy”{/b}{/i}."
        "El {i}{b}“=”{/b}{/i} no iguala, sentencia. {i}{b}“Sueño + pesadilla = realidad”{/b}{/i}.{w} {i}{b}“Padre + distancia = normalidad”{/b}{/i}."
        "{sc=4}{i}{b}“Ella + ausencia = yo”.{/b}{/i}{/sc}"
        show screen red_effect2
        nobody "{sc=4}Todo se reduce a fórmulas, Laila.{/sc}"
        nobody "{sc=5}Tú eres la incógnita que nadie quiere despejar.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
        $ renpy.pause(3.0, hard=True)
        "Las paredes blancas del aula no son paredes, son membranas que se expanden y contraen con cada latido de mi corazón."
        "El aire no es aire, es gelatina espesa que tengo que atravesar para respirar."
        "Cada inhalación es un esfuerzo consciente: uno...{w} dos...{w} tres...{w} ¿O debería ser x...{w} y...{w} z?"
        l_thought "Mi tasa de cambio es siempre negativa."
        extend " Cada día soy menos de lo que era ayer."
        extend " Pronto llegaré a cero."
        extend " ¿Y después?"
        extend " ¿Números imaginarios?"
        extend " ¿Raíces cuadradas de números negativos?"
        l_thought "Eso sería apropiado: una existencia imposible, definida por algo que no puede existir."
        prandom "Señorita Jackson."
        hide vignette
        "Su voz llega como desde otro planeta.{w} Marte, quizás.{w} Donde no hay atmósfera y el sonido no viaja."
        $ renpy.pause(4.0, hard=True)
        prandom "Laila Jackson."
        "Más fuerte.{w} Una onda de choque que atraviesa la gelatina."
        show blaze 1preocupada with Dissolve(0.5):
            center2
        "Blaze se voltea ligeramente, en su mirada mostrando preocupación. Como siempre."
        show blaze 1preocupadat
        $ enfocar("blaze")
        b "¿Laila?"
        $ normal("blaze")
        show blaze 1preocupada
        "Su susurro es un alfiler en el costado.{w} Me punza."
        "Me despierta del trance matemático para arrojarme a uno peor: el de la realidad."
        prandom "¿Podría explicarnos el paso tres de esta ecuación?"
        prandom "Si a = b y b = c, entonces a = c. La propiedad transitiva.{w} Simple lógica."
        l_thought "Propiedad transitiva."
        extend " {b}“Ella = muerta”{/b} y {b}“muerta = ausente”{/b}, entonces {b}“Ella = ausente”{/b}."
        l_thought "{b}“Si yo = culpable”{/b} y {b}“culpable = insufrible”{/b}, entonces {b}“yo = insufrible”{/b}."
        l_thought "Simple lógica."
        extend " Impecable."
        extend " Irrefutable."
        show screen red_effect2
        nobody "{sc=4}Hasta los números te rechazan.{/sc}"
        nobody "{sc=5}Hasta las abstracciones prefieren no tener nada que ver contigo.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)

        $ renpy.music.play("heartbeat.ogg", channel="heartbeat", loop=True)
        show vignette at vineta_organico zorder 100
        show class3A:
            rotate 0
            xanchor 0.5 yanchor 0.5
            xalign 0.5 yalign 0.5
            subpixel True
            easein 15.0 rotate 15
            
        "El aula gira.{w} No es metáfora.{w} El mundo literalmente se inclina 15 grados a la derecha."
        "Las cabezas de mis compañeros se alargan, se deforman como en un espejo de feria."
        "Algunos sonríen—¿o es que sus bocas están torcidas por la gravedad de mi colapso?"
        l "¿Perdón?"
        "La palabra sale automática, una respuesta de robot con las pilas gastadas.{w} No pregunta, constata{w}: estoy perdida."
        "Un suspiro.{w} No es de cansancio.{w} Es de frustración acumulada."
        "El suspiro de quien ha intentado regar una piedra esperando que florezca."
        prandom "La ecuación, Laila.{w} Parece que sus pensamientos están en otro planeta. Compártalos con la clase.{w} Tal vez nos ilumine a todos."
        l_thought "Soy la piedra. La piedra estéril. La que ocupa espacio en el jardín donde antes había flores."
        l_thought "Área = π * r²."
        l_thought "El área de mi existencia se reduce cada día."
        extend " Mi radio se acerca a cero."
        prandom "Tomemos está: 3x + 5 = 17.{w} Despeje x."
        $ renpy.pause(2.0, hard=True)
        l_thought "3x + 5 = 17."
        extend " 3x = 12."
        extend " x = 4."
        show black with Dissolve(0.5):
            alpha 0.7
        l_thought "Cuatro."
        extend " Cuatro palabras en el sueño."
        l_thought "Cuatro líneas rojas en mi cuello."
        l_thought "Cuatro personas que he lastimado."
        l_thought "Cuatro intentos antes de rendirme."
        l_thought "Cuatro paredes en mi habitación a las {b}3:07 AM{/b}."
        "Las caras ya no son caras.{w} Son pantallas en blanco que proyectan mis propios fracasos."
        "En esa, veo a Blaze el día que le grité. En esa otra, a papá recogiendo el periódico manchado de café."
        "En esa de allá, a Arai–...{w}  Cuando aún nos peleamos por esa estupidez."
        "A ella... a {i}ella{/i} dándome la espalda mucho antes de que se fuera para siempre."
        show black with Dissolve(0.5):
            alpha 0.9
        "El aire se condensa. Ahora huele a hospital.{w} A un limpiador frío y a algo dulce que se pudre debajo.{w} El olor de mi sueño.{w} El olor de ella en los últimos días."
        $ renpy.pause(2.0, hard=True)
        "La pizarra parpadea.{w} Por un segundo, las ecuaciones desaparecen. En su lugar:"
        "{sc=4}{b}PERDÓN ≠ VERDAD{b}{/sc}"
        "{sc=5}{b}CULPA > AMOR{b}{/sc}"
        "{sc=6}{b}ADIÓS = INFINITO{b}{/sc}"
        show black with Dissolve(0.5):
            alpha 1.0
        "Parpadea de nuevo.{w} Vuelven los números. Pero yo ya no los veo.{w} Veo las desigualdades grabadas con fuego en mi córnea."
        prandom "¿Laila?"
        hide black
        $ renpy.music.stop(channel="heartbeat")
        "Mi nombre.{w} Otra vez.{w} Siempre mi nombre precediendo una caída."
        "El zumbido no solo está en mis oídos.{w} Está en mis dientes, en mis huesos, en el espacio entre mis células."
        "Es la frecuencia de la estática que llenaba la habitación a las {b}3:07 AM{/b}."
        "Es el sonido del vacío tratando de entrar."
        show screen red_effect2
        nobody "{sc=4}Shhhhh...{w} Solo cierra los ojos.{/sc}"
        nobody "{sc=4}La respuesta no está en la pizarra.{/sc}"
        nobody "{sc=4}Está en el {b}peso = masa gravedad{/b}.{/sc}"
        nobody "{sc=5}En la promesa del impacto.{/sc}"
        nobody "{sc=4}En el {b}silenciо = 1 / grito{/b}.{/sc}"
        nobody "{sc=5}En la ecuación final:{/sc}"
        nobody "{sc=6}{b}Vida < Dolor.{/b}{/sc}"
        show blaze 1preocupadat
        $ enfocar("blaze")
        b "Profesor, creo que no se siente bien.{w} ¿Puedo acompañarla a la enfermería?"
        $ normal("blaze")
        show blaze 1preocupada
        "Su voz suena a kilómetros de distancia.{w} A años luz.{w} Es la voz de un fantasma tratando de negociar con otro fantasma."
        show blaze 2preocupada
        prandom "La pregunta es para Laila, Señorita Zafire."
        prandom "Un esfuerzo Laila, por favor.{w} Intente al menos."
        l_thought "{i}{b}“Intente al menos”{i}{/b}."
        show screen red_effect
        nobody "{sc=4}{b}INTENTE.{/b}{w} Como si no lo hubiera hecho.{/sc}"
        nobody "{sc=4}Como si no intentas respirar cada mañana.{/sc}"
        nobody "{sc=4}Como si no intentaras fingir que el dolor es solo un mal hábito.{/sc}"
        nobody "{sc=5}Y no la estructura misma de tu ser.{/sc}"
        nobody "{sc=4}{b}AL MENOS.{/b}{w} Como si lo mínimo ya fuera un triunfo.{/sc}"
        nobody "{sc=4}Como si sobrevivir al día fuera un logro digno de medalla.{/sc}"
        nobody "{sc=4}Como si pedir “al menos” no fuera la confirmación de que ya renunciaron a esperar.{/sc}"
        nobody "{sc=5}“Algo” de ti.{/sc}"
        hide screen red_effect with Dissolve(0.5)
        hide screen red_effect2 with Dissolve(0.5)
        "Mis dedos se cierran sobre el borde de la mesa.{w} La madera cruje. No es metafórico.{w} Siento la fibra cediendo bajo mi presión."
        "Es lo único real en este momento: la madera, mis uñas clavándose en ella, la certeza de que si aprieto lo suficiente, algo se romperá."
        l_thought "Y yo quiero que algo se rompa. Preferiblemente yo."
        extend " Preferiblemente ahora."
        $ renpy.pause(4.0, hard=True)
        show class3A:
            rotate 15
            xanchor 0.5 yanchor 0.5
            xalign 0.5 yalign 0.5
            subpixel True
            easeout 8.0 rotate 0 
        prandom "¿Nos honra con una respuesta o debo asumir que su silencio es la respuesta?"
        show blaze 2desinteresada3
        "Una risa sofocada en el fondo del aula.{w} No sé de quién es.{w} Podría ser de cualquiera.{w} Podría ser mía, atascada en mi garganta."
        l_thought "Asúmelo."
        l_thought "Asume que mi silencio es mi único idioma coherente."
        l_thought "Asume que cada palabra que no digo es una verdad que no quieres oír."
        l_thought "Asume que esta ecuación no tiene solución, profesor, porque la variable principal—yo—está indefinida."
        l_thought "O mejor, definida como “error”."
        "La presión en mi pecho ya no es ansiedad.{w} Es física.{w} Como si alguien hubiera llenado mi cavidad torácica con cemento fresco.{w} Cada latido es un martillazo contra el molde."
        l_thought "Más. Siempre más. Más preguntas. Más miradas. Más evidencia."
        extend " Más pruebas de que no sirvo para esto."
        l_thought "¿Cuándo entenderán que no vale la pena? ¿Cuándo dejarán de pedirle peras al olmo, flores al desierto, vida a un cadáver que todavía se mueve por inercia?"
        show blaze 2seria
        "Mis ojos encuentran los de Blaze. No veo preocupación."
        show blaze 2desinteresada3
        extend " Veo incomodidad. Y la verdad es que soy un problema."
        "La mentira es que ella puede arreglarme.{w} El tiempo se agota. La incomodidad crece."
        show screen red_effect2
        nobody "{sc=4}{b}Déjala.{/b}{w} Déjala estar incómoda.{/sc}"
        nobody "{sc=4}Al menos la incomodidad es una emoción honesta.{/sc}"
        nobody "{sc=5}Mejor que la falsa paciencia que ha estado mostrando.{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
        $ inac2("blaze")
        "La ecuación en la pizarra ya no es matemática. Es mi biografía en símbolos:"
        window hide
        show black with Dissolve(0.3):
            alpha 0.8
        centered "{sc=4}{b}Laila = (Culpa * Ausencia) / Tiempo{/b}{/sc}"
        centered "{sc=4}{b}Límite cuando Tiempo → 0 = ?{/b}{/sc}"
        centered "{sc=4}{b}Solución: Indefinido{/b}{/sc}"
        centered "{sc=7}{b}{color=#ff0000}Error: División por cero{/b}{/sc}"
        hide black 
        show vignette at vineta_organico zorder 100
        l_thought "¿O es simplemente cero, porque nada de esto importa, porque al final todo se reduce a polvo y sueños rotos y pizarras que siguen parpadeando en aulas vacías?"
        prandom "Bueno, si la señorita Jackson prefiere guardar sus conocimientos para sí...{w} Siéntese."
        prandom "Anotaré su...{w} Participación."
        "{b}{i}“Anotaré.”{/i}{/b} Otra palabra.{w} Otro clavo."
        prandom "La matemática no perdona, señorita Jackson.{w} O sigue las reglas, o el universo te deja atrás."
        prandom "Es pura lógica."
        l_thought "El universo ya me dejó atrás, profesor."
        l_thought "Estoy en el lugar donde las reglas se descomponen y 2+2 puede igualar “nada” si lo dices con suficiente convicción."
        show screen red_effect2
        nobody "{sc=6}Anota esto, profesor:{/sc}"
        show black with Dissolve(0.3):
            alpha 0.8
        centered "{sc=4}{b}Participación = 0{/b}{/sc}"
        centered "{sc=4}{b}Comprensión = 0{/b}{/sc}"
        centered "{sc=4}{b}Futuro = 0{/b}{/sc}"
        centered "{sc=4}{b}Valor = 0{/b}{/sc}"
        centered "{sc=4}{b}Suma total = CERO{/b}{/sc}"
        centered "{sc=6}{b}Ecuación verificada. Solución confirmada.{/b}{/sc}"
        hide screen red_effect2 with Dissolve(0.5)
        show black with Dissolve(0.5):
            alpha 0.9
        window show
        "Me siento. El mundo vuelve a su eje, pero a un precio{w}: todo ahora tiene un filtro gris, como si alguien hubiera bajado el brillo de la realidad."
        "Las voces se callan, pero dejan un zumbido de fondo—el sonido del silencio después de un grito."
        "Pero en mi pecho, el cemento sigue ahí, endureciéndose."
        "Pero en la pizarra, aunque ya nadie más lo ve, la ecuación final sigue ahí:"
        window hide
        centered "{sc=4}{b}VIDA - ELLA = YO{/b}{/sc}"
        centered "{sc=4}{b}YO + DOLOR = AHORA{/b}{/sc}"
        centered "{sc=4}{b}AHORA * TIEMPO = NADA {/b}{/sc}"
        centered "{sc=5}{b}YO = NADA{/b}{/sc}"
        window show
        l_thought "Propiedad transitiva.{w} Si A = B y B = C, entonces A = C."
        l_thought "Si yo = culpable y culpable = nada..."
        l_thought "Entonces yo = nada."
        extend " Lo que se quería demostrar."
        l_thought "Siempre más castigo."
        extend " Más evidencia de que no sirvo para esto."
        extend " ¿Cuándo entenderán que no vale la pena?"

    stop music fadeout 4.5
    scene black
    $ quick_menu = False
    with dissolve_scene_full3

return    