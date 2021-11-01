# This python program receives a compound number from user
# input and returns a list of the factors of that number.

from modules.get_factors import get_factors


def run():
    program_messages = {
        'welcome_message': open('./messages/welcome.txt'),
        'result_message': open('./messages/result.txt'),
        'closing_message': open('./messages/closing.txt')
    }

    print(program_messages['welcome_message'].read())
    program_messages['welcome_message'].close()

    while True:
        user_choice = input()
        if user_choice == '':
            break
        elif user_choice.lower() == 'exit':
            print(program_messages['closing_message'].read())
            return
        else:
            print('Please enter a valid choice')

    while True:
        user_number = input('Enter your number: ')
        try:
            user_number = int(user_number)
        except:
            print('Please enter a number')
            continue
        break
        
    print(program_messages['result_message']
    .read()
    .format(user_number, get_factors(user_number)))
    
    print(program_messages['closing_message'].read())
    program_messages['closing_message']


if __name__ == '__main__':
    run()
    