import requests
import re

def check(ip, port):
    try:
        # 尝试HTTP请求
        http_url = f"http://{ip}:{port}"
        response = requests.get(http_url, timeout=5)
        title = extract_title(response.text)
        if title:
            return title

    except requests.exceptions.RequestException:
        pass

    try:
        # 尝试HTTPS请求
        https_url = f"https://{ip}:{port}"
        response = requests.get(https_url, timeout=5,verify=False)
        title = extract_title(response.text)
        if title:
            return "Http_Title:"+ title

    except requests.exceptions.RequestException:
        pass

    return False

def extract_title(html_content):
    # 使用正则表达式匹配<title>标签
    match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    else:
        return None