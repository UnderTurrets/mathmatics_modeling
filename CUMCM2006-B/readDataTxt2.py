'''
Created by Han Xu
email:736946693@qq.com
'''
total=[]
f=open("附件2纯数据.txt",encoding="utf-8",mode="r")
lastID=""
currentID=""
for line in f:

    lineData=line.split()
    currentID = float(lineData[0])
    method = float(lineData[1])
    age = float(lineData[2])

    time = float(lineData[3])
    CD4Count = float(lineData[4])


    new_data={"time":time,"CD4Count":CD4Count}

    if(currentID!=lastID):
        individual = {"id": None, "method":None,"age":None,"data": []}
        individual["id"] = currentID
        individual["method"] = method
        individual["age"] = age
        individual["data"].append(new_data)
        total.append(individual)


    else:
        total[len(total)-1]["data"].append(new_data)

    lastID = currentID

# print(total)


