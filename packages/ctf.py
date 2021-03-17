#color's
red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"
blink = "\033[5m"
#end

def art():
    print(green + """
╔═╗╔╦╗╔═╗  ╔╦╗┌─┐┌─┐┬  ┌─┐
║   ║ ╠╣    ║ │ ││ ││  └─┐
╚═╝ ╩ ╚     ╩ └─┘└─┘┴─┘└─┘
""")

def clear():
    import os
    os.system(['clear', 'cls'][os.name == 'nt'])

def menu():
    clear()
    art()
    print("")
    print("")
    print("""Como posso ajudar em seu CTF ?
    
    01(Linpeas)

    02(Winpeas)
    
    03(OpenVpn)
    
    04(Server Python)""")
    print("")
    print("")
    pergunta = input(yellow + """Oque vai levar hoje meu condecorado ?
    ↪ """)
    if pergunta == "1":
        clear()
        linpeas()
    elif pergunta == "2":
        clear()
        winpeas()
    elif pergunta == "3":
        clear()
        openvpn()
    elif pergunta == "4":
        clear()
        serverpython()
    elif pergunta == "5":
        clear()
        commondirbrute()

def linpeas():
    import os
    from time import sleep
    clear()
    art()
    print("")
    print("")
    print(green + "\nFazendo o download do linpeas.. \n")
    sleep(2)
    os.system("wget https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/blob/master/linPEAS/linpeas.sh")
    os.system("chmod +x linpeas.sh")
    print("")
    print("")
    print(green + "Download concluido com sucesso. ")
    sleep(3)
    clear()
    return menu()

def winpeas():
    import os
    from time import sleep
    clear()
    art()
    print("")
    print("")
    print(green + "\nFazendo o download do winpeas.. \n")
    sleep(2)
    os.system("wget https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS")
    print("")
    print("")
    print(green + "Download concluido com sucesso. ")
    sleep(3)
    clear()
    return menu()

def openvpn():
    import os
    from time import sleep
    clear()
    art()
    print("")
    print("")
    print(green + "\nInstalando OpenVpn.. \n")
    sleep(2)
    os.system("sudo apt install openvpn")
    print("")
    print("")
    print(green + "Instalado completamente. ")
    sleep(3)
    clear()
    return menu()

def serverpython():
    import os
    from time import sleep
    clear()
    art()
    print("")
    print("")
    print(blue + "Subindo server em 3 segundos..")
    print("")
    print("")
    sleep(3)
    try:
        os.system("python3 -m http.server")
    except KeyboardInterrupt:
        print(blink + "Server fechado.")
    sleep(3)
    clear()
    return menu()
