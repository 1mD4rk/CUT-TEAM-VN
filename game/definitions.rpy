########################### Variables ###########################

#default persistent.day = 0
default rutaCanon = 0
default rutaSuicida = 0
define contador = 0 

define gui.dialogue_text_outlines = [ (3, "#000005", 0, 0) ]

######################## Animaciones y Pantalla #############################

transform fade_in:
    alpha 0.0
    easein 0.1 alpha 0.8
    easeout 0.1 alpha 1.0

transform _no_animation:
    alpha 1.0 

transform vineta_organico:
    alpha 0.0
    easein 40.0 alpha 5.0

transform vineta_rapido:
    alpha 0.0
    easein 6.0 alpha 5.0

transform vineta_rapido2:
    alpha 0.0
    easein 20.0 alpha 5.0

transform sigh_animation:
    linear 0.3 yzoom 1.03 xzoom 0.99
    pause 0.2
    linear 0.5 yzoom 1.0 xzoom 1.0 yoffset 0

transform shake:
    linear 0.1 xoffset -2 yoffset 0
    linear 0.1 xoffset 4 yoffset 0
    linear 0.1 xoffset -2 yoffset 0
    linear 0.1 xoffset 0 yoffset 0

transform shake1:
    linear 0.1 xoffset -5 yoffset 0
    linear 0.1 xoffset 10 yoffset 0
    linear 0.1 xoffset -5 yoffset 0
    linear 0.1 xoffset 0 yoffset 0
    repeat 3

transform hug_on:
        linear 0.4 zoom 1.9 xalign 0.5 yalign 0.45

transform hug2_on:
        ypos 1080
        linear 0.2 zoom 1.9 xalign 0.5 yalign 0.45

transform hug_off:
        linear 0.4 zoom 1.0 yalign 0.9
        center

transform hug2_off:
        linear 0.4 zoom 1.0 yalign 1.0
        linear 0.4 center2

transform boo:
    linear 0.01 yoffset -5 xoffset 0
    linear 0.01 yoffset -6 xoffset 0
    linear 0.01 yoffset -5 xoffset 0
    linear 0.01 yoffset 0 xoffset 0

transform boo2:
    linear 0.02 yoffset -5 xoffset 0
    linear 0.02 yoffset -7 xoffset 0
    linear 0.02 yoffset -5 xoffset 0
    linear 0.02 yoffset 0 xoffset 0

transform boo3:
    linear 0.02 yoffset -7 xoffset 0
    linear 0.02 yoffset -9 xoffset 0
    linear 0.02 yoffset -7 xoffset 0
    linear 0.02 yoffset 0 xoffset 0    

transform slide_left_slight:
    xanchor 0.5 yanchor 1.0
    ease 0.4 xpos 250

transform slow_slide_left_slight:
    xanchor 0.5 yanchor 1.0
    ease 0.4 xpos 300

transform slide_center_slight:
    xanchor 0.5 yanchor 1.0  
    ease 0.4 xpos 750

transform slide_right_slight:
    xanchor 0.5 yanchor 1.0
    ease 0.4 xpos 1150

transform slide_in_right_fast:
    xanchor 0.5 yanchor 1.0
    xpos 2500 ypos 1080
    easein 0.3 xpos 1610

transform slide_out_right_fast:
    xanchor 0.5 yanchor 1.0
    xpos 1610 ypos 1080
    easein 0.3 xpos 2500

transform jadeo_rapido:
    xanchor 0.5 yanchor 1.0
    parallel:
        block:
            ease 0.3 yoffset 6
            ease 0.2 yoffset 0
            ease 0.3 yoffset 4
            ease 0.2 yoffset 0
            repeat

transform mani_left:
    flip_off
    pause 0.5
    boo3
    pause 0.2
    slide_out_right_fast

transform pos_left_slight2:
    xanchor 0.5 yanchor 1.0
    xpos 190 ypos 1080

transform pos_center_slight2:
    xanchor 0.5 yanchor 1.0
    xpos 500 ypos 1080

transform pos_right_slight2:
    xanchor 0.5 yanchor 1.0
    xpos 780 ypos 1080

transform slide_left_slight2:
    xanchor 0.5 yanchor 1.0
    ease 0.4 xpos 190
    pos_left_slight2

