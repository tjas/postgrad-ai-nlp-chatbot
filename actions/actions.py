# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset

import re
import requests
import json

import logging
logger = logging.getLogger(__name__)

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ClearSlots(Action):

	def name(self) -> Text:
		return "action_clear_slots"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		#limpa slots do agendamento
		return [AllSlotsReset()]

class ConsultaCep(Action):

    # def __init__(self) -> None:
    #     super().__init__()
    #     logger = logging.getLogger(__name__)

    def name(self) -> Text:
	    return "action_submit_consultacep"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dict == parâmetro de entrada, de onde pega as variáveis de entrada
        # cep = dict['cep']

        try:
            # recebe dados dos slots
            cep = tracker.get_slot('cep')
            
            #mantem somente numeros
            r = re.compile(r'\D')
            cep = r.sub('', str(cep))
            
            logger.info(msg='Iniciando consulta para o CEP ' + str(cep))

            request = requests.get("https://viacep.com.br/ws/" + str(cep) + "/json")
            
            #result = request
            result = json.loads(request.content)
            # print(result)

            #rasa_sdk.logger.info(f'Consulta realizada com sucesso: {result}')
            logger.info(msg='Consulta realizada com sucesso: ' + str(result))
            #print(result)
            
            # return result
            if 'erro' in result:
                logger.warn(msg="Falha na consulta do CEP " + str(cep) + ". CEP não encontrado.", exc_info=True)
                dispatcher.utter_message(response="utter_falha_consultacep_notfound")
                return [SlotSet('found', False)]
            else:
                return [
                    SlotSet('resultado_consultacep_cep', result['cep']),
                    SlotSet('resultado_consultacep_logradouro', result['logradouro']),
                    SlotSet('resultado_consultacep_complemento', result['complemento']),
                    SlotSet('resultado_consultacep_bairro', result['bairro']),
                    SlotSet('resultado_consultacep_localidade', result['localidade']),
                    SlotSet('resultado_consultacep_uf', result['uf']),
                    SlotSet('found', True),
                    SlotSet('cep', None)
                ]
        except Exception as e:
            logger.error(msg="Falha na consulta do CEP " + str(cep) + ". Error: " + str(e), exc_info=True)
            dispatcher.utter_message(response="utter_falha_consultacep")
            return [SlotSet('found', False)]

        

  

  

  

  

  