####################### REPUTACION ##########################

default relacion_counter = 0 
default relacion_blaze = 0
default relacion_dark = 0 
default relacion_jeremy = 0 
default relacion_steve = 0 
default relacion_mani = 0 

####################### TEXT SOUNDS ######################### CREDITOS: Bamboo Calculator
init python:
    import random
##############################################################################
# This function is optional. Only include it if you want automatic pauses between punctuation
    def typography(what):
        replacements = [
                ('. ','. {w=.2}'), # Moderate pause after periods
                ('? ','? {w=.25}'), # Long pause after question marks
                ('! ','! {w=.25}'), # Long pause after exclamation marks
                (', ',', {w=.15}'), # Short pause after commas
        ]
        for item in replacements:
            what = what.replace(item[0],item[1])
        return what
    config.say_menu_text_filter = typography # This ensures the text block has the same ID value, even after all the replacements are made
##############################################################################

##############################################################################
    # This function makes the continuous text sounds
    def laila_sound(event, interact=False, **kwargs):
        if event == "show": # If textbox is shown
            what = renpy.store._last_say_what # This grabs the text that was most recently spoken on-screen
            if what:
                sound_count = len(what)
            else:
                sound_count = 5
            for _ in range(sound_count): # This creates a sound queue based on how many characters are in the dialog block
                randosound = renpy.random.randint(1, 11) # This generates a random number between 1 and 11 inclusive. Change this based on how many sound files you have
                renpy.sound.queue(f"audio/sounds/laila_sounds/laila{randosound}.wav", channel="sound", loop=True, relative_volume=preferences.text_sound_volume) # Change "popcat" to the name of your sound file
        elif event == "end" or event == "slow_done": # This stops the text sounds if there is a pause in the dialog or the text has finished displaying
            renpy.sound.stop(channel="sound")

    def dark_sound(event, interact=False, **kwargs):
        if event == "show": 
            what = renpy.store._last_say_what
            if what:
                sound_count = len(what)
            else:
                sound_count = 5
            for _ in range(sound_count): 
                randosound = renpy.random.randint(1, 11)
                renpy.sound.queue(f"audio/sounds/dark_sounds/dark{randosound}.wav", channel="sound", loop=True, relative_volume=preferences.text_sound_volume)
        elif event == "end" or event == "slow_done":
            renpy.sound.stop(channel="sound")

    def blaze_sound(event, interact=False, **kwargs):
        if event == "show": 
            what = renpy.store._last_say_what
            if what:
                sound_count = len(what)
            else:
                sound_count = 5
            for _ in range(sound_count): 
                randosound = renpy.random.randint(1, 11)
                renpy.sound.queue(f"audio/sounds/blaze_sounds/blaze{randosound}.wav", channel="sound", loop=True, relative_volume=preferences.text_sound_volume)
        elif event == "end" or event == "slow_done":
            renpy.sound.stop(channel="sound")

    def counter_sound(event, interact=False, **kwargs):
        if event == "show": 
            what = renpy.store._last_say_what
            if what:
                sound_count = len(what)
            else:
                sound_count = 5
            for _ in range(sound_count): 
                randosound = renpy.random.randint(1, 11)
                renpy.sound.queue(f"audio/sounds/counter_sounds/counter{randosound}.wav", channel="sound", loop=True, relative_volume=preferences.text_sound_volume)
        elif event == "end" or event == "slow_done":
            renpy.sound.stop(channel="sound")

    def steve_sound(event, interact=False, **kwargs):
        if event == "show": 
            what = renpy.store._last_say_what
            if what:
                sound_count = len(what)
            else:
                sound_count = 5
            for _ in range(sound_count): 
                randosound = renpy.random.randint(1, 11)
                renpy.sound.queue(f"audio/sounds/steve_sounds/steve{randosound}.wav", channel="sound", loop=True, relative_volume=preferences.text_sound_volume)
        elif event == "end" or event == "slow_done":
            renpy.sound.stop(channel="sound")
    
    def strike_sound(event, interact=False, **kwargs):
        if event == "show": 
            what = renpy.store._last_say_what
            if what:
                sound_count = len(what)
            else:
                sound_count = 5
            for _ in range(sound_count): 
                randosound = renpy.random.randint(1, 11)
                renpy.sound.queue(f"audio/sounds/strike_sounds/strike{randosound}.wav", channel="sound", loop=True, relative_volume=preferences.text_sound_volume)
        elif event == "end" or event == "slow_done":
            renpy.sound.stop(channel="sound")
