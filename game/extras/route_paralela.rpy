
transform fade_to_black_routes:
    alpha 0.0
    linear 2.0 alpha 1.0

screen fade_to_game_routes(target_label=None):
    modal True
    zorder 200
    add "#000" at fade_to_black_routes
    timer 2.0 action [Hide("fade_to_game_routes"), Hide("route_paralela"), Start(target_label)]
    
screen route_paralela:
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
            
            # Imagen roja - Rutas Paralelas
            if persistent.paralela1:
                imagebutton:
                    idle im.Scale("images/extras/CGs/a_red.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/a_red.png", 280, 158), matrixcolor=BrightnessMatrix(0.15))
                    action Show("fade_to_game_routes", target_label="elpesodelcuidado")
                    xsize 280
                    ysize 158
            else:
                # Mostrar imagen bloqueada
                add im.Scale("images/extras/locked.jpg", 280, 158)
            
            if persistent.paralela2:
                imagebutton:
                    idle im.Scale("images/extras/CGs/a_orange.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/a_orange.png", 280, 158), matrixcolor=BrightnessMatrix(0.15))
                    action Jump("para_day1_orange")
                    xsize 280
                    ysize 158
            else:
                add im.Scale("images/extras/locked.jpg", 280, 158)
            
            if persistent.paralela3:
                imagebutton:
                    idle im.Scale("images/extras/CGs/a_yellow.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/a_yellow.png", 280, 158), matrixcolor=BrightnessMatrix(0.15))
                    action Jump("para_day1_yellow")
                    xsize 280
                    ysize 158
            else:
                add im.Scale("images/extras/locked.jpg", 280, 158)
            
            if persistent.paralela4:
                imagebutton:
                    idle im.Scale("images/extras/CGs/a_green.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/a_green.png", 280, 158), matrixcolor=BrightnessMatrix(0.15))
                    action Jump("para_day1_green")
                    xsize 280
                    ysize 158
            else:
                add im.Scale("images/extras/locked.jpg", 280, 158)
            
            if persistent.paralela5:
                imagebutton:
                    idle im.Scale("images/extras/CGs/a_blue.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/a_blue.png", 280, 158), matrixcolor=BrightnessMatrix(0.15))
                    action Jump("para_day1_blue")
                    xsize 280
                    ysize 158
            else:
                add im.Scale("images/extras/locked.jpg", 280, 158)
            
            if persistent.paralela6:
                imagebutton:
                    idle im.Scale("images/extras/CGs/a_indigo.png", 280, 158)
                    hover Transform(im.Scale("images/extras/CGs/a_indigo.png", 280, 158), matrixcolor=BrightnessMatrix(0.15))
                    action Jump("para_day1_indigo")
                    xsize 280
                    ysize 158
            else:
                add im.Scale("images/extras/locked.jpg", 280, 158)