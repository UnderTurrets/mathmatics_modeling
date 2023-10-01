'''
Created by Han Xu
email:736946693@qq.com
'''
def IsBroken(stage_data_dic):
    if (stage_data_dic["RNADate"]==-1 or stage_data_dic["CD4Date"] ==-1):
        return True
    else:return False


def find_last_data(individual_data_list,stage_data_dic):
    for i in range(0,len(individual_data_list)):
        if(individual_data_list[i]==stage_data_dic):
            if(i>=1 and IsBroken(individual_data_list[i-1])==False):
                return individual_data_list[i-1]
    return None


def find_next_data(individual_data_list,stage_data_dic):
    for i in range(0,len(individual_data_list)):
        if(individual_data_list[i]==stage_data_dic):
            if(i<=len(individual_data_list)-2 and IsBroken(individual_data_list[i+1])==False):
                return individual_data_list[i+1]
    return None


def compute_median_data(last_data, next_data, stage_data_dic):
    if (stage_data_dic["RNADate"] ==-1):
        stage_data_dic["RNADate"] = stage_data_dic["CD4Date"]

        x=stage_data_dic["CD4Date"]
        x_k=last_data["RNADate"]
        x_k_plus_1=next_data["RNADate"]
        y_k=last_data["VLoad"]
        y_k_plus_1 = next_data["VLoad"]
        stage_data_dic["VLoad"]=y_k*(x-x_k_plus_1)/(x_k-x_k_plus_1)+y_k_plus_1*(x-x_k)/(x_k_plus_1-x_k)

    if(stage_data_dic["CD4Date"] ==-1):
        stage_data_dic["CD4Date"] = stage_data_dic["RNADate"]

        x = stage_data_dic["RNADate"]
        x_k = last_data["CD4Date"]
        x_k_plus_1 = next_data["CD4Date"]
        y_k = last_data["CD4Count"]
        y_k_plus_1 = next_data["CD4Count"]
        stage_data_dic["CD4Count"] = y_k * (x - x_k_plus_1) / (x_k - x_k_plus_1) + y_k_plus_1 * (x - x_k) / (
                    x_k_plus_1 - x_k)

    return stage_data_dic


def find_last2_data(individual_data_list, stage_data_dic):
    for i in range(0,len(individual_data_list)):
        if(individual_data_list[i]==stage_data_dic):
            if(i>=2 and IsBroken(individual_data_list[i-2])==False and IsBroken(individual_data_list[i-1])==False):
                return [individual_data_list[i-2],individual_data_list[i-1]]
    return None


def compute_edgeFinal_data(last2_data, stage_data_dic):
    if (stage_data_dic["RNADate"] ==-1):
        stage_data_dic["RNADate"]=stage_data_dic["CD4Date"]

        x=last2_data[1]["RNADate"]
        x_k=last2_data[0]["RNADate"]
        x_k_plus_1=stage_data_dic["RNADate"]
        y_k=last2_data[0]["VLoad"]
        y=last2_data[1]["VLoad"]

        stage_data_dic["VLoad"]=(  y-y_k*(x-x_k_plus_1)/(x_k-x_k_plus_1)  )*(x_k_plus_1-x_k)/(x-x_k)

    if(stage_data_dic["CD4Date"] ==-1):
        stage_data_dic["CD4Date"]=stage_data_dic["RNADate"]

        x=last2_data[1]["CD4Date"]
        x_k=last2_data[0]["CD4Date"]
        x_k_plus_1=stage_data_dic["CD4Date"]
        y_k=last2_data[0]["CD4Count"]
        y=last2_data[1]["CD4Count"]

        stage_data_dic["CD4Count"]=(  y-y_k*(x-x_k_plus_1)/(x_k-x_k_plus_1)  )*(x_k_plus_1-x_k)/(x-x_k)

    return stage_data_dic


def find_next2_data(individual_data_list, stage_data_dic):
    for i in range(0,len(individual_data_list)):
        if(individual_data_list[i]==stage_data_dic):
            if(i<=len(individual_data_list)-3 and IsBroken(individual_data_list[i+1])==False and IsBroken(individual_data_list[i+2])==False):
                return [individual_data_list[i+1],individual_data_list[i+2]]
    return None


