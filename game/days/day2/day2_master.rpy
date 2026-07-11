label day2:
    $ discord.set(details="Tuesday - (16/02/2066)", state="Day 2")
    $ phone.system.battery_level = 80
    #$ phone.system.date = datetime.date(2066, 2, 16)

    $ contador = 0

    call scene1_day2
    $ renpy.pause(5.0, hard=True)
    call scene2_day2
    $ renpy.pause(10.0, hard=True)
    call scene3_day2
    $ renpy.pause(10.0, hard=True)
    call scene4_day2
    $ renpy.pause(5.0, hard=True)
    call scene5_day2

return