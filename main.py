erreq = False
ercolorama = False
moderror = False
try:
    import os
    from os import system
    system("title " + "Swattinghouses Proxy Scraper")
except:
    pass
import os
try:
    import colorama
except Exception:
    print("Missing Colorama Module")
    ercolorama = True
    moderror = True
try:
    import requests
except Exception:
    print("Missing Requests Module")
    erreq = True
    moderror = True
if moderror == True:
    for u in range(1):
        localerror = False
        while True:
            autofix = input("Missing Module(s) Wanna Auto Fix (y/n): ")
            if autofix == "y" or autofix == "n":
                break
            else:
                print("Enter A Valid Choice")
        if autofix == "y":
            if ercolorama == True:
                try:
                    os.system("pip install colorama")
                except:
                    print("Failed To Download Colorama")
                    localerror == True
            if erreq == True:
                try:
                    os.system("pip install requests")
                except:
                    print("Failed To Download Requests")
                    localerror == True
            if localerror == True:
                print("Failed To Fix The Problem")
                input("")
                exit()
            if localerror == False:
                print("Problems Should Be Fixed Now, Restart The Program")
                input("")
                exit()
        if autofix == "n":
            print("Press Enter To Close The Program")
            input("")
            exit()

def cred():
    print("(1) Made by Clokz#9433 but resold by feen#2451")
    input("")
    return
def sniper():
    print(colorama.Fore.CYAN + """
    1. Http
    2. Https
    3. Socks4
    4. Socks5
""")

    while True:
        
        type = input(" Number: ")
        if type == "1" or type == "2" or type == "3" or type == "4":
            break
        else:
            print("Enter A Valid Choice")

    while True:
        try:
            ms = input("Enter Delay (50-10000, Lower = Less Proxies i recomend 10000): ")
            ms = int(ms)
            if ms < 10001 and ms > 49:
                break
            else:
                print("Enter A Valid Choie")
        except Exception:
            print("Enter A Valid Choice")
    try:
        if type == "1":
            r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={ms}&country=all").text
        if type == "2":
            r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout={ms}&country=all").text
        if type == "3":
            r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout={ms}&country=all").text
        if type == "4":
            r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout={ms}&country=all").text
        while True:
            save = input("""
Pick One:

    1. Save In A Txt File
    2. Only Print Proxies
    3. Both
    """)
            if save == "1" or save == "2" or save == "3":
                break
            else:
                print("Enter A Valid Choice")
        if save == "1" or save == "3":
            file = open("proxies.txt", "a")
            file.write(str(r))
            file.close()
        if save == "2" or save == "3":
            print(str(r))
        print(" Done! Press enter to go back to the menu!")
        input("")
    except Exception:
        print("Error While Getting Proxies")
        input("")
        return


colorama.init(autoreset=False)
while True:
    print(colorama.Fore.CYAN + """
███████╗███████╗███████╗███╗   ██╗███████╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔════╝██╔════╝████╗  ██║██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
█████╗  █████╗  █████╗  ██╔██╗ ██║███████╗    ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██╔══╝  ██╔══╝  ██╔══╝  ██║╚██╗██║╚════██║    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
██║     ███████╗███████╗██║ ╚████║███████║    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
╚═╝     ╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                                      
                                                                                                     
                                                                                              
                                                                                              
                                                                                                               
                                                                                                        
                                     Resold by feen#2451!""")
    
    print("""
    1. Credits
    2. Proxy Scraper
""")
    main = input(" Number: ")
    if main == "2":
        sniper()
    if main == "1":
        cred()
