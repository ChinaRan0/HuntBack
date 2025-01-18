import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "NextScan" in res.text:
            print(f"http://{ip}:{port}/----NextScan(黑盒扫描)")
            return "NextScan(黑盒扫描)"
    except:
        pass