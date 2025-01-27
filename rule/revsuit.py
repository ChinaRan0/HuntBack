import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/",timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "RevSuit Control Pane" in res.text:
            print(f"http://{ip}:{port}/----RevSuit(反连平台)")
            return "RevSuit(反连平台)"
    except:
        pass