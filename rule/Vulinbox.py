import requests
def check(ip,port):
    try:
        res =requests.get(f"https://{ip}:{port}/",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "Vulinbox - Agent" in res.text:

            print(f"https://{ip}:{port}/----Vulinbox(Yakit靶场)")
            return "Vulinbox(Yakit靶场)"
    except:
        pass
