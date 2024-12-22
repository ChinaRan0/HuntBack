import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/#/user/login",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "Medusa doesn't work properly without JavaScript" in res.text:
            print(f"https://{ip}:{port}/----美杜莎红队武器库平台")
    except:
        pass