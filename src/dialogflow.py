import json
from google.cloud import dialogflow_v2
from google.oauth2 import service_account

project_id = "assistente-supermercado-t99y"
session_id = "client"
language_code = "pt-br"
creds_file = "credentials.json"
dialogflow_key = json.load(open(creds_file))
credentials = (service_account.Credentials.from_service_account_info(dialogflow_key))
session_client = dialogflow_v2.SessionsClient(credentials=credentials)

def detect_intent(text):
  session = session_client.session_path(project_id, session_id)
  text_input = dialogflow_v2.types.TextInput(text=text, language_code=language_code)
  query_input = dialogflow_v2.types.QueryInput(text=text_input)
  response_dialogflow = session_client.detect_intent(session=session, query_input=query_input)
  return response_dialogflow

def get_action(text):
  response_dialogflow = detect_intent(text)
  action = response_dialogflow.query_result.action
  parameters = response_dialogflow.query_result.parameters
  return action, parameters
