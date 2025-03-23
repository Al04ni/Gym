from colorama import Fore, Style, init
init(autoreset= True) #initialzing Colorama
def menu():    
    while True:
        print(Fore.YELLOW + r"""
         ___ ___  ____  ____   ___   _____  ____  _____  ___ 
        |   |   ||    ||    \ |   \ / ___/ /    ||     |/  _]
        | _   _ | |  | |  _  ||    (   \_ |  o  ||   __/  [_ 
        |  \_/  | |  | |  |  ||  D  \__  ||     ||  |_|    _]
        |   |   | |  | |  |  ||     /  \ ||  _  ||   _]   [_ 
        |   |   | |  | |  |  ||     \    ||  |  ||  | |     |
        |___|___||____||__|__||_____|\___||__|__||__| |_____|
        """)
        print(f"\n{Fore.MAGENTA}Mental Health Anonymous Booking System")
        print()
        print(f"{Fore.CYAN}1.Patient Portal")
        print(f"{Fore.GREEN}2.Doctor Portal")
        print(f"{Fore.RED}3.Admin Portal")
        print(f"{Fore.WHITE}4.Exit")
        
        choice = input(f"\n{Fore.WHITE}Select your role: ")
        
        if choice == '1':
            patient_menu()
        elif choice == '2':
            handle_doctor_login()
        elif choice == '3':
            admin_menu()
        elif choice == '4':
            print(f"{Fore.YELLOW}Exiting system...")
            break
        else:
            print(f"{Fore.RED}Invalid choice!")


if __name__ == "__main__":
    menu()
