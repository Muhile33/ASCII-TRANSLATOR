from colorama import init, Fore, Back, Style

def ascii_converter():
    # Initialize colorama
    init(autoreset=True)
    
    # Colorful header
    header = f"""
    {Style.BRIGHT}{Fore.MAGENTA}╔══════════════════════════════════════╗
    ║{Fore.GREEN}      🅰🆂🅲🅸🅸  🅲🅾🅽🆅🅴🆁🆃🅴🆁      {Fore.MAGENTA}║
    ╚══════════════════════════════════════╝{Style.RESET_ALL}
    """
    
    print(header)
    
    while True:
        print(f"\n{Style.BRIGHT}{Fore.BLUE}Main Menu:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1.{Style.RESET_ALL} ASCII codes to Text")
        print(f"{Fore.YELLOW}2.{Style.RESET_ALL} Text to ASCII codes")
        print(f"{Fore.YELLOW}3.{Style.RESET_ALL} Number to ASCII character")
        print(f"{Fore.YELLOW}4.{Style.RESET_ALL} ASCII character to Number")
        print(f"{Fore.RED}5.{Style.RESET_ALL} Exit")
        
        try:
            choice = input(f"\n{Style.BRIGHT}{Fore.CYAN}Enter your choice (1-5): {Style.RESET_ALL}")
            
            if choice == '1':
                # ASCII codes to Text
                print(f"\n{Style.BRIGHT}{Fore.GREEN}ASCII to Text Conversion{Style.RESET_ALL}")
                ascii_input = input(f"{Fore.YELLOW}Enter ASCII codes (comma or space separated): {Style.RESET_ALL}")
                codes = ascii_input.replace(',', ' ').split()
                text = ''
                for code in codes:
                    try:
                        text += chr(int(code))
                    except ValueError:
                        print(f"{Fore.RED}Invalid ASCII code: {code}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}Resulting text: {Style.BRIGHT}{Fore.WHITE}{text}{Style.RESET_ALL}")
                
            elif choice == '2':
                # Text to ASCII codes
                print(f"\n{Style.BRIGHT}{Fore.GREEN}Text to ASCII Conversion{Style.RESET_ALL}")
                text = input(f"{Fore.YELLOW}Enter text: {Style.RESET_ALL}")
                ascii_codes = [str(ord(char)) for char in text]
                print(f"{Fore.GREEN}ASCII codes: {Style.BRIGHT}{Fore.CYAN}{' '.join(ascii_codes)}{Style.RESET_ALL}")
                
            elif choice == '3':
                # Number to ASCII character
                print(f"\n{Style.BRIGHT}{Fore.GREEN}Number to ASCII Character{Style.RESET_ALL}")
                try:
                    num = int(input(f"{Fore.YELLOW}Enter a number (0-127): {Style.RESET_ALL}"))
                    if 0 <= num <= 127:
                        print(f"{Fore.GREEN}ASCII character: {Style.BRIGHT}{Fore.WHITE}{chr(num)}{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}Number must be between 0 and 127{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Please enter a valid number{Style.RESET_ALL}")
                    
            elif choice == '4':
                # ASCII character to Number
                print(f"\n{Style.BRIGHT}{Fore.GREEN}ASCII Character to Number{Style.RESET_ALL}")
                char = input(f"{Fore.YELLOW}Enter a single character: {Style.RESET_ALL}")
                if len(char) == 1:
                    print(f"{Fore.GREEN}ASCII code: {Style.BRIGHT}{Fore.CYAN}{ord(char)}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Please enter exactly one character{Style.RESET_ALL}")
                    
            elif choice == '5':
                print(f"\n{Style.BRIGHT}{Fore.MAGENTA}Thank you for using the ASCII Converter!{Style.RESET_ALL}")
                print(f"{Fore.BLUE}Exiting program...{Style.RESET_ALL}")
                break
                
            else:
                print(f"{Fore.RED}Invalid choice. Please enter a number between 1 and 5.{Style.RESET_ALL}")
                
        except Exception as e:
            print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    ascii_converter()