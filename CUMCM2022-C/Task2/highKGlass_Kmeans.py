from classify2Two import highK_glass_data,highK_glass
import numpy as np
from sklearn.cluster import KMeans

# 初始化KMeans模型
kmeans = KMeans(n_clusters=4,n_init=10)

# 执行聚类
kmeans.fit(highK_glass_data)

# 获取聚类的标签
labels = kmeans.labels_

# 将聚类标签加入原始数据中
highK_glass['Cluster'] = labels

# 打印每个簇的样本数量
print(highK_glass['Cluster'].value_counts())
#打印结果
print(highK_glass)

# 打印每个簇的平均值
for cluster_id in range(4):
    cluster_mean = np.mean(highK_glass_data[labels == cluster_id], axis=0)
    print(f"Cluster {cluster_id+1} Mean: {cluster_mean}")


from sklearn.metrics import silhouette_score, pairwise_distances
# 计算轮廓系数
silhouette_avg = silhouette_score(highK_glass_data, labels)
print("Silhouette Score:", silhouette_avg)

# 计算簇内平均距离
intra_cluster_dist = []
for cluster_id in range(4):
    cluster_data = highK_glass_data[labels == cluster_id]
    intra_cluster_dist.append(pairwise_distances(cluster_data).mean())

avg_intra_cluster_dist = np.mean(intra_cluster_dist)
print("Intra-Cluster Average Distance:", avg_intra_cluster_dist)

# 计算簇间平均距离
inter_cluster_dist = pairwise_distances(
    kmeans.cluster_centers_, metric='euclidean').mean()
print("Inter-Cluster Average Distance:", inter_cluster_dist)

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
# 执行PCA降维（由14维降至2维）
pca = PCA(n_components=2)
highK_glass_pca = pca.fit_transform(highK_glass_data)

# 创建一个图形窗口
fig = plt.figure()
ax = fig.add_subplot(111)

# 根据聚类标签绘制散点图
for i in range(4):
    cluster_data = highK_glass_pca[labels == i]
    ax.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f"Cluster {i+1}")

# 设置图形标题和坐标轴标签
ax.set_title("Clustering Result (PCA)")
ax.set_xlabel("Dimension 1")
ax.set_ylabel("Dimension 2")

# 添加图例
ax.legend()

#保存结果
plt.savefig("../res/高钾材质的二维聚类结果.png",dpi=400)
highK_glass.to_excel("../res/高钾材质的聚类结果.xlsx")
# 显示图形
plt.show()

