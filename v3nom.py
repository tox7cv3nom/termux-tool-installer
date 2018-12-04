import os
import sys
def animation():
   print("""

 
|__/                      | $$              | $$| $$                    
 /$$ /$$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$ | $$| $$  /$$$$$$   /$$$$$$ 
| $$| $$__  $$ /$$_____/|_  $$_/   |____  $$| $$| $$ /$$__  $$ /$$__  $$
| $$| $$  \ $$|  $$$$$$   | $$      /$$$$$$$| $$| $$| $$$$$$$$| $$  \__/
| $$| $$  | $$ \____  $$  | $$ /$$ /$$__  $$| $$| $$| $$_____/| $$      
| $$| $$  | $$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$| $$|  $$$$$$$| $$      
|__/|__/  |__/|_______/    \___/   \_______/|__/|__/ \_______/|__/      
                                                                        
                                     
                                      ****automate modified tool installer******
                                         ~greetz to:-Luc!f@r,rooting-tom,blackc0bra,mr.proton,mr.m4d 
                                                and all indian hackers                                                        
""")
 
def install():
  print('#####thanx for using my tool######')
  print"please select one tool"
  print "1.bingo  ~dork exploiter"
  print "2.beelogger ~python keylogger"
  print "3.metasploit."
  print "4.darkfly."
  print "5.kali nethunter."
 
