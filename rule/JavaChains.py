import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/#/login",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "Jains" in res.text:
            print(f"http://{ip}:{port}/----Java Chains(Java反序列化攻击工具)")
            return "Java Chains(Java反序列化攻击工具)"
    except:
        pass
