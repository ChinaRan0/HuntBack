import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/login/?next=/",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "Login reNgine" in res.text:
            print(f"http://{ip}:{port}/----reNgine(Web渗透工具)")
            return "reNgine(Web渗透工具)"
    except:
        pass