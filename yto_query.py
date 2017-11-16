import requests as r
import time
from lxml import etree as etree
from stops import StopNode


class Yto():
    def __init__(self, bill=''):
        self.bill = bill

    def get_page(self, bill_number):
        host = 'http://wap.yto.net.cn'

        query_url = '/QueryTrack/Trace.aspx'
        user_agent = 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
        para = {"waybillNo": bill_number}
        s = r.session()
        res = s.post(host + query_url, data=para,
                     headers={"User-Agent": user_agent})
        # print(res.text)
        if res.status_code == 200:
            return res.text
        else:
            return ''

    def parser(self, html):
        tree = etree.HTML(html)
        lis = tree.xpath(u"//ul[@class='OrderTracking']/li")
        # lis = ul.xpath(u"//li")
        infos = {}
        for li in lis:
            detail = li.xpath("p")[0].text
            time_str = li.xpath("span")[1].text
            detaillist = detail.strip().split()
            name = detaillist[0]
            status = detaillist[1]
            next_stop = None
            if len(detaillist) > 3:
                next_stop = detaillist[3]

            infos[name] = StopNode(name,
                                   time.mktime(time.strptime(
                                       time_str.strip(), "%Y-%m-%d %H:%M:%S")),
                                   status,
                                   next_stop)
        return infos

    def query(self, bill=None):
        if bill is not None:
            self.bill = bill
        if self.bill:
            page = self.get_page(self.bill)
            info = self.parser(page)
            return info
        return None


def main():
    b = input("Please input your express bill number:")
    if b:
        q = Yto(b)
        info = q.query()
        for i in info:
            print(i)


if __name__ == '__main__':
    main()