transform slide_center_slight2:
    xanchor 0.5 yanchor 1.0  
    ease 0.4 xpos 500
    pos_center_slight2

transform slide_right_slight2:
    xanchor 0.5 yanchor 1.0
    ease 0.4 xpos 780
    pos_right_slight2

transform pos_in_left_fast2:
    xanchor 0.5 yanchor 1.0
    xpos 1150 ypos 1080

transform pos_in_left_slight:
    xanchor 0.5 yanchor 1.0
    xpos 1420 ypos 1080

transform pos_in_left_slight2:
    xanchor 0.5 yanchor 1.0
    xpos 1680 ypos 1080

transform slide_in_left_fast2:
    xanchor 0.5 yanchor 1.0
    xpos 2500 ypos 1080
    easein 0.3 xpos 1150
    pos_in_left_fast2

transform slide_in_left_slight:
    xanchor 0.5 yanchor 1.0
    xpos 2500 ypos 1080
    easein 0.4 xpos 1420
    pos_in_left_slight

transform slide_in_left_slight2:
    xanchor 0.5 yanchor 1.0
    xpos 2500 ypos 1080
    easein 0.4 xpos 1680

transform pos_of_left_to_center_fast:
    xanchor 0.5 yanchor 1.0
    xpos 500 ypos 1080

transform slide_of_left_to_center_fast:
    xanchor 0.5 yanchor 1.0
    xpos 1150 ypos 1080
    easein 0.2 xpos 500
    pos_of_left_to_center_fast

transform pos_left_move:
    xanchor 0.5 yanchor 1.0
    xpos 820 ypos 1080

transform slide_left_move:
    xanchor 0.5 yanchor 1.0
    xpos 500 ypos 1080
    easein 0.2 xpos 820
    pos_left_move

transform pos_left_move2:
    xanchor 0.5 yanchor 1.0
    xpos 1150 ypos 1080

transform slide_left_move2:
    xanchor 0.5 yanchor 1.0
    xpos 780 ypos 1080
    easein 0.2 xpos 1150
    pos_left_move2 


transform pos_of_left_to_center_fast:
    xanchor 0.5 yanchor 1.0
    xpos 500 ypos 1080

transform slide_of_left_to_center_fast:
    xanchor 0.5 yanchor 1.0
    xpos 1150 ypos 1080
    easein 0.2 xpos 500
    pos_of_left_to_center_fast

transform pos_left_move:
    xanchor 0.5 yanchor 1.0
    xpos 820 ypos 1080

transform slide_left_move:
    xanchor 0.5 yanchor 1.0
    xpos 500 ypos 1080
    easein 0.2 xpos 820
    pos_left_move

transform pos_left_move2:
    xanchor 0.5 yanchor 1.0
    xpos 1150 ypos 1080

transform slide_left_move2:
    xanchor 0.5 yanchor 1.0
    xpos 780 ypos 1080
    easein 0.2 xpos 1150
    pos_left_move2 

transform pos_center_to_left_move3:
    xanchor 0.5 yanchor 1.0
    xpos 525 ypos 1080

transform slide_center_to_left_move3:
    xanchor 0.5 yanchor 1.0
    xpos 820 ypos 1080
    easein 0.2 xpos 525
    pos_center_to_left_move3

transform pos_of_left_to_center:
    xanchor 0.5 yanchor 1.0
    xpos 850 ypos 1080

transform slide_of_left_to_center:
    xanchor 0.5 yanchor 1.0
    xpos 500 ypos 1080
    easein 0.2 xpos 850
    pos_of_left_to_center

transform pos_of_left_to_center3:
    xanchor 0.5 yanchor 1.0
    xpos 1150 ypos 1080

transform slide_of_left_to_center3:
    xanchor 0.5 yanchor 1.0
    xpos 835 ypos 1080
    easein 0.2 xpos 1150
    pos_of_left_to_center3

transform pos_of_center_to_left2:
    xanchor 0.5 yanchor 1.0
    xpos 840 ypos 1080

transform slide_of_center_to_left2:
    xanchor 0.5 yanchor 1.0
    xpos 1000 ypos 1080
    easein 0.2 xpos 840
    pos_of_center_to_left2

##### PARPADEO

