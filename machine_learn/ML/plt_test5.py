import matplotlib.pyplot as plt
import random
import matplotlib

matplotlib.rc('font', family='SimHei', weight='bold')

city_name = ['北京', '上海', '广州', '深圳', '成都']
city_name.reverse()

data = []
for i in range(len(city_name)):
    data.append(random.randint(100, 200))

colors = ['red', 'yellow', 'blue', 'green', 'gray']
colors.reverse()

plt.barh(range(len(data)), data, tick_label=city_name, color=colors)

# 不要X横坐标标签。
# plt.xticks(())

plt.show()