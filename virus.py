import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
import openpyxl


def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    response = requests.get(url,headers=headers).text
    with open("./response.html", "w+") as f:
        f.write(response)
    return response


def getCsv(response):
    html = etree.HTML(response)
    result = html.xpath('//script[@type="application/json"]/text()')
    result = result[0]
    result = json.loads(result)
    print(result)
    result1 = result['component'][0]['caseList']

    # 创建工作簿
    wb = openpyxl.Workbook()
    # 创建工作表
    ws = wb.active
    ws.title = "国内疫情"
    ws.append(['省份', '累计确诊', '死亡', '治愈', '现有确诊', '累计确诊', '死亡增量', '治愈增量', '现有确诊增量'])

    for each in result1:
        temp_list = [each['area'], each['confirmed'], each['died'], each['crued'], each['relativeTime'],
                     each['confirmedRelative'], each['diedRelative'], each['curedRelative'], each['curConfirmRelative']]
        for i in range(len(temp_list)):
            if temp_list[i] == '':
                temp_list[i] = '0'
        ws.append(temp_list)

    wb.save('./国内疫情.csv')


# 网站url
url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4"
# 获取html
response = getHtml(url)
# 获取疫情数据csv
getCsv(response)
