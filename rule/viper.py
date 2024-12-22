import requests
def check(ip,port):
    try:
        res =requests.get(f"https://{ip}:{port}/#/user/login",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "VIPER" in res.text:
            print(f"https://{ip}:{port}/#/user/login----Viper(C2)")
    except:
        pass