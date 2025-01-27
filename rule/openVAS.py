import requests
def check(ip,port):
    try:
        res =requests.get(f"https://{ip}:{port}/login",timeout=3,verify=False)
        res.encoding="utf-8"
        # print(res.text)
        if "Greenbone Security Assistant" in res.text:
            print(f"https://{ip}:{port}/login----OpenVAS(漏洞扫描)")
            return "OpenVAS(漏洞扫描)"
    except:
        pass
