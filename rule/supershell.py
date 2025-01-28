import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/supershell/login",timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "Supershell" in res.text:
            print(f"http://{ip}:{port}/supershell/login----SuperShell(C2)")
            return "SuperShell(C2)"
    except:
        pass