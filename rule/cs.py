from jarm.scanner.scanner import Scanner

def check(ip, port):
    try:
        print("[-]正在探测JARM指纹,可能会报错,请忽略")
        res = Scanner.scan(dest_host=ip, dest_port=int(port),timeout=5)
        if res[0] == "2ad2ad16d2ad2ad00042d42d00042ddb04deffa1705e2edc44cae1ed24a4da":
            print(f"tcp://{ip}:{port}----C2服务器(Cobalt Strike)")
            return "C2服务器(Cobalt Strike)"
        elif res[0] == "2ad2ad0002ad2ad00042d42d000000ad9bf51cc3f5a1e29eecb81d0c7b06eb":
            print(f"tcp://{ip}:{port}----C2服务器(Mythic)")
            return "C2服务器(Mythic)"
        elif res[0] == "07d14d16d21d21d00042d43d000000aa99ce74e2c6d013c745aa52b5cc042d":
            print(f"tcp://{ip}:{port}----C2服务器(Metasploit ssl listener)")
            return  "C2服务器(Metasploit ssl listener)"
        elif res[0] == "07d14d16d21d21d07c42d43d000000f50d155305214cf247147c43c0f1a823":
            print(f"tcp://{ip}:{port}----C2服务器(Metasploit ssl listener)")
            return "C2服务器(Metasploit ssl listener)"
        elif res[0] == "07d14d16d21d21d07c42d41d00041d24a458a375eef0c576d23a7bab9a9fb1":
            print(f"tcp://{ip}:{port}----C2服务器(Cobalt Strike)")
            return "C2服务器(Cobalt Strike)"
        elif res[0] == "29d21b20d29d29d21c41d21b21b41d494e0df9532e75299f15ba73156cee38":
            print(f"tcp://{ip}:{port}----C2服务器(Merlin)")
            return "C2服务器(Merlin)"
        elif res[0] == "00000000000000000041d00000041d9535d5979f591ae8e547c5e5743e5b64":
            print(f"tcp://{ip}:{port}----C2服务器(CDeimos)")
            return "C2服务器(CDeimos)"
        elif res[0] == "2ad2ad0002ad2ad22c42d42d000000faabb8fd156aa8b4d8a37853e1063261":
            print(f"tcp://{ip}:{port}----C2服务器(MacC2)")
            return "C2服务器(MacC2)"
        elif res[0] == "2ad000000000000000000000000000eeebf944d0b023a00f510f06a29b4f46":
            print(f"tcp://{ip}:{port}----C2服务器(MacShellSwift)")
            return "C2服务器(MacShellSwift)"
        elif res[0] == "2ad2ad0002ad2ad00041d2ad2ad41da5207249a18099be84ef3c8811adc883":
            print(f"tcp://{ip}:{port}----C2服务器(Sliver)")
            return "C2服务器(Sliver)"
        elif res[0] == "20d14d20d21d20d20c20d14d20d20daddf8a68a1444c74b6dbe09910a511e6":
            print(f"tcp://{ip}:{port}----C2服务器(EvilGinx2)")
            return "C2服务器(EvilGinx2)"
        elif res[0] == "2ad2ad0002ad2ad00042d42d000000ad9bf51cc3f5a1e29eecb81d0c7b06eb":
            print(f"tcp://{ip}:{port}----C2服务器(Shad0w)")
            return "C2服务器(Shad0w)"
        elif res[0] == "07d19d12d21d21d07c07d19d07d21da5a8ab90bcc6bf8bbc6fbec4bcaa8219":
            print(f"tcp://{ip}:{port}----C2服务器(Get2)")
            return "C2服务器(Get2)"
        elif res[0] == "2ad2ad0002ad2ad00042d42d000000ad9bf51cc3f5a1e29eecb81d0c7b06eb":
            print(f"tcp://{ip}:{port}----C2服务器(GRAT2 C2)")
            return  "C2服务器(GRAT2 C2)"
        elif res[0] == "21d14d00000000021c21d14d21d21d1ee8ae98bf3ef941e91529a93ac62b8b":
            print(f"tcp://{ip}:{port}----C2服务器(Covenant)")
            return  "C2服务器(Covenant)"
        elif res[0] == "2ad2ad0002ad2ad00042d42d000000ad9bf51cc3f5a1e29eecb81d0c7b06eb":
            print(f"tcp://{ip}:{port}----C2服务器(SILENTRINITY)")
            return "C2服务器(SILENTRINITY)"
        elif res[0] == "2ad2ad0002ad2ad22c42d42d000000faabb8fd156aa8b4d8a37853e1063261":
            print(f"tcp://{ip}:{port}----C2服务器(PoshC2)")
            return "C2服务器(PoshC2)"
        elif res[0] == "1dd40d40d00040d1dc1dd40d1dd40d3df2d6a0c2caaa0dc59908f0d3602943":
            print(f"tcp://{ip}:{port}----C2服务器(AsyncRAT)")
            return "C2服务器(AsyncRAT)"
        elif res[0] == "22b22b09b22b22b22b22b22b22b22b352842cd5d6b0278445702035e06875c":
            print(f"tcp://{ip}:{port}----C2服务器(Trickbot)")
            return "C2服务器(Trickbot)"

    except Exception as e:
        # 忽略其他异常并记录错误信息（可选）
        print(f"Error scanning {ip}:{port} - {str(e)}")
        pass