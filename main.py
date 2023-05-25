# import module
import socket
import re
import time,os,random
import requests
import json
from collections import deque
from bs4 import BeautifulSoup
import urllib.parse
import colored
from colored import fg
from rich import print as cetak
from rich.panel import Panel as panel

# color
red = fg('light_red')
blue = fg('light_blue')
yellow = fg('light_yellow')
green = fg('light_green')
white = fg('white')
cyan = fg('cyan')

# banner
def banner_scanIp():
  cetak(panel(f"""[bold purple]
[[[[[[]]]]]] [[[[[[]]]]]]     [[[[]]]]     [[[[]]]]    [[]]
[[]]         [[]]            [[]]  [[]]    [[]] [[]]   [[]]
[[[[[[]]]]]] [[]]           [[]]    [[]]   [[]]  [[]]  [[]]
        [[]] [[]]          [[[[[[[]]]]]]]  [[]]   [[]] [[]]
[[[[[[]]]]]] [[[[[[]]]]]] [[]]        [[]] [[]]    [[[[]]]]\n\n[bold red][!] use the exit command to quit[bold white]\n[bold red][!] use the menu command to menu[bold white]
""",width=100,padding=(0,18),title=f"[bold cyan]Port Scanner",style=f"bold purple"))

def banner_checkIp():
  cetak(panel(f"""[bold purple]
[[[[[]]]]] [[]]    [[]] [[[[[[]]]]]] [[[[[]]]]] [[]]    [[]]   [[]] [[[[[[]]]]]]
[[]]       [[]]    [[]] [[]]         [[]]       [[]]  [[]]     [[]] [[]]    [[]]
[[]]       [[[[[[]]]]]] [[[[[[]]]]]] [[]]       [[[[]]]]       [[]] [[[[[[]]]]]]
[[]]       [[]]    [[]] [[]]         [[]]       [[]]  [[]]     [[]] [[]]
[[[[[]]]]] [[]]    [[]] [[[[[[]]]]]] [[[[[]]]]] [[]]    [[]]   [[]] [[]]\n\n[bold red][!] use the exit command to quit[bold white]\n[bold red][!] use the menu command to menu[bold white]
""",width=100,padding=(0,8),title=f"[bold cyan]Check Ip",style=f"bold purple"))

def banner_scraper():
  cetak(panel(f"""[bold purple]
[[[[[]]]]] [[[[[]]]]] [[[[[[]]]]]]     [[[[]]]]     [[[[[[]]]]]] [[[[[]]]]] [[[[[[]]]]]]
[[]]       [[]]       [[]]    [[]]    [[]]  [[]]    [[]]    [[]] [[]]       [[]]    [[]]
[[[[[]]]]] [[]]       [[[[[[]]]]]]   [[]]    [[]]   [[[[[[]]]]]] [[[[[]]]]] [[[[[[]]]]]]
      [[]] [[]]       [[]]  [[]]    [[[[[[[]]]]]]]  [[]]         [[]]       [[]]  [[]]
[[[[[]]]]] [[[[[]]]]] [[]]    [[]] [[]]        [[]] [[]]         [[[[[]]]]] [[]]    [[]]\n\n[bold red][!] use the exit command to quit[bold white]\n[bold red][!] use the menu command to menu[bold white]
""",width=100,padding=(0,5),title=f"[bold cyan]Email Scraper",style=f"bold purple"))
  
def banner():
  cetak(panel(f"""[bold ppurple]
[[[[[[]]]]]] [[[[[[]]]]]] [[[[[[]]]]]] [[]]         [[[[[[]]]]]]
    [[]]     [[]]    [[]] [[]]    [[]] [[]]         [[]]
    [[]]     [[]]    [[]] [[]]    [[]] [[]]         [[[[[[]]]]]]
    [[]]     [[]]    [[]] [[]]    [[]] [[]]                 [[]]
    [[]]     [[[[[[]]]]]] [[[[[[]]]]]] [[[[[[]]]]]] [[[[[[]]]]]]
    \n
[bold green][+] author  : [bold red]NdyZ\n[bold green][+] contact : [bold red]085346923840\n[bold green][+] github  : [bold red]cooming soon
    """,width=100,padding=(0,15),title=f"[bold cyan] Version 1.5",style=f"bold purple"))

