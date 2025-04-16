#importação
import socket
from termcolor import colored

#----------


ip = input('address: ').strip()

#formatação das portas de STR ---> INT
porta = []
with open('/storage/emulated/0/Download/py_project/ports.txt')as file:
    for port in file:
        port = port.strip()
        port = int(port)
        porta.append(port)
        
#recorte do address        
def cc(ip):
    if ip.endswith('/'):
        ip = ip[:-1]
    if ip.startswith('http://'):
        ip = ip[7:]
        print(f'endereço -- {ip} -- {colored("CONFIRMADO", "green")}')
        return ip
    elif ip.startswith('https://'):
        ip = ip[8:]
        print(f'endereço -- {ip} -- {colored("CONFIRMADO", "green")}')
        return ip
    elif ip.startswith('www.'):
        print(f'endereço -- {ip} -- {colored("CONFIRMADO", "green")}')
        return ip
    else:
        print(f'erro de digitação {ip}')
        return None

#ip = cc(ip)

#alma do negócio ou não...
def scanning(ip, porta, timeout = 3):
    for v in porta:
        #try:
        
        net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        net.settimeout(timeout)
        test = net.connect_ex((ip, v))
        if test == 0:
            print(f'address:{ip} -- {colored(v,"yellow")} --{colored("OPEN","green")}')
            
        else:
             print(f'address:{ip} -- {v} --{colored("CLOSED","red")}')
        net.close()   
        #except (socket.timeout, socket.error):
        #    print(f'address:  {ip} -----  {v} ----- CLOSED')
        

scanning(ip, porta)
#os.system('pause')