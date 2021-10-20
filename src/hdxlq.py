import requests
import random
import os

import pandas as pd
from bs4 import BeautifulSoup


def fetchData() :
    url = ""

    payload = {}

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/51.0.2704.63 Safari/537.36'
    }

    data = []
    for i in range(2) :
        if i==0 : continue

        result = requests.request("GET", url.format(i), headers=headers, data=payload)
        bs = BeautifulSoup(result.text, "html.parser")
        target = bs.find(name="div",attrs={"class":"mcon f14 l200"})
        print(target.find(name="h3", attrs={'class':'mt'}).find_all_next(name='p')[0].get_text())
        print(target.find(name="h3", attrs={'class':'mt'}).find_all_next(name='p')[1].get_text())
        print(target.find(name="h3", attrs={'class':'mt'}).find_all_next(name='p')[2].get_text())
        print(target.find(name="h3", attrs={'class':'mt'}).find_all_next(name='h3')[0].find_all_next(name='p')[0].get_text())
        ys = target.find(name="h3", attrs={'class':'mt'}).find_all_next(name='h3')[1].find_all_next(name='p')
        for j in range(len(ys)): 
            if j < 2:
                print(target.find(name="h3", attrs={'class':'mt'}).find_all_next(name='h3')[1].find_all_next(name='p')[j].get_text())
            else:
                print(target.find(name="h3", attrs={'class':'mt'}).find_all_next(name='h3')[1].find_all_next(name='p')[j].get_text())
        # obj = {
        #     'id': i,
        #     'name': target.find(name="h2"),
        #     'content': target.find(name="h3", attrs={'class':'mt'}).find(name="a").get_text(),
        #     'poem': target.find_all(name='h3')[1].find_next(name="p").get_text(),
        #     'explain': target.find_all(name='h3')[2].find_next(name="p").get_text(),
        #     'god': target.find_all(name='h3')[3].find_next(name="p").get_text(),
        #     'story': target.find_all(name='h3')[4].find_next(name="p").get_text().replace('www.911cha.com',''),
        # }

        # data.append(obj)
    
    # print("数据获取完成，开始保存")
    # data = pd.DataFrame(data)
    # data.to_csv("./data/hdxlq.csv", encoding='utf_8_sig', index=False)

# pandas.DataFrame.to_dict()的使用详解: https://blog.csdn.net/weixin_39791387/article/details/87627235
if __name__ == '__main__':
    fetchData()
    # number = random.randint(1,100)
    # data = pd.read_csv(os.getcwd()+'/data/hdxlq.csv', index_col=False)
  
    # data = data.to_dict(orient='index')
    # print(data[number])