label day3:
    $ discord.set(details="Wednesday - (17/02/2066)", state="Day 3")
    $ phone.system.battery_level = 95

    scene black with fade
    $ renpy.pause(1.0, hard=True)
    play ambient bus fadein(2.0)
    show bus_mask_sky
    show bus_shake
    show blaze 1desinteresada:
        flip
        size (1000, 1300)
        xalign 0.1
        yalign 0.25
        shake_bus
    with dissolve
    $ renpy.pause(10.0, hard=True)
    "..."
    show blaze 1felizt
    b "Hey! Look outside!"