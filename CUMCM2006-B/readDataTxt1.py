'''
Created by Han Xu
email:736946693@qq.com
'''
total=[]
f=open("附件1纯数据.txt",encoding="utf-8",mode="r")
lastID=""
currentID=""
for line in f:

    lineData=line.split()
    currentID = float(lineData[0])

    CD4Date = -1
    CD4Count = -1
    RNADate = -1
    VLoad = -1

    if (len(lineData) == 5):
        CD4Date = float(lineData[1])
        CD4Count = float(lineData[2])
        RNADate = float(lineData[3])
        VLoad = float(lineData[4])

    else:
        if (lineData[0] == "23496"):
            RNADate = float(lineData[1])
            VLoad = float(lineData[2])

        else:
            CD4Date = float(lineData[1])
            CD4Count = float(lineData[2])

    new_data={"CD4Date":CD4Date,"CD4Count":CD4Count,"RNADate":RNADate,"VLoad":VLoad}

    if(currentID!=lastID):
        individual = {"id": None, "data": []}
        individual["id"] = currentID
        individual["data"].append(new_data)
        total.append(individual)


    else:
        total[len(total)-1]["data"].append(new_data)

    lastID = currentID

# print(total[0])

