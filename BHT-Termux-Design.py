#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import time
import sys

os.system('apt update')
os.system('apt upgrade -y')
os.system("pkg i cowsay -y ; pkg i sl -y ")
os.system('pkg install figlet -y')
os.system('pkg install ncurses-utils -y')
os.system('pkg install ruby -y')
os.system('gem install lolcat')


logo = ("""\033[1;32m
       
                                                                              
                                                                            
BBBBBBBBBBBBBBBBB        HHHHHHHHH     HHHHHHHHH     TTTTTTTTTTTTTTTTTTTTTTT
B::::::::::::::::B       H:::::::H     H:::::::H     T:::::::::::::::::::::T
B::::::BBBBBB:::::B      H:::::::H     H:::::::H     T:::::::::::::::::::::T
BB:::::B     B:::::B     HH::::::H     H::::::HH     T:::::TT:::::::TT:::::T
  B::::B     B:::::B       H:::::H     H:::::H       TTTTTT  T:::::T  TTTTTT
  B::::B     B:::::B       H:::::H     H:::::H               T:::::T        
  B::::BBBBBB:::::B        H::::::HHHHH::::::H               T:::::T        
  B:::::::::::::BB         H:::::::::::::::::H               T:::::T        
  B::::BBBBBB:::::B        H:::::::::::::::::H               T:::::T        
  B::::B     B:::::B       H::::::HHHHH::::::H               T:::::T        
  B::::B     B:::::B       H:::::H     H:::::H               T:::::T        
  B::::B     B:::::B       H:::::H     H:::::H               T:::::T        
BB:::::BBBBBB::::::B     HH::::::H     H::::::HH           TT:::::::TT      
B:::::::::::::::::B      H:::::::H     H:::::::H           T:::::::::T      
B::::::::::::::::B       H:::::::H     H:::::::H           T:::::::::T      
BBBBBBBBBBBBBBBBB        HHHHHHHHH     HHHHHHHHH           TTTTTTTTTTT \033
__________________×______________________
  
  Auther   :  BD-JAHIED 
 
  Github   :  BLACK-HUNTER-TEEM

  Facebook : ROOT.OFF.JAHIED
  
  Contact : +8801747951169
__________________×______________________\033[1;37m""")
os.system('xdg-open https://m.facebook.com/100076888617615')


output = '/data/data/com.termux/files/usr/etc/'

print('')
name = raw_input('Input your Name : ')

wlc = '''
import os,sys,time,random
print("")
print("")
color = ["\\033[1;31m","\\033[1;32m"]
m = random.choice(color)+"Welcome {} \\n"
for msg in m:
    sys.stdout.write(msg)
    sys.stdout.flush()
    time.sleep(0.06)
print("")
'''.format(name)

h1 = open(output+'wlc.py', 'w')
h1.write(wlc)
h1.close()

bashrc1 = '''
clear
sl |lolcat
clear
echo
echo "
   < ━━━━━━━━━━━━ [★] 𖧷𖧷👿𝐇.𝐀.𝐂.𝐊.𝐄.𝐑👿 𖧷𖧷[★] ━━━━━━━━━━━━ >  " |lolcat
echo
    echo "                  𝐀𝐃𝐌𝐈𝐍: 𝐌𝐑.𝐑𝐀𝐊𝐈𝐁☀︎︎𝐂𝐄𝐎: 𝐁𝐃-𝐉𝐀𝐇𝐈𝐄𝐃 " |lolcat
'''

bashrc2 = '''
echo "
	         Cyber Security Ethical Hacker
   < ━━━━━━━━━━━━ [🔥] 𝐁𝐋𝐀𝐂𝐊  𝐇𝐔𝐍𝐓𝐄𝐑 𝐓𝐄𝐀𝐌 [🔥] ━━━━━━━━━━━━ > " |lolcat

python /data/data/com.termux/files/usr/etc/wlc.py
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi

#PS1="\\033[1;31mCyber~#"

PS1="\[\e[1;34m┌──\\a─T─I─M─E─\\a──┐\\033[1;34m\\a┌──\\a─D─A─T─E─\\a───>\\033[1;34m
\\a┌─[\\033[1;93m \@\\033[1;34m ]──[\\033[1;93m \d\\033[1;34m ]\\033[1;34m
\\a├─[\\033[1;32m\w\\033[1;34m]\\033[1;34m
'''

h2 = open(output+'bash.bashrc', 'w')
h2.write(bashrc1)
h2.write("\nfiglet    '    "+name+"' |lolcat\n")
#h2.write("\n\ncowsay    '    "+name+"' |lolcat\n")
h2.write(bashrc2)
h2.write('\[\e[34m\]└─>\[\e[35m\]'+name+'\[\e[34m\][~]:#\[\e[1;32m\] "\n')
h2.write('echo -e "\e[6 q"')
h2.close()
print('DONE Now Exit Your Termux And Following Command Bellow')
