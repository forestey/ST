import matplotlib.pyplot as plt

from random_walk import RandomWalk


# 只要程度处于活动状态,就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例,并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸,figsize()用于指定图表的宽度\高度\分辨率和背景色
    plt.figure(dpi=128, figsize=(10, 6))

    # 绘制点并将图形显示出来
    point_numbers = list((range(rw.num_points)))

    # 隐藏x,y坐标轴
    plt_axes = plt.axes()
    plt_axes.get_xaxis().set_visible(False)
    plt_axes.get_yaxis().set_visible(False)

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=100)

    plt.show()

    keep_running = input(r"Make another walk? (y/n): ")
    if keep_running == 'n':
        break