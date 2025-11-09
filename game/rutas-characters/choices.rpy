label rutacanon_choice1:
        l 'Pues... Tuve un pequeño "problema" con el Profesor Todd...'
        "La culpa me sigue invadiendo, haciéndome sentir pequeña y expuesta."
        l "Que concluyó en mí fuera del salón."
        l "Ese es un pequeño resumen que le puedo dar a tu pregunta."
        show dark 2neutral
        "Ahora Dark luce sorprendido."
        pause 1.5
        show dark 2neutralt
        $ enfocar("dark")
        d "Espera... ¿Respondiste?"
        show dark 2neutral
        $ normal("dark")
        l "Claro..."
        "Se le ve una genuina confusión en su rostro."
        l_thought "¿Él esperaba que no lo hiciera?"
        l_thought "¿Le dí tan mala imagen? Bueno, supongo que me la gané."
        pause 1.5
        show dark 2distraidot
        $ _history = False
        d "{size=18}Se suponía que en esta versión eres algo más problemática...{/size}"
        d "{size=18}Como en la de célu-{/size}{nw}"
        $ _history = True
        show dark 2distraido
        "Esa última parte la dice para sí mismo. Aun así lo oí.{w} Otra vez."
        l_thought "¿En esta...{w=0.5} Versión?"
        "Mi rostro refleja la confusión, sus palabras me desconciertan."
        l_thought "¿Qué carajos dice este?"
        extend " Como sea..."
        l_thought "Parece tener la mirada perdida."
        l_thought "Creo que es hora de despertarlo."
        l "Ejem."
        show dark 2neutral
        l_thought "Ya reaccionó."
return

label rutasuicida_choice1:
        l "No es problema tuy-{nw}"
        show dark 2distraidot
        $ enfocar("dark")
        d "Olvidalo." 
        show dark 2seriot
        extend " Ya sé la respuesta."
        "Ni siquiera me dejó terminar la oración. Dejando las palabras medio salir."
        d "¿No será qué estás por aquí por estar durmiendote en las clases?"
        show dark 2juzga2t
        d "O en el peor de los casos"
        show dark 2seriot
        extend ", ¿Tuviste algún problema con el profesor y te echaron?"
        d "¿Y por eso casualmente estás por aquí?"
        show dark 2distraidot
        $ normal("dark")
        $ _history = False
        d "{size=18}En verdad... En esta versión eres {i}muy{/i} problematica.{/size}"
        $ _history = True
        show dark 2enojao
        l_thought "¿En esta...{w=0.5} Versión?"
        l_thought "¿Qué carajos dice este?"
        extend " Como sea..."
        l_thought "Esa fue una observación muy... detallada."
        l_thought "Es como si él hubiera estado allí, cuando sé que no."
        l_thought "Por el bien de mi ya deteriorada salud mental, mejor no quiero saber lo que piensa de mí."
        l "¿Mi opinión? Prefiero guardármela para algo que realmente importe."
        l_thought "No tengo energía para dar opiniones hoy. ¿Puedes simplemente dejarme en paz?"
        show dark 2seriot
        $ enfocar("dark")
        d "Sin ofender, pero."
        extend " Eres una chica demasiado problemática."
        show dark 2enojao
        $ normal("dark")
        "Como si no hubiera escuchado, desvío la mirada."
        l_thought "Wow, viniendo de ti, eso casi suena a proyección."
return

label rutasuicida_nochoice1:
        $ rutaSuicida += 1
        l "No es problema tuy-{nw}"
        show dark 2distraidot
        $ enfocar("dark")
        d "Olvidalo." 
        show dark 2seriot
        extend " Ya sé la respuesta."
        "Ni siquiera me dejó terminar la oración. Dejando las palabras medio salir."
        d "¿No será qué estás por aquí por estar durmiendote en las clases?"
        show dark 2juzga2t
        d "O en el peor de los casos"
        show dark 2seriot
        extend ", ¿Tuviste algún problema con el profesor y te echaron?"
        d "¿Y por eso casualmente estás por aquí?"
        show dark 2distraidot
        $ normal("dark")
        $ _history = False
        d "{size=18}En verdad... En esta versión eres {i}muy{/i} problematica.{/size}"
        $ _history = True
        show dark 2enojao
        l_thought "¿En esta...{w=0.5} Versión?"
        l_thought "¿Qué carajos dice este?"
        extend " Como sea..."
        l_thought "Esa fue una observación muy... detallada."
        l_thought "Es como si él hubiera estado allí, cuando sé que no."
        l_thought "Por el bien de mi ya deteriorada salud mental, mejor no quiero saber lo que piensa de mí."
        l "¿Mi opinión? Prefiero guardármela para algo que realmente importe."
        l_thought "No tengo energía para dar opiniones hoy. ¿Puedes simplemente dejarme en paz?"
        show dark 2seriot
        $ enfocar("dark")
        d "Sin ofender, pero."
        extend " Eres una chica demasiado problemática."
        show dark 2enojao
        $ normal("dark")
        "Como si no hubiera escuchado, desvío la mirada."
        l_thought "Wow, viniendo de ti, eso casi suena a proyección."
        jump dark_scene_afterchoice1
return