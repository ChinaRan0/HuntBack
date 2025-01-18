import warnings
warnings.filterwarnings("ignore")
from tqdm import tqdm
from rule import arl
from rule import viper
from rule import awvs
from rule import medusa
from rule import nessus
from rule import LangSrc
from rule import nemo
from rule import NextScan
from rule import Manjusaka
from rule import Hzichan
from rule import nps
from rule import nps2
from rule import ChatGPTnextWeb
from rule import DBJ
from rule import linbing
from rule import ScopeSentry
from rule import PrismX
from rule import CyberEdge
from rule import cyberedge_
from rule import SerializedPayloadGenerator
from rule import xray_dongjian
from rule import xray_scan
from rule import vulfocus
from rule import Vulinbox
from rule import golin
from rule import JavaChains
from rule import cs
from rule import vshell_tcp
from rule import afrog
from rule import XSS_Platform
from rule import reNgine
from rule import gophish
from rule import TestNet
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import rule.http_test as http_test

postType = ''

def finger(IPport):
    ip, port = IPport.split(":") 
    port = int(port)

    # 首先使用http_test检查是否为HTTP/HTTPS服务
    is_http_https = http_test.check(ip, port)

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
        ]

        # 使用线程池加速执行
        with ThreadPoolExecutor() as executor:
            # 通过executor.submit提交所有任务
            futures = [executor.submit(check, ip, port) for check in checks]
            
            # 使用tqdm显示进度条，注意tqdm和线程池并发执行时的同步
            for future in tqdm(as_completed(futures), total=len(futures), desc=f"主动探测指纹： {ip}:{port}", unit="check"):
                future.result()  # 获取结果（如果需要的话，可以处理返回值）
    else:
        # 如果不是HTTP/HTTPS服务，使用JARM_test进行进一步检测
        cs.check(ip, port)