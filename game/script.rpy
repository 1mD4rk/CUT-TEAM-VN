image phone_wallpaper = "phone/assets/phone_wallpaper.png" 
image capa_personalizada = "phone/assets/roto.png"

label start:
    $ phone.data[store.pov_key]["background_image"] = "phone_wallpaper"
    stop music fadeout 4.0 
    scene black with Dissolve(5.0)

    call day1 from _call_day1
    $ renpy.pause(10.0, hard=True)

    call day2 from _call_day2
    $ renpy.pause(10.0, hard=True)
    
    call day3 from _call_day3
    $ renpy.pause(10.0, hard=True)

    return