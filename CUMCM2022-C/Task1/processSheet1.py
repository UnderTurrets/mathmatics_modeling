import pandas as pd

#读取数据
excel_df=pd.read_excel("../res/附件.xlsx",sheet_name=0,index_col=0)
# print(excel_df)

#取出风化的样本
weathering_simples=excel_df[:][excel_df["表面风化"]=="风化"]
# print(weathering_simples)

#取出无风化的样本
noWeathering_simples= excel_df[:][excel_df["表面风化"] == "无风化"]
# print(no_weathering_simples)


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='simHei'  #黑体
matplotlib.pyplot.rcParams['axes.unicode_minus'] = False	# 显示负号

#分析风化样本中的纹饰
decorationName_list=["A纹饰","B纹饰","C纹饰",]
plt.clf()
plt.pie(x=[len(weathering_simples[:][weathering_simples["纹饰"]=="A"]),len(weathering_simples[:][weathering_simples["纹饰"]=="B"]),len(weathering_simples[:][weathering_simples["纹饰"]=="C"]),],
        labels=decorationName_list,autopct="%0.1f%%")
plt.title("风化样本中的纹饰")
plt.savefig("../res/风化样本中的纹饰.png",dpi=400)

#分析风化样本中的材质类型
materialName_list=["铅钡","高钾",]
plt.clf()
plt.pie(x=[len(weathering_simples[:][weathering_simples["类型"]=="铅钡"]),len(weathering_simples[:][weathering_simples["类型"]=="高钾"]),],
        labels=materialName_list,autopct="%0.1f%%")
plt.title("风化样本中的材料类型")
plt.savefig("../res/风化样本中的材料类型.png",dpi=400)

#分析风化样本中的颜色
colorName_list=["黑","蓝绿","浅蓝","浅绿","深绿","紫",]
plt.clf()
plt.pie(x=[len(weathering_simples[:][weathering_simples["颜色"]=="黑"]),len(weathering_simples[:][weathering_simples["颜色"]=="蓝绿"]),
           len(weathering_simples[:][weathering_simples["颜色"]=="浅蓝"]),len(weathering_simples[:][weathering_simples["颜色"]=="浅绿"]),
           len(weathering_simples[:][weathering_simples["颜色"]=="深绿"]),len(weathering_simples[:][weathering_simples["颜色"]=="紫"]),],
        labels=colorName_list,autopct="%0.1f%%")
plt.title("风化样本中的颜色")
plt.savefig("../res/风化样本中的颜色.png",dpi=400)

#分析无风化样本中的纹饰
plt.clf()
plt.pie(x=[len(noWeathering_simples[:][noWeathering_simples["纹饰"]=="A"]),len(noWeathering_simples[:][noWeathering_simples["纹饰"]=="B"]),len(noWeathering_simples[:][noWeathering_simples["纹饰"]=="C"]),],
        labels=decorationName_list,autopct="%0.1f%%")
plt.title("无风化样本中的纹饰")
plt.savefig("../res/无风化样本中的纹饰.png",dpi=400)

#分析无风化样本中的材质类型
plt.clf()
plt.pie(x=[len(noWeathering_simples[:][noWeathering_simples["类型"]=="铅钡"]),len(noWeathering_simples[:][noWeathering_simples["类型"]=="高钾"]),],
        labels=materialName_list,autopct="%0.1f%%")
plt.title("无风化样本中的材料类型")
plt.savefig("../res/无风化样本中的材料类型.png",dpi=400)

#分析无风化样本中的颜色
plt.clf()
plt.pie(x=[len(noWeathering_simples[:][noWeathering_simples["颜色"]=="黑"]),len(noWeathering_simples[:][noWeathering_simples["颜色"]=="蓝绿"]),
           len(noWeathering_simples[:][noWeathering_simples["颜色"]=="浅蓝"]),len(noWeathering_simples[:][noWeathering_simples["颜色"]=="浅绿"]),
           len(noWeathering_simples[:][noWeathering_simples["颜色"]=="深绿"]),len(noWeathering_simples[:][noWeathering_simples["颜色"]=="紫"]),],
        labels=colorName_list,autopct="%0.1f%%")
plt.title("无风化样本中的颜色")
plt.savefig("../res/无风化样本中的颜色.png",dpi=400)

