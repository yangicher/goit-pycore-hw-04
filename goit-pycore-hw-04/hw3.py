import sys
from pathlib import Path
from colorama import Fore, Style

def visualize_directory(directory_path, deep=1):
    try:
        prefix=deep*'   '
        for path in directory_path.iterdir():
            if path.is_dir():
                print(f"{prefix}{Fore.BLUE}{path.name}/{Style.RESET_ALL}")
                visualize_directory(path, deep+1)
            else:
                print(f"{prefix}{Fore.GREEN}{path.name}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: An unexpected error occurred: {str(e)}{Style.RESET_ALL}")

def main():    
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Error: Please provide a directory path as an argument{Style.RESET_ALL}")
        print("Usage: python hw3.py <directory_path>")
        sys.exit(1)
    
    directory_path = Path(sys.argv[1])
    
    try:
        if not directory_path.exists():
            raise FileNotFoundError("Directory does not exist")
        if not directory_path.is_dir():
            raise NotADirectoryError("Path is not a directory")
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)
        
    try:
        print(f"{Fore.BLUE}{directory_path.name}{"/"}{Style.RESET_ALL}")
        visualize_directory(directory_path)
    except PermissionError:
        print(f"{Fore.RED}Error: Permission denied to access some directories{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: An unexpected error occurred: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()