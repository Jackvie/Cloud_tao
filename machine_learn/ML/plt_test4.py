import matplotlib
import random
import matplotlib.pyplot as plt

# 中文乱码和坐标轴负号处理。
matplotlib.rc('font', family='SimHei', weight='bold')
plt.rcParams['axes.unicode_minus'] = False

# 城市数据。
city_name = ['北京', '上海', '广州', '深圳', '成都']

# 数组反转。
city_name.reverse()

# 装载随机数据。
data = []
for i in range(len(city_name)):
    data.append(random.randint(100, 150))
# 绘图。
fig, ax = plt.subplots()
b = ax.barh(range(len(city_name)), data, color='#6699CC')

# 为横向水平的柱图右侧添加数据标签。
for rect in b:
    w = rect.get_width()
    ax.text(w, rect.get_y() + rect.get_height() / 2, '%d' %
            int(w), ha='left', va='center')

# 设置Y轴纵坐标上的刻度线标签。
ax.set_yticks(range(len(city_name)))
ax.set_yticklabels(city_name)

# 不要X横坐标上的label标签。
plt.xticks(())

plt.title('水平横向的柱状图', loc='center', fontsize='25',
          fontweight='bold', color='red')

plt.show()