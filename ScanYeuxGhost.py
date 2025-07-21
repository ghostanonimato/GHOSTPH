print(r"""
   _____                                 _   __           
  / ____|                               | | / /           
 | (___   ___  ___ _   _ _ __ ___   __ _| |/ / ___  _ __  
  \___ \ / _ \/ __| | | | '_ ` _ \ / _` |    \ / _ \| '_ \ 
  ____) |  __/ (__| |_| | | | | | | (_| | |\  \ (_) | | | |
 |_____/ \___|\___|\__,_|_| |_| |_|\__,_\_| \_/\___/|_| |_|
                                                            
        Scanner de Redes - Projeto Didático
        Autor: YeuxGhost
        Github: https://github.com/ghostanonimato
        -----------------------------------
""")
"""
Scanner de Redes Didático em Python
-----------------------------------
Este script realiza:
1. Descoberta de hosts ativos na rede local usando ARP.
2. Scan de portas TCP em cada host encontrado.
Requer privilégios de administrador para enviar pacotes ARP.
"""


from scapy.all import ARP, Ether, srp, IP, TCP, sr1, conf
import socket

def descobrir_hosts(rede):
    """
    Descobre hosts ativos na rede usando ARP.
    :param rede: string com o endereço da rede (ex: '192.168.1.0/24')
    :return: lista de IPs ativos
    """
    print(f"[*] Descobrindo hosts ativos na rede {rede}...")
    # Cria um pacote ARP para toda a rede
    pacote = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=rede)
    # Envia o pacote e recebe as respostas
    resultado = srp(pacote, timeout=2, verbose=0)[0]
    hosts = []
    for enviado, recebido in resultado:
        # Corrigido: verifica se recebido tem atributo 'psrc'
        if hasattr(recebido, 'psrc'):
            hosts.append(recebido.psrc)
    print(f"[+] {len(hosts)} hosts encontrados.")
    return hosts

def scan_portas(ip, portas):
    """
    Realiza um scan de portas TCP em um host.
    :param ip: IP do host alvo
    :param portas: lista de portas a serem testadas
    :return: lista de portas abertas
    """
    print(f"[*] Escaneando portas em {ip}...")
    portas_abertas = []
    conf.verb = 0  # Desativa verbosidade do scapy
    for porta in portas:
        pkt = IP(dst=ip)/TCP(dport=porta, flags="S")
        resp = sr1(pkt, timeout=0.5, verbose=0)
        if resp and resp.haslayer(TCP) and resp[TCP].flags == 0x12:
            portas_abertas.append(porta)
            # Envia RST para fechar conexão
            sr1(IP(dst=ip)/TCP(dport=porta, flags="R"), timeout=0.1, verbose=0)
    return portas_abertas

def obter_nome_host(ip):
    """
    Tenta obter o nome do host via DNS reverso.
    """
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return "Desconhecido"
# Defina sua rede local aqui (ex: '192.168.1.0/24')
rede = input("Digite o endereço da rede (ex: 192.168.1.0/24): ")
hosts = descobrir_hosts(rede)
portas_comuns = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]
for ip in hosts:
    nome = obter_nome_host(ip)
    print(f"\nHost: {ip} ({nome})")
    portas_abertas = scan_portas(ip, portas_comuns)
    if portas_abertas:
        print(f"  Portas abertas: {', '.join(map(str, portas_abertas))}")
    else:
        print("  Nenhuma porta comum aberta encontrada.")