image blink = "images/blink/blink.png"
image blink0 = "images/blink/blink_0.png"
image blink1 = "images/blink/blink_1.png"
image blink2 = "images/blink/blink_2.png"
image blink3 = "images/blink/blink_3.png"
image blink4 = "images/blink/blink_4.png"
image blink5 = "images/blink/blink_5.png"
image blink6 = "images/blink/blink_6.png"

image parpadeo_on:
    "blink0"
    pause 0.05
    "blink1"
    pause 0.05
    "blink2"
    pause 0.05
    "blink3"
    pause 0.05
    "blink4"
    pause 0.05
    "blink5"
    pause 0.05
    "blink6"

image parpadeo_off:
    "blink6"
    pause 0.05
    "blink5"
    pause 0.05
    "blink4"
    pause 0.05
    "blink3"
    pause 0.05
    "blink2"
    pause 0.05
    "blink1"
    pause 0.05
    "blink0"
    pause 0.05
    "blink"

image parpadeo_off2:
    "blink6"
    pause 0.08
    "blink5"
    pause 0.08
    "blink4"
    pause 0.08
    "blink3"
    pause 0.08
    "blink2"
    pause 0.08
    "blink1"
    pause 0.08
    "blink0"
    pause 0.08
    "blink"

######################## Posiciones #############################

transform flip:
        xzoom -1.0

transform flip_off:
        xzoom 1.0

transform left:
    xpos 400 ypos 1080
    xanchor 0.5 yanchor 1.0

transform left5:
    xpos 460 ypos 1080
    xanchor 0.5 yanchor 1.0

transform left_littemove:
    xanchor 0.5 yanchor 1.0
    xpos 400 ypos 1080
    easein 0.3 xpos 350

transform left_littemove1:
    xanchor 0.5 yanchor 1.0
    xpos 350 ypos 1080
    easein 0.3 xpos 460

transform left_littemoveon:
    flip
    boo
    pause 1.5
    left_littemove

transform left_littemoveoff:
    flip_off 
    pause 0.5
    boo
    left_littemove1

transform center:
    xpos 960 ypos 1080  
    xanchor 0.5 yanchor 1.0

transform center2:
    xpos 995 ypos 1080  
    xanchor 0.5 yanchor 1.0

transform center_flip:
    flip
    xpos 960 ypos 1080  
    xanchor 0.55 yanchor 1.0

transform right:
    xpos 1520 ypos 1080 
    xanchor 0.5 yanchor 1.0

transform right5:
    xpos 1555 ypos 1080 
    xanchor 0.5 yanchor 1.0

transform right6:
    xpos 1610 ypos 1080
    xanchor 0.5 yanchor 1.0

transform right2:
    xpos 1680 ypos 1080 
    xanchor 0.5 yanchor 1.0

transform right4:
    xpos 1600 ypos 1080 
    xanchor 0.5 yanchor 1.0

transform right1:
    xpos 1200

transform left1:
    xpos 735

transform right3:
    xpos 1200 ypos 1080 
    xanchor 0.5 yanchor 1.0

transform left3:
    xpos 735 ypos 1080 
    xanchor 0.5 yanchor 1.0

transform outwalk_right3:
    xpos 740 ypos 1080 
    xanchor 0.5 yanchor 1.0
    parallel:
        ease 3.0 xpos 2500 
    parallel:
        block:
            ease 0.07 yoffset 15
            ease 0.21 yoffset 0
            repeat 9
        yoffset 0

transform outwalk_right4:
    xpos 960 ypos 1080 
    xanchor 0.5 yanchor 1.0
    parallel:
        ease 8.0 xpos 2500 
    parallel:
        block:
            ease 0.6 yoffset 15
            ease 0.31 yoffset 0
            repeat 11
        yoffset 0

transform inwalk_left_toright:
    xanchor 0.5 yanchor 1.0 
    xpos -300 ypos 1080 
    
    parallel:
        ease 5.0 xpos 735
    parallel:
        block:
            ease 0.1 yoffset 15
            ease 0.35 yoffset 0
            repeat 11
        yoffset 0

transform inwalk_right_toleft:
    xanchor 0.5 yanchor 1.0
    xpos 2220 ypos 1080 
    
    parallel:
        ease 5.0 xpos 1200
    parallel:
        block:
            ease 0.1 yoffset 15
            ease 0.35 yoffset 0
            repeat 11
        yoffset 0

