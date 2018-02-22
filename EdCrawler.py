
import urllib.request as ur
from collections import deque
import re

class EdCrawler():
    def urldoc(self,url):
        doc = ur.urlopen(url)
        doc = doc.read().decode('utf-8')
        return doc
    
    def search_ed2k(self,keyword):
        url = "https://tieba.baidu.com/f?ie=utf-8&kw=%E6%9D%8E%E6%AF%85&fr=search"
        pre_url = "https://tieba.baidu.com"
#         url = "https://tiea.baidu.com"
        doc = self.urldoc(url)
#         else:
#             print("error parse url")
        queue = []
        count = 0
        pat = re.compile(r"\/p\/\d+")
        for u in pat.findall(doc):
            url = pre_url+u
            if not url in queue:
                count+=1
                queue.append(url)
                print("surffed %d\t%s"%(count,url))
        
        for p in queue:
            count = 0
            print(p)
            doc = self.urldoc(p)
            pat = re.compile(r"ed2k:\/\/.*")
            for e in pat.findall(doc):
                count+=1
                print("surffed %d\t%s"%(count,e))      
    