#function scan
def scan(ipaddress, port, timeouts):
    try:
        soc = socket.socket()
        soc.settimeout(timeouts)
        soc.connect((ipaddress, port))
        service = soc.recv(1024)
        service = service.decode('utf-8')
        service = service.strip('\n')
        print(green + f'Port {str(port)} open {service}')
    except ConnectionRefusedError:
        print(yellow + f'Port {str(port)} closed')
    except UnicodeDecodeError:
        print(red + f'port {str(port)} closed')
    
def validate_ip_address(ipaddress):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ipaddress):
        return True
    else:
        return False

def validate_port(port):
    try:
        port = int(port)
        if 0 <= port <= 65535:
            return True
        else:
            return False
    except ValueError:
        return False

def validate_timeout(timeouts):
  try:
        timeouts = int(timeouts)
        if 1 <= timeouts <= 5:
            return True
        else:
            return False
  except ValueError:
        return False

# function port scanner
def port_scanner():
  while True:
    os.system('clear')
    banner_scanIp()
    
    target = input(cyan+'╰─ ' + blue + 'Target: '+white)
    if target in('menu','Menu','MENU','m','M'):
      main()
    elif target in('exit','Exit','EXIT','ex','Ex','EX'):
      print(red+'[!] exit')
      time.sleep(.5)
      exit()
    else:
      pass
    
    if not validate_ip_address(target):
        print(red + '[!] Alamat IP tidak valid')
        time.sleep(2)
        continue
    
    ports = input(cyan+'╰─ ' + blue + 'Port: '+white)
    
    timeouts = input(cyan+'╰─ ' + blue + 'Time Out: '+white)
    if not validate_timeout(timeouts):
        print(red + '[!] error[timeout(1-5)]')
        time.sleep(2)
        continue
    
    
    if ',' in ports:
        portlist = ports.split(',')
        for port in portlist:
            if not validate_port(port):
                print(red + f'[!] Port tidak valid: {port}')
                continue
            scan(target, int(port), int(timeouts))
    elif '-' in ports:
        portrange = ports.split('-')
        start = portrange[0]
        end = portrange[1]
        if not validate_port(start) or not validate_port(end):
            print(red + '[!] Port tidak valid')
            time.sleep(2)
            continue
        for port in range(int(start), int(end)+1):
            scan(target, port, int(timeouts))
    elif ports == 'all':
      for port in range(1, 65535+1):
        scan(target, port, int(timeouts))
    else:
        if not validate_port(ports):
            print(red + '[!] Port tidak valid')
            time.sleep(2)
            continue
        scan(target, int(ports), int(timeouts))
    cip = input(cyan+'╰─ ' + blue + 'Menu(y/n)'+white)
    if cip in('menu','Menu','MENU','m','M','y','Y'):
      main()
    elif cip in('exit','Exit','EXIT','ex','Ex','EX'):
      print(red+'[!] exit')
      time.sleep(.5)
      exit()
    else:
      pass

# function check ip
def check_ip():
  while True:
    try:
      os.system('clear')
      banner_checkIp()
      hostname = input(cyan+'╰─ ' + blue+'domain name: '+white)
      
      if hostname in('menu','Menu','m','M'):
        main()
      elif hostname in('exit','Exit','quit','Quit','ex'):
        print(red+'[!] exit')
        time.sleep(.5)
        exit()
      else:
        pass
      
      if ',' in hostname:
        host = hostname.split(',')
        for hostname in host:
          ipaddress = socket.gethostbyname(hostname)
          print(red+'\n', '='*40)
          print(green + f"domain name : {hostname}")
          print(green + f"ip address : {ipaddress}")
          print(red+'='*40)
      else:
        ipaddress = socket.gethostbyname(hostname)
        '''req_url = 'https://geolocation-db.com/jsonp/' + ipaddress
        response = requests.get(req_url)
        geolocation = response.content.decode()
        geolocation = geolocation.split("(")[1].strip(")")
        geolocation = json.loads(geolocation)'''
      
        print(red+'\n', '='*40)
        print(green + f"'domain name : {hostname}'")
        print(green + f"'ip address : {ipaddress}'")
        '''for k, v in geolocation.items():
         print(green + f"{str(k)} : {str(v)}")'''
        print(red+'='*40)
      cip = input(cyan+'╰─ ' + blue + 'Menu(y/n)'+white)
      if cip in('menu','Menu','MENU','m','M','y','Y'):
        main()
      elif cip in('exit','Exit','EXIT','ex','Ex','EX'):
        print(red+'[!] exit')
        time.sleep(.5)
        exit()
      else:
        pass
    except socket.gaierror:
      print(red+'[!] not https/Connection Error')
      time.sleep(.8)
    except KeyboardInterrupt:
      print(red+'[!] keywoord error')
      time.sleep(.8)
    
