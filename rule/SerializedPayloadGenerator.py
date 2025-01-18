import requests
def check(ip,port):
    try:
        res =requests.get(f"http://{ip}:{port}/",verify=False,timeout=3)
        res.encoding="utf-8"
        # print(res.text)
        if "Home Page - Serialized Payload Generator" in res.text:
            print(f"http://{ip}:{port}/----SerializedPayloadGenerator(反序列化生成器)")
            return "SerializedPayloadGenerator(反序列化生成器)"
    except:
        pass