transform anim_center:
    xpos 1200 ypos 1080 
    xanchor 0.5 yanchor 1.0

    parallel:
        ease 0.5 xpos 960

transform walking_center:
    xanchor 0.5 yanchor 1.0 
    xpos 960 ypos 1080 

    parallel:
        block:
            ease 0.8 yoffset 13
            ease 0.45 yoffset 0
            repeat
        yoffset 0


######################## CBG ###############################

image math = Movie(play="cbg/math.webm")
image cbg_dark = Movie(play="cbg/dark.webm")
image cbg_st_tv = Movie(play="cbg/tv_and_struke.webm")
image cbg_dirc = Movie(play="cbg/director.webm")
image cbg_b_ptod = Movie(play="cbg/blaze_and_ptod.webm")
image cbg_bz = Movie(play="cbg/blaze.webm")

######################## Background ##############################

### Laila's House 

image out_house_d = "images/bg/laila_house/out_house_day.png"
image out_house_e = "images/bg/laila_house/out_house_evening.png"
image out_house_n = "images/bg/laila_house/out_house_night.png"
image kitchen = "images/bg/laila_house/kitchen.png"
image livingroom_d = "images/bg/laila_house/livingroom_day.png"
image livingroom_l = "images/bg/laila_house/livingroom_lights.png"
image livingroom_n = "images/bg/laila_house/livingroom_dark.png"
image lailaroom_d = "images/bg/laila_house/lailaroom_day.png"
image lailaroom_l = "images/bg/laila_house/lailaroom_lights.png"
image lailaroom_n = "images/bg/laila_house/lailaroom_night.png"

### City

image intersection_night = "images/bg/intersection_night.jpg"
image intersection_day = "images/bg/intersection_day.jpg"
image intersection_afternoon = "images/bg/intersection_afternoon.jpg"
image bus = "images/bg/bus.png"
image sky = "images/bg/sky_bg.png"

### School

image pasillo = "images/bg/9k.jpg"
image pasillo2 = "images/bg/pasillo2.png"
image pasillo_2dopiso = "images/bg/pasillo-piso2.png"
image stairs_2dopiso = "images/bg/escaleras-piso2.png"
image azotea = "images/bg/azotea.png"
image azotea_stairs = "images/bg/escalerasazotea.png"
image despacho_dirc = "images/bg/principals_office.png"
image consejo_day = "images/bg/consejo_day.jpg"
image consejo_afternoon = "images/bg/consejo_afternoon.jpg"


image pasillo-blur:
        "images/bg/9k.jpg"
        function apply_blur_gradually

image class3A = "images/bg/classroom 3-A.png"
image class3A-blur1:
    contains:  # Imagen base con blur
        "images/bg/classroom 3-A.png"
        blur 25
    contains:  # Borde superior
        Solid("#000000")
        ypos 0.0
        xsize 1920
        ysize 150
    contains:  # Borde inferior
        Solid("#000000")
        ypos 1.0
        anchor (0.0, 1.0)
        xsize 1920
        ysize 150
image class3A-blur: 
    "images/bg/classroom 3-A.png" 
    function waking_up_blur

image pasillo_extend = "images/bg/9k2.jpg"

image pasillo_walk:
    "pasillo_extend"
    xtile 2 subpixel True
    xoffset 0
    linear 30.0 xoffset -3840
    repeat

image pasillo_walking = Composite((1920, 1080), (0, 0), "pasillo_walk")

image bus_mask:
    "sky"
    xtile 2 subpixel True
    xoffset 0
    linear 15.0 xoffset -3840
    repeat

image bus_mask_sky = Composite((1920, 1080), (0, 0), "bus_mask")

image bus_shake:
    "bus"
    shake_bus

transform shake_bus:
    linear 0.1 xoffset -1 yoffset 2
    linear 0.1 xoffset 3 yoffset 0
    linear 0.1 xoffset -1 yoffset 2
    linear 0.1 xoffset 0 yoffset 0
    repeat

###################### EFECTOS ###############################

