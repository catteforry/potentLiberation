# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:44:02 2019

@author: IBM
"""
import numpy
import dataTest
'''
class Data:
    
    def __init__(self, ret):
        self.ret = ret
        
        
        self.averPrice = 0
        self.averExRate = 0
'''
#fee代表手续费扣除后的剩余
fee = 1

isIncList = [-3, -2, -1, 0, 1, 2, 3]
isActList = [-1, 0, 1]
isAbovePriceList = [-2, -1, 0, 1, 2]
isAboveRateList = [-2, -1, 0, 1, 2]

def stats(i, border, isInc, isAct, isAbovePrice, isAboveRate):
    statsInc = [0, 0, 0, 0, 0, 0, 0]
    statsAct = [0, 0, 0]
    statsAbovePrice = [0, 0, 0]
    statsAboveRate = [0, 0, 0]
    
    while i < border:
        
        if isInc[i] == 3:
            statsInc[6] = statsInc[6] + 1
        elif isInc[i] == 2:
            statsInc[5] = statsInc[5] + 1
        elif isInc[i] == 1:
            statsInc[4] = statsInc[4] + 1
        elif isInc[i] == 0:
            statsInc[3] = statsInc[3] + 1
        elif isInc[i] == -1:
            statsInc[2] = statsInc[2] + 1
        elif isInc[i] == -2:
            statsInc[1] = statsInc[1] + 1
        else:
            statsInc[0] = statsInc[0] + 1
        
        if isAct[i] == 1:
            statsAct[2] = statsAct[2] + 1
        elif isAct[i] == -1:
            statsAct[0] = statsAct[0] + 1
        else:
            statsAct[1] = statsAct[1] + 1
        
        if isAbovePrice[i] == 1:
            statsAbovePrice[2] = statsAbovePrice[2] + 1
        elif isAbovePrice[i] == -1:
            statsAbovePrice[0] = statsAbovePrice[0] + 1
        else:
            statsAbovePrice[1] = statsAbovePrice[1] + 1
        
        if isAboveRate[i] == 1:
            statsAboveRate[2] = statsAboveRate[2] + 1
        elif isAboveRate[i] == -1:
            statsAboveRate[0] = statsAboveRate[0] + 1
        else:
            statsAboveRate[1] = statsAboveRate[1] + 1
        
        i = i + 1 
        
    return {"statsInc": statsInc, "statsAct": statsAct, "statsAbovePrice": statsAbovePrice, "statsAboveRate": statsAboveRate}


#查找股价走势特征
def findChar(end, final, price, isInc, isAct, isAbovePrice1, isAbovePrice2, isAboveRate):
    i = 0
    j = 0
    l = 0
    m = 0
    n = 0
    earn = 100
    characterInc = []
    characterDec = []
    for i in isIncList:
        for j in isIncList:
            for m in isAbovePriceList:
                for k in isActList:
                    for l in isActList:
                        for n in isAboveRateList:
                            for o in isAbovePriceList:
                                
                                basic = 100
                                start = end
                                parser = 0
#                        incReal = 0
                                count = 0
                                while start < final:
                                    if isInc[parser] == i:
                                        if isInc[parser - 1] == j:
                                            if isAct[parser] == k:
                                                if isAct[parser - 1] == l:
                                                    if isAbovePrice1[parser] == m:
                                                        if isAboveRate[parser] == n:
                                                            if isAbovePrice2[parser] == o:
                                                                count = count + 1
                                                                basic = basic * price[start + 1] / price[start] * fee
                                                                
                                                                break
                                    start = start + 1
                                    parser = parser + 1
#                            print([i, j, k, l, m, n], count, '\t', basic)
                                if count != 0 and basic / 100 > 1.025 ** count:
#                            if basic > 115:
                                    characterInc.append([i, j, k, l, m, n])
                                    earn = earn * basic / 100 
#                                print([i, j, k, l, m, n], count, '\t', basic)
                                elif count != 0 and basic / 100 < 0.975 ** count:
                                    characterDec.append([i, j, k, l, m, n, o])

    start = end
    parser = 1                            
    while start < final:
        if price[start + 1] < (price[start] * 0.95):
#                                                       incReal = incReal + 1
            if [isInc[parser], isInc[parser - 1], isAct[parser], isAct[parser - 1], isAbovePrice1[parser], isAboveRate[parser], isAbovePrice2[parser]] not in characterDec:
                characterDec.append([isInc[parser], isInc[parser - 1], isAct[parser], isAct[parser - 1], isAbovePrice1[parser], isAboveRate[parser], isAbovePrice2[parser]])
        start = start + 1
        i = i + 1
    return characterInc, characterDec, earn
'''
                            elif basic < 70:
                                characterDec.append([i, j, k, l, m, n])
                                
                            try:
                                if (basic / 100) ** (1 / count) > 1.01:
                                    character.append([i, j, k, l, m, n])
                                    earn = earn * basic / 100
                            except ZeroDivisionError:
                                continue
'''

def findMatrix(end, final, price, isInc, isAct, isAbovePrice, isAboveRate, indexInc, matrix):
    parser = end
    
    differ = [0, 0, 0, 0, 0, 0, 0]
    learnRate = 0.1
    i = 1000
    while i > 0:
        while parser < final - 1:
            test = [isInc[parser], isInc[parser - 1], isAct[parser], isAct[parser - 1], isAbovePrice[parser], isAboveRate[parser]]
            result = [isInc[parser + 1], isInc[parser], isAct[parser + 1], isAct[parser], isAbovePrice[parser + 1], isAboveRate[parser + 1]]
            differ = result - numpy.dot(test, matrix)
            matrix = matrix - differ * learnRate
            parser = parser + 1
        parser = end  
        i = i - 1
    print(matrix)
                             
def simulation(basic, price, priceFuture, isInc, isAct, isAbovePrice, isAboveRate):
    if condition(isInc, isAct, isAbovePrice, isAboveRate):
        return basic * priceFuture / price
    
def test(price, isInc, isAct, isAbovePrice, isAboveRate, end, start = 60):
    
#对start和end之间的交易数据，代入筛选算法进行复盘，得到区间交易回报和算法准确率
    date = start
    point = 0
    realRet = 100
    incDet = 0
    incReal = 0
    earn = 0
    while date < end:
        charI = []
        charD = []
        count = 0
        if count == 0:
            charI, charD, earn = findChar(60, date, price, isInc, isAct, isAbovePrice, isAboveRate)
            count = count - 50
        test = [isInc[point], isInc[point - 1], isAct[point], isAct[point - 1], isAbovePrice[point], isAboveRate[point]]
        if dataTest.decision(test, charI):
            incDet = incDet + 1
            realRet = realRet * price[date + 1] / price[date]
            if price[date + 1] > price[date]:
                incReal = incReal + 1
        elif dataTest.decision(test, charD):
            realRet = realRet * price[date] / price[date + 1]
        point = point + 1
        date = date + 1
        count = count + 1
    print(realRet)
    try:
        print('increase detected:' ,incReal / incDet)
    except ZeroDivisionError:
        print('division by zero')
    
                            
def condition(isInc, isAct, isAbovePrice, isAboveRate):
    if isInc == 2:
        if isAct > -1:
            if isAboveRate == 1:
                return True
    elif isInc == 0:
        if isAbovePrice == -1:
            if isAboveRate== 1:
                return True
        elif isAboveRate == 0:
            return True
    elif isInc == -1:
        if isAct == 0:
            if isAbovePrice == -1:
                if isAboveRate < 1:
                    return True


'''
#---condition1---
    if isInc[i] == 2:
        if isAct[i] > -1:
            if isAboveRate[i] == 1:
                incDet = incDet + 1
                basic = basic * price[end + 1] / price[end]
                if price[end + 1] > price[end]:
                    stat = stat + 1
                    incReal = incReal + 1
    if isInc[i] == 0:
        if isAbovePrice[i] == -1:
            if isAboveRate[i] == 1:
                incDet = incDet + 1
                basic = basic * price[end + 1] / price[end]
                if price[end + 1] > price[end]:
                    stat = stat + 1
                    incReal = incReal + 1
        elif isAboveRate[i] == 0:
            incDet = incDet + 1
            basic = basic * price[end + 1] / price[end]
            if price[end + 1] > price[end]:
                stat = stat + 1
                incReal = incReal + 1
    if isInc[i] == -1:
        if isAct[i] == 0:
            if isAbovePrice[i] == -1:
                if isAboveRate[i] < 1:
                    incDet = incDet + 1
                    basic = basic * price[end + 1] / price[end]
                    if price[end + 1] > price[end]:
                        stat = stat + 1
                        incReal = incReal + 1
                        '''

        