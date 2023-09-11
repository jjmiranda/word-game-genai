import os
import openai
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.callbacks import get_openai_callback

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/process", methods=['GET'])
def process():
  args = request.args
  load_dotenv()
  openai_azure = os.getenv('OPENAI_AZURE', True)
  if openai_azure :
    openai.api_type = "azure"
    api_key = os.getenv('OPENAI_API_KEY_AZURE', 'YourAPIKeyIfNotSet')
    openai.api_key = api_key
    api_base = "https://dtilabperu.openai.azure.com/"
    openai.api_base = api_base
    api_version = "2023-05-15"
    openai.api_version = api_version  # subject to change
    deployment_id = "modelo0613pruebaDTI"
  else :
    openai.api_type = "open_ai"
    api_key = openai.api_key = os.getenv('OPENAI_API_KEY', 'YourAPIKeyIfNotSet')

  class CommaSeparatedListOutputParser(BaseOutputParser):
      """Parse the output of an LLM call to a comma-separated list."""
      def parse(self, text: str):
          """Parse the output of an LLM call."""
          return text.strip().split(", ")

  system_template = """Eres un experto generador de nuevas palabras y además clasificador de palabras para el juego de palabras dentro de la categoría: {category}.
  Un jugador te pasará una palabra y una lista de palabras.
  En una estructura JSON, en la llave 'nueva_palabra', asegurate de generar una palabra que NO esté en la lista de palabras que el jugador te pase,
  NO uses la palabra que te ha pasado el jugador y asegúrate que la lista con la nueva palabra que has generado no tenga ninguna palabra repetida.
  En la llave 'respuesta', tienes que responder con Si, si la palabra que te pasó el jugador entra dentro de la categoría: {category} y con No, si no entra en la categoría.
  También agrega a tu respuesta, en la llave 'porcentaje', el porcentaje que crees que la palabra que te pasó el jugador calza con la categoría: {category}."""
  system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
  human_template = "Palabra:{word}. Lista de palabras:{list}"
  human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

  llm=AzureChatOpenAI(openai_api_key = api_key, deployment_name=deployment_id,
                    openai_api_version=api_version, model_name="gpt-35-turbo",
                    openai_api_base=api_base, openai_api_type="azure")

  chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
  chain = LLMChain(
      llm=llm,
      prompt=chat_prompt,
      output_parser=CommaSeparatedListOutputParser()
  )
  # list = chain.run(category='Frutas', word= 'plato', list=['mandarina', 'naranja', 'maracuya', 'kiwi', 'uva', 'pera', 'mora', 'sandia', 'platano', 'banano', 'cerezas',
  #                  'aguaymanto', 'lucuma', 'guanábana', 'membrillo', 'ciruela', 'granadilla', 'frambuesa', 'guayaba', 'papaya', 'palta', 'piña', 'durazno', 'pitaya', 'fresa',
  #                  'manzana verde', 'manzana roja', 'manzana amarilla', 'mango verde', 'limón', 'uva blanca', 'coco', 'granada', 'lima', 'mora', 'zapote', 'mamey', 'cacao',
  #                  'chirimoya', 'melocontón', 'manzana', 'uva', 'mango', 'pomelo', 'melón', 'carambola', 'fruta de la pasión', 'mazorca', 'guanábana'])
  resp_json = chain.run(category=args.get("cat"), word=args.get("word"), list=[args.get("listado")])
  print(resp_json)
  return resp_json

if __name__ == "__main__":
  app.run(port=os.getenv('PORT', 80), debug=True)
