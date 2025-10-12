default pc_sk  = phone.character.Character("SkyHub", phone.asset("skyhub_icon.png"), "sk", 22, "#096092")
default pc_laila  = phone.character.Character("Laila", phone.asset("default_icon.png"), "la", 22, "#c7c7c7")
default pc_counter  = phone.character.Character("Papá", phone.asset("default_icon.png"), "coun", 22, "#554c4c")
default pc_blaze  = phone.character.Character("Blaze", phone.asset("default_icon.png"), "bz", 22, "#da7603")

default dad_gc = phone.group_chat.GroupChat("Papá", phone.asset("default_icon.png"), "dad_la"). add_character("coun").add_character("la")
default bz_gc = phone.group_chat.GroupChat("Blaze", phone.asset("default_icon.png"), "bz_la"). add_character("bz").add_character("la")

init phone register dad_gc:
    time month 1 day 1 year 2066 hour 1 minute 1
    "coun" "hola"
    "la" "..."

init phone register bz_gc:
    time month 1 day 1 year 2066 hour 1 minute 1
    "bz" "W<W"
    "la" "..."

label chat_blaze:
    phone discussion "bz_la":
        "bz" "si"
        "la" "si"
    phone end discussion

    return