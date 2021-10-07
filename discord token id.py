# Modules importation
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """
   ____           _     _   _            _             
  / ___|___   ___| |_  | | | | __ _  ___| | _____ _ __ 
 | |   / _ \ / _ \ __| | |_| |/ _` |/ __| |/ / _ \ '__|
 | |__| (_) |  __/ |_  |  _  | (_| | (__|   <  __/ |   
  \____\___/ \___|\__| |_| |_|\__,_|\___|_|\_\___|_|   
                                                       

""" + Fore.LIGHTCYAN_EX)
print(banner)
userid = input(" [creado por x'Zyx] Usario id : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [Token encontrado] Este es su token corto xDD: {encodedStr}')
os.system('pause >nul')  # Pause command in Batch (press any key to exit the code)
