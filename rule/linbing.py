import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/#/login?redirect=%2Fdashboard",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "临兵" in res.text:
            print(f"http://{ip}:{port}/#/login?redirect=%2Fdashboard----临兵(漏扫)")
            return "临兵(漏扫)"
    except:
        pass