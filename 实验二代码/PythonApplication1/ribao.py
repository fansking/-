import urllib.request
import re
import time
url='http://daily.zhihu.com/'

 
def getHtml(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36'}#每台计算机到模拟登录不一样，具体知浏览器寻找
    myrequest = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(myrequest)
    text = response.read()
    return text
 
 
def getUrls(html):#解析每条日报到链接
    html=html.decode('utf-8')
    pattern = re.compile('<a href="/story/(.*?)"', re.S)
    items = re.findall(pattern, html)
    urls=[]
    for item in items:
        urls.append('http://daily.zhihu.com/story/'+item)
 
    return urls
 
 
def getContent(url):
    html = getHtml(url)
    html = html.decode('utf-8')
    patten = re.compile('<h1 class="headline-title">(.*?)</h1>')
    items = re.findall(patten, html)
    #raw.write(items[0])
    pattern2 = re.compile('<div class="content">\\n<p>(.*?)</div>',re.S)
    items_withtag = re.findall(pattern2, html)
    for items2 in items_withtag:
        for content in characterProcessing(items2):
            raw.write(content)
 
def characterProcessing(html):
    pattern = re.compile('<p>(.*?)</p>|<li>(.*?)</li>.*?', re.S)
    items3 = re.findall(pattern,html)
    result = []
    for index in items3:
        if index != '':
            for content in index:
                tag = re.search('<.*?>', content)
                http = re.search('<.*?http.*?',content)
                html_tag = re.search('&',content)
                if html_tag:
                    content = html.unescape()
                if http:
                    continue
                elif tag:
                    pattern = re.compile('(.*?)<.*?>(.*?)</.*?>(.*?)')
                    items4 = re.findall(pattern, content)
                    content_tags = ''
                    if len(items4) > 0:
                        for item in items4:
                            if len(item) > 0:
                                for item_s in item:
                                    content_tags = content_tags + item_s
                            else:
                                content_tags = content_tags + items4
                        content_tags = re.sub('<.*?>','',content_tags)
                        result.append(content_tags)
                    else:
                        continue
                else:
                    result.append(content)
    return result
 
 

html = getHtml(url)
urls = getUrls(html)
with open("./output/rawfile/ribao_result.txt",'w',encoding='utf-8') as raw: 
    for url in urls:
        try:
            
           getContent(url)
            
        except Exception as e:
            time.sleep(1)

raw.close()
print('完成操作')