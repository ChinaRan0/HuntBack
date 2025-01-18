import requests
def check(ip,port):
    try:
        res =requests.get(f"https://{ip}:{port}/login?next=%2F",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "Gophish" in res.text:
            print(f"https://{ip}:{port}/login?next=%2F----gophish(钓鱼工具)")
            return "gophish(钓鱼工具)"
    except:
        pass