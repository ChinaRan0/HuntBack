import requests
def check(ip,port):
    try:
        res =requests.get(f"https://{ip}:{port}/login",verify=False,timeout=3)
        res.encoding="utf-8"
        if "资产灯塔系统" in res.text:
            print(f"https://{ip}:{port}/login----灯塔ARL")
    except:
        pass