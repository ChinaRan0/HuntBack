import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "Nemo" in res.text:
            print(f"https://{ip}:{port}/----nemo(自动化信息收集)")
    except:
        pass