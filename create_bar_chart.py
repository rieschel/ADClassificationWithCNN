import matplotlib.pyplot as plt
import numpy as np


Models_female_data = ['female','male','all']
Accuracy_female_data_ad = [0.73, 0.67, 0.69]
Accuracy_female_data_cn = [0.89, 0.65, 0.83]

Models_male_data = ['male', 'female','all']
Accuracy_male_data_ad = [0.83, 0.64, 0.74]
Accuracy_male_data_cn = [0.66, 0.65, 0.81]

x = np.arange(len(Models_female_data))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Accuracy_female_data_ad, width, label='AD')
rects2 = ax.bar(x + width/2, Accuracy_female_data_cn, width, label='CN')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Accuracy')
ax.set_xlabel('Models')
ax.set_xticks(x, Models_female_data)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.ylim(0, 1)
plt.show()