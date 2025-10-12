default persistent.phone_tutorial_seen = False

define sb = Character("SkyBot", 
    who_bold=True,
    who_outlines=[(4, "#222c41", 0, 0)],  
    what_outlines = [(2, "#222c41", 3, 3)],
    color="#ffff",
    image="circle") 

### IMAGE

image side circle = "images/circle.png"

label celu_tutorial:
    $ persistent.phone_tutorial_seen = True

    show screen phone with dissolve

    $ _history = False
    sb "Ya veo que le dio click al botón que abre esto..."
    sb "¡Bienvenido, Jugador, al tutorial del celular!"
    sb "Para darle un poco de contexto... El celular de Laila ahora será el nuevo menú de pausa."
    sb "Para esta explicación, lo separaré por dos categorias.\n En las acciones principales tenemos: "
    sb "{i}- Guardar (Save Game) y Cargar partida (Load Game).{/i}"
    sb "{i}- Ir al apartado de opciones del juego (Settings).{/i}"
    sb "{i}- Salir al menu principal (Menu).{/i}"
    sb "{i}- Recibir y ver mensajes de tus contactos. Estos tendrán selecciones (Message).\n- Recibir y ver las llamadas que hagan tus contactos (Call).{/i}"
    sb "Ahora con las secundarias:"
    sb "{i}- Visualizar el historial (History).{/i}"
    sb "{i}- Salir del juego (Exit).{/i}"
    sb "{i}- El calendario. Podrás ver el día que esta transcurriendo (Calendar).{/i}"
    sb '{i}- Para acceder a cada "aplicación", es solamente darle click con el mouse a la app que desea acceder.'
    sb "Una vez especificado todo esto..."
    sb "Puedes abrir el celular en cualquier momento presionando el botón 'Cel.' en la esquina inferior."
    $ _history = True
    
    hide screen phone with dissolve
    return