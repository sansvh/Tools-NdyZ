import os,sys,time,random
from colored import fg

red = fg('light_red')
blue = fg('blue')
white = fg('white')
green = fg('light_green')
yellow = fg('light_yellow')
cyan = fg('cyan')

def jalan(text):
      for abc in f"{text}\n":
        sys.stdout.write(abc)
        sys.stdout.flush()
        time.sleep(random.choice([.2,.3,.4,.5,.6]))
        


sansZ = """
cd ..
rm -fr Tools-NdyZ
git clone
cd Tools-NdyZ
"""
print(blue+" [!] wait Update Script....")
tex = ' >>>>>>>>>>>>>>>>>>>>>>>>>>'
jalan(yellow+f'{tex}')
os.system(sansZ)
time.sleep(.5)
print(green+' [+] Update Script success...'+cyan)
os.system('cat .update.txt')
print(green+' [!] use the '+ red+ 'python main.py'+ green+' to run tool'+white)
time.sleep(.3)
os.sys.exit()
