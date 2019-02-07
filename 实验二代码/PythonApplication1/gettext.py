
from selenium import webdriver
import time

import urllib.request

from bs4 import BeautifulSoup

import html.parser

def main():
    driver = webdriver.Chrome()  
    driver.get("https://www.zhihu.com/question/35204851") 

   
    def execute_times(times):

        for i in range(times):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            try:
                driver.find_element_by_css_selector('button.QuestionMainAction').click()
                print("page" + str(i))
                time.sleep(1)
            except:
                continue

    execute_times(5)

    result_raw = driver.page_source 
    result_soup = BeautifulSoup(result_raw, 'html.parser')
    result_bf = result_soup.prettify() 
    with open("./output/rawfile/raw_result.txt", 'w',encoding="utf-8") as raw: 
        raw.write(result_bf)
    raw.close()
    print("爬取回答页面成功!!!")


    with open("./output/rawfile/p_meta.txt", 'wb') as noscript_meta:
        p_tag = result_soup.find_all('p') 
        p_inner_all = ""
        for noscript in p_tag:
            noscript_inner = noscript.get_text()  
            p_inner_all += noscript_inner + "\n"

        noscript_all = html.parser.unescape(p_inner_all).encode('utf-8')  
        noscript_meta.write(noscript_all)

    noscript_meta.close()
    print("爬取p标签成功!!!")

if __name__ == '__main__':
    main()