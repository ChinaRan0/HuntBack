import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "ChatGPT Next Web" in res.text:
            print(f"http://{ip}:{port}/----ChatGPT Next Web")
    except:
        pass