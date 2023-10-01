'''
Created by Han Xu
email:736946693@qq.com
'''
import numpy as np
import matplotlib
matplotlib.rcParams['font.family']='simHei'  #黑体
matplotlib.pyplot.rcParams['axes.unicode_minus'] = False	# 显示负号
from fitFunc import fit_with_numpy
from CD4_modelData import final_points
import dataProcessing
import matplotlib.pyplot as plt

# print(final_points)

x = dataProcessing.separateX_PointSet(final_points)
y = dataProcessing.separateY_PointSet(final_points)
print(np.max(y))
y_expre=fit_with_numpy(x_sequence=x,y_sequence=y,order=12)

x_draw=np.linspace(min(x),max(x),num=1000)
y_draw=y_expre(x_draw)

# draw the results
plt.scatter(x, y, marker='*', label='original values')
plt.plot(x_draw, y_draw, 'r', label='fit values')
plt.title("CD4fit.png")
plt.xlabel('')
plt.ylabel('')
plt.legend(loc="upper left")
plt.savefig("CD4fit.png",dpi=400)
plt.show()