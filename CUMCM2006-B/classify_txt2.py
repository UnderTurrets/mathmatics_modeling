import dataProcessing
from readDataTxt2 import total
# import matplotlib.pyplot as plt

'''
classify the data based on the age
'''
group_age14to25=[]
group_age25to35=[]
group_age36to45=[]
group_age45More=[]
for individual in total:
    if (individual["age"]>14 and individual["age"]< 25):group_age14to25.append(individual)
    elif (individual["age"] > 25 and individual["age"] < 35): group_age25to35.append(individual)
    elif (individual["age"] > 35 and individual["age"] < 45): group_age36to45.append(individual)
    elif (individual["age"] > 45 ): group_age45More.append(individual)


'''
classify the data based on the treatment method
@:group_treatment vector<Point>
@:return vector<vector<Point>>
'''
def classifyBy_method(individual_list):
    group_treatment1 = []
    group_treatment2 = []
    group_treatment3 = []
    group_treatment4 = []
    for individual in individual_list:
        if (individual["method"]==1):
            for data_dic in individual["data"]:
                group_treatment1.append([data_dic["time"],data_dic["CD4Count"]])
        elif (individual["method"]==2):
            for data_dic in individual["data"]:
                group_treatment2.append([data_dic["time"],data_dic["CD4Count"]])
        elif (individual["method"]==3):
            for data_dic in individual["data"]:
                group_treatment3.append([data_dic["time"],data_dic["CD4Count"]])
        elif (individual["method"]==4):
            for data_dic in individual["data"]:
                group_treatment4.append([data_dic["time"],data_dic["CD4Count"]])

    group_treatment1.sort()
    group_treatment2.sort()
    group_treatment3.sort()
    group_treatment4.sort()
    return [group_treatment1,group_treatment2,group_treatment3,group_treatment4]

age14to25_data=classifyBy_method(group_age14to25)
age25to35_data=classifyBy_method(group_age25to35)
age35to45_data=classifyBy_method(group_age36to45)
age45More_data=classifyBy_method(group_age45More)


age14to25_Method1_data=dataProcessing.process_PointSet_txt2(age14to25_data[0])
age14to25_Method2_data=dataProcessing.process_PointSet_txt2(age14to25_data[1])
age14to25_Method3_data=dataProcessing.process_PointSet_txt2(age14to25_data[2])
# print(age14to25_data[3])
age14to25_Method4_data=dataProcessing.process_PointSet_txt2(age14to25_data[3])

age25to35_Method1_data=dataProcessing.process_PointSet_txt2(age25to35_data[0])
age25to35_Method2_data=dataProcessing.process_PointSet_txt2(age25to35_data[1])
age25to35_Method3_data=dataProcessing.process_PointSet_txt2(age25to35_data[2])
age25to35_Method4_data=dataProcessing.process_PointSet_txt2(age25to35_data[3])

age35to45_Method1_data=dataProcessing.process_PointSet_txt2(age35to45_data[0])
age35to45_Method2_data=dataProcessing.process_PointSet_txt2(age35to45_data[1])
age35to45_Method3_data=dataProcessing.process_PointSet_txt2(age35to45_data[2])
age35to45_Method4_data=dataProcessing.process_PointSet_txt2(age35to45_data[3])

age45More_Method1_data=dataProcessing.process_PointSet_txt2(age45More_data[0])
age45More_Method2_data=dataProcessing.process_PointSet_txt2(age45More_data[1])
age45More_Method3_data=dataProcessing.process_PointSet_txt2(age45More_data[2])
age45More_Method4_data=dataProcessing.process_PointSet_txt2(age45More_data[3])

# print(age14to25_Method1_data,age45More_Method4_data,sep="\n")