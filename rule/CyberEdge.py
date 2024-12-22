import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/target/list",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "<title>CyberEdge</title>" in res.text:
            print(f"http://{ip}:{port}/target/list----CyberEdge(未知开发者-信息收集平台)")
    except:
        pass
