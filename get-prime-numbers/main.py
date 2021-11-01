# This python program returns a list of the first 'x' prime numbers,
# when 'x' is a number received from the user input.

from modules.prime import get_prime_numbers


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
        user_number = input('Amount of prime numbers: ')
        print('>'+user_number+'<')
        if user_number == '':
            break
        try:
            user_number = int(user_number)
        except:
            print('Please enter a number')
            continue
        break

    if user_number == '':
        print(program_messages['result_message']
        .read()
        .format(len(get_prime_numbers()), get_prime_numbers()))
    else:
        print(program_messages['result_message']
        .read()
        .format(user_number, get_prime_numbers(user_number)))
    
    print(program_messages['closing_message'].read())
    program_messages['closing_message'].close()


if __name__ == '__main__':
    run()