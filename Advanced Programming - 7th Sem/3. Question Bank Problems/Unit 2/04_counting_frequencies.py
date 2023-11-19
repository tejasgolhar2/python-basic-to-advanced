# Write a program for counting the frequencies in a list using dictionary


def countFreq(v_list):
    countDict = dict()
    
    for item in v_list:
        if item not in countDict:
            countDict[item]=1
        else:
            count = countDict[item]
            countDict[item]=count+1

    for key,value in countDict.items():
        print(key,":",value,"times")



list1 = [1,1,2,45,7,8,9,4,4,6,1,5,36,1,6]
countFreq(list1)