import matplotlib.pyplot as plt


# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
# # print(y_values)
# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds,  edgecolors='none', s=10)
#
# # 设置图表标题，并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)
#
# # 设置每个坐标轴的取值范围
# plt.axis([0, 1100, 0, 1100000])
# plt.savefig(r"data_folder\squares_plot.png", bbox_inches='tight')
# plt.show()

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

# 设置每个坐标轴的取值范围
plt.axis([0, 6000, 0, 125000000000])

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=10)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig(r"data_folder\squares_plot.png", bbox_inches='tight')
plt.show()