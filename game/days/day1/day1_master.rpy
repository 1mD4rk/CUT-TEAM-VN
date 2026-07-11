label day1:
    $ discord.set(details="Monday - (15/02/2066)", state="Day 1")
    $ phone.system.battery_level = 100
    #$ phone.system.date = datetime.date(2066, 2, 15)

    $ contador = 0

    call scene1_day1
    $ renpy.pause(2.0, hard=True)
    call scene2_day1
    $ renpy.pause(4.0, hard=True)
    call scene3_day1
    call scene4_day1
    $ renpy.pause(6.0, hard=True)
    call scene5_day1
    $ renpy.pause(4.0, hard=True)
    call scene6_day1

return