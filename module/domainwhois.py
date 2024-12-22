import whois
from prettytable import PrettyTable
import datetime

def get_whois_info(domain):
    try:
        # 查询域名的WHOIS信息
        w = whois.whois(domain)
        
        # 创建表格对象
        table = PrettyTable()
        
        # 设置表格的列名
        table.field_names = ["Field", "Value"]
        
        # 设置表格的最大列宽
        table.max_width = 50  # 设置最大列宽，超过这个宽度会自动换行
        
        # 将WHOIS信息的关键字段添加到表格中
        for field, value in w.items():
            if value:
                # 如果值是datetime类型，格式化成字符串
                if isinstance(value, list):
                    value = [str(v)[:30] for v in value]  # 截取字符串的前30个字符
                elif isinstance(value, datetime.datetime):
                    value = value.strftime('%Y-%m-%d %H:%M:%S')  # 格式化datetime对象

                # 如果字段值过长，缩短或者将其拼接为字符串
                if isinstance(value, list):
                    value = ', '.join(value[:5]) + ('...' if len(value) > 5 else '')
                elif isinstance(value, str) and len(value) > 50:
                    value = value[:47] + '...'  # 字符串过长时截取
            
                # 添加到表格
                table.add_row([field, value])
        
        # 输出表格
        print(table)
        
    except whois.parser.PywhoisError:
        print(f"Error: WHOIS information for '{domain}' could not be retrieved. The domain may not exist or the server may be down.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
