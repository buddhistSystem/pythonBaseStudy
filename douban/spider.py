# -*- codeing = utf-8 -*-
import sqlite3
from bs4 import BeautifulSoup  # 网页解析
import re  # 正则
import urllib.request  # 定制url
import xlwt  # 进行Excel操作
import pymysql  # mysql

# 查取链接正则规则
findLink = re.compile(r'<a href="(.*?)">')
# 查找图片链接,忽略换行
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
# 查找片名
findTitle = re.compile(r'<span class="title">(.*?)</span>')
# 评分
findRatingNum = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 相关内容
findDb = re.compile(r'<p class="">(.*?)</p>', re.S)
# 常量
sava2excelPath = "豆瓣电影TOP250.xls"
save2sqlitePath = "../sqlitedb/douban.sqlite"
baseUrl = "https://movie.douban.com/top250?start="


def main():
    # 爬取网页
    dataList = getData(baseUrl)
    # 保存数据
    # save2excel(sava2excelPath, dataList)
    # save2sqlite(save2sqlitePath, dataList)
    save2mysql(dataList)


def getData(baseUrl):
    print("parse data ......")
    dataList = []
    # 每页25条一共10页
    for i in range(0, 10):
        url = baseUrl + str(i * 25)
        html = askUrl(url)
        # 解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            data = []
            item = str(item)

            link = re.findall(findLink, item)[0]
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)
            if len(titles) > 1:
                ctitle = titles[0]  # 中文名
                data.append(ctitle)
                otitile = titles[1].strip().replace("/", "")  # 外国名
                otitile = trim(otitile)
                data.append(otitile)
            else:
                data.append(titles[0])
                data.append("")

            ratingNum = re.findall(findRatingNum, item)[0]
            data.append(ratingNum)

            judge = re.findall(findJudge, item)[0]
            data.append(judge)

            inqs = re.findall(findInq, item)
            if len(inqs) > 0:
                data.append(inqs[0])
            else:
                data.append("")

            db = re.findall(findDb, item)[0]
            db = trim(db)
            db = db.replace("<br/>", "")
            data.append(db)

            dataList.append(data)
    print("parse data end ......")
    return dataList


def trim(s):
    if s == '':
        return
    else:
        # unix下一bai般只有一个0x0A表示换行("\n"），windows下一般都是0x0D和0x0A两个字符("\r\n")
        s = s.replace(u'\xa0', u'')
        s = s.replace(u'\n', u'').replace(u'\r', u'')
        s = s.strip()
        return s


def askUrl(url):
    header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    req = urllib.request.Request(url=url, headers=header)
    try:
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
    except Exception as e:
        print(e)
    return html


def save2excel(sava2excelPath, dataList):
    print("sava to file ......")
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet("豆瓣电影TOP250", cell_overwrite_ok=True)
    col = ("电影详情连接", "封面图", "中文名称", "外国名称", "评分", "评价数", "概况", "相关信息")
    for i in range(0, len(col)):
        worksheet.write(0, i, col[i])
    for i in range(1, len(dataList)):
        for j in range(0, len(dataList[i])):
            worksheet.write(i, j, dataList[i][j])
    workbook.save(sava2excelPath)
    print("sava success ......")


def save2sqlite(save2sqlitePath, dataList):
    print("save to sqlite ......")
    conn = sqlite3.connect(save2sqlitePath)
    cursor = conn.cursor()
    for item in dataList:
        for i in range(len(item)):
            item[i] = '"' + item[i] + '"'
        sql = 'insert into douban_top250(info_link,pic_link,cname ,ename ,score ,rated ,instroduction ,info)VALUES (%s)' % (
            ",".join(item))
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    print("save to sqlite success ......")


def save2mysql(dataList):
    print("save to mysql ......")
    init_mysql_db()
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='showchart')
    cursor = conn.cursor()
    for item in dataList:
        for i in range(len(item)):
            item[i] = '"' + item[i] + '"'
        sql = 'insert into douban_top250(info_link,pic_link,cname ,ename ,score ,rated ,instroduction ,info)VALUES (%s)' % (
            ",".join(item))
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    print("save to mysql success......")


def init_mysql_db():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='showchart')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS douban_top250')
    sql = '''CREATE TABLE IF NOT EXISTS douban_top250(
            id int NOT NULL AUTO_INCREMENT,
            info_link varchar(255),
            pic_link varchar(255),
            cname varchar(255),
            ename varchar(255),
            score double(16,2),
            rated int,
            instroduction varchar(255),
            info varchar(900),
            primary key(id)
            )
    '''
    cursor.execute(sql)
    cursor.close()
    conn.close()


def init_sqlite_db(save2sqlitePath):
    conn = sqlite3.connect(save2sqlitePath)
    cursor = conn.cursor()
    sql = '''
        create table douban_top250(
            id integer  not null primary key autoincrement,
            info_link text,
            pic_link text,
            cname text,
            ename text,
            score numeric,
            rated numeric,
            instroduction text,
            info text
        )
    '''
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
