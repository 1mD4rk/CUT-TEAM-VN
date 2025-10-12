screen phone_savegame():
    use _phone():
        style_prefix "phone_saveload"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Save Game") xalign 0.5 text_align 0.5
            use phone_saveload("save")

screen phone_loadgame():
    use _phone():
        style_prefix "phone_saveload"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Load Game") xalign 0.5 text_align 0.5
            use phone_saveload("load")

screen phone_saveload(which):
    default page_name_value = FilePageNameInputValue()
    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        # The page name, which can be edited by clicking on a button.

        viewport:
            draggable True
            mousewheel True
            yfill True
            vbox:
                null height 20
                style_prefix "phone_slot"

                xalign 0.03
                yalign 0

                spacing 0

                for i in range(1 * 30):

                    $ slot = i + 1
                    
                    button:
                        if which == "save":
                            action [Hide("phone"), FileSave(slot), Show("phone_savegame")]
                        if which == "load":
                            action FileLoad(slot)
                        hbox:
                            xsize 340
                            null width 8
                            viewport:
                                xsize 130
                                xalign 0.0
                                null height 7
                                yalign 0.5
                                add FileScreenshot(slot):
                                    xalign 0
                                    zoom 0.3
                                text FileSlotName(slot, 30):
                                    style "phone_page_label_text"
                                    xalign 0.06
                                    yalign 0.11

                            viewport:
                                ysize 70
                                key "save_delete" action FileDelete(slot)
                                imagebutton:
                                    xalign 0.0
                                    yalign 0.4
                                    idle phone.config.basedir + "button.png"
                                    hover phone.config.basedir + "hoverbutton.png"
                                    insensitive phone.config.basedir + "nonebutton.png"
                                    action FileDelete(slot)
                                text FileSaveName(slot):
                                    style "phone_slot_time_text2"
                                    yalign 0.5
                                    xalign 0.97
                                text FileTime(slot, format=_("{#file_time}%b %d %Y, %H:%M"), empty=_("empty slot")):
                                    style "phone_slot_time_text"
                                    yalign 0.5
                                    xalign 0.97


style phone_page_label is gui_label
style phone_page_label_text is gui_label_text
style phone_page_button is gui_button
style phone_page_button_text is gui_button_text

style phone_slot_button is empty
style phone_slot_button_text is empty
style phone_slot_time_text is phone_slot_button_text

style phone_slot_time_text2 is phone_slot_time_text:
    textalign 1.0
    size 15

style phone_slot_name_text is phone_slot_button_text

style phone_page_label:
    xpadding 10
    ypadding 1

style phone_page_label_text:
    color "#000"
    outlines [(2, "#fff", 0, 0), (1, "#fff", 1, 1)]
    size 22

style phone_page_button:
    outlines []

style phone_page_button_text:
    outlines []

style phone_slot_button:
    xsize 120
    ysize 88
    idle_background Frame("gui/button/slot_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/slot_hover_background.png", gui.choice_button_borders)

style phone_slot_button_text:
    color "#666"
    size 17
    font (phone.config.basedir + "Aller_Rg.ttf")
    outlines []

init python:
    import string
    def Namer(name):
        store.save_name = name

style phone_save_input is empty:
    color "#000"
    text_align 0.5