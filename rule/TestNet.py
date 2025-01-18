import requests
def check(ip,port):
    try:
        res =requests.get(f"https://{ip}:{port}/login?redirect=/dashboard/analysis",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "TestNet 资产管理平台" in res.text:
            print(f"https://{ip}:{port}/login?redirect=/dashboard/analysis----TestNet(资产管理平台)")
            return "TestNet(资产管理平台)"
    except:
        pass