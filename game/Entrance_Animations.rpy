#######################################################################################
#######################################################################################
#######################################################################################
############ Entrance Animations for Ren'Py

# Hey there! Thanks for grabbing my set of entrance animations (tranforms) for Ren'Py.
# Below you will find a collection of seven different transforms you can use to show your sprites (or other things).
# You can use them with your positions - "show 'sprite' at left, slidein_entrance" works just fine.
# The last transform uses the 3D stage - you must turn on the camera in order for it to work. More details to read below!
#
#
# If you like this set of transforms, consider checking out my games (Two and a Half Studios)!
#
#
# If you'd like to, you can credit "Gabmag", but it's not necessary :)
# - Gabmag


############## Animations #########################################################

# Slide in entrance randomizes whether it slides from the left or right. You can adjust this.
transform slidein_entrance():
    alpha 0.0
    choice:
        xoffset -50
    choice:
        xoffset 50
    easein 0.6 alpha 1.0 xoffset 0

# A smaller bounce entrance
transform bounce_entrance():
    alpha 0.0
    yoffset -20
    easein 0.3 alpha 1.0 yoffset 5
    easeout 0.2 yoffset 0

# A larger bounce entrance
transform big_bounce_entrance():
    alpha 0.0
    yoffset -30
    easein 0.3 alpha 1.0 yoffset 10
    easeout 0.2 yoffset -5
    easein 0.15 yoffset 5
    easeout 0.1 yoffset -2
    easein 0.1 yoffset 2
    easeout 0.1 yoffset 0

# Floats up from below.
transform float_entrance():
    alpha 0.0
    yoffset 20
    easein 0.5 alpha 1.0 yoffset 0
    ease 0.2 yoffset 5
    ease 0.2 yoffset 0

# A very exaggerated entrance. You can adjust the zoom to make it subtler.
transform zoom_pop_entrance():
    alpha 0.0 zoom 0.5
    easein 0.4 alpha 1.0 zoom 1.1
    easeout 0.2 zoom 1.0

# Similar to the bounce entrances, but drops further
transform drop_entrance():
    alpha 0.0 yoffset -100
    easein 0.4 alpha 1.0 yoffset 10
    easeout 0.3 yoffset -5
    ease 0.2 yoffset 0

# The only 3d entrance - you must set the 3d camera on before this will work.
# Do this by adding the following to your script:

# camera:
#     perspective True

transform spring_up_3d():
    alpha 0.0 xrotate 90 zpos 200
    easeout 0.4 alpha 1.0 xrotate -20 zpos -100
    easein 0.2 xrotate 10 zpos -50
    easein 0.15 xrotate 0 zpos 0
