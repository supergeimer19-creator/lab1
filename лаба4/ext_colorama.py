from colorama import init, Fore

def test_colorama():
    init(autoreset=True)
    print(Fore.CYAN + "colorama: Цей текст виведено блакитним кольором.")