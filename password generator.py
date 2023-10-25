import random
import string

class Password_Generator:
    """a class that asks for a password and checks if it meets the requirements, if not it will make one for the user"""

    def __init__(self):
        self.alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        self.password_length = 8
        self.attemps = 0

    def password_necessities(self):
        """tells the user the requirements of the passwords"""
        print('Passwords must contain at least one of each of these elements:\n'
              'Passwords must include at least 1 of the following:\n'
              '1. A capital letter\n'
              '2. One number \n'
              '3. At least one special character\n'
              '4. Passwords must have a minimum length of 8 characters.')
        
    def generate_random_password(self):
        """generates a random password"""
        return ''.join(random.choice(self.alphabet) for _ in range(self.password_length))

        
    def check_user_password(self):
        """asks the user to enter their password and checks to make sure it meets the necessary requirements"""
        while True:
            print("You will have three attemps to make a password that meets all the requirements. " 
                  "After three failed attempts, one will be generated for you.")
            self.the_user_password = input('Please enter your password here: ')
            self.includes_uppercase = any(char.isupper() for char in self.the_user_password)
            self.includes_number = any(char.isdigit() for char in self.the_user_password)
            self.includes_special = any(char in string.punctuation for char in self.the_user_password)
            self.is_long_enough = len(self.the_user_password) >= self.password_length

            if self.includes_uppercase and self.includes_number and self.includes_special and self.is_long_enough:
                print('Password meets the necessary requirements.')
                break  
            else:
                print('This password does not meet the necessary requirements.')
                self.create_user_password = input("Would you like a generated password? If so, please enter (1). If not, please enter (2). ")

                try:
                    self.create_user_password = int(self.create_user_password)
                    self.attemps += 1
                except ValueError:
                    print("You need to enter a number.")
                    continue

                if self.create_user_password != 1 and self.create_user_password != 2:
                    print("You need to choose either (1) or (2).")
                if self.create_user_password == 1:
                    self.computer_generated_password = self.generate_random_password()
                    print(f"Generated password: {self.computer_generated_password}")
                    break
                if self.create_user_password == 2:
                    print('Sounds good. Please enter another password below.')
                    self.the_user_password
                    self.attemps += 1
                if self.attemps > 3:
                    self.computer_generated_password
                    print("You have three failed attemps. Your generated password is below. \n"
                          f"Generated password: {self.computer_generated_password}")


    def running_password_generator(self):
        """runs the password generator portion of the program"""
        self.password_necessities()
        self.check_user_password()


class Saved_Passwords_and_User_Names(Password_Generator):
    """a class that saves the usernames, passwords and websites"""

    def __init__(self):
        super.__init__(self)
        self.user_data_list = []

    def saved_user_names(self):
        """asks user for websites, usernames and passwords they want saved"""
        while True:
            self.websites = input('Please enter the website here: ') 
            need_more = input("Are there any more websites you want the usernames remembered for? Select 'yes' or 'no' here: ")
            if need_more != 'no' and need_more != 'yes':
                print('Must choose either yes or no.')
            else:
                if need_more == 'no':
                    break
            
            self.user_data = {"websites": self.websites}


        while True:
            self.usernames = input('Please enter the usernames for the websites in the same corresponding order here: ')
            need_more_user_names = input('Any more user names needed to be saved? Select yes or no below: \n')

            if need_more_user_names != 'no' and need_more_user_names != 'yes':
                print('Must choose either yes or no.')
            else:
                if need_more_user_names == 'no':
                    break
     
        


    #this is where i want the program to ask the user for the passwords and save them in a dictionary with the corresponding \
    #usernames and websites 
    def saved_user_passwords(self):
        passwords = True
        while passwords:
            self.saved_passwords = input('Do you want to save passwords for these websites? Yes or no \n')
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
        
        
        self.user_data_dict = {"website": self.websites,
                          "username" : self.usernames,
                          "password" : self.saved_passwords}
        
        self.user_data_list.append(self.user_data_dict)


    def running_password_saver(self):
        self.saved_user_names()
        self.saved_user_passwords()


if __name__ == '__main__':
    running_the_password_program = Password_Generator() 
    running_the_password_program.running_password_generator()
    running_the_saver_program = Saved_Passwords_and_User_Names()
    running_the_saver_program.running_password_saver()