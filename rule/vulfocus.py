import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/#/login?redirect=%2Fdashboard",timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "vulfocus" in res.text:
            print(f"http://{ip}:{port}/#/login?redirect=%2Fdashboard----vulfocus(vulfocus漏洞平台)")
            return "vulfocus漏洞平台"
    except:
        pass
