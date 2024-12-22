from ipwhois import IPWhois
import prettytable as pt

def ipwhois(ip):
    # 定义要查询的IP地址
    ip_address = ip

    # 使用ipwhois库获取IP地址的whois信息
    obj = IPWhois(ip_address)
    whois_info = obj.lookup_rdap()

    # 创建一个PrettyTable对象
    table = pt.PrettyTable()

    # 定义表格的字段名
    table.field_names = ['Field', 'Value']

    def add_to_table(key, value):
        if value is not None:  # 检查值是否为None
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    add_to_table(f"{key}/{sub_key}", sub_value)
            elif isinstance(value, list):
                for item in value:
                    add_to_table(key, item)
            else:
                table.add_row([key, str(value)])

    # 遍历whois_info字典，并添加到表格中
    for key, value in whois_info.items():
        add_to_table(key, value)

    # 设置表格风格
    table.set_style(pt.MSWORD_FRIENDLY)

    # 打印表格
    print(table)