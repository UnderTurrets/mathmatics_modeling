import numpy as np
import matplotlib
matplotlib.rcParams['font.family']='simHei'  #黑体
matplotlib.pyplot.rcParams['axes.unicode_minus'] = False	# 显示负号
from fit_for_CD4 import y_expre as func1
from fit_for_VLoad import  y_expre as func2
x=np.linspace(0,50,num=1000)
y1=func1(x)
y2=-func2(x)
final_y=y1+y2
import matplotlib.pyplot as plt
plot1 = plt.plot(x, final_y,label='original values')
plt.title('combine2func')
plt.xlabel('')
plt.ylabel('')
plt.legend(loc="upper left")
plt.savefig("combine_func.png",dpi=400)
plt.show()