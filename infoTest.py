import warnings
warnings.filterwarnings("ignore")
import os
import time
from datetime import datetime
from tqdm import tqdm
from rule import arl, viper, awvs, medusa, nessus, LangSrc,supershell ,nemo, NextScan, Manjusaka, Hzichan, nps, nps2, ChatGPTnextWeb, DBJ, linbing, ScopeSentry, PrismX, CyberEdge, cyberedge_, SerializedPayloadGenerator, xray_dongjian, xray_scan, vulfocus, Vulinbox, golin, JavaChains, cs, vshell_tcp, afrog, XSS_Platform, reNgine, gophish, TestNet,http_test_rule,Directory,openVAS,revsuit,MemShellParty
from concurrent.futures import ThreadPoolExecutor, as_completed
import rule.http_test as http_test

postType = ''

def finger(IPport):
    ip, port = IPport.split(":") 
    port = int(port)

    # 首先使用http_test检查是否为HTTP/HTTPS服务
    is_http_https = http_test.check(ip, port)

    results = []

    if is_http_https:
        # 如果是HTTP/HTTPS服务，继续进行HTTP/HTTPS检测
        checks = [
            arl.check,
            viper.check,
            awvs.check,
            medusa.check,
            nessus.check,
            LangSrc.check,
            nemo.check,
            NextScan.check,
            Manjusaka.check,
            Hzichan.check,
            nps.check,
            nps2.check,
            ChatGPTnextWeb.check,
            DBJ.check,
            linbing.check,
            ScopeSentry.check,
            PrismX.check,
            CyberEdge.check,
            cyberedge_.check,
            SerializedPayloadGenerator.check,
            xray_dongjian.check,
            xray_scan.check,
            vulfocus.check,
            Vulinbox.check,
            golin.check,
            JavaChains.check,
            XSS_Platform.check,
            vshell_tcp.check,
            afrog.check,
            reNgine.check,
            gophish.check,
            TestNet.check,
            Directory.check,
            http_test_rule.check,
            openVAS.check,
            revsuit.check,
            MemShellParty.check,
            supershell.check
        ]

        # 使用线程池加速执行
        with ThreadPoolExecutor() as executor:
            # 通过executor.submit提交所有任务
            futures = [executor.submit(check, ip, port) for check in checks]
            
            # 使用tqdm显示进度条，注意tqdm和线程池并发执行时的同步
            for future in tqdm(as_completed(futures), total=len(futures), desc=f"主动探测指纹： {ip}:{port}", unit="check"):
                result = future.result()  # 获取结果
                if result:
                    results.append({"ip": ip, "port": port, "type": "Web", "name": result})

    else:
        # 如果不是HTTP/HTTPS服务，使用JARM_test进行进一步检测
        result = cs.check(ip, port)
        if result:
            results.append({"ip": ip, "port": port, "type": "Other", "name": result})

    return results
  