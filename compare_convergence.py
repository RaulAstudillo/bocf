import numpy as np
import matplotlib.pyplot as plt
from pylab import savefig

path = './experiments_cluster/test2_'
test_number = '2'
files_names = ['random', 'EIf', 'EIh'] #['random', 'uKG', 'uKG_cf']#['random', 'maEI', 'maKG']
legend_names = ['random', 'EI_{f}', 'EI_{h}']#['random', 'KG-exact ', 'u-KG']
colors = ['y', 'b', 'r']#['y', 'g', 'r', 'b']
markers = ['>', 'D', 'o']#['>', 's', 'o', 'D']
n_iterations = 50
x_axis = [i+1 for i in range(n_iterations)]
plt.figure()
for i in range(len(files_names)):
    log_regret = np.loadtxt(path + files_names[i] + '/test' + test_number + '_' + files_names[i] + '_noiseless' + '_log_regret_stats.txt')
    #for k in range(3):
        #for j in range(n_iterations-1):
            #data[j+1] = 0.5*(data[j+1] + data[j]) + .001*j
    #plt.plot(x_axis, data[:,0], colors[i], markersize=5) #, label = legend_names[i])
    plt.errorbar(x_axis, log_regret[:,0], yerr=log_regret[:,1], marker=markers[i], markersize=4, markeredgecolor ='k', markevery=4, color=colors[i], ecolor=colors[i], errorevery=4, capsize=2, label=legend_names[i])
    #plt.fill_between(x_axis, data[:,0] - 0.5*data[:,1], data[:,0] + 0.75*data[:,1],alpha=0.75, edgecolor=colors[i], facecolor=shaded_colors[i])
plt.xlabel('function evaluations')
plt.ylabel('log scale of immediate regret')
plt.legend(loc='lower left')
plt.grid(True)
savefig('test' + test_number + '_fval.png')

plt.figure()
for i in range(len(files_names)):
    time = np.loadtxt(path + files_names[i] + '/test' + test_number + '_' + files_names[i] + '_noiseless' + '_time_tats.txt')
    #for k in range(3):
        #for j in range(n_iterations-1):
            #data[j+1] = 0.5*(data[j+1] + data[j]) + .001*j
    #plt.plot(x_axis, data[:,0], colors[i], markersize=5) #, label = legend_names[i])
    plt.errorbar(x_axis, time[:, 0], yerr=time[:, 1], marker=markers[i], markersize=4, markeredgecolor='k',
                 markevery=4, color=colors[i], ecolor=colors[i], errorevery=4, capsize=2, label=legend_names[i])
    #plt.fill_between(x_axis, data[:,0] - 0.5*data[:,1], data[:,0] + 0.75*data[:,1],alpha=0.75, edgecolor=colors[i], facecolor=shaded_colors[i])

plt.xlabel('function evaluations')
plt.ylabel('cpu time (min)')
#plt.legend(loc='lower right')
plt.grid(True)
savefig('test' + test_number + '_time.png')
plt.show()
