# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 23:58:02 2019

@author: IBM
"""



#import functions as f
#from stats import Stats
import numpy as np

#import urllib, sys
#import json
import xlrd
#import xlwt
import dataProcess, dataAnalysis, dataTest

import time

'''
host = 'http://stock.market.alicloudapi.com'
path = '/sz-sh-stock-history'
method = 'GET'
appcode = '164204833cc3472686aaf5aae759826a'
querys = 'begin=2018-12-01&code=000002&end=2018-12-29'
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print('true')
number = '000002'
with open('C:/Users/IBM/AnacondaProjects/' + number + '.json', 'wb') as f:
    f.write(content)
stock = json.loads(content)
turnover = stock['turnover']
code = 000001
'''
#数据请求

#url = 'http://quotes.money.163.com/trade/lsjysj_zhishu_' + str(code) + '.html'
try:
    stockFile = xlrd.open_workbook(r'C:\Users\IBM\Documents\601222.xlsx')
except Exception as e:
    print(str(e))
dataSheet = stockFile.sheet_by_name('601222')
print('601222')
#indexSheet = indexFile.sheet_by_name('000001')
#将excel文件中的数据提取，并且规范化，以列表的形式，方便后续处理
final = dataSheet.nrows
price = dataSheet.col(3, start_rowx= 1, end_rowx = final)
#ret = dataSheet.col(5, start_rowx= 1, end_rowx = final)
exRate = dataSheet.col(6, start_rowx= 1, end_rowx = final)
#index = dataProcess.getIndex(indexSheet, dataSheet)
'''
print(ret[2])
print(str(ret[2])[6:-1])

print(float(str(price[2])[7:]))
'''
end = 100
final = final - 2


for i in range(final + 1):
    price[i] = round(float(str(price[i])[7:]), 3)
#    ret[i] = float(str(ret[i])[6:-1])
    exRate[i] = float(str(exRate[i])[7:])
    if price[i] == 0:
        print(i)
    
#print(len(price))
    
#数据处理
        
end = 59
daysInc1 = 20
daysInc2 = 60
daysAct = 60
averPrice1 = []
averPrice2 = []
averExRate = []

#计算前五十日均价和均换手率
while end <= final:
    averPrice1.append(dataProcess.averagePrice(price, end, daysInc1))
    averPrice2.append(dataProcess.averagePrice(price, end, daysInc2))
    averExRate.append(dataProcess.averageRate(exRate, end, daysAct))
    end = end + 1
    
end = 60
i = 0

stdIndex = 0.01
isInc = []
isAct = []
isAbovePrice1 = []
isAbovePrice2 = []
isAboveRate = []

indexInc = []

#对四项基本条件进行判定，所谓四项基本条件，就是股价和换手率，分别与前值和均值的关系
isInc, isAct, isAbovePrice1, isAbovePrice2, isAboveRate = dataProcess.getDataList(end, final, price, exRate, isInc, isAct, isAbovePrice1, isAbovePrice2, isAboveRate, averPrice1, averPrice2, averExRate)

#结果分析    
i = 0
end = 60
inc = 0
incDet = 0
incReal = 0
border = len(isInc)# - 1

#stats是对数据进行基本统计的数组
stats = []
#stats = dataAnalysis.stats(i, border, isInc, isAct, isAbovePrice1, isAboveRate)
    
#    if isInc[i + 1] > 0:
#        print(isInc[i], isAct[i], isAbovePrice[i], isAboveRate[i])
decisionList = []
#decisionList = dataTest.getDecisionList(60, 4337, price, isInc, isAct, isAbovePrice, isAboveRate)     
final = final - 1
'''
char1 = []
char2 = []
char3 = []
earn1 = 0
eran2 = 0
earn3 = 0
fee = 1             #交易损失，包括手续费，印花税等

char1, earn1 = dataAnalysis.findChar(end, 1000, fee, price, isInc, isAct, isAbovePrice, isAboveRate)
char2, earn2 = dataAnalysis.findChar(1000, 2000, fee, price, isInc, isAct, isAbovePrice, isAboveRate)
char3, earn3 = dataAnalysis.findChar(2000, 3000, fee, price, isInc, isAct, isAbovePrice, isAboveRate)
end = 61
point = 2200

fee = 1
charInc = []
charDec = []
earn = 0
#charInc, charDec, earn = dataAnalysis.findChar(60, final, price, isInc, isAct, isAbovePrice, isAboveRate)
test = [isInc[point], isInc[point - 1], isAct[point], isAct[point - 1], isAbovePrice[point], isAboveRate[point]]
count = 400
print('stdInc:', stdInc1, stdInc2, stdInc3)
print('stdAct:', stdAct)
print('stdAbovePrice:', stdAbovePrice, stdBelowPrice)
print('stdAboveRate:', stdAboveRate, stdBelowRate)
t = time.time()

charInc, charDec, earn = dataAnalysis.findChar(60, final - 200, price, isInc, isAct, isAbovePrice, isAboveRate)
dataAnalysis.findMatrix(0, len(isInc), price, isInc, isAct, isAbovePrice, isAboveRate, matrix)
'''
final = 800

statInc = 0
realRet = 100

#charInc, charDec, earn = dataAnalysis.findChar(end - 200, end, price, isInc, isAct, isAbovePrice, isAboveRate)

baseRet = 1
while final < len(price):
    end = final - 200
    base = end
    point = end - 60
    realRet = 100
    while end < final:
        
        charInc, charDec, earn = dataAnalysis.findChar(end - 400, end, price, isInc, isAct, isAbovePrice1, isAbovePrice2, isAboveRate)
        test = [isInc[point], isInc[point - 1], isAct[point], isAct[point - 1], isAbovePrice1[point], isAboveRate[point], isAbovePrice2[point]]
        if price[end + 1] > price[end]:
            statInc = statInc + 1
        if dataTest.decision(test, charInc):# and not dataTest.decision(test, charDec):
            incDet = incDet + 1
            realRet = realRet * price[end + 1] / price[end]
            if price[end + 1] > price[end]:
                incReal = incReal + 1
        elif dataTest.decision(test, charDec):# and not dataTest.decision(test, charInc):
            realRet = realRet * price[end] / price[end + 1]
    
        point = point + 1
        end = end + 1
    baseRet = price[end] / price[base] * 100
    print(point, "calculated return : ", realRet, " hold return : ", baseRet)
    final = final + 200
'''
try:
    print('Total Increase:', statInc / 200, 'Increase Detected:' ,incReal / incDet)
except ZeroDivisionError:
    print('division by zero')

#while count + 60 < final:
#    dataAnalysis.test(price, isInc, isAct, isAbovePrice, isAboveRate, count + 100, count)
#    count = count + 100
#print(time.time() - t)
#music = r'D:\音乐\Midnight Flight.mp3'
#winsound.PlaySound(music, winsound.SND_ALIAS)

while count + 260 < final:
    
    point = count
    end = count + 60
    realRet = 100
    statInc = 0
    if count % 200 == 0:
        charInc, charDec, earn = dataAnalysis.findChar(60, count, price, isInc, isAct, isAbovePrice, isAboveRate, indexInc)
    while point < count + 200:
        
        test = [isInc[point], isInc[point - 1], isAct[point], isAct[point - 1], isAbovePrice[point], isAboveRate[point], indexInc[point]]
        if price[end + 1] > price[end]:
            statInc = statInc + 1
        if dataTest.decision(test, charInc) and not dataTest.decision(test, charDec):
            incDet = incDet + 1
            realRet = realRet * price[end + 1] / price[end]
            if price[end + 1] > price[end]:
                incReal = incReal + 1
        else:
            realRet = realRet * price[end] / price[end + 1]
        point = point + 1
        end = end + 1
    
    print('Start Point:', count, '\t Return Rate:', realRet)
    count = count + 200
    try:
        print('Total Increase:', statInc / 200, 'Increase Detected:' ,incReal / incDet)
    except ZeroDivisionError:
        print('division by zero')
        continue
print(time.time() - t)    
#行情预测

# 由四个指标取值0/1，组成数组，共有16种可能性。
# 四个指标分别是，当日上涨/下跌，当日放量/缩量，当日价格高于/低于50日平均价格，当日成交量高于/低于50日平均成交量
'''