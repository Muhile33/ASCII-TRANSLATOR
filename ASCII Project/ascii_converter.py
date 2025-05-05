from colorama import init, Fore, Back, Style

def ascii_converter():
    # Initialize colorama
    init(autoreset=True)
    
    # Colorful header
    header = f"""
    {Style.BRIGHT}{Fore.MAGENTA}╔══════════════════════════════════════╗
    ║{Fore.GREEN}      🅰🆂🅲🅸🅸 / 🅷🅴🆇 / 🅳🅴🅲 🅲🅾🅽🆅🅴🆁🆃🅴🆁      {Fore.MAGENTA}║
    ╚══════════════════════════════════════╝{Style.RESET_ALL}
    """
    print(header)
    
    # Helper functions
    def validate_code(code, max_val=127):
        """Validate if code is within ASCII range (0-127 by default)."""
        try:
            num = int(code)
            return 0 <= num <= max_val
        except ValueError:
            return False

    def get_codes(text, mode="ascii"):
        """Convert text to codes (ASCII, HEX, or Decimal)."""
        if mode == "hex":
            return [hex(ord(char)) for char in text]  # Format: '0x41'
        elif mode == "dec":
            return [ord(char) for char in text]  # Decimal (same as ASCII)
        else:  # ASCII by default
            return [str(ord(char)) for char in text]

    def get_text_from_codes(codes_input, mode="ascii"):
        """Convert codes (ASCII/HEX/Dec) back to text."""
        codes = codes_input.replace(',', ' ').split()
        text = ""
        invalid_codes = []
        
        for code in codes:
            try:
                if mode == "hex":
                    # Handle HEX input 
                    num = int(code, 16) if code.startswith("0x") else int(code, 16)
                else:  # ASCII or Decimal
                    num = int(code)
                
                if validate_code(num):
                    text += chr(num)
                else:
                    invalid_codes.append(code)
            except ValueError:
                invalid_codes.append(code)
                
        return text, invalid_codes

    while True:
        print(f"\n{Style.BRIGHT}{Fore.BLUE}Main Menu:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1.{Style.RESET_ALL} Text → ASCII Codes")
        print(f"{Fore.YELLOW}2.{Style.RESET_ALL} ASCII Codes → Text")
        print(f"{Fore.YELLOW}3.{Style.RESET_ALL} Text → HEX Codes")
        print(f"{Fore.YELLOW}4.{Style.RESET_ALL} HEX Codes → Text")
        print(f"{Fore.YELLOW}5.{Style.RESET_ALL} Text → Decimal Codes")
        print(f"{Fore.YELLOW}6.{Style.RESET_ALL} Decimal Codes → Text")
        print(f"{Fore.RED}7.{Style.RESET_ALL} Exit")

        try:
            choice = input(f"\n{Style.BRIGHT}{Fore.CYAN}Enter your choice (1-7): {Style.RESET_ALL}")

            # Text → ASCII 
            if choice == '1':
                print(f"\n{Style.BRIGHT}{Fore.GREEN}Text → ASCII Codes{Style.RESET_ALL}")
                text = input(f"{Fore.YELLOW}Enter text: {Style.RESET_ALL}")
                codes = get_codes(text, mode="ascii")
                print(f"{Fore.GREEN}ASCII codes: {Style.BRIGHT}{Fore.CYAN}{' '.join(codes)}{Style.RESET_ALL}")

            # ASCII → Text 
            elif choice == '2':
                print(f"\n{Style.BRIGHT}{Fore.GREEN}ASCII Codes → Text{Style.RESET_ALL}")
                ascii_input = input(f"{Fore.YELLOW}Enter ASCII codes (comma/space-separated): {Style.RESET_ALL}")
                text, invalid = get_text_from_codes(ascii_input, mode="ascii")
                if invalid:
                    print(f"{Fore.RED}Invalid codes skipped: {', '.join(invalid)}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}Decoded text: {Style.BRIGHT}{Fore.WHITE}{text}{Style.RESET_ALL}")

            # Text → HEX 
            elif choice == '3':
                print(f"\n{Style.BRIGHT}{Fore.GREEN}Text → HEX Codes{Style.RESET_ALL}")
                text = input(f"{Fore.YELLOW}Enter text: {Style.RESET_ALL}")
                hex_codes = get_codes(text, mode="hex")
                print(f"{Fore.GREEN}HEX codes: {Style.BRIGHT}{Fore.CYAN}{' '.join(hex_codes)}{Style.RESET_ALL}")

            # HEX → Text 
            elif choice == '4':
                print(f"\n{Style.BRIGHT}{Fore.GREEN}HEX Codes → Text{Style.RESET_ALL}")
                hex_input = input(f"{Fore.YELLOW}Enter HEX codes (e.g., '0x41 42' or '41 42'): {Style.RESET_ALL}")
                text, invalid = get_text_from_codes(hex_input, mode="hex")
                if invalid:
                    print(f"{Fore.RED}Invalid HEX codes skipped: {', '.join(invalid)}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}Decoded text: {Style.BRIGHT}{Fore.WHITE}{text}{Style.RESET_ALL}")

            # Text → Decimal 
            elif choice == '5':
                print(f"\n{Style.BRIGHT}{Fore.GREEN}Text → Decimal Codes{Style.RESET_ALL}")
                text = input(f"{Fore.YELLOW}Enter text: {Style.RESET_ALL}")
                dec_codes = get_codes(text, mode="dec")
                print(f"{Fore.GREEN}Decimal codes: {Style.BRIGHT}{Fore.CYAN}{' '.join(map(str, dec_codes))}{Style.RESET_ALL}")

            # Decimal → Text 
            elif choice == '6':
                print(f"\n{Style.BRIGHT}{Fore.GREEN}Decimal Codes → Text{Style.RESET_ALL}")
                dec_input = input(f"{Fore.YELLOW}Enter Decimal codes (comma/space-separated): {Style.RESET_ALL}")
                text, invalid = get_text_from_codes(dec_input, mode="dec")
                if invalid:
                    print(f"{Fore.RED}Invalid Decimal codes skipped: {', '.join(invalid)}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}Decoded text: {Style.BRIGHT}{Fore.WHITE}{text}{Style.RESET_ALL}")

            # Exit 
            elif choice == '7':
                print(f"\n{Style.BRIGHT}{Fore.MAGENTA}Thank you for using the ultimate converter!{Style.RESET_ALL}")
                print(f"{Fore.BLUE}Exiting...{Style.RESET_ALL}")
                break

            else:
                print(f"{Fore.RED}Invalid choice. Enter 1-7.{Style.RESET_ALL}")

        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    ascii_converter()