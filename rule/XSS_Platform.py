import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/xss.php?do=login",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "XSS Platform" in res.text:
            print(f"http://{ip}:{port}/xss.php?do=login----XSS Platform(XSS平台)")
    except:
        pass