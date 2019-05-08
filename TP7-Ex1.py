from psutil import net_if_addrs
import netifaces

def infoRede():
    info = net_if_addrs()
    gateway = netifaces.gateways()
    print("IP: ", info['Ethernet 7'][1][1])
    print("Gateway: ", gateway['default'][2][0])
    print("Mascara de subrede: ", info['Ethernet 7'][1][2])
    
infoRede()