import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/swt",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "enabledelayedexpansion" in res.text:
            print(f"http://{ip}:{port}/swt----C2(Vshell_tcp)")
    except:
        pass