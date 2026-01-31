label elpesodelcuidado:
    $ discord.set(details="El Peso del Cuidado", state="Parallel Route 1")
    stop music fadeout 4.0 
    $ quick_menu = False
    scene black with Dissolve(5.0)    
    $renpy.pause (5.0, hard=True)
  
    scene pasillo2
    with Dissolve(3.0)
    $renpy.pause (1.5, hard=True)
    show bg_bz
    show route1 "Ruta Paralela I:\nEl Peso del Cuidado" at truecenter
    with Dissolve(1.0)
    $renpy.pause (3.0, hard=True)
    hide bg_bz
    hide route1
    with Dissolve(1.0)
    $renpy.pause (1.0, hard=True)

    $ quick_menu = True
    with Dissolve(0.5)

    "..." 
    "(W.I.P)."

    scene black 
    $ quick_menu = False
    with Dissolve(2.0) 
    $ persistent.paralela1_complete = True
    
    $ renpy.pause(2.0, hard=True)
    return