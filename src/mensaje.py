class Mensaje():
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type

class TipoMensaje:
    chat_msg = "chat_message"
    login_msg = "login_message"

    