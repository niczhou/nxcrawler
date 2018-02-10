#coding = utf-8

import urllib.request as ur
import urllib.error as ue
import re
from collections import deque

url="http://finance.sina.com.cn/"
doc=ur.urlopen(url).read().decode('utf-8')
##print(doc)

queue=deque()
visited=set() #set that visited
queue.append(url)
count=0

while count<22:
    url=queue.popleft()
    visited={url}
    print("collected %d! now is collecting <-- %s"%(count,url))
    doc=ur.urlopen(url)
    count+=1
    if 'html' not in doc.getheader('Content-Type'):
        continue
    try:
        doc=doc.read().decode('utf-8')
    except:
        continue                      

    pat=re.compile("href=['\"]([^\"'>]*?)['\"].*?")
    for u in pat.findall(doc):
##        print(u)
        if 'http' in u and u not in visited:
            queue.append(u)
            print("append to queue --> "+str(u))
            
    
