import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/login",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "Flask Datta Able" in res.text:
            print(f"http://{ip}:{port}/login----H(资产收集)")
            return "H(资产收集)"
    except:
        pass