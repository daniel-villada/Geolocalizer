# author: Daniel villada
#date: 07 - agust - 2020
#Obtener informacion del isp 
import urllib.request
import json
from datetime import date
from datetime import datetime
# Ascii Art Banner
print("\n")
print("██████╗ ██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗ █████╗  █████╗")
print("╚════██╗╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝██╔══██╗██╔══██╗")
print(" █████╔╝ ╚███╔╝ ██████╔╝██║     ██║   ██║██║   ██║   ╚██████║╚█████╔╝")
print(" ╚═══██╗ ██╔██╗ ██╔═══╝ ██║     ██║   ██║██║   ██║    ╚═══██║██╔══██╗")
print("██████╔╝██╔╝ ██╗██║     ███████╗╚██████╔╝██║   ██║    █████╔╝╚█████╔╝")
print("╚═════╝ ╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝    ╚════╝  ╚════╝ ")
print("*************************** Daniel Villada ****************************\n")
print("************************* Date: " + str(date.today()) + " ****************************\n")
print("********** Function: obtener informacion del isp *******\n")

def main():
  address = input("Introduce la direccion ip publica del objetivo: ")
  target = "https://ipinfo.io/"+address+"/json"
  url = urllib.request.urlopen(target)
  loadjson = json.loads(url.read())

  for data in loadjson:
    print(data + " : " + loadjson[data])

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    exit()
