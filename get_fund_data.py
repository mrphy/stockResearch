import requests
from bs4 import BeautifulSoup
import xlwt

workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('fundValue')
url = 'http://fund.jrj.com.cn/archives,510050,jjjz.shtml'
# params = {'pageIndex': 1}
#  headers={'Accept': '*/*',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
# 'Connection': 'keep-alive',
# 'Cookie': 'st_pvi=16523176741599; st_si=73470699215519; EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; EMFUND7=null; EMFUND8=null; EMFUND0=null; EMFUND9=10-12 11:49:38@#$%u534E%u590F%u4E0A%u8BC150ETF@%23%24510050',
# 'Host': 'api.fund.eastmoney.com',
# 'Referer': 'http://fundf10.eastmoney.com/jjjz_510050.html',
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# r = requests.get(url=url,params=params,headers=headers)
r = requests.get(url=url)

soup = BeautifulSoup(r.text,  # HTML文档字符串
                     'html.parser',  # HTML解析器
                     from_encoding='utf8')  # HTML文档的编码

times = soup.find_all('td', class_='jrj-tc')
i = 0
for time in times:
    print(time.get_text())
    worksheet.write(0, i, time.get_text())
    i = i + 1

values = soup.find_all('td', class_='jrj-tr')
i = 0
for value in values:
    print(value.get_text())
    if(value.get_text()=='--'):
        break
    if (i % 2 == 0):
        worksheet.write(1, int(i / 2), value.get_text())
    else:
        worksheet.write(2, int(i / 2), value.get_text())
    i = i + 1

workbook.save('fundValue_2018.xls')