# function email_scraper
def email_scraper():
    while True:
      try:
        os.system('clear')
        banner_scraper()
        user_url = str(input(cyan+'╰─ ' + blue+'URL: '+white))
        if user_url in('menu','Menu','m','M'):
          main()
        elif user_url in('exit','Exit','ex','Ex','quit','Quit'):
          print(red+'[!] exit')
          time.sleep(.5)
          exit()
        else:
          pass
        urls = deque([user_url])
        scraped_urls = set()
        emails = set()
        count = 0
        limit = int(input(cyan+'╰─ ' + blue+'limit: '+white))
        
        try:
          while True:
            count += 1
            if count > limit:
              break
            
            if urls:
              url = urls.popleft()
            else:
              print(red+"\n[!] List is empty!")
              break
              
            scraped_urls.add(url)
            parts = urllib.parse.urlsplit(url)
            base_url = f'{parts.scheme}://{parts.netloc}'
            path = url[:url.rfind('/')+1] if '/' in parts.path else url
            
            print(green+'['+white+f'{count}'+green+']'+green+' processing '+red+f'{url}')
            
            try:
              response = requests.get(url)
            except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
              continue
        
            new_emails = set(re.findall(r'[a-z0-9\.\-+_]+@\w+\.+[a-z\.]+', response.text, re.I))
            emails.update(new_emails)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            for anchor in soup.find_all('a'):
              link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
              if link.startswith('/'):
                link = base_url + link
              elif not link.startswith('http') or link.startswith('https'):
                link = path + link
              if not link in urls and not link is scraped_urls:
                urls.append(link)
            
        except KeyboardInterrupt:
          print(red+'[-] Closing')
          
        print(green+'\n[!] proccess done\n')
        print(cyan+f'{len(emails)}'+yellow+' emails \n','='*40)
        for mail in emails:
          print('  '+mail)
        print('\n')
        cin = input(cyan+'╰─ ' + blue + 'Menu(y/n): '+white)
        if cin in('menu','Menu','MENU','m','M','y','Y'):
          main()
        elif cin in('exit','Exit','EXIT','ex','Ex','EX'):
          print(red+'[!] exit')
          time.sleep(.5)
          exit()
        else:
          pass
      except ValueError:
        pass

# function menu
def main():
  while True:
    tex = ['pilih yang bener asu','pilih yang bener ngntd','pilih yang bener ajg','bisa baca ga sih']
    os.system('clear')
    banner()
    cetak(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Check IP[bold white] [/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Port Scanner[bold white]\n[bold white][[bold cyan]03[/][bold white]][/] [bold white]Email Scraper[bold white]\n[bold white][[bold cyan]04[/][bold white]][/] [bold white]Update Tools[bold white]\n\n[bold red][+] use the exit command to quit[bold white]',width=43,title=f"[bold purple]Menu",style=f"bold purple"))
    
    input_menu = input(cyan+'╰─ ' + white+'Opsi : ')
    if input_menu in('1','01'):
      check_ip()
    elif input_menu in('2','02'):
      port_scanner()
    elif input_menu in('3','03'):
      email_scraper()
    elif input_menu in('exit','quit'):
      print(red+'\n[!] exit')
      time.sleep(.5)
      exit()
    elif input_menu in('4','04'):
      os.system('python .update.py')
      exit()
    else:
      print(red + f'[!] {random.choice(tex)}')
      time.sleep(1)
      
# function basa-basi
class basa_basi():
  os.system('clear')
  cetak(panel(f" [bold white][+] Hallo Cuy Gw [bold red]NdyZ [bold white]Dan Gw harap anda tidak recode sc ini \n [+] Dan Semua Pengguna Termux. Semoga Kalian makin pro wkwkwk \n [+] Beribu-Ribu Kali Mohon Maaf jika ingin recode silahkan izin sama author, oke..?\n [+] Jangan Lupa Juga Cuy [bold red]donasi[bold white] Untuk Gw Yakan Awokawok \n [bold white][+][bold green] Dana : [bold red]085346923840 \n [bold white][+][bold green] Pulsa : [bold red]085346923840 \n [bold white][+] Thanks To All",width=100,padding=(0,2),title=f"[bold cyan]Basa-Basi",style=f"bold purple"))
  time.sleep(.5)
  main()
  
# function start/run program
if __name__=='__main__':
  basa_basi()