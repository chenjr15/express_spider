
import random
class kd_hundred():
    def __init__(self,bill = ''):
        self.bill = bill
    def get_page(self,bill_number,bill_type):
        host = 'https://m.kuaidi100.com'

        query_url = '/query'
        user_agent = 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
        para = {"type":bill_type ,"postid":bill_number,"id":"1","valicode":None,"temp":random.random() }
        s = r.session()
        s.get(host+'/result.jsp',params = {'nu':bill_number}, headers = {"User-Agent": user_agent})
        print(s.headers)
        res = s.get(host + query_url, data = para, headers = {"User-Agent": user_agent})
        #print(res.text)
        if res.status_code == 200:
            return res.text
        else:
            return  ''
    def parser(self,html):
        tree = etree.HTML(html)
        lis = tree.xpath(u"//ul[@class='OrderTracking']/li")
        # lis = ul.xpath(u"//li")
        infos = []
        for li in lis:
            detail = li.xpath("p")[0].text
            time_str = li.xpath("span")[1].text
            infos.append((detail.strip(),time_str.strip(),))
        return  infos
    def query(self,bill = None):
        if bill is not  None:
            self.bill =bill
        if self.bill :
            page = self.get_page(self.bill)
            info = self.parser(page)
            return  info
        return  None
