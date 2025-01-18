import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/auth/login",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "大宝剑-实战化攻防对抗系统" in res.text:
            print(f"http://{ip}:{port}/auth/login----大宝剑(边界资产梳理工具)")
            return "大宝剑(边界资产梳理工具)"
    except:
        pass