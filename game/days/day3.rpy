label day3:
    play sound closet_open
    $ renpy.pause(1.0, hard=True)
    scene azotea with fade
    play ambient ext_day fadein(2.0)
    play sound closet_close
    $ renpy.pause(1.0, hard=True)
    show screen pulse_black
    show mani 1face
    show blaze 1neutral:
        right3
    $ renpy.pause(10.0, hard=True)
    return