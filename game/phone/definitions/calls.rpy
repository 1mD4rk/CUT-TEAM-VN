define phone_bz  = Character("Blaze", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_la = Character("Laila", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")

label call_blaze: #call call_blaze
    hide screen phone_button with dissolve     
    phone call "bz"
    phone_bz "Ohayouuu!!!!!!!!!!!!!!!!"
    phone_la "Hey!"
    "Why is she always this energetic?"
    phone end call
    "..."
    show screen phone_button with dissolve
    return

label phone_video_call_blaze:
    scene pasillo onlayer phone_video_call
    show blaze 1felizt onlayer phone_video_call
    phone call "bz" video
    phone_bz "Hey! That's my room"
    phone end call
    "..."

    return