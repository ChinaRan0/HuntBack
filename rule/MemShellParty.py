import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/",timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "MemShellParty" in res.text:
            print(f"http://{ip}:{port}/----MemShellParty(内存马生成器)")
            return "MemShellParty(内存马生成器)"
    except:
        pass