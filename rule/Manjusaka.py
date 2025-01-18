import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/manjusaka/static/#/login?redirect=/agents",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "Manjusaka" in res.text:
            print(f"http://{ip}:{port}/#/user/login----Manjusaka(牛屎花C2管理)")
            return "Manjusaka(牛屎花C2管理)"
    except:
        pass