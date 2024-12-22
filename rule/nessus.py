import requests
def check(ip,port):
    try:
        res =requests.get(f"https://{ip}:{port}/#/",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "Nessus" in res.text:
            print(f"https://{ip}:{port}/#/user/login----Nessus(漏洞扫描器)")
    except:
        pass