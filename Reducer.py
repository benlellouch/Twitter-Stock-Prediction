
def regularReducer(scoreList, timeInterval): #scorelist made of (score, timeStamp)
    tempTime = 0 #time to start list from
    outputList =[]
    while len(scoreList > 0): #will apply to entire list
        tempScore = 0
        numberInInterval = 0
        for i in range(0,len(scoreList)):
            if scoreList[i][1] < (tempTime + timeInterval) and scoreList[i][1] >= tempTime: #if in desired time interval
                tempScore  += scoreList[i][0]
                numberInInterval += 1
                del(scoreList[i])
        valueToAdd = [(tempScore/numberInInterval),(tempTime + (timeInterval / 2))]
        outputList.append(valueToAdd)
    return outputList



def accurateReducer(scoreList, timeInterval):
    tempTime = 0 #time to start list from
    outputList =[]
    while len(scoreList > 0): #will apply to entire list
        tempScore = 0
        timeWeighter =0
        numberInInterval = 0
        for i in range(0,len(scoreList)):
            if scoreList[i][1] < (tempTime + timeInterval) and scoreList[i][1] >= tempTime: #if in desired time interval
                tempScore += scoreList[i][0]
                timeWeighter += scoreList[i][1]
                numberInInterval += 1
                del(scoreList[i])
        valueToAdd = [(tempScore/numberInInterval), timeWeighter / numberInInterval]
        outputList.append(valueToAdd)
    return outputList





