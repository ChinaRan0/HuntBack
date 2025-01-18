import requests
def check(ip,port):
    try:
        res =requests.get(f"https://{ip}:{port}/golin/gys",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "Golin 网络安全等级保护核查工具" in res.text:
            print(f"https://{ip}:{port}/golin/gys----golin(基线核查工具)")
            return "golin(基线核查工具)"
    except:
        pass