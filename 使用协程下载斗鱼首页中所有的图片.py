import urllib.request
import re


max_retry_count = 3

def down_img(url):
    """https://rpic.douyucdn.cn/live-cover/appCovers/2017/10/24/12017.jpg"""
    for i in range(max_retry_count):
        try:
            response = urllib.request.urlopen(url)
            # bytes
            data = response.read()

            # 从url中得到文件名
            file_name = url[url.rfind('/')+1:]

            # 打开文件用以写入
            with open("img/"+ file_name, "wb") as file:
                file.write(data)

        except Exception as e:
            print("出错 %s 正在重试" % e)
        else:
            break

if __name__ == '__main__':
    home = """http://www.58pic.com/"""
    # 请求的时候需要带上头部 可以防止初步的反爬措施
    headers = {
        "Host":"www.58pic.com",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    # 构造好请求对象 将请求提交到服务器 获取的响应就是到首页的html代码
    request = urllib.request.Request(url=home, headers=headers)

    # urlopen函数可以直接传入url网址 也可以指定好一个请求对象
    response = urllib.request.urlopen(request)

    # 将收到的响应对象中数据的bytes数据读出出来 并且解码
    html_data = response.read().decode()

    # 使用正则 从首页网页中 提取出所有的图片链接
    img_list = re.findall(r"http://.*?\.(?:jpg|png|gif)", html_data)
    print(img_list)
    for img_url in img_list:
        down_img(img_url)