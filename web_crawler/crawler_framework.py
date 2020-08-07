import requests
import time


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态码不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


if __name__ == '__main__':
    start_time = time.time()
    for i in range(100):
        url = 'http://www.baidu.com'  # 8.933248519897461
        # url = 'http://www.bit.edu.cn'  # 50.076802492141724
        print(getHTMLText(url))
    end_time = time.time()

    time = end_time - start_time
    print(time)

