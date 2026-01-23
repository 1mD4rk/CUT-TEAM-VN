screen route_navigation:
    vbox:
        style_prefix "navigation"
        spacing 20
        xalign 0.5
        yalign 0.1

        # Título arriba y centrado
        text "EXTRAS":
            size 60
            color "#ffffff"
            bold True
            outlines [(4, "#5b1e99", 0, 0)]
            xalign 0.5

        # Botones en una fila horizontal
        hbox:
            spacing 50
            xalign 0.5
            
            textbutton "Rutas Paralelas" action ShowMenu("route_paralela")
            textbutton "Rutas Alternativas" action ShowMenu("route_alternativa")
            # textbutton "Love Interest C" action ShowMenu("gallery_c")

screen return_button_screen():
    key "K_ESCAPE" action Return()
    textbutton "Volver":
        action Return()
        xalign 0.0  # Izquierda
        yalign 1.0  # Abajo
        xoffset 20  # Margen izquierdo
        yoffset -20 # Margen inferior