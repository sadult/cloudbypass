import os

try:
    import requests
except Exception:
    print('requests library not found please install it by : pip3 install requests')
    install = input('do you want insall this library for you Y or N >>')
    if install=="Y" or install=='y':
        os.system('sudo apt-get install python3-pip')
        os.system('pip3 install requests')
    else:
        quit()
try:
    import subprocess
except Exception:
    print('subprocess library not found please install it by : pip3 install subprocess')
    install = input('do you want insall this library for you Y or N >>')
    if install=="Y" or install=='y':
        os.system('sudo apt-get install python3-pip')
        os.system('pip3 install subprocess')
    else:
        quit()
try:
    import re
except Exception:
    print('re library not found please install it by : pip3 install re')
    install = input('do you want insall this library for you Y or N >>')
    if install=="Y" or install=='y':
        os.system('sudo apt-get install python3-pip')
        os.system('pip3 install re')
    else:
        quit()
try:
    import multiprocessing
except Exception:
    print('multiprocessing library not found please install it by : pip3 install multiprocessing')
    install = input('do you want insall this library for you Y or N >>')
    if install=="Y" or install=='y':
        os.system('sudo apt-get install python3-pip')
        os.system('pip3 install multiprocessing')
    else:
        quit()


#i know i used alot of try but it's funn ;)
os.system('clear')
print('\x1b[1;32;40m'+'''


 .d8888b.  888                        888 888888b.                                                
d88P  Y88b 888                        888 888  "88b                                               
888    888 888                        888 888  .88P                                               
888        888  .d88b.  888  888  .d88888 8888888K.  888  888 88888b.   8888b.  .d8888b  .d8888b  
888        888 d88""88b 888  888 d88" 888 888  "Y88b 888  888 888 "88b     "88b 88K      88K      
888    888 888 888  888 888  888 888  888 888    888 888  888 888  888 .d888888 "Y8888b. "Y8888b. 
Y88b  d88P 888 Y88..88P Y88b 888 Y88b 888 888   d88P Y88b 888 888 d88P 888  888      X88      X88 
 "Y8888P"  888  "Y88P"   "Y88888  "Y88888 8888888P"   "Y88888 88888P"  "Y888888  88888P'  88888P' 
                                                          888 888                                 
                                                     Y8b d88P 888                                 
                                                      "Y88P"  888                                 

'''+ '\033[0m')
print('''
 ====================================================================================================
                                              By : Mercad
                                           github.com/sadult
                                        bypass Cloud Protection
 =====================================================================================================
''')
try:

    domain = input('[+] enter Target domain >> ')
except KeyboardInterrupt:
    print('\n[-] Cloud Killer is closed !! ')
    quit()
def checker(domain):

    try:

        link=requests.get('http://'+domain)
        if link.status_code ==200 or link.status_code==403:


            ping_command = subprocess.check_output('ping -c 1 '+domain,shell=True)
            filtered_re = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ping_command.decode('utf-8'))
            print('\x1b[1;32;40m'+'[+] the domain : '+domain+' has Ip address by : '+filtered_re[0]+ '\033[0m')

        else:

            print('\x1b[0;31;40m'+'[-] the domain : '+domain+' has Ip address by : N/A '+ '\033[0m')
    except Exception:
        print('\x1b[0;31;40m'+'[-] the domain : '+domain+' has Ip address by : N/A '+ '\033[0m')
        pass




try:

    with open('subsfile.txt','r')as wordlist:
        for word in wordlist:
            word = word.strip()

            try:

                subwdom= word+'.'+domain
                #checker(subwdom)
                p= multiprocessing.Process(target=checker,args=(subwdom,))
                p.start()
                p.join()
            except Exception:
                quit()
except KeyboardInterrupt:

    print('[-] Cloud Killer is closed !! ')
    quit()
print('[-] Cloud Killer is closed !! ')
