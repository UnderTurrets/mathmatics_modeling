import pandas as pd
import numpy as np

#读取数据
excel_df=pd.read_excel("../res/附件.xlsx",sheet_name=1,index_col=0)

#空白数据归零
excel_df=excel_df.fillna(0)
# print(excel_df)

#转为numpy矩阵
excel_array=excel_df.to_numpy()
# print(excel_array)


#去除无效数据
invalid_rowIndex=[]
for i in range(excel_array.shape[0]):
    if (excel_array[i].sum()<85 or excel_array[i].sum()>105):
        invalid_rowIndex.append(i)

print("无效数据行{}".format(invalid_rowIndex))
excel_valid_array=np.delete(excel_array, invalid_rowIndex, axis=0)
# print(excel_array.shape)
# print(excel_valid_array.shape)
# print(excel_valid_array)

#画出缺失样本的各种物质含量的条形图
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='simHei'  #黑体
matplotlib.pyplot.rcParams['axes.unicode_minus'] = False	# 显示负号


broken_data1=np.array(excel_df.loc["19"])
broken_data2=np.array(excel_df.loc["40"])
broken_data3=np.array(excel_df.loc["48"])
broken_data4=np.array(excel_df.loc["58"])

def save_barImage(broken_data,imageName):
    # name_list = ["二氧化硅(SiO2)", "氧化钠(Na2O)", "氧化钾(K2O)", "氧化钙(CaO)", "氧化镁(MgO)", "氧化铝(Al2O3)",
    #              "氧化铁(Fe2O3)", "氧化铜(CuO)", "氧化铅(PbO)",
    #              "氧化钡(BaO)", "五氧化二磷(P2O5)", "氧化锶(SrO)", "氧化锡(SnO2)", "二氧化硫(SO2)", ]
    name_list = ["SiO2", "Na2O", "K2O", "CaO", "MgO", "Al2O3",
                 "Fe2O3", "CuO", "PbO","BaO", "P2O5", "SrO", "SnO2", "SO2", ]
    plt.clf()
    plt.title(imageName)
    plt.xlabel("各种物质")
    plt.ylabel("物质的百分比含量(%)")
    plt.bar(x=np.linspace(0,len(name_list),num=len(name_list)),height=broken_data,tick_label=name_list)
    plt.savefig("../res/"+imageName+".png",dpi=400)
    plt.clf()

save_barImage(broken_data1,"19号")
save_barImage(broken_data2,"40号")
save_barImage(broken_data3,"48号")
save_barImage(broken_data4,"58号")

name_list = ["SiO2", "Na2O", "K2O", "CaO", "MgO", "Al2O3",
             "Fe2O3", "CuO", "PbO", "BaO", "P2O5", "SrO", "SnO2", "SO2", ]
plt.title("19号、40号、48号、58号对比")
plt.xlabel("各种物质")
plt.ylabel("物质的百分比含量(%)")
bar_width=0.2
plt.bar(x=np.linspace(0,len(name_list),num=len(name_list))-bar_width*2,height=broken_data1,width=bar_width,label="19号",color="r",align="edge")
plt.bar(x=np.linspace(0,len(name_list),num=len(name_list))-bar_width*1,height=broken_data2,width=bar_width,label="40号",color="g",align="edge")
plt.bar(x=np.linspace(0,len(name_list),num=len(name_list)),height=broken_data3,width=bar_width,label="48号",color="b",align="edge",tick_label=name_list)
plt.bar(x=np.linspace(0,len(name_list),num=len(name_list))+bar_width*1,height=broken_data4,width=bar_width,label="58号",color="c",align="edge")
plt.legend()
plt.savefig("../res/19号、40号、48号、58号对比.png",dpi=400)



