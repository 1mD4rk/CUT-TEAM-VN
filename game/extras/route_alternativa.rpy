screen route_alternativa:
    tag menu
    add gui.main_menu_background

    # Botones de navegación (con el título "EXTRAS" y botones)
    # Envolvemos route_navigation en un contenedor para posicionarlo
    frame:
        background None
        xalign 0.5
        yalign 0.25
        use route_navigation
    
    # Botón Volver en esquina inferior izquierda
    use return_button_screen
    
    # Cuadrícula de imágenes centrada y más abajo
    vbox:
        xalign 0.5
        yalign 0.58
        
        grid 3 2:
            spacing 65
            xalign 0.5
            
            # Imagen roja
            if persistent.unlocked_red:
                imagebutton:
                    idle im.Scale("images/extras/CGs/b_red.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/b_red.png", 280, 158), zoom=1.07)
                    action Jump("day1_red")
                    xsize 280
                    ysize 158
            else:
                # Mostrar imagen bloqueada CORREGIDO
                add im.Scale("images/extras/locked.jpg", 280, 158)
            
            # Imagen naranja - Solo clickeable si está desbloqueada
            if persistent.unlocked_orange:
                imagebutton:
                    idle im.Scale("images/extras/CGs/b_orange.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/b_orange.png", 280, 158), zoom=1.07)
                    action Jump("day1_orange")
                    xsize 280
                    ysize 158
            else:
                add im.Scale("images/extras/locked.jpg", 280, 158)
            
            # Imagen amarilla - Solo clickeable si está desbloqueada
            if persistent.unlocked_yellow:
                imagebutton:
                    idle im.Scale("images/extras/CGs/b_yellow.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/b_yellow.png", 280, 158), zoom=1.07)
                    action Jump("day1_yellow")
                    xsize 280
                    ysize 158
            else:
                add im.Scale("images/extras/locked.jpg", 280, 158)
            
            # Imagen verde - Solo clickeable si está desbloqueada
            if persistent.unlocked_green:
                imagebutton:
                    idle im.Scale("images/extras/CGs/b_green.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/b_green.png", 280, 158), zoom=1.07)
                    action Jump("day1_green")
                    xsize 280
                    ysize 158
            else:
                add im.Scale("images/extras/locked.jpg", 280, 158)
            
            # Imagen azul - Solo clickeable si está desbloqueada
            if persistent.unlocked_blue:
                imagebutton:
                    idle im.Scale("images/extras/CGs/b_blue.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/b_blue.png", 280, 158), zoom=1.07)
                    action Jump("day1_blue")
                    xsize 280
                    ysize 158
            else:
                add im.Scale("images/extras/locked.jpg", 280, 158)
            
            # Imagen índigo - Solo clickeable si está desbloqueada
            if persistent.unlocked_indigo:
                imagebutton:
                    idle im.Scale("images/extras/CGs/b_indigo.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/b_indigo.png", 280, 158), zoom=1.07)
                    action Jump("day1_indigo")
                    xsize 280
                    ysize 158
            else:
                add im.Scale("images/extras/locked.jpg", 280, 158)