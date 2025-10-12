init python:
    def RoundedFrame(child, radius=15.0, outline_width=0, outline_color="#000"):
        return Frame(
            Transform(child, corner_radius=radius),
            left=radius, top=radius, right=radius, bottom=radius,
            tile=False
        )

screen phone_settings():
    use _phone():
        style_prefix "phone_settings"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Settings") xalign 0.5 text_align 0.5
            viewport:
                draggable True
                mousewheel True
                yfill True
                frame:
                    vbox:
                        null height 10
                        text _("SALTAR")
                        null height 4
                        hbox:
                            xfill True
                            style_prefix "phone_settings2"
                            text _("Texto no visto") yalign 0.5
                            imagebutton:
                                xalign 1.0 yalign 0.5
                                idle (phone.config.basedir + "settings1.png")
                                selected_idle (phone.config.basedir + "settings3.png")
                                hover (phone.config.basedir + "settings2.png")
                                selected_hover (phone.config.basedir + "settings4.png")
                                action Preference("skip", "toggle")
                        null height 4
                        hbox:
                            xfill True
                            style_prefix "phone_settings2"
                            text _("Tras elecciones") yalign 0.5
                            imagebutton:
                                xalign 1.0 yalign 0.5
                                idle (phone.config.basedir + "settings1.png")
                                selected_idle (phone.config.basedir + "settings3.png")
                                hover (phone.config.basedir + "settings2.png")
                                selected_hover (phone.config.basedir + "settings4.png")
                                action Preference("after choices", "toggle")
                        null height 30
                        null height 4
                        text _("VELOC. TEXTO")
                        bar value Preference("text speed") xsize 330
                        null height 2
                        null height 2
                        text _("VELOC. AUTO")
                        bar value Preference("auto-forward time") xsize 330
                        null height 4
                        null height 30
                        text _("VOLUMEN MÚSICA")
                        bar value Preference("music volume") xsize 330
                        null height 2
                        null height 2
                        text _("VOLUMEN SONIDO")
                        bar value Preference("sound volume") xsize 330
                        null height 2
                        null height 2
                        text _("VOLUMEN SONIDOS DE TEXTO")
                        bar value FieldValue(preferences, "text_sound_volume", range=1.0) xsize 330 style "phone_settings_slider"
                        text _("VOLUMEN DE AMBIENTE")
                        bar value Preference("ambient volume") xsize 330 style "phone_settings_slider"
                        null height 2
                        null height 2
                        hbox:
                            xfill True
                            style_prefix "phone_settings2"
                            text _("Silenciar TODO") yalign 0.5
                            imagebutton:
                                xalign 1.0 yalign 0.5
                                idle (phone.config.basedir + "settings1.png")
                                selected_idle (phone.config.basedir + "settings3.png")
                                hover (phone.config.basedir + "settings2.png")
                                selected_hover (phone.config.basedir + "settings4.png")
                                action Preference("all mute", "toggle")
                        null height 34
                        if renpy.variant("pc"):
                            hbox:
                                xfill True
                                style_prefix "phone_settings2"
                                text _("Pantalla completa") yalign 0.5
                                imagebutton:
                                    xalign 1.0 yalign 0.5
                                    idle (phone.config.basedir + "settings1.png")
                                    selected_idle (phone.config.basedir + "settings3.png")
                                    hover (phone.config.basedir + "settings2.png")
                                    selected_hover (phone.config.basedir + "settings4.png")
                                    action Preference("display", "toggle")
                        null height 34

style phone_settings_side is phone_contacts_side
style phone_settings_frame is phone_contacts_frame
style phone_settings_vbox is phone_contacts_vbox
style phone_settings_button is phone_contacts_button:
    idle_background Frame(Solid("#eeeeee"), left=15, top=15, right=15, bottom=15)
    hover_background Frame(Solid("#b4b4b4"), left=15, top=15, right=15, bottom=15)
    ysize 34

style phone_settings_fixed is empty
style phone_settings_hbox is phone_contacts_hbox
style phone_settings_text is phone_contacts_text:
    outlines [ ]
    color "#525252"
    size 15
    font phone.config.basedir + "Aller_Rg.ttf"
    
style phone_settings is empty
style phone_settings2 is empty
style phone_settings2_text is phone_contacts_text:
    color "#000"
    size 18

style phone_settings_slider:
    ysize 35
    base_bar Frame(phone.config.basedir + "settings_bar.png")
    thumb (phone.config.basedir + "settings_thumb.png")

#color picker by Feniks

#set these to true in the script to allow changing their colors
default sayoritexted = False
default monikatexted = False
default yuritexted = False
default natsukitexted = False

screen color_picker():
    use _phone():
        style_prefix "phone_settings"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Message Colors") xalign 0.5 text_align 0.5

            viewport:
                yfill True
                frame:
                    vbox:
                        null height 10
                        button:
                            action PhoneMenu("color_picker2", character="MC")
                            hbox:
                                xfill True
                                text _("[player]") xalign 0.0 yalign 0.5
                                text _(">") xalign 1.0 yalign 0.5
                        if sayoritexted:
                            button:
                                action PhoneMenu("color_picker2", character="Sayori")
                                hbox:
                                    xfill True
                                    text _("[s_name]") xalign 0.0 yalign 0.5
                                    text _(">") xalign 1.0 yalign 0.5
                        if monikatexted:
                            button:
                                action PhoneMenu("color_picker2", character="Monika")
                                hbox:
                                    xfill True
                                    text _("[m_name]") xalign 0.0 yalign 0.5
                                    text _(">") xalign 1.0 yalign 0.5
                        if yuritexted:
                            button:
                                action PhoneMenu("color_picker2", character="Yuri")
                                hbox:
                                    xfill True
                                    text _("[y_name]") xalign 0.0 yalign 0.5
                                    text _(">") xalign 1.0 yalign 0.5
                        if natsukitexted:
                            button:
                                action PhoneMenu("color_picker2", character="Natsuki")
                                hbox:
                                    xfill True
                                    text _("[n_name]") xalign 0.0 yalign 0.5
                                    text _(">") xalign 1.0 yalign 0.5
                    vbox:
                        yalign 0.97
                        button:
                            action Show("confirm", message="Are you sure you want to change the color of your messages? The script will reload.", yes_action=[Function(renpy.reload_script)], no_action=Hide("confirm"))
                            hbox:
                                xfill True
                                text _("Apply") xalign 0.0 yalign 0.5
                                text _(">") xalign 1.0 yalign 0.5


screen color_picker2(character="MC"):
    use _phone():
        style_prefix "phone_settings"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Message Colors") xalign 0.5 text_align 0.5

            viewport:
                yfill True
                frame:
                    ## The picker itself. Its size is 700x700 with the starting colour #ff8335.
                    ## You may declare this outside of the screen to make it easier to access;
                    default picker = ColorPicker(280, 280, "#000000")
                    ## The preview swatch. Needs to be provided the picker variable from above.
                    ## You can specify its size as well.
                    default picker_swatch = DynamicDisplayable(picker_color, picker=picker,
                        xsize=40, ysize=40)
                    ## The hexcode of the current colour. Demonstrates updating the picker
                    ## colour information in real-time.
                    default picker_hex = DynamicDisplayable(picker_hexcode, picker=picker)

                    style_prefix 'phone_cpicker' ## Simplifies some of the style property code

                    add "#21212d" ## The background

                    hbox:
                        xalign 0.5
                        yalign 0.1
                        vbox:
                            ## The picker itself
                            add picker
                            null height 10
                            ## A horizontal bar that lets you change the hue of the picker
                            bar value FieldValue(picker, "hue_rotation", 1.0)
                    vbox:
                        xsize 100 spacing 5 yalign 0.72
                        ## The swatch
                    
                        add picker_swatch

                    ## You can display other information on the color here, as desired
                    ## Some examples are provided. Note that these do not update in
                    ## tandem with the picker, but when the mouse is released. You
                    ## will need to use a DynamicDisplayable for real-time updates.
                    ## The hex code is provided as an example.

                        add picker_hex 

                    ## The DynamicDisplayable from earlier
                    ## These update when the mouse button is released
                    ## since they aren't a dynamic displayable
                    vbox:
                        spacing 4 xalign 0.9 yalign 0.72
                        text "R: [picker.color.rgb[0]:.2f]" 
                        text "G: [picker.color.rgb[1]:.2f]"
                        text "B: [picker.color.rgb[2]:.2f]"
                    hbox:
                        style_prefix "phone_settings"
                        yalign 0.88
                        text _(" Note: picking a color that is too bright will result \n in less readable text.")
                    vbox:
                        yalign 0.97
                        style_prefix "phone_settings"
                        if character == "MC":
                            button:
                                action [SetField(persistent, "playercolor", picker.color.hexcode), PhoneReturn()]
                                hbox:
                                    xfill True
                                    text _("Done") xalign 0.0 yalign 0.5
                                    text _(">") xalign 1.0 yalign 0.5
                        if character == "Sayori":
                            button:
                                action [SetField(persistent, "s_color", picker.color.hexcode), PhoneReturn()]
                                hbox:
                                    xfill True
                                    text _("Done") xalign 0.0 yalign 0.5
                                    text _(">") xalign 1.0 yalign 0.5
                        if character == "Monika":
                            button:
                                action [SetField(persistent, "m_color", picker.color.hexcode), PhoneReturn()]
                                hbox:
                                    xfill True
                                    text _("Done") xalign 0.0 yalign 0.5
                                    text _(">") xalign 1.0 yalign 0.5
                        if character == "Yuri":
                            button:
                                action [SetField(persistent, "y_color", picker.color.hexcode), PhoneReturn()]
                                hbox:
                                    xfill True
                                    text _("Done") xalign 0.0 yalign 0.5
                                    text _(">") xalign 1.0 yalign 0.5
                        if character == "Natsuki":
                            button:
                                action [SetField(persistent, "n_color", picker.color.hexcode), PhoneReturn()]
                                hbox:
                                    xfill True
                                    text _("Done") xalign 0.0 yalign 0.5
                                    text _(">") xalign 1.0 yalign 0.5

################################################################################
## Styles

style phone_cpicker_bar:
    xysize (300, 25)
    base_bar At(Transform("#000", xysize=(280, 25)), spectrum())
    thumb Transform("selector_bg", xysize=(16, 25))
    thumb_offset 10

style phone_cpicker_text:
    color "#fff"
    font phone.config.basedir + "Aller_Rg.ttf"

style phone_cpicker_frame is phone_settings_frame