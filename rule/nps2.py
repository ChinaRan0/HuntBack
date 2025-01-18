import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/login/index",timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if '<a href="https://ehang.io/nps"' in res.text:
            print(f"http://{ip}:{port}/login/index----NPS(穿透工具)")
            return "NPS(穿透工具)"
    except:
        pass
