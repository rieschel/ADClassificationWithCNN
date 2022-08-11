# Import libraries
import matplotlib.pyplot as plt
import numpy as np
 
 
# Creating dataset

data_f_1 = [0.7900, 0.7662, 0.5925, 0.8375, 0.8138]
data_f_2 = [0.7675, 0.7300, 0.7150, 0.7988, 0.8175]
data_both_1 = [0.7250, 0.7113, 0.6075, 0.8125, 0.7125]
data_both_2 = [0.7650, 0.7950, 0.6800, 0.7413, 0.7262]

data_m_1 = [0.5875, 0.7100, 0.5537, 0.6200, 0.7563]
data_m_2 = [0.6487, 0.6912, 0.5313, 0.6887, 0.7325]
data_both_3 = [0.6050, 0.6712, 0.6762, 0.6838, 0.7587]
data_both_4 = [0.5337, 0.7625, 0.6463, 0.7300, 0.7088]

female = [0.7725000381469727, 0.8187500238418579, 0.7875000238418579, 0.8825000524520874, 0.8925000429153442]
male = [0.6899999380111694, 0.768750011920929, 0.8600000143051147, 0.6887500286102295, 0.8125]


# Allt:
#data = [data_f_1, data_f_2, data_both_1, data_both_2, data_both_3, data_both_4, data_m_1, data_m_2]

# FEMALE
#data = [data_f_1, data_f_2, data_both_1, data_both_2]

# MALE 
#data = [data_m_1, data_m_2, data_both_3, data_both_4]

# VERSION 2
data = [female, male]
 
fig = plt.figure()
 
# Creating plot
plt.boxplot(data)
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.grid(True)

# Allt:
#plt.xticks([1, 2, 3, 4, 5, 6, 7, 8], ["Female Attempt 1", "Female Attempt 2", "Both Sexes Attempt 1", "Both Sexes Attempt 2", "Both Sexes Attempt 3", "Both Sexes Attempt 4", "Male Attempt 1", "Male Attempt 2"], rotation=10)

# FEMALE
#plt.xticks([1, 2, 3,4], ["Female Attempt 1", "Female Attempt 2", "Both Sexes Attempt 1", "Both Sexes Attempt 2"], rotation=10)

# MALE
#plt.xticks([1, 2, 3, 4], ["Male Attempt 1", "Male Attempt 2", "Both Sexes Attempt 1", "Both Sexes Attempt 2"], rotation=10)

# VERSION 2
plt.xticks([1, 2], ["Female", "Male"])

# show plot
plt.show()