import requests
def check(ip,port):
    try:
        res =requests.get(f"https://{ip}:{port}/user/login?redirect=/",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "Prism X" in res.text and "root" in res.text:
            print(f"https://{ip}:{port}/user/login?redirect=/----PrismX(PrismX/棱镜X·单兵渗透平台)")
            return "PrismX(PrismX/棱镜X·单兵渗透平台)"
    except:
        pass