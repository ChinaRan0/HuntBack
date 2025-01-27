import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/",timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "Directory listing for" in res.text:
            print(f"http://{ip}:{port}/----Directory(目录浏览)")
            return "Directory(目录浏览)"
    except:
        pass