init python:

    def waking_up_blur(trans, st, at):
        if st < 3.5:  # Duración del efecto (3 segundos)
            blur_amount = 25 - (st * 8)  # Reduce el blur progresivamente (25 → 1)
            trans.blur = blur_amount
            return 0.01  # Actualiza cada 0.01 segundos
        else:
            trans.blur = 0  # Sin blur al final
            return None

    def waking_up_blur2(trans, st, at):
        if st < 8.0:
            blur_amount = 50 - (st * 8)
            trans.blur = blur_amount
            return 0.01
        else:
            trans.blur = 0
            return None

    def apply_blur_gradually(trans, st, at):
        if st < 3.5:  # Duración del efecto (3.5 segundos)
            blur_amount = st * 5 
            trans.blur = blur_amount
            return 0.05  # Actualiza cada 0.01 segundos
        else:
            trans.blur = 17.5  # Blur final (puedes ajustar este valor)
            return None

    def apply_blur_gradually2(trans, st, at):
        if st < 3.5:
            blur_amount = st * 2 
            trans.blur = blur_amount
            return 0.01
        else:
            trans.blur = 7 
            return None

    def apply_blur_gradually3(trans, st, at):
        if st < 0.0:
            blur_amount = st * 2 
            trans.blur = blur_amount
            return 0.0
        else:
            trans.blur = 7
            return None

image vignette:
    "images/vignette.png"

init python:
    def apply_filter_with_fade(channel="music", target_filters=None, duration=2.0):
        if target_filters is None:
            target_filters = []

        start_time = renpy.display.core.get_time()
        end_time = start_time + duration

        while renpy.display.core.get_time() < end_time:
            progress = (renpy.display.core.get_time() - start_time) / duration
            current_filters = []
            
            for filt in target_filters:
                if hasattr(filt, 'amount'):  # Reverb
                    current_filters.append(af.Reverb(filt.amount * progress))
                elif hasattr(filt, 'frequency'):  # Lowpass
                    current_hz = 22000 - (22000 - filt.frequency) * progress
                    current_filters.append(af.Lowpass(current_hz))
            
            renpy.music.set_audio_filter(channel, current_filters, replace=True)
            renpy.pause(0.01)  # Pausa mínima para actualizar

        # Asegurar que se apliquen los filtros finales
        renpy.music.set_audio_filter(channel, target_filters, replace=True)

transform black_pulse():
    alpha 0.0
    parallel:
        alpha 0.8
        linear 0.2 alpha 0.5
        0.1
        alpha 0.4
        linear 0.1 alpha 0.8
        alpha 0.0
        1.19
        repeat

screen pulse_black():
    add "#000000" at black_pulse

transform red_pulse():
    alpha 0.0
    easein 2.0 alpha 0.5

transform red_pulse2():
    alpha 0.5
    easein 1.0 alpha 0.2

screen red_effect():
    add "#f00" at red_pulse

screen red_effect2():
    add "#f00" at red_pulse2

transform semiblack_trans():
    alpha 0.0   
    easein 1.5 alpha 0.75

transform semiblack_trans2():
    alpha 0.0   
    easein 1.5 alpha 1.0

transform semiblack_trans3():
    alpha 5.0
    
screen semiblack():
    add "#000000" at semiblack_trans

screen vignette_screen():
    add "vignette" 

screen vignette_screen2():
    add "vignette" at semiblack_trans3

transform night_effect:
    matrixcolor TintMatrix("#4A6FC3") * BrightnessMatrix(-0.15) * SaturationMatrix(0.7)
    blur 0.7

transform night_urban:
    matrixcolor TintMatrix("#8A9BC9") * BrightnessMatrix(-0.15) * SaturationMatrix(0.6)
    blur 0.6
   
transform night_deep:
    matrixcolor TintMatrix("#5A75A5") * BrightnessMatrix(-0.3) * SaturationMatrix(0.9)
    blur 0.4

transform night_purple:
    matrixcolor TintMatrix("#7A88C9") * BrightnessMatrix(-0.25) * SaturationMatrix(0.7)
    blur 0.5

transform night_cold:
    matrixcolor TintMatrix("#6B82B5") * BrightnessMatrix(-0.35) * SaturationMatrix(0.85)
    blur 0.3

transform afternoon_filter:
    matrixcolor TintMatrix("#ffb347") * BrightnessMatrix(-0.10) * SaturationMatrix(0.7)

