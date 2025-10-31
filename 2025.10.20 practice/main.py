import numpy as np
import matplotlib.pyplot as plt

from skimage.data import coins
from skimage.transform import rescale
from skimage.util import img_as_float
from scipy.ndimage import gaussian_filter
from sklearn.feature_extraction.image import grid_to_graph
from sklearn.cluster import AgglomerativeClustering

# 1) 读图与预处理
orig = coins()
img = img_as_float(orig)                       # 转 float，范围 [0,1]
img = gaussian_filter(img, sigma=2)            # 平滑
img = rescale(img, 0.25, mode="reflect", anti_aliasing=True)  # 适度下采样（更平滑）

h, w = img.shape
Xg, Yg = np.meshgrid(np.arange(w), np.arange(h))  # 坐标网格

# 2) 组装特征：强度 + 空间坐标（坐标要缩放，避免“坐标量级压倒灰度”）
alpha = 0.3    # 空间权重（可调：0.3~1.0 之间找感觉）
feat = np.c_[
    img.ravel(),
    alpha * (Xg.ravel() / w),
    alpha * (Yg.ravel() / h),
]

connectivity = grid_to_graph(h, w)   # 8邻域连通（scikit-learn 会按稀疏图约束聚类）

# 3) 层次聚类（Ward）
n_clusters = 27   # 可微调：20~40
ward = AgglomerativeClustering(
    n_clusters=n_clusters,
    linkage="ward",
    connectivity=connectivity,
)
labels = ward.fit_predict(feat).reshape(h, w)

# 4) 可视化（背景=灰度图，叠加各簇轮廓）
plt.figure(figsize=(6, 6))
plt.imshow(img, cmap="gray")
for l in range(n_clusters):
    plt.contour(
        labels == l,                # ★ 关键修正：逐簇绘制，不再是 label == 1
        levels=[0.5],
        linewidths=0.7,
        colors=[plt.cm.nipy_spectral(l / float(n_clusters))],
    )
plt.axis("off")
plt.tight_layout()
plt.show()

from skimage.color import label2rgb

overlay = label2rgb(labels, image=img, alpha=0.35, kind="avg")
plt.figure(figsize=(6, 6))
plt.imshow(overlay)
plt.axis("off")
plt.tight_layout()
plt.show()

