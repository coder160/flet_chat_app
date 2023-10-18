# Chat personal con IA, utilizando Python y Flet.


>Contenido:
>
>1.  [Guía Rápida](#guia-rapida)
>2.  [Procedimiento General](#procedimiento-general)
>3.  [Mas Información](#mas-informacion)
>


## <a name="guia-rapida"></a>Guía Rápida:

Linux:

0.  **Siempre es recomendable mantener al día el sistema operativo:**
``` bash
sudo apt-get update
```

1.  **Instalar la librería PIP para Python:**
``` bash
sudo apt-get install pip
```

2.  **Instalar la dependencia para Entornos Virtuales de Pip:**
``` bash
pip install pipenv
```

3.  **Descargar el Repositorio con el Código de la Aplicación:**
``` bash
git clone https://github.com/coder160/flet_chat_app.git
```

4.  **Navegar hasta la Ruta del Repositorio:**
``` bash
cd flet_chat_app
```

5.  **Instalar las Dependencias necesarias para la Aplicación:**
``` bash
pipenv install -r requirements.txt
```

6.  **Iniciar tu Aplicación con el siguiente Comando:**
``` bash
pipenv run flet run chat.py
```

## <a name="procedimiento-general"></a>**Procedimiento General:**

**Instalemos** la librería **Transformers** proporcionada por **[HuggingFace](https://huggingface.co)** directamente desde su repositorio oficial en **[GitHub](https://github.com/huggingface/transformers.git)**.

``` bash
pip install git+https://github.com/huggingface/transformers.git
```


Ahora **Iniciemos** la aplicación, utilizando el Modelo de Lenguaje Pre-entrenado **[distilbert-base-uncased-distilled-squad](https://huggingface.co/distilbert-base-uncased-distilled-squad)**.


*Basado en la documentación oficial **[Question Answering](https://huggingface.co/docs/transformers/tasks/question_answering)** proporcionado por **[HuggingFace](https://HuggingFace.co/)**.*


Crearemos una **clase** llamada ***Preguntas_Chat***, la cual iniciaremos con el *modelo* y *tokenizador* por default distilbert-base-uncased-distilled-squad'**

``` python
 class Preguntas_Chat:
     respuesta__default = "Esa información al parecer no está disponible dentro del contexto dado. ¿Requiere entrenar un modelo personalizado?"
     def __init__(self, modelo="distilbert-base-uncased-distilled-squad", tokenizer="distilbert-base-uncased-distilled-squad"):
         self.__tokenizer = DistilBertTokenizer.from_pretrained(tokenizer)        
         self.__modelo = TFDistilBertForQuestionAnswering.from_pretrained(modelo)
         self.__respuesta = str()
         self.__contexto = str()
```

**Definiremos** el contexto mediante la **funcion** llamada ***'nuevo_contexto'***:
``` python
     def nuevo_contexto(self,contexto:str):
         self.__contexto = contexto
```

**Definiremos** una **función** llamada ***'nueva_pregunta'***, la cual recibirá nuestra pregunta.
 
*Opcionalmente* podemos pedirle que imprima el resultado.
``` python 
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
```

**Iniciamos** nuestra **Aplicación**:
```python 
App = Preguntas_Chat()
```



## <a name="mas-informacion"></a>**Mas Información:**


Flet es una librería de Python basada en flutter para renderizar aplicaciones de escritorio, web, y móviles. 

>Mas información:
>
>[Flet Dev - https://flet.dev/](https://flet.dev/)



Este es un ejemplo rápido basado en la guía oficial:


[Creating realtime chat app in Python](https://flet.dev/docs/tutorials/python-realtime-chat)

[GitHub Realtime chat app in Python](https://github.com/flet-dev/examples/blob/main/python/tutorials/chat/chat.py)


