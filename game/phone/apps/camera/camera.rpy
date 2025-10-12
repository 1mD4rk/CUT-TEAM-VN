init python:
    import os
    import datetime
    from store import phone, config

    class CameraApp:
        def __init__(self):
            self.save_dir = os.path.join(config.basedir, "screenshots")
            if not os.path.exists(self.save_dir):
                os.makedirs(self.save_dir)
            self.capture_sound = phone.asset("camera_shutter.wav")

        def take_screenshot(self):
            try:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = os.path.join(self.save_dir, f"captura_{timestamp}.png")
                
                renpy.screenshot(filename)
                
                if not os.path.exists(filename):
                    raise Exception("El archivo no se creó")
                
                renpy.play(self.capture_sound, channel="sound")
                renpy.notify(_("¡Captura guardada correctamente!"))
                return True
                
            except Exception as e:
                renpy.notify(_("Error al capturar: {}").format(str(e)))
                return False

    if not hasattr(store, 'camera_app_instance'):
        store.camera_app_instance = CameraApp()

screen phone_camera_save():
    zorder 100
    # Eliminamos use _phone() para quitar la interfaz del teléfono
    
    # Solo mostramos los controles de la cámara
    frame:
        style "camera_control_bar"
        background "#00000080"
        yalign 1.0  # Posicionamos en la parte inferior
        xfill True
        
        hbox:
            style "camera_controls"
            xalign 0.5
            
            textbutton _("Galería"):
                action PhoneMenu("phone_gallery")
                style "camera_button"
            
            button:
                style "camera_capture_button"
                background Transform(
                    phone.asset("circle.png"),
                    zoom=0.7,
                    align=(0.5, 0.5)
                )
                hover_background Transform(
                    phone.asset("circle.png"),
                    matrixcolor=BrightnessMatrix(0.2),
                    zoom=0.7,
                    align=(0.5, 0.5)
                )
                action Function(store.camera_app_instance.take_screenshot)
            
            textbutton _("Salir"):
                action PhoneReturn()
                style "camera_button"

style camera_control_bar is empty:
    background "#00000000"  # Fondo completamente transparente
    xfill True
    ysize 100
    yalign 1.0
    padding (10, 10)

style camera_controls is empty:
    xalign 0.5
    yalign 0.5
    spacing 15

style camera_button is empty:
    padding (10, 50)
    font phone.asset("Aller_Rg.ttf")
    color "#FFFFFF"
    hover_color "#AAAAAA"
    selected_color "#FFFFFF"

style camera_capture_button is empty:
    background None
    hover_background None
    xysize (59, 60)
    yalign 0.5