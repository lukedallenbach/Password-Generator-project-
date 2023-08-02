
class Password_Generator_Project:

    def __init__(self, password, user):
        self.password = password
        self.user = user

    def password_generator(self):

        import random
        import string
        from string import punctuation

        alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + punctuation

        def password_necessities(self):
            print('Passwords must contain at least one of each of these elements:')
            print('Passwords must include at least 1 of the following: \nA capital letter\nOne number \nAt least one special character')
            print('Passwords must have a minimum length of 8 characters.')

        def generate_password(self, length = 12):                
            characters = string.ascii_letters + string.digits + punctuation
            password = ''.join(random.choice(characters) for _ in range(length))

            print('\nIf you need help creating a password, one can be created for you.')
            create_password = input('If you would like a password created for you, please press 1: \n')
        
            if create_password == '1':
                generated_password = password
                print('Generated Password:', generated_password)
                print('You can copy and paste this password.')
            
            else:
                print('Sounds good. Please continue.')
        generate_password(length = 12)
            
        user_password = input('Please enter your password below: \n')

        includes_uppercase = any(char.isupper() for char in user_password)
        includes_number = any(char.isdigit() for char in user_password)
        includes_special = any(char in punctuation for char in user_password)
        is_long_enough = len(user_password) >= 8

        if includes_uppercase and includes_number and includes_special and is_long_enough:
            print('Password meets the necessary requirements.')
        else:
            print('This password does not meet the necessary requirements, please try again.')
                

        #password_necessities() 

        def saved_passwords_and_user_names(self):
            saved_user_passwords = []
            saved_user_names = {}

            websites = True
            while websites:
                new_keys = input('Please enter the website below: \n')
                need_more = input('Are there any more websites you want the usernames remembered for? Select yes or no below: \n')
                if need_more != 'no' and need_more != 'yes':
                    print('Must choose either yes or no.')
                else:
                    if need_more == 'no':
                        websites = False
                

            user_names = True
            while user_names:
                new_values = input('Please enter the usernames for the websites in the same corresponding order below: \n')
                need_more_user_names = input('Any more user names needed to be saved? Select yes or no below: \n')

                if need_more_user_names != 'no' and need_more_user_names != 'yes':
                    print('Must choose either yes or no.')
                else:
                    if need_more_user_names == 'no':
                        user_names = False

                saved_user_names[new_keys] = new_values 
                print(saved_user_names)

            passwords = True
            while passwords:
                saved_passwords = input('Do you want to save this password? Yes or no \n')
                if saved_passwords != 'yes' and saved_passwords != 'no':
                    print('You must select a valid choice.')
                else:
                    if saved_passwords == 'no':
                        print('Okay sounds good yo')
                        passwords = False
                    else:
                        while True:
                            the_passwords = input("Please enter the passwords below. Once finished, please type 'stop' \n")
                            print('Password saved')
                            if the_passwords == 'stop':
                                passwords = False
                                break

                print(the_passwords)


        #saved_passwords_and_user_names()

    #password_generator()




