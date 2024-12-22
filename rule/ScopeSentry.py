import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/#/login?redirect=/dashboard",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "Scope Sentry" in res.text:
            print(f"http://{ip}:{port}/#/login?redirect=/dashboard----ScopeSentry(信息收集资产管理系统)")
    except:
        pass