transform afternoon_character:
    matrixcolor TintMatrix("#FFA94D") * BrightnessMatrix(-0.08) * SaturationMatrix(0.85)

define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

define dissolve_scene_full2 = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(0.5),
    True])


######### AUDIOS Y MUSICA ################################

## Audio
define classroom = "audio/classroom.mp3"
define teens_laugh = "audio/teens_laugh.mp3"
define closet_open = "audio/closet-open.ogg"
define closet_close = "audio/closet-close.ogg"
define fall = "audio/fall.ogg"
define bell = "audio/bell.mp3"
define pushing_a_metal1 = "audio/pushing-a-metal1.ogg"
define ear_ringing = "audio/ear-ringing.mp3"
define miedomujere = "audio/miedoalamujere.ogg"
define car_horn = "audio/car-horn.mp3"
define open_car_door = "audio/open-car-door.mp3"
define close_car_door = "audio/close-car-door.mp3"
define light_switch = "audio/light-switch.mp3"
define door_knock = "audio/knock1.mp3"
define country_radio = "audio/country.mp3"
define radio_interference = "audio/radio-interference.mp3"
define drop = "audio/drop.ogg"
define keylock = "audio/key-lock-sound.wav"
define phone_quiet = "audio/phone_quiet.ogg"
define slam = "audio/slam.ogg"
define bus_arrive = "audio/bus-arrival.ogg"
define pageflip = "audio/pageflip.ogg"
define microwave = "<loop 3.191>sfx/microwave.ogg"

## Music
define bgm1 = "<from 0 to 198.425 loop 11.339>bgm/nude.ogg"
define bgm2 = "<from 0 to 244.653 loop 92.645>bgm/tinkertailor.ogg"
define bgm3 = "<from 0 to 163.997 loop 83.974>bgm/cutahole.ogg"
define bgm32 = "<from 163.997 to 246.980 loop 183.950>bgm/cutahole.ogg"
define bgm4 = "bgm/Tell_The_Truth.ogg"
define bgm5 = "bgm/kilobytes.ogg"
define bgm6 = "<from 0 to 113.814 loop 0.334>bgm/iwill.ogg"
define bgm7 = "<from 0 to 98.863 loop 7.353>bgm/illwind.ogg"
define bgm72 = "<from 98.863 to 209.976 loop 98.863>bgm/illwind.ogg"
define bgm8 = "<from 0 to 172.839 loop 130.263>bgm/presenttense.ogg"
define bgm82 = "<from 172.839 to 260.818 loop 180.981>bgm/presenttense.ogg"
define bgm9 = "<from 0 to 146.213 loop 12.346>bgm/setmyselfonfire.ogg"
define bgm10 = "<from 0 to 231.849 loop 126.526>bgm/thenumbers.ogg"

## Ambient
define ext_day = "<loop 3.090>ambient/ext_day.ogg"
define ext_night = "<loop 4.103>ambient/ext_night.ogg"
define int_day = "<loop 3.090>ambient/int_day.ogg"
define int_night = "<loop 4.103>ambient/int_night.ogg"
define fountain = "<loop 1.801>ambient/fountain.ogg"
define bus = "<loop 3.247>ambient/bus.ogg"
define wind = "<loop 2.069>ambient/wind.ogg"
define clifftop = "<loop 0.000>ambient/clifftop.ogg"
define rain_ext = "<loop 2.094>ambient/rain_ext.ogg"
define rain_int = "<loop 2.102>ambient/rain_int.ogg"


init python:
    renpy.music.register_channel("heartbeat", "sfx", loop=True)
    renpy.music.register_channel("ambient", "ambient", True)

######### EXTRAS ################################

screen phone_button:
    zorder 200
    imagebutton:
        idle Transform("gui/cell_button.png")
        hover Transform("gui/cell_button_hover.png")
        at fade_transform
        action If(
            not persistent.phone_tutorial_seen,
            Call("celu_tutorial"),
            PhoneMenu('phone')
            )
        xalign 0.99
        yalign 0.99
        
transform fade_transform:
    on hover:
        linear 0.2 alpha 1.0
    on idle:
        linear 0.2 alpha 0.7

######### SE USARAN DESPUES ################################

image struke = "images/characters/struke.png"
#image counter = "images/characters/counter.png"
image jasper1 = "images/characters/jasper.png"