def load():
  tool = input('enter the tool:')
  if tool == 1:
   os.system("clear")
   print("""
         
  /$$       /$$                              
| $$      |__/                              
| $$$$$$$  /$$ /$$$$$$$   /$$$$$$   /$$$$$$ 
| $$__  $$| $$| $$__  $$ /$$__  $$ /$$__  $$
| $$  \ $$| $$| $$  \ $$| $$  \ $$| $$  \ $$
| $$  | $$| $$| $$  | $$| $$  | $$| $$  | $$
| $$$$$$$/| $$| $$  | $$|  $$$$$$$|  $$$$$$/
|_______/ |__/|__/  |__/ \____  $$ \______/ 
                         /$$  \ $$          
                        |  $$$$$$/          
                         \______/    
""")       
   print("\033[91m\033[1m[+]plzz wait  installing is done[+]")
   print("\033[91m\033[1m[+]......installing")
   print("\033[91m\033[1m[+]......installing")
   os.system("pkg install -y python")
   os.system("pkg install -y python 2")
   os.system("pkg install -y wget")
   os.system("cd /data/data/com.termux/files/home && git clone https://github.com/parthahex/bingo.git")
   os.system("pkg update -y")
   print('\033[1;33;40m[+]bingo installed success fully[+]')
   install()
   load()
  if tool == 2:
   os.system("clear")
   print(""" 

 /$$                           /$$                                                  
| $$                          | $$                                                  
| $$$$$$$   /$$$$$$   /$$$$$$ | $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
| $$__  $$ /$$__  $$ /$$__  $$| $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$  \ $$| $$$$$$$$| $$$$$$$$| $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  | $$| $$_____/| $$_____/| $$| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$$$$$$/|  $$$$$$$|  $$$$$$$| $$|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      
|_______/  \_______/ \_______/|__/ \______/  \____  $$ \____  $$ \_______/|__/      
                                             /$$  \ $$ /$$  \ $$                    
                                            |  $$$$$$/|  $$$$$$/                    
                                             \______/  \______/                     
""") 
   print('\033[91m\033[1m[+][+]plzz wait installing is done[+]')
   print('\033[91m\033[1m[+][+]installing.....')
   print('\033[91m\033[1m[+][+]installing....')
   os.system("pkg install -y python")
   os.system("pkg install -y python 2")
   os.system("pkg install -y wget")
   os.system("cd /data/data.com.termux/files/home && git clone https://github.com/4w4k3/BeeLogger.git")
   os.system("pkg update -y")
   print('\033[1;33;40mbeeloogger installled succesfully')
   install()
   load()
  if tool == 3:
   os.system("clear")
   print(""" 
                           /$$                                   /$$           /$$   /$$    
                          | $$                                  | $$          |__/  | $$    
 /$$$$$$/$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$$  /$$$$$$ | $$  /$$$$$$  /$$ /$$$$$$  
| $$_  $$_  $$ /$$__  $$|_  $$_/   |____  $$ /$$_____/ /$$__  $$| $$ /$$__  $$| $$|_  $$_/  
| $$ \ $$ \ $$| $$$$$$$$  | $$      /$$$$$$$|  $$$$$$ | $$  \ $$| $$| $$  \ $$| $$  | $$    
| $$ | $$ | $$| $$_____/  | $$ /$$ /$$__  $$ \____  $$| $$  | $$| $$| $$  | $$| $$  | $$ /$$
| $$ | $$ | $$|  $$$$$$$  |  $$$$/|  $$$$$$$ /$$$$$$$/| $$$$$$$/| $$|  $$$$$$/| $$  |  $$$$/
|__/ |__/ |__/ \_______/   \___/   \_______/|_______/ | $$____/ |__/ \______/ |__/   \___/  
                                                      | $$                                  
                                                      | $$                                  
                                                      |__/   
""")                               
           
                                  
   print('\033[91m\033[1m[+]plzz wait  installing is done[+]')
   print('\033[91m\033[1m[+]installing.....')
   print('\033[91m\033[1m[+]installing....')
   os.system("pkg install wget")
   os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
   os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
   os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
   os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
   os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
   os.system("cd /data/data/com.termux/files/home && bundle install")
   os.system("cd /data/data/com.termux/files/home")
   print("\033[1;33;40m[++++] metasploit installed sucess fully [+++]")
   install()
   load()
  if tool == 4:
   os.system("clear")
   print("""
 /$$$$$$$                      /$$              /$$$$$$  /$$          
| $$__  $$                    | $$             /$$__  $$| $$          
| $$  \ $$  /$$$$$$   /$$$$$$ | $$   /$$      | $$  \__/| $$ /$$   /$$
| $$  | $$ |____  $$ /$$__  $$| $$  /$$/      | $$$$    | $$| $$  | $$
| $$  | $$  /$$$$$$$| $$  \__/| $$$$$$/       | $$_/    | $$| $$  | $$
| $$  | $$ /$$__  $$| $$      | $$_  $$       | $$      | $$| $$  | $$
| $$$$$$$/|  $$$$$$$| $$      | $$ \  $$      | $$      | $$|  $$$$$$$
|_______/  \_______/|__/      |__/  \__/      |__/      |__/ \____  $$
                                                             /$$  | $$
                                                            |  $$$$$$/  
                                                             \______/ 
""")
   print('\033[91m\033[1m[+]plzz wait  installing is done[+]')
   print('\033[91m\033[1m[+]installing.....')
   print('\033[91m\033[1m[+]installing....')
   os.system("pkg install-y git")
   os.system("pkg install -y python2")
   os.system("pip2 install -r requests")
   os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Ranginang67/DarkFly-Tool")
   print("darkfly successfully installed")
   install()
   load()
  if tool == 5:
   os.system("clear")
   print("""
          /$$        /$$ /$$                             /$$     /$$                             /$$                        
| $$                | $$|__/                            | $$    | $$                            | $$                        
| $$   /$$  /$$$$$$ | $$ /$$       /$$$$$$$   /$$$$$$  /$$$$$$  | $$$$$$$  /$$   /$$ /$$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
| $$  /$$/ |____  $$| $$| $$      | $$__  $$ /$$__  $$|_  $$_/  | $$__  $$| $$  | $$| $$__  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$$$$$/   /$$$$$$$| $$| $$      | $$  \ $$| $$$$$$$$  | $$    | $$  \ $$| $$  | $$| $$  \ $$  | $$    | $$$$$$$$| $$  \__/
| $$_  $$  /$$__  $$| $$| $$      | $$  | $$| $$_____/  | $$ /$$| $$  | $$| $$  | $$| $$  | $$  | $$ /$$| $$_____/| $$      
| $$ \  $$|  $$$$$$$| $$| $$      | $$  | $$|  $$$$$$$  |  $$$$/| $$  | $$|  $$$$$$/| $$  | $$  |  $$$$/|  $$$$$$$| $$      
|__/  \__/ \_______/|__/|__/      |__/  |__/ \_______/   \___/  |__/  |__/ \______/ |__/  |__/   \___/   \_______/|__/      
""")
        
         print('\033[91m\033[1m[+]plzz wait  installing is done[+]')
         print('\033[91m\033[1m[+]installing.....')
         print('\033[91m\033[1m[+]installing....')
         os.system("pkg update -y")
         os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
         os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
         os.system("cd /data/data/com.termux/files/home")
         print("#######nethunter installed successfully#####")
         install()
         load()
animation()
install()
load()
 

                                                                
