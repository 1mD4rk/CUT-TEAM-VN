label day3:
    $ discord.set(details="Wednesday - (17/02/2066)", state="Day 3")
    $ phone.system.battery_level = 95
    $ contador = 0

    call scene1_day3
    $ renpy.pause(2.0, hard=True)
    call scene2_day3
    $ renpy.pause(5.0, hard=True)
    call scene3_day3
    $ renpy.pause(5.0, hard=True)
    call scene4_day3
    $ renpy.pause(4.0, hard=True)
    call scene5_day3
    $ renpy.pause(4.0, hard=True)
    call scene6_day3
    $ renpy.pause(2.0, hard=True)
    call scene7_day3
    $ renpy.pause(4.0, hard=True)   
    call scene8_day3 

return

    