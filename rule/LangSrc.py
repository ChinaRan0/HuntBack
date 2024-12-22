import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "LangSrc" in res.text:
            print(f"https://{ip}:{port}/#/user/login----LangSrc(资产监控平台)")
    except:
        pass