# Transformaciones con ajuste para sprites altos
transform activo:
    anchor (0.5, 1.0)  # Punto de anclaje en centro inferior
    linear 0.1 zoom 1.05 alpha 1.0 yoffset 0

transform activo_flip:
    anchor (0.55, 1.0)  # Punto de anclaje en centro inferior
    linear 0.1 zoom 1.05 alpha 1.0 yoffset 0

transform inactivo:
    anchor (0.5, 1.0)
    linear 0.1 zoom 1.0 alpha 1.0 yoffset 0

transform a_normal:
    anchor (0.5, 1.0)
    linear 0.1 zoom 1.0 alpha 1.0 yoffset 0

transform a_normal_flip:
    anchor (0.55, 1.0)
    linear 0.1 zoom 1.0 alpha 1.0 yoffset 0

transform paraguay:
    anchor (0.5, 1.0)
    linear 0.1 zoom 0.9 alpha 0.8 yoffset 0

transform paraguay2:
    anchor (0.5, 1.0)
    linear 0.1 zoom 0.9 alpha 0.5 yoffset 0

# Sistema de manejo de personajes
init python:
    personajes = ["dark", "jeremy", "ptod", "blaze", "dad", "dirc", "tv", "strike", "mani"]
    
    def enfocar(tag):
        if renpy.showing(tag):
            renpy.show(tag, at_list=[activo], tag=tag)
    
    def enfocar_flip(tag):
        if renpy.showing(tag):
            renpy.show(tag, at_list=[activo_flip], tag=tag)

    def enfocar1(tag_activo):
        for tag in personajes:
            if renpy.showing(tag):
                if tag == tag_activo:
                    renpy.show(tag, at_list=[activo], tag=tag)
                else:
                    renpy.show(tag, at_list=[inactivo], tag=tag)
    
    def normal(tag):
        if renpy.showing(tag):
            renpy.show(tag, at_list=[a_normal], tag=tag)
    
    def normal_flip(tag):
        if renpy.showing(tag):
            renpy.show(tag, at_list=[a_normal_flip], tag=tag)
    
    def inac(tag):
        if renpy.showing(tag):
            renpy.show(tag, at_list=[paraguay], tag=tag)

    def inac2(tag):
        if renpy.showing(tag):
            renpy.show(tag, at_list=[paraguay2], tag=tag)
    
    def reset_personajes():
        for tag in personajes:
            normal(tag)

# Transformaciones combinadas (caminata + enfoque)
transform walking_a_activo:
    anchor (0.5, 1.0)
    parallel:
        block:
            ease 0.35 xoffset -6 yoffset 9
            ease 0.35 xoffset 0 yoffset -5
            ease 0.35 xoffset 6 yoffset 9
            ease 0.35 xoffset 0 yoffset -5
            repeat
    parallel:
        linear 0.1 zoom 1.05 alpha 1.0 yoffset 0

transform walking_b_activo:
    anchor (0.5, 1.0)
    parallel:
        block:
            ease 0.5 xoffset 4 yoffset 5
            ease 0.3 xoffset 0 yoffset -2
            ease 0.5 xoffset -4 yoffset 5
            ease 0.3 xoffset 0 yoffset -2
            repeat
    parallel:
        linear 0.1 zoom 1.05 alpha 1.0 yoffset 0

transform walking_c_activo:
    anchor (0.5, 1.0)
    parallel:
        block:
            ease 0.4 xoffset 0 yoffset -3
            ease 0.4 xoffset -5 yoffset 5
            ease 0.4 xoffset 0 yoffset -3
            ease 0.4 xoffset 5 yoffset 5
            repeat
    parallel:
        linear 0.1 zoom 1.05 alpha 1.0 yoffset 0

# Y también las versiones normales (sin zoom pero manteniendo caminata)
transform walking_a_normal:
    anchor (0.5, 1.0)
    parallel:
        block:
            ease 0.35 xoffset -6 yoffset 9
            ease 0.35 xoffset 0 yoffset -5
            ease 0.35 xoffset 6 yoffset 9
            ease 0.35 xoffset 0 yoffset -5
            repeat
    parallel:
        linear 0.1 zoom 1.0 alpha 1.0 yoffset 0

transform walking_ab_normal:
    anchor (0.5, 1.0)
    parallel:
        block:
            ease 0.5 xoffset -6 yoffset 9
            ease 0.5 xoffset 0 yoffset -5
            ease 0.5 xoffset 6 yoffset 9
            ease 0.5 xoffset 0 yoffset -5
            repeat
    parallel:
        linear 0.1 zoom 1.0 alpha 1.0 yoffset 0

transform walking_a_inactive:
    anchor (0.5, 1.0)
    parallel:
        block:
            ease 0.35 xoffset -6 yoffset 9
            ease 0.35 xoffset 0 yoffset -5
            ease 0.35 xoffset 6 yoffset 9
            ease 0.35 xoffset 0 yoffset -5
            repeat
    parallel:
        paraguay2

transform walking_b_normal:
    anchor (0.5, 1.0)
    
    parallel:
        block:
            ease 0.5 xoffset 4 yoffset 5
            ease 0.3 xoffset 0 yoffset -2
            ease 0.5 xoffset -4 yoffset 5
            ease 0.3 xoffset 0 yoffset -2
            repeat
    parallel:
        linear 0.1 zoom 1.0 alpha 1.0 yoffset 0

transform walking_b_inactive:
    anchor (0.5, 1.0)
    paraguay
    parallel:
        block:
            ease 0.5 xoffset 4 yoffset 5
            ease 0.3 xoffset 0 yoffset -2
            ease 0.5 xoffset -4 yoffset 5
            ease 0.3 xoffset 0 yoffset -2
            repeat
    parallel:
        paraguay2

transform walking_c_normal:
    anchor (0.5, 1.0)
    parallel:
        block:
            ease 0.4 xoffset 0 yoffset -3
            ease 0.4 xoffset -5 yoffset 5
            ease 0.4 xoffset 0 yoffset -3
            ease 0.4 xoffset 5 yoffset 5
            repeat
    parallel:
        linear 0.1 zoom 1.0 alpha 1.0 yoffset 0

transform walking_c_inactive:
    anchor (0.5, 1.0)
    parallel:
        block:
            ease 0.4 xoffset 0 yoffset -3
            ease 0.4 xoffset -5 yoffset 5
            ease 0.4 xoffset 0 yoffset -3
            ease 0.4 xoffset 5 yoffset 5
            repeat
    parallel:
        paraguay2

## scene2_day3.rpy
transform move_out_right_fast:
    linear 3.0 xpos -400 

transform jadeo_activo:
    anchor (0.5, 1.0)
    parallel:
        block:
            ease 0.6 yoffset 8
            ease 0.4 yoffset 0
            ease 0.8 yoffset 5
            ease 0.6 yoffset 0
            repeat
    parallel:
        # Efecto de enfoque
        linear 0.1 zoom 1.05 alpha 1.0

transform jadeo_normal:
    anchor (0.5, 1.0)
    parallel:

        block:
            ease 0.6 yoffset 8
            ease 0.4 yoffset 0
            ease 0.8 yoffset 5
            ease 0.6 yoffset 0
            repeat
    parallel:
        # Sin efecto de enfoque
        linear 0.1 zoom 1.0 alpha 1.0

transform jadeo_off:
    anchor (0.5, 1.0)
    parallel:
        ease 1.0 yoffset 0
    parallel:
        linear 0.1 zoom 1.0 alpha 1.0

