import pygal

from die import Die

# 创建一个D6(面数默认为6面)的实例
die_1 = Die()


# 掷几次骰子,并将结果存储在一个列表中
results = []
# 掷骰子100次,并将结果保存在results中
for roll_num in range(1000):
    result = die_1.roll()
    results.append(result)

# 分析结果
frequencies = []

for value in range(1, die_1.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist._x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

print(results)
print(frequencies)