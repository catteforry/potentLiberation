# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 21:12:24 2019

@author: IBM
"""
import dataAnalysis


def decision(test, char):
    if test in char:
        return True
    else:
        return False
    
def getDecisionList(end, final, price, isInc, isAct, isAbovePrice, isAboveRate):
    point = end - 60
    decisionList = []
    while end < final:
        
        charInc, charDec, earn = dataAnalysis.findChar(0, end - 1, price, isInc, isAct, isAbovePrice, isAboveRate)
        test = [isInc[point], isInc[point - 1], isAct[point], isAct[point - 1], isAbovePrice[point], isAboveRate[point]]
        if decision(test, charInc) and not decision(test, charDec):
            decisionList.append(True)
        else:
            decisionList.append(False)
        
        point = point + 1
        end = end + 1
        print(end)
    return decisionList