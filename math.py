from celluloid import Camera
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x) / x


fig, ax = plt.subplots(figsize=(6, 6))

camera = Camera(fig)

for i in range(200):
    x = np.arange(-10, -10 + i / 20, 0.001)
    x1 = np.arange(10, 10 - i / 20, -0.001)
    y = f(x)
    y1 = f(x1)
    plt.plot(x, y, 'r', x1, y1, 'b')
    camera.snap()

animation = camera.animate(interval=41.6)

plt.ylim(-0.3, 1.1)
plt.grid(c='g', linestyle='-.')
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.title('基于python数学极限公式的动态展示')
plt.xlabel('x')
plt.ylabel('sinx/x')
plt.show()
