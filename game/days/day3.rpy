label day3:
    play sound closet_open
    $ renpy.pause(1.0, hard=True)
    scene azotea with fade
    play ambient ext_day fadein(2.0)
    play sound closet_close
    $ renpy.pause(1.0, hard=True)
    show screen pulse_black
    show dark 1feli:
        left
    show jeremy 1juzga:
        flip
        right5
    "si"
    show jeremy 2juzga
    "si"

    return