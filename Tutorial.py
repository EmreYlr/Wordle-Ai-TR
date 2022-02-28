from colorama import Fore, Back, Style

while 1:
    answer = int(input("1-Program Start\n2-Tutorial\n3-Program Exit\n>"))
    if answer == 1:
        break
    elif answer == 2:
        a = Fore.LIGHTBLACK_EX + Back.GREEN + " A " + Style.RESET_ALL
        b = Fore.LIGHTBLACK_EX + Back.YELLOW + " M " + Style.RESET_ALL
        c = Back.LIGHTBLACK_EX + Fore.WHITE + " K " + Style.RESET_ALL
        d = Back.LIGHTBLACK_EX + Fore.WHITE + " L " + Style.RESET_ALL
        e = Back.LIGHTBLACK_EX + Fore.WHITE + " E " + Style.RESET_ALL

        print("Ekrana çıkan kelimenin içindeki harflerin renklerine göre giriş yapılır.\n"
              "Yeşil(Green) için 'G' harfi\n"
              "Sarı(Yellow) için 'Y' harfi\n"
              "Siyah(Black) için 'B' harfi kullanınız."
              "\n"
              "Örnek:\n"
              " +---+---+---+---+---+\n"
              " |{}|{}|{}|{}|{}|\n".format(c, a, d, e, b),
              "+---+---+---+---+---+\n"
              " K harfi siyah yandığı için 'B' harfini kullanıyoruz.\n"
              " A harfi yeşil yandığı için 'G' harfini kullanıyoruz.\n"
              " M harfi sarı yandığı için 'Y' harfini kullanıyoruz\n\n"
              "Yani Kısaca girmemiz gereken girdi 'BGBBY' olacaktır.\n"
              "Böylelikle program bize buna uygun tekrar kelime üretecektir.\n\n")
        while 1:
            back = int(input("1-Back\n>"))
            if back == 1:
                break
            else:
                print("Wrong Key\n")
    elif answer == 3:
        exit(0)
    else:
        print("Wrong Key\n")