def compute_edgeFirst_data(next2_data, stage_data_dic):
    if (stage_data_dic["RNADate"] ==-1):
        stage_data_dic["RNADate"] = stage_data_dic["CD4Date"]

        x = next2_data[0]["RNADate"]
        x_k = stage_data_dic["RNADate"]
        x_k_plus_1 = next2_data[1]["RNADate"]
        y = next2_data[0]["VLoad"]
        y_k_plus_1 = next2_data[1]["VLoad"]

        stage_data_dic["VLoad"] = (y - y_k_plus_1 * (x - x_k) / (x_k_plus_1 - x_k)) * (x_k - x_k_plus_1) / (x - x_k_plus_1)

    if (stage_data_dic["CD4Date"]==-1):
        stage_data_dic["CD4Date"] = stage_data_dic["RNADate"]

        x = next2_data[0]["CD4Date"]
        x_k = stage_data_dic["CD4Date"]
        x_k_plus_1 = next2_data[1]["CD4Date"]
        y = next2_data[0]["CD4Count"]
        y_k_plus_1 = next2_data[1]["CD4Count"]

        stage_data_dic["CD4Count"] = (y - y_k_plus_1 * (x - x_k) / (x_k_plus_1 - x_k)) * (x_k - x_k_plus_1) / (
                    x - x_k_plus_1)

    return stage_data_dic


def repair_from_last2(individual_data_list,order):
    last2_data = find_last2_data(individual_data_list=individual_data_list,
                                 stage_data_dic=individual_data_list[order])
    if (last2_data is not None):
        individual_data_list[order] = compute_edgeFinal_data(last2_data=last2_data,
                                                             stage_data_dic=individual_data_list[order])
    # else:
    #     current_id = individual["id"]
    #     print("编号{}号病人的第{}号数据无法使用拉格朗日插值法填补".format(current_id, str(order)))

    return individual_data_list[order]


def repair_from_next2(individual_data_list,order):
    next2_data = find_next2_data(individual_data_list=individual_data_list,
                                 stage_data_dic=individual_data_list[order])
    if (next2_data is not None):
        individual_data_list[order] = compute_edgeFinal_data(last2_data=next2_data,
                                                             stage_data_dic=individual_data_list[order])
    # else:
    #     current_id = individual["id"]
    #     print("编号{}号病人的第{}号数据无法使用拉格朗日插值法填补".format(current_id, str(order)))
    return individual_data_list[order]


def repair_from_lastAndnext(individual_data_list,order):
    last_data = find_last_data(individual_data_list=individual_data_list, stage_data_dic=individual_data_list[order])
    next_data = find_next_data(individual_data_list=individual_data_list, stage_data_dic=individual_data_list[order])
    if (last_data is not None and next_data is not None):
        individual_data_list[order] = compute_median_data(last_data=last_data, next_data=next_data,
                                                          stage_data_dic=individual_data_list[order])

    else:
        if (next_data is None and last_data is not None):
            repair_from_last2(individual_data_list=individual_data_list,order=order)

        elif (last_data is None and next_data is not None):
            repair_from_next2(individual_data_list=individual_data_list,order=order)

        # else:
        #     current_id = individual["id"]
        #     print("编号{}号病人的第{}号数据无法使用拉格朗日插值法填补".format(current_id, str(order)))
    return individual_data_list[order]


def repair_stage_data(individual_data_list,order):

    # print(individual_data_list[order])
    if (order == 0):
        individual_data_list[order]=repair_from_next2(individual_data_list=individual_data_list,order=order)

    elif (order == len(individual_data_list) - 1):
        individual_data_list[order]=repair_from_last2(individual_data_list=individual_data_list,order=order)

    else:
        individual_data_list[order]=repair_from_lastAndnext(individual_data_list=individual_data_list,order=order)

    # print(individual_data_list[order])

    return individual_data_list[order]


from readDataTxt1 import total
repaired_total=total

try:
    for individual in repaired_total:
        individual_data_list=individual["data"]
        for order in range(0, len(individual_data_list)):
            if(IsBroken(individual_data_list[order])==True):
                individual_data_list[order]=repair_stage_data(individual_data_list=individual_data_list,order=order)


        for order in range(0, len(individual_data_list)):
            if (IsBroken(individual_data_list[order]) == True):
                individual_data_list[order] = repair_stage_data(individual_data_list=individual_data_list, order=order)

except (Exception)  as error :
    print(error)

f=open("repaired_data.txt",mode="w+",encoding="utf-8")
f.write(str(repaired_total))
f.close()






