'''
Created by Han Xu
email:736946693@qq.com
'''

import torch.utils.data
import torch
import matplotlib.pyplot as plt
import torch.nn as nn
import numpy as np

# 如果可以用cuda就在cuda上运行，这样会快很多
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device to train")

# # 生成训练数据用的数据
# x = torch.linspace(-torch.pi, torch.pi, 10000)  # (1000, )
# x = torch.unsqueeze(input=x, dim=1)  # (1000, 1)
# y = torch.sin(x)  # (1000, 1)

# 准备数据
from CD4_modelData import final_points

x = torch.tensor(np.array([single_point[0] for single_point in final_points]), device=device,
                 dtype=torch.float32).reshape(-1, 1)
y = torch.tensor(np.array([single_point[1] for single_point in final_points]), device=device,
                 dtype=torch.float32).reshape(-1, 1)


'''划分数据集'''
dataset = torch.utils.data.TensorDataset(x, y)  # 组成torch专门的数据库
batch_size = 6  # 设置批次大小



# 定义NN模型，继承自nn.Module
class NeuralNetwork(nn.Module):
    def __init__(self):
        # 调用
        super(NeuralNetwork, self).__init__()

        self.linear_relu_stack = nn.Sequential(
            nn.Linear(1, 100),
            nn.ReLU(),
            nn.Linear(100, 200),
            nn.ReLU(),
            nn.Linear(200, 100),
            nn.ReLU(),
            nn.Linear(100, 1),
        )

    def forward(self, x):
        y_pred = self.linear_relu_stack(x)
        return y_pred


# 把模型放到GPU上训练
model = NeuralNetwork().to(device)
# 均方差做损失函数
loss_fn = nn.MSELoss()

# 用下Adam优化器会收敛的快很多
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)

# 轮次
epoch = 5

plt.figure("regression")  # 新建一张画布，打印数据点和预测值
plt.ion()  # 开启交互模式
plt.show()
MydataLoader=torch.utils.data.DataLoader(dataset=dataset,batch_size=batch_size,shuffle=True)
for i in range(epoch):
    for batch_idx,(data,target) in enumerate(MydataLoader):
        pred = model(data)
        loss = loss_fn(target, pred)

        #
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch_idx % 10 == 0:
            loss, batch = loss.item(), i
            print(f'loss: {loss} {batch}')
            plt.cla()
            y_pre=model.forward(x)
            plt.scatter(x.to("cpu").numpy(), y.to("cpu").numpy())
            plt.plot(x.cpu().numpy(), y_pre.detach().cpu().numpy())
            plt.pause(0.001)
# 保存
# torch.save(model.state_dict(), "model.pth")

pred = model(x)
plt.scatter(x.cpu().numpy(), y.cpu().numpy())
plt.plot(x.cpu().numpy(), pred.detach().cpu().numpy())
plt.savefig("pytorchfit_CD4.png")

print("Saved PyTorch Model State to model.pth")
from goodness_of_fit import goodness_of_fit
rr = goodness_of_fit(pred, y)
print(rr)
