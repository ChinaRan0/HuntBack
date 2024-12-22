import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/target/list",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "<title>cyberedge</title>" in res.text and "We're sorry but cyberedge doesn't work properly without JavaScript "in res.text:
            print(f"http://{ip}:{port}/target/list----cyberedge(信息收集平台)")
    except:
        pass
