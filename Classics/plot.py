import matplotlib.pyplot as plt
import numpy as np

num_ep = []
cum_r = []
loss  = []
avg_q = []

with open('cartpole_test_result.txt', 'r') as qq:
  for line in qq:
    if line[0] == ' ': continue
    line2 = line.strip().split('\t')
    num_ep.append(float(line2[0]))
    cum_r.append(float(line2[1]))
    loss.append(float(line2[3]))
    avg_q.append(float(line2[4]))


plt.style.use('ggplot')

plt.plot(loss, '-', linewidth = 1)

plt.show()
