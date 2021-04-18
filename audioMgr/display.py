import os

def print_menu():
    clear()
    print("-" *20)
    print("** Audio Mgr 3000 **")
    print("-" * 20)

    print("[1] Register a new Album")
    print("[2] Register a new Song")
    print("[3] Display album catalog")
    print("[4] Print the songs inside an Album")
    print("[5] Cunt all the songs in the System")
    print("[6] Total $ in the catalog")
    print("[7] Most expensive Album")
    print("[8] Change the title of an specific Album")

    print("[q] Quit")

def print_header(text):
    clear()
    print("-" * 30)
    print(text)
    print("-" * 30)

def clear():
    if(os.name==  'nt' ):
        return os.system("clr")
    else:
        return os.system("clear")

    #return os.system('cls if os.name == 'nt'  else 'clear')