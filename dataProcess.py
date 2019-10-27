# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:16:05 2019

@author: IBM
"""
import pandas as pd
#import datetime

#设定股价上涨的基准，换手率增加的基准
stdInc1 = 0.015
stdInc2 = 0.045
stdInc3 = 0.08
stdAct = 0.4
stdAbovePrice11 = 1.05
stdAbovePrice12 = 1.15
stdBelowPrice11 = 0.95
stdBelowPrice12 = 0.85
stdAbovePrice21 = 1.15
stdAbovePrice22 = 1.25
stdBelowPrice21 = 0.85
stdBelowPrice22 = 0.75
stdAboveRate1 = 1.25
stdAboveRate2 = 2.45
stdBelowRate1 = 0.75
stdBelowRate2 = 0.25

def csv_to_xlsx_pd(filename):
    csv = pd.read_csv(filename + '.csv', encoding='utf-8')
    csv.to_excel(filename + '.xlsx', sheet_name='data')
    
def averagePrice(price, end, days):
    averageP = 0
    for i in range(days):
        position = int(end - i)
        averageP = averageP + price[position]
    averageP /= days
    return averageP

def averageRate(exRate, end, days):
    averageR = 0
    for i in range(days):
        position = int(end - i)
        averageR = averageR + exRate[position]
    averageR /= days
    return averageR

def getIndex(sheetIndex, sheetStock):
    index = []
    i = 0
    j = 0
    indexFinal = sheetIndex.nrows
    stockFinal = sheetStock.nrows
    
    indexDate = sheetIndex.col(0, start_rowx= 1, end_rowx = indexFinal)
    stockDate = sheetStock.col(0, start_rowx= 1, end_rowx = stockFinal)
    
    indexPrice = sheetIndex.col(5, start_rowx= 1, end_rowx = indexFinal)

    while i < indexFinal - 1 and j < stockFinal - 1:
        if str(indexDate[i]) == str(stockDate[j]):
            index.append(float(str(indexPrice[i])[7:]) / 100)
            i = i + 1
            j = j + 1
        else:
            i = i + 1       
                
    return index

#四组交易数据列表

def getDataList(end, final, price, exRate, isInc, isAct, isAbovePrice1, isAbovePrice2, isAboveRate, averPrice1, averPrice2, averExRate):
    i = 0
    while end <= final:

        if (price[end] - price[end - 1]) / price[end - 1] > stdInc3:
            isInc.append(3)
        elif (price[end] - price[end - 1]) / price[end - 1] < (-1) * stdInc3:
            isInc.append(-3)
        elif (price[end] - price[end - 1]) / price[end - 1] > stdInc2:
            isInc.append(2)
        elif (price[end] - price[end - 1]) / price[end - 1] < (-1) * stdInc2:
            isInc.append(-2)
        elif (price[end] - price[end - 1]) / price[end - 1] > stdInc1:
            isInc.append(1)
        elif (price[end] - price[end - 1]) / price[end - 1] < (-1) * stdInc1:
            isInc.append(-1)
        else:
            isInc.append(0)
        
        if (exRate[end] - exRate[end - 1]) / exRate[end - 1] > stdAct:
            isAct.append(1)
        elif (exRate[end] - exRate[end - 1]) / exRate[end - 1] < (-1) * (1 - 1 / (1 + stdAct)):
            isAct.append(-1)
        else:
            isAct.append(0)
  
        if price[end] / averPrice1[i] > stdAbovePrice12:
            isAbovePrice1.append(2)
        elif price[end] / averPrice1[i] < stdBelowPrice12:
            isAbovePrice1.append(-2)
        elif price[end] / averPrice1[i] > stdAbovePrice11:
            isAbovePrice1.append(1)
        elif price[end] / averPrice1[i] < stdBelowPrice11:
            isAbovePrice1.append(-1)
        else:
            isAbovePrice1.append(0)
            
        if price[end] / averPrice2[i] > stdAbovePrice22:
            isAbovePrice2.append(2)
        elif price[end] / averPrice2[i] < stdBelowPrice22:
            isAbovePrice2.append(-2)
        elif price[end] / averPrice2[i] > stdAbovePrice21:
            isAbovePrice2.append(1)
        elif price[end] / averPrice2[i] < stdBelowPrice21:
            isAbovePrice2.append(-1)
        else:
            isAbovePrice2.append(0)

        if exRate[end] / averExRate[i] > stdAboveRate2:
            isAboveRate.append(2)
        elif exRate[end] / averExRate[i] < stdBelowRate2:
            isAboveRate.append(-2)
        elif exRate[end] / averExRate[i] > stdAboveRate1:
            isAboveRate.append(1)
        elif exRate[end] / averExRate[i] < stdBelowRate1:
            isAboveRate.append(-1)
        else:
            isAboveRate.append(0)
        '''
        if index[end] > stdIndex:
            indexInc.append(1)
        elif index[end] < -1 * stdIndex:
            indexInc.append(-1)
        else:
            indexInc.append(0)
        '''
        end = end + 1
        i = i + 1
        
    return isInc, isAct, isAbovePrice1, isAbovePrice2, isAboveRate