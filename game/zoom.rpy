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
    personajes = ["dark", "jeremy", "ptod", "blaze", "dad", "dirc", "tv", "strike"]
    
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
            ease 0.35 xoffset -2 yoffset 5
            ease 0.35 xoffset 0 yoffset -1
            ease 0.35 xoffset 2 yoffset 5
            ease 0.35 xoffset 0 yoffset -1
            repeat
    parallel:
        linear 0.1 zoom 1.05 alpha 1.0 yoffset 0

transform walking_b_activo:
    anchor (0.5, 1.0)
    parallel:
        block:
            ease 0.5 xoffset 2 yoffset 3
            ease 0.3 xoffset 0 yoffset -1
            ease 0.5 xoffset -2 yoffset 3
            ease 0.3 xoffset 0 yoffset -1
            repeat
    parallel:
        linear 0.1 zoom 1.05 alpha 1.0 yoffset 0

transform walking_c_activo:
    anchor (0.5, 1.0)
    parallel:
        block:
            ease 0.4 xoffset 0 yoffset -1
            ease 0.4 xoffset -3 yoffset 3
            ease 0.4 xoffset 0 yoffset -1
            ease 0.4 xoffset 3 yoffset 3
            repeat
    parallel:
        linear 0.1 zoom 1.05 alpha 1.0 yoffset 0

# Y también las versiones normales (sin zoom pero manteniendo caminata)
transform walking_a_normal:
    anchor (0.5, 1.0)
    parallel:
        block:
            ease 0.35 xoffset -2 yoffset 5
            ease 0.35 xoffset 0 yoffset -1
            ease 0.35 xoffset 2 yoffset 5
            ease 0.35 xoffset 0 yoffset -1
            repeat
    parallel:
        linear 0.1 zoom 1.0 alpha 1.0 yoffset 0

transform walking_b_normal:
    anchor (0.5, 1.0)
    parallel:
        block:
            ease 0.5 xoffset 2 yoffset 3
            ease 0.3 xoffset 0 yoffset -1
            ease 0.5 xoffset -2 yoffset 3
            ease 0.3 xoffset 0 yoffset -1
            repeat
    parallel:
        linear 0.1 zoom 1.0 alpha 1.0 yoffset 0

transform walking_c_normal:
    anchor (0.5, 1.0)
    parallel:
        block:
            ease 0.4 xoffset 0 yoffset -1
            ease 0.4 xoffset -3 yoffset 3
            ease 0.4 xoffset 0 yoffset -1
            ease 0.4 xoffset 3 yoffset 3
            repeat
    parallel:
        linear 0.1 zoom 1.0 alpha 1.0 yoffset 0

init python:
    def enfocar_walking(tag):
        if renpy.showing(tag):
            renpy.show(tag, at_list=[walking_c_activo], tag=tag)
    
    def normal_walking(tag):
        if renpy.showing(tag):
            renpy.show(tag, at_list=[walking_c_normal], tag=tag)
