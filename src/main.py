import dialogflow
import actions

def main():
  user_input = None
  while user_input != 'sair':
    user_input = input('> ')
    if user_input == 'sair':
        break

    action, parameters = dialogflow.get_action(user_input)

    action_result = actions.run(action, parameters)
    if action_result:
      print(action_result)

if __name__ == "__main__":
  main()
