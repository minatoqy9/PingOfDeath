#!/usr/bin/python

import os
import sys
import time
os.system("clear")

#header
os.system("cat banner.txt")
print("")
print("01.Simple User Mode")                   
print("02.Root User Mode")
print("")
print("00.Exit")

ping = input("[PoD]~> ")

#input

if ping == '01' or ping == '1':
   time.sleep(1)
   print("Please Insert IP")
   ip = input("IP or URL: ")
   os.system("ping -i 0.2 -s 65500 %s" % (ip))
   sys.exit()

elif ping == '02' or ping == '2':
     time.sleep(1)
     print("Please Insert IP:")
     ip2 = input("IP or URL: ")
     os.system("ping -i 0.1 -s 65500 %s" % (ip2))
     sys.exit()

elif ping == '00' or ping == '1':
     print("Exiting…")
     sys.exit

else:
     print("[ERROR] Wrong Input!")
     sys.exit
