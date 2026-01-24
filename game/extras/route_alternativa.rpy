screen route_alternativa:
    tag menu
    add gui.main_menu_background

    # Botones de navegación
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
            if persistent.unlocked_alternativa1:
                imagebutton:
                    idle im.Scale("images/extras/CGs/b_red.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/b_red.png", 280, 158), matrixcolor=BrightnessMatrix(0.15))
                    action Jump("day1_red")
                    xsize 280
                    ysize 158
            else:
                # Mostrar imagen bloqueada
                add im.Scale("images/extras/locked.jpg", 280, 158)
            
            if persistent.unlocked_alternativa2:
                imagebutton:
                    idle im.Scale("images/extras/CGs/b_orange.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/b_orange.png", 280, 158), matrixcolor=BrightnessMatrix(0.15))
                    action Jump("day1_orange")
                    xsize 280
                    ysize 158
            else:
                add im.Scale("images/extras/locked.jpg", 280, 158)
            
            if persistent.unlocked_alternativa3:
                imagebutton:
                    idle im.Scale("images/extras/CGs/b_yellow.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/b_yellow.png", 280, 158), matrixcolor=BrightnessMatrix(0.15))
                    action Jump("day1_yellow")
                    xsize 280
                    ysize 158
            else:
                add im.Scale("images/extras/locked.jpg", 280, 158)
            
            if persistent.unlocked_alternativa4:
                imagebutton:
                    idle im.Scale("images/extras/CGs/b_green.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/b_green.png", 280, 158), matrixcolor=BrightnessMatrix(0.15))
                    action Jump("day1_green")
                    xsize 280
                    ysize 158
            else:
                add im.Scale("images/extras/locked.jpg", 280, 158)
            
            if persistent.unlocked_alternativa5:
                imagebutton:
                    idle im.Scale("images/extras/CGs/b_blue.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/b_blue.png", 280, 158), matrixcolor=BrightnessMatrix(0.15))
                    action Jump("day1_blue")
                    xsize 280
                    ysize 158
            else:
                add im.Scale("images/extras/locked.jpg", 280, 158)
            
            if persistent.unlocked_alternativa6:
                imagebutton:
                    idle im.Scale("images/extras/CGs/b_indigo.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/b_indigo.png", 280, 158), matrixcolor=BrightnessMatrix(0.15))
                    action Jump("day1_indigo")
                    xsize 280
                    ysize 158
            else:
                add im.Scale("images/extras/locked.jpg", 280, 158)