# -*- coding: utf-8 -*-
"""
Created on Sun May 13 18:55:48 2018

@author: Administrator
"""
'''
https://www.duitang.com/napi/blog/list/by_search/?
kw=%E6%A0%A1%E8%8A%B1&start=0&limit=1000
'''
import requests
import urllib.parse
#引入多线程
import threading  
# 设置最大线程锁
threading_lock=threading.BoundedSemaphore(value=10)

print(threading)
# 通过url获取数据
def get_page(url):
    
    page=requests.get(url)
    
    page=page.content
    
    # 将bytes转为字符串
    page=page.decode('utf-8')
    
    return page

#print(get_page('https://www.duitang.com/napi/blog/list/by_search/?kw=%E6%A0%A1%E8%8A%B1&start=0&limit=1000'))
    

def pages_from_duitang(label):
    pages=[]
    url='https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}&limit=1000'
#    将中文转成URL编码
    label=urllib.parse.quote(label)
    for index in range(0,2000,100):
        print(index)
        u=url.format(label,index)
        print(u)
        
        page=get_page(u)
        
        pages.append(page)
        
    return pages 
    

# 找到图片path  
def findal_in_page(page,startpart,endstart):
    all_strings= []
    
    end=0
    
    while page.find(startpart,end) != -1:
        
        start=page.find(startpart,end)+len(startpart)
        
        end=page.find(endstart,start)
        string=page[start:end]

        all_strings.append(string)
        
        return all_strings


        
def pic_urls_from_pages(pages):
    pic_urls=[]
    
    for page in pages:
        
        urls=findal_in_page(page,'"path":"','"')
        print(urls)
        pic_urls.extend(urls)
        
    return pic_urls

def dowload_pics(url,m):
    
    r=requests.get(url)
    
    path='pics/'+str(m)+'.jpg'
    
    with open(path,'wb') as f:
        
        f.write(r.content)
#        下载完了 解锁
    threading_lock.release()

def mian(label):
    pages=pages_from_duitang(label)
    pic_urls=pic_urls_from_pages(pages)
    n=0
    for url in pic_urls:
        n+=1
        print('正在下载第{} 张图片'.format(n))
#        上锁
        threading_lock.acquire()
        t=threading.Thread(target=dowload_pics,args=(url,n))
        t.start()
mian("校花")
        
        
        
    