##############################################################################


################################DEFINICION DE LOS PERSONAJES###############################

define l = Character("Laila", 
    who_bold=True,
    who_outlines=[(4, "#6a5d7ac7", 0, 0)],  
    what_outlines = [(2, "#6a5d7ac7", 3, 3)],
    color="#ffff",
    callback=laila_sound)

define l_thought = Character(
    None,
    what_italic=True,
    what_outlines = [(3, "#272727", 0, 0)],
    what_prefix='"',
    what_suffix='"',
)

define nobody = Character(
    None,
    what_bold=True,
    who_outlines=[(4, "#ffffff", 0, 0)],  
    what_outlines = [(5, "#000000", 0, 0)],
    color="#1a1a1aff"
)

define d = Character("Dark", 
    who_bold=True,
    who_outlines=[(4, "#da0303", 0, 0)],  
    what_outlines = [(2, "#da0303", 3, 3)],
    color="#ffff",
    callback=dark_sound)

define je = Character("Jeremy", 
    who_bold=True,
    who_outlines=[(4, "#039dda", 0, 0)],  
    what_outlines = [(2, "#039dda", 3, 3)],
    color="#ffffff")

define b = Character("Blaze", 
    who_bold=True,
    who_outlines=[(4, "#da7603", 0, 0)],  
    what_outlines = [(2, "#da7603", 3, 3)],
    color="#ffffff",
    callback=blaze_sound)


define dad = Character("Papá", 
    who_bold=True,
    who_outlines=[(4, "#ffe1c76c", 0, 0)],  
    what_outlines = [(2, "#ffe1c76c", 3, 3)],
    color="#ffff",
    callback=counter_sound)

define m = Character("Manu", 
    who_bold=True,
    who_outlines = [(4, "#d3d3d3", 0, 0)],
    what_outlines = [(2, "#d3d3d3", 3, 3)],
    color="#ffffff")

define tv = Character("Steve", 
    who_bold=True,  
    who_outlines = [(4, "#805d12", 0, 0)],
    what_outlines = [(2, "#805d12", 3, 3)],
    color="#ffffff",
    callback=steve_sound)

define st = Character("Strike", 
    who_bold=True,  
    who_outlines = [(4, "#2634aa", 0, 0)],
    what_outlines = [(2, "#2634aa", 3, 3)],
    color="#ffffff",
    callback=strike_sound)

define ptod = Character("Prof. Todd", 
    who_bold=True,  
    who_outlines = [(4, "#5e5353", 0, 0)],
    what_outlines = [(2, "#5e5353", 3, 3)],
    color="#ffffff")

define dirc = Character("Director", 
    who_bold=True,  
    who_outlines = [(4, "#5d4037", 0, 0)],
    what_outlines = [(2, "#5d4037", 3, 3)],
    color="#ffffff")

define idk1 = Character("???", 
    who_bold=True,  
    who_outlines = [(4, "#707070", 0, 0)],
    what_outlines = [(2, "#707070", 3, 3)],
    color="#ffffff")

define idk2 = Character("??? 2", 
    who_bold=True,  
    who_outlines = [(4, "#333333", 0, 0)],
    what_outlines = [(2, "#333333", 3, 3)],
    color="#ffffff")

############################### POSES ###############################

init python:
    

    # Configuración para Dark 
    dark_bases = ["1", "2"]
    dark_expressions = ["desafiante", "desafiantet", 
                        "distraido", "distraidot",  "distraido2", "distraido2t",
                        "enojao", 
                        "neutral", "neutral2", "neutralt",
                        "feli", "felit",
                        "incomodo", "incomodot", "incomodo2", "incomodo2t",
                        "juzga", "juzgat", "juzga2", "juzga2t", "juzga3",
                        "serio", "seriot", "serio2", "serio2t"]
    for base in dark_bases:
        for expr in dark_expressions:
            renpy.image(
                f"dark {base}{expr}",
                im.Composite(
                    (864, 1152),
                    (0, 0), f"images/characters/dark/{base}.png",
                    (0, 0), f"images/characters/dark/{expr}.png"
                )
            )

    # Configuración para Jeremy 
    jeremy_bases = ["1", "2"]
    jeremy_expressions = ["feliz", "felizt",
                        "incomodo", "incomodot", "incomodo2", "incomodo2t", "incomodo3", "incomodo3t",
                        "juzga", "juzgat", "juzga2", "juzga2t",
                        "neutral", "neutralt",
                        "serio", "seriot", "serio2", "serio2t", "serio3", "serio3t",
                        "surprise", "surpriset"]
    for base in jeremy_bases:
        for expr in jeremy_expressions:
            renpy.image(
                f"jeremy {base}{expr}",
                im.Composite(
                    (864, 1152),
                    (0, 0), f"images/characters/jeremy/{base}.png",
                    (0, 0), f"images/characters/jeremy/{expr}.png"
                )
            )

    # Configuración para Bleiz
    bleis_bases = ["1", "2", "3"]
    bleis_expressions = ["desinteresada", "desinteresada2", "desinteresada3", "desinteresadat", "desinteresada2t", "desinteresada3t",
                        "enojada", "enojadat", "enojada2", "enojada2t",
                        "feliz", "felizt",
                        "juzga", "juzga2", "juzgat", "juzga2t",
                        "nerviosa", "nerviosat",
                        "neutral", "neutral2", "neutralt", "neutral2t",
                        "seria", "seria2", "seriat", "seria2t",
                        "sonriente", "sonrientet",
                        "compadecer", "compadecert",
                        "preocupada"]

    for base in bleis_bases:
        for expr in bleis_expressions:
            renpy.image(
                f"blaze {base}{expr}",
                im.Composite(
                    (864, 1152),
                    (0, 0), f"images/characters/blaze/{base}.png",
                    (0, 0), f"images/characters/blaze/{expr}.png"
                )
            )

    # Configuración para Counter
    counter_bases = ["1"]
    counter_expressions = ["enojao", "enojaot",
                        "feliz", "felizt",
                        "nosurprise", "nosurpriset", "surprise",
                        "serio", "seriot",
                        "compadecer", "compadecert"]
    for base in counter_bases:
        for expr in counter_expressions:
            renpy.image(
                f"counter {base}{expr}",
                im.Composite(
                    (864, 1152),
                    (0, 0), f"images/characters/counter/{base}.png",
                    (0, 0), f"images/characters/counter/{expr}.png"
                )
            )
    

    # Configuración para Steve 
    steve_bases = ["1", "2"]
    steve_expressions = ["neutral", "neutralt",
                        "amargado", "amargadot",
                        "remedar", "remedar2", "remedart", "remedar2t",
                        "rizz", "rizzt",
                        "sonriente", "sonrientet",
                        "triste", "triste2", "triste3", "tristet", "triste2t",
                        "juzga", "juzgat",
                        "enamorao",
                        "vacilante"]
    for base in steve_bases:
        for expr in steve_expressions:
            renpy.image(
                f"steve {base}{expr}",
                im.Composite(
                    (864, 1152),
                    (0, 0), f"images/characters/steve/{base}.png",
                    (0, 0), f"images/characters/steve/{expr}.png"
                )
            )

    # Configuración para Strike
    strike_bases = ["1"]
    strike_expressions = ["distraido", "distraidot", 
                        "enojado", "enojado2", "enojadot", "enojado2t",
                        "juzga", "juzgat", 
                        "serio", "seriot",
                        "sarcasmo", "sarcasmot"]
    for base in strike_bases:
        for expr in strike_expressions:
            renpy.image(
                f"strike {base}{expr}",
                im.Composite(
                    (864, 1152),
                    (0, 0), f"images/characters/strike/{base}.png",
                    (0, 0), f"images/characters/strike/{expr}.png"
                )
            )

    # Configuración para Todd 
    tod_bases = ["tieso", "cruzado"]
    for base in tod_bases:
            renpy.image(
                f"ptod {base}",
                im.Composite(
                    (864, 1152),
                    (0, 0), f"images/characters/todd/{base}.png",
                )
            )

    # Configuración para el Director 
    dirc_bases = ["tieso", "cintura", "hand_corbata"]
    for base in dirc_bases:
            renpy.image(
                f"dirc {base}",
                im.Composite(
                    (864, 1152),
                    (0, 0), f"images/characters/director/{base}.png",
                )
            )

