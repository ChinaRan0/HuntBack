import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "XRay Report" in res.text:
            print(f"http://{ip}:{port}/----Xray_scan(Xray扫描器)")
    except:
        pass