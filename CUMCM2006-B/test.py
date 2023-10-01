import matplotlib.pyplot as plt
import numpy as np

# 生成一组随机数据
data = np.linspace(0,10,num=10)
weight=[0.05]*9+[0.55]

# 绘制直方图
fig1=plt.figure()
plt.hist(data, bins=30, color='skyblue', alpha=0.8,weights=weight)
# 设置图表属性
plt.title('RUNOOB hist() Test')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
# 显示图表
plt.show()
