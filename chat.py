import flet as ft

from custom.textos import Textos
from custom.colores import Colores

from src.ventana_chat import ChatMessage
from src.mensaje import Mensaje, TipoMensaje

from components.information_display import Display
from components.inputs_selections import Input


class Chat_App:
    def __init__(self,page):
        self.page = page
        self.page.horizontal_alignment = "stretch"
        self.page.title = Textos.titulo_app
        
        input_nuevo_usuario = Input.textfield(lbl=Textos.modal_mensaje,f=True,fn=self.unirse_al_chat)
        modal_bienvenido = ft.AlertDialog(open=True,modal=True,
                                    title=Display.texto(t=Textos.modal_bienvenido,
                                                        c=None,bgc=None,w=None),
                                    content=ft.Column([input_nuevo_usuario], 
                                                      width=300, height=70, tight=True),
                                    actions=[ft.ElevatedButton(text=Textos.btn_modal, 
                                                               on_click=self.unirse_al_chat)],
                                    actions_alignment="end")
        ventana_chat = ft.ListView(expand=True,spacing=10,auto_scroll=True)
        input_nuevo_mensaje = Input.textfield(lbl=None,h=Textos.nuevo_mensaje_hint,f=True,se=True, miL=1,mxL=5,fill=True,xp=True,fn=self.enviar_mensaje)

        self.nuevo_usuario = input_nuevo_usuario
        self.chat = ventana_chat
        self.nuevo_mensaje = input_nuevo_mensaje
        
        self.page.dialog = modal_bienvenido
        self.page.pubsub.subscribe(self.enviando_mensajes)
        self.page.add(ft.Container(content=self.chat,border=ft.border.all(1, ft.colors.OUTLINE),border_radius=5,padding=10,expand=True),
                ft.Row([self.nuevo_mensaje,ft.IconButton(icon=ft.icons.SEND_ROUNDED,tooltip=Textos.btn_tooltip,on_click=self.enviar_mensaje)]))


    def unirse_al_chat(self, e):
        if not self.nuevo_usuario.value:
            self.nuevo_usuario.error_text = Textos.nuevo_usuario_vacio
            self.nuevo_usuario.update()
        else:
            self.page.session.set("user_name", self.nuevo_usuario.value)
            self.page.dialog.open = False
            self.nuevo_mensaje.prefix = Display.texto(f"{self.nuevo_usuario.value}: ")
            self.page.pubsub.send_all(Mensaje(user_name=self.nuevo_usuario.value,
                                        text=Textos.bienvenido_usuario.format(usuario=self.nuevo_usuario.value),
                                        message_type=TipoMensaje.login_msg))
            self.page.update()

    def enviar_mensaje(self, e):
        if self.nuevo_mensaje.value != Textos.nuevo_mensaje_vacio:
            self.page.pubsub.send_all(Mensaje(user_name = self.page.session.get("user_name"), 
                                        text = self.nuevo_mensaje.value, 
                                        message_type=TipoMensaje.chat_msg))
            self.nuevo_mensaje.value = Textos.nuevo_mensaje_vacio
            self.nuevo_mensaje.focus()
            self.page.update()

    def enviando_mensajes(self, message: Mensaje):
        if message.message_type == TipoMensaje.chat_msg:
            m = ChatMessage(message)
        elif message.message_type == TipoMensaje.login_msg:
            m = Display.texto(t=message.text, i=True, c=Colores.texto_fondo_negro,s=12)
        self.chat.controls.append(m)
        self.page.update()
    
ft.app(target=Chat_App)