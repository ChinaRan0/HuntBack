import argparse
import socket
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import infoTest
from module import ipwhois_Search
from tqdm import tqdm
from module import domainwhois

def is_port_open(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=1):
            return True
    except (socket.timeout, socket.error):
        return False

def scan_ports(target_ip, port_list, num_threads=10):
    open_ports = []
    
    # 创建进度条，指定总任务数
    with tqdm(total=len(port_list), desc="扫描端口中:", unit="port") as pbar:
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = {executor.submit(is_port_open, target_ip, port): port for port in port_list}

            for future in concurrent.futures.as_completed(futures):
                port = futures[future]
                try:
                    if future.result():
                        open_ports.append(port)
                except Exception as e:
                    print(f"Error scanning port {port}: {e}")
                # 每完成一个端口扫描，更新进度条
                pbar.update(1)
    
    return open_ports

def main_info(ipInput, porttype):
    target_ip = ipInput
    if porttype == "common":
        port_list = [80, 443, 8080, 22, 3389,4567,8010, 5003, 47808 ,8888, 3443, 5000, 6000,9443, 7000, 8081, 5005, 3200, 8001, 8834, 8082, 8083, 8084, 8085, 11000, 8800]  # 常用端口列表
    elif porttype == "all":
        port_list = range(1, 65536)  # 全端口扫描
    
    open_ports = scan_ports(target_ip, port_list)
    zichanList = []  # 存储开放端口列表

    if open_ports:
        for it in open_ports:
            zichanList.append(f"{target_ip}:{it}")
            print(f"{target_ip}:{it}")

    if len(zichanList) != 0:
        for zichan in zichanList:
            infoTest.finger(zichan)

    else:
        print(f"没有常用红队端口开放 {target_ip}")

def import_file(file_path):
    with open(file_path, 'r') as f:
        ips = f.readlines()
    return [ip.strip() for ip in ips]

def process_ip(ip):
    print(f"处理 IP 地址: {ip}")

def main():
    parser = argparse.ArgumentParser(description="""本程序为蓝队在进行防守过程中，对威胁情报或者安全设备上恶意IP进行溯源的工具
    程序功能：文件导入、循环模式、单IP模式   By:ChinaRan404&知攻善防实验室""")
    
    # 文件导入方式
    parser.add_argument('--file', type=str, help="输入文件路径")
    
    # 循环模式
    parser.add_argument('--cmds', action='store_true', help="启用循环模式，用于常驻终端")
    
    # 单IP模式
    parser.add_argument('--ip', type=str, help="输入单个IP地址进行处理")

    parser.add_argument('--ipwhois', type=str, help="IPwhois查询")

    parser.add_argument('--domainwhois', type=str, help="域名Whois查询")

    # 可选参数，启用全端口扫描
    parser.add_argument('--fullscan', action='store_true', help="【可选参数】启用全端口扫描")

    args = parser.parse_args()

    if args.file:
        # 文件导入方式
        print(f"从文件 {args.file} 导入 IP 地址列表")
        ips = import_file(args.file)
        for ip in ips:
            process_ip(ip)
            # 根据是否启用全端口扫描，选择扫描方式
            porttype = "all" if args.fullscan else "common"
            main_info(ip, porttype)

    elif args.cmds:
        # 循环模式
        print("启用循环模式，处理多个IP地址")
        while True:
            ip = input("请输入一个 IP 地址 (或输入 'exit' 退出): ")
            if ip.lower() == 'exit':
                break
            # 根据是否启用全端口扫描，选择扫描方式
            porttype = "all" if args.fullscan else "common"
            main_info(ip, porttype)

    elif args.ip:
        # 单IP模式
        print(f"处理单个 IP 地址: {args.ip}")
        # 根据是否启用全端口扫描，选择扫描方式
        porttype = "all" if args.fullscan else "common"
        main_info(args.ip, porttype)

    elif args.ipwhois:
        ipwhois_Search.ipwhois(args.ipwhois)
    
    elif args.domainwhois:
        domainwhois.get_whois_info(args.domainwhois)

    else:
        print("请提供有效的参数。使用 -h 查看帮助信息。")

if __name__ == "__main__":
    main()
