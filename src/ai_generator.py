from transformers import DistilBertTokenizer, TFDistilBertForQuestionAnswering
import tensorflow as tf


class Preguntas_Chat:    
    respuesta__default = "Esa información al parecer no está disponible dentro del contexto dado. ¿Requiere entrenar un modelo personalizado?"
  
    def __init__(self, modelo="distilbert-base-uncased-distilled-squad", tokenizer="distilbert-base-uncased-distilled-squad"):
        self.__tokenizer = DistilBertTokenizer.from_pretrained(tokenizer)        
        self.__modelo = TFDistilBertForQuestionAnswering.from_pretrained(modelo)
        self.__respuesta = str()
        self.__contexto = str()
        print(f"Utilizando:\n\n[Tokenizador\t:\t{tokenizer}]\n[Modelo\t\t:\t{modelo}]")

    def get_respuesta_default(self) -> str:
        return self.respuesta__default

    def get_tokenizer(self):
        return self.__tokenizer
    
    def get_model(self):
        return self.__modelo

    def get_contexto(self) -> str:
        return self.__contexto

    def get_respuesta(self) -> str:
        return self.__respuesta
    
    def nuevo_contexto(self,contexto:str):
        self.__contexto = contexto
    
    def nueva_pregunta(self,pregunta:str, imprimir=False):
        try:
            inputs = self.get_tokenizer()(pregunta, self.get_contexto(), return_tensors="tf")
            outputs = self.get_model()(**inputs)
            answer_start_index = int(tf.math.argmax(outputs.start_logits, axis=-1)[0])
            answer_end_index = int(tf.math.argmax(outputs.end_logits, axis=-1)[0])
            prediccion_codificada = inputs.input_ids[0, answer_start_index : answer_end_index + 1]
            self.__respuesta = self.get_tokenizer().decode(prediccion_codificada)
            if self.__respuesta == "" or self.__respuesta == "[CLS]":
                self.__respuesta = self.get_respuesta_default()
        except Exception as e:
            print(e)
        finally:
            if imprimir == True:
                print(f"[Pregunta]:\t{pregunta}")
                print(f"[Respuesta]:\t{self.__respuesta}")
