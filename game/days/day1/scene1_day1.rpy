label scene1_day1:
     
    play music classroom fadeout 1.0 fadein 3.5
    pause 4.0 
    $ quick_menu = True 
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
    play audio teens_laugh volume 0.5
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
    play audio closet_open
    pause 1.0
    scene black with fade 
    scene pasillo with dissolve
    show vignette at vineta_rapido zorder 100 
    play audio closet_close
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

return