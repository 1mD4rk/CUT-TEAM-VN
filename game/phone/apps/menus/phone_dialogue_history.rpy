init python:
    def filter_text_tags(s, allow=None, deny=None):
        """
        Filtra etiquetas de texto de Ren'Py del string proporcionado.
        """
        if allow is None:
            allow = set()
        if deny is None:
            deny = set()
            
        import re
        # Patrón para encontrar etiquetas de texto
        tag_pattern = re.compile(r'\{.*?\}|\[.*?\]|\\.')
        
        def replace_tag(m):
            tag = m.group(0)
            # Si es una etiqueta permitida, la dejamos
            if tag in allow:
                return tag
            # Si es una etiqueta denegada, la eliminamos
            if tag in deny:
                return ""
            # Por defecto eliminamos todas las etiquetas
            return ""
            
        return tag_pattern.sub(replace_tag, s)

screen phone_dialogue_history():
    predict False
    use _phone():
        style_prefix "phone_history"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("History") xalign 0.5 text_align 0.5
            viewport:
                yinitial 1.0
                draggable True
                mousewheel True
                yfill False
                frame:
                    vbox:
                        for h in _history_list:
                            window:
                                has fixed:
                                    yfit True
                                if h.who:
                                    label h.who:
                                        style "phone_history_name"
                                null height 4
                                $ what = filter_text_tags(h.what, allow=set([]))
                                text what:
                                    substitute False
                            null height 10
                        if not _history_list:
                            label _("The dialogue history is empty.")


style phone_history_window is empty

style phone_history_name is empty
style phone_history_name_text is empty
style phone_history_text is empty

style phone_history_text is empty

style phone_history_label is empty
style phone_history_label_text is empty

style phone_history_window:
    xfill True
    ysize gui.history_height
    background "#fff"

style phone_history_frame:
    background "#fff"

style phone_history_vbox:
    background "#fff"
    spacing 2

style phone_history_viewport:
    background "#fff"

style phone_history_name:
    xalign 0.0
    xanchor 0
    xpos 0
    yoffset 0
    ysize 10

style phone_history_name_text:
    min_width gui.history_name_width
    font phone.config.basedir + "Aller_Rg.ttf"
    text_align 0.0
    outlines [ ]
    color "#525252"
    size 15

style phone_history_text:
    xalign 0.0
    outlines [ ]
    color "#000000"
    size 18
    font phone.config.basedir + "Aller_Rg.ttf"
    xpos 0
    yoffset 16
    xanchor 0
    text_align 0
    layout ("subtitle" if gui.history_text_xalign else "tex")

style phone_history_label:
    xfill True

style phone_history_label_text:
    xalign 0.0
    outlines [ ]
    color "#525252"
    size 15
    font phone.config.basedir + "Aller_Rg.ttf"