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
from rule import vshel_tcp
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


def finger(IPport):
    ip, port = IPport.split(":") 
    port = int(port)

    # 定义需要执行的检查列表
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
        cs.check,
        vshel_tcp.check
    ]

    # 使用线程池加速执行
    with ThreadPoolExecutor() as executor:
        # 通过executor.submit提交所有任务
        futures = [executor.submit(check, ip, port) for check in checks]
        
        # 使用tqdm显示进度条，注意tqdm和线程池并发执行时的同步
        for future in tqdm(as_completed(futures), total=len(futures), desc=f"主动探测指纹： {ip}:{port}", unit="check"):
            future.result()  # 获取结果（如果需要的话，可以处理返回值）