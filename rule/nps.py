import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/login/index",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "nps" in res.text:
            print(f"http://{ip}:{port}/login/index----NPS(穿透工具)")
    except:
        pass