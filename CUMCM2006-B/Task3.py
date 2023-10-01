import matplotlib
import matplotlib.pyplot as plt
import dataProcessing
import fitFunc
import numpy as np
import Task2_fit
matplotlib.rcParams['font.family']='simHei'  #黑体
matplotlib.pyplot.rcParams['axes.unicode_minus'] = False	# 显示负号

price_list=[68.6,193.2,137.2,204.4,]

def get_U_function(array_like, float_price, float_r):
    invalid_percent=array_like[array_like<=0].shape[0]/array_like.shape[0]
    print("失效率：{}".format(invalid_percent))

    mean=np.mean(a=array_like,axis=0)
    std=np.std(a=array_like,axis=0)

    return (  (  (mean*(1-invalid_percent)  )  **2)/std  )/(float_price**float_r)

def Task3(array_x,y1_expression,y2_expression,y3_expression,y4_expression,float_r):

    y1_draw = y1_expression(array_x)
    y2_draw = y2_expression(array_x)
    y3_draw = y3_expression(array_x)
    y4_draw = y4_expression(array_x)

    print("疗法一得分:{}".format(get_U_function(y1_draw,68.6,float_r)))
    print("疗法二得分:{}".format(get_U_function(y2_draw,193.2,float_r)))
    print("疗法三得分:{}".format(get_U_function(y3_draw,137.2,float_r)))
    print("疗法四得分:{}".format(get_U_function(y4_draw,204.4,float_r)))
    return

Task3(Task2_fit.age14to25_x,Task2_fit.age14to25_y1_expression,Task2_fit.age14to25_y2_expression,
      Task2_fit.age14to25_y3_expression,Task2_fit.age14to25_y4_expression,1)
Task3(Task2_fit.age25to35_x,Task2_fit.age25to35_y1_expression,Task2_fit.age25to35_y2_expression,
      Task2_fit.age25to35_y3_expression,Task2_fit.age25to35_y4_expression,1)
Task3(Task2_fit.age35to45_x,Task2_fit.age35to45_y1_expression,Task2_fit.age35to45_y2_expression,
      Task2_fit.age35to45_y3_expression,Task2_fit.age35to45_y4_expression,1)
Task3(Task2_fit.age45More_x,Task2_fit.age45More_y1_expression,Task2_fit.age45More_y2_expression,
      Task2_fit.age45More_y3_expression,Task2_fit.age45More_y4_expression,1)