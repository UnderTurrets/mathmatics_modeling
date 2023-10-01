import numpy as np

import classify_txt2 as dataResource
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family']='simHei'  #黑体
matplotlib.pyplot.rcParams['axes.unicode_minus'] = False	# 显示负号
import dataProcessing
import fitFunc

def Task2_fit(label,age_Method1_data,order1,age_Method2_data,order2,age_Method3_data,order3,age_Method4_data,order4):

    plt.clf()
    plt.title(label=label)

    x1=dataProcessing.separateX_PointSet(age_Method1_data)
    x2=dataProcessing.separateX_PointSet(age_Method2_data)
    x3=dataProcessing.separateX_PointSet(age_Method3_data)
    x4=dataProcessing.separateX_PointSet(age_Method4_data)

    y1=dataProcessing.separateY_PointSet(age_Method1_data)
    y2=dataProcessing.separateY_PointSet(age_Method2_data)
    y3=dataProcessing.separateY_PointSet(age_Method3_data)
    y4=dataProcessing.separateY_PointSet(age_Method4_data)

    print("疗法一：")
    y1_expression=fitFunc.fit_with_numpy(x_sequence=x1,
                                   y_sequence=y1,
                                   order=order1)

    print("疗法二：")
    y2_expression=fitFunc.fit_with_numpy(x_sequence=x2,
                                   y_sequence=y2,
                                   order=order2)
    print("疗法三：")
    y3_expression=fitFunc.fit_with_numpy(x_sequence=x3,
                                   y_sequence=y3,
                                   order=order3)
    print("疗法四：")
    y4_expression=fitFunc.fit_with_numpy(x_sequence=x4,
                                   y_sequence=y4,
                                   order=order4)

    x_draw = np.linspace(min(min(x1),min(x2),min(x3),min(x4)),max(max(x1),max(x2),max(x3),max(x4)), num=1000)
    y1_draw = y1_expression(x_draw)
    y2_draw = y2_expression(x_draw)
    y3_draw = y3_expression(x_draw)
    y4_draw = y4_expression(x_draw)

    plt.plot(x_draw,y1_draw,label="method 1",color="r", linestyle="-")
    plt.plot(x_draw,y2_draw,label="method 2",color="g", linestyle="--")
    plt.plot(x_draw,y3_draw,label="method 3",color="b", linestyle="-.")
    plt.plot(x_draw,y4_draw,label="method 4",color="m", linestyle=":")
    plt.legend(loc="lower left")
    plt.savefig(label+".png",dpi=400)
    plt.cla()

    plt.scatter(x1,y1,label="method 1",color="r")
    plt.plot(x_draw,y1_draw,label="method 1",color="r", linestyle="-")
    plt.legend(loc="lower left")
    plt.savefig(label+"_Method1.png",dpi=400)
    plt.cla()

    plt.scatter(x2,y2,label="method 2")
    plt.plot(x_draw,y2_draw,label="method 2",color="g", linestyle="--")
    plt.legend(loc="lower left")
    plt.savefig(label+"_Method2.png",dpi=400)
    plt.cla()

    plt.scatter(x3,y3,label="method 3")
    plt.plot(x_draw,y3_draw,label="method 3",color="b", linestyle="-.")
    plt.legend(loc="lower left")
    plt.savefig(label+"_Method3.png",dpi=400)
    plt.cla()

    plt.scatter(x4,y4,label="method 4")
    plt.plot(x_draw,y4_draw,label="method 4",color="m", linestyle=":")
    plt.legend(loc="lower left")
    plt.savefig(label+"_Method4.png",dpi=400)
    plt.cla()

    return x_draw,y1_expression,y2_expression,y3_expression,y4_expression

age14to25_x,age14to25_y1_expression,age14to25_y2_expression,age14to25_y3_expression,age14to25_y4_expression=Task2_fit("年龄14至25岁",dataResource.age14to25_Method1_data,3,
                                                                                                                          dataResource.age14to25_Method2_data,3,
                                                                                                                          dataResource.age14to25_Method3_data,4,
                                                                                                                          dataResource.age14to25_Method4_data,3)
age25to35_x,age25to35_y1_expression,age25to35_y2_expression,age25to35_y3_expression,age25to35_y4_expression=Task2_fit("年龄25至35岁",dataResource.age25to35_Method1_data,3,
                                                                                                                          dataResource.age25to35_Method2_data,3,
                                                                                                                          dataResource.age25to35_Method3_data,4,
                                                                                                                          dataResource.age25to35_Method4_data,4)
age35to45_x,age35to45_y1_expression,age35to45_y2_expression,age35to45_y3_expression,age35to45_y4_expression=Task2_fit("年龄35至45岁",dataResource.age35to45_Method1_data,4,
                                                                                                                          dataResource.age35to45_Method2_data,4,
                                                                                                                          dataResource.age35to45_Method3_data,3,
                                                                                                                          dataResource.age35to45_Method4_data,3)
age45More_x,age45More_y1_expression,age45More_y2_expression,age45More_y3_expression,age45More_y4_expression=Task2_fit("年龄大于45岁",dataResource.age45More_Method1_data,5,
                                                                                                                          dataResource.age45More_Method2_data,4,
                                                                                                                          dataResource.age45More_Method3_data,5,
                                                                                                                          dataResource.age45More_Method4_data,3)




