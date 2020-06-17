import matplotlib
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt

import csv
import pandas as pd
import numpy as np

def print_time(test_to_pass, proj, tests, cond):
	pass_time = []
	for key in tests:
                if len(test_to_pass.get(key,[])) == 500 or len(test_to_pass.get(key,[])) == 0:
                        continue
		for (rank, time) in test_to_pass.get(key,[]):
			pass_time.append(float(time))

	pass_mean = sum(pass_time) / len(pass_time)
	pass_median = get_median(pass_time)
	print proj + "," + cond + ',' + str(len(pass_time)) + ',' + str(round(pass_mean, 2)) + "," + str(round(pass_median,2)) 
	return pass_time

def plot_ranks(proj_ranks):
	fig1, ax1 = plt.subplots()

	projs = proj_ranks.keys()
	ax1.boxplot([proj_ranks["ProjC"], proj_ranks["ProjD"], proj_ranks["ProjE"]], showmeans=True)
	ax1.set_ylim([-4,104])
	ax1.get_xticklabels()[0].set_fontsize(12)
	ax1.get_xticklabels()[1].set_fontsize(12)
	ax1.get_xticklabels()[2].set_fontsize(12)

	ax1.get_yticklabels()[0].set_fontsize(12)
	ax1.get_yticklabels()[1].set_fontsize(12)
	ax1.get_yticklabels()[2].set_fontsize(12)
	ax1.get_yticklabels()[3].set_fontsize(12)
	ax1.get_yticklabels()[4].set_fontsize(12)
	ax1.get_yticklabels()[5].set_fontsize(12)
	ax1.get_yticklabels()[6].set_fontsize(12)

	plt.xticks([1, 2, 3], ['ProjC', 'ProjD', 'ProjE'])
	plt.grid()
	plt.savefig('reproducibility-plot.png', bbox_inches='tight')

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

def plot_time(proj_ranks):
	data_a = [proj_ranks["ProjC"][0], proj_ranks["ProjD"][0], proj_ranks["ProjE"][0]]
	data_b = [proj_ranks["ProjC"][1], proj_ranks["ProjD"][1], proj_ranks["ProjE"][1]]

	ticks = ['ProjC', 'ProjD', 'ProjE']

	plt.figure()

	bpl = plt.boxplot(data_a, positions=np.array(xrange(len(data_a)))*2.0-0.4, sym='', widths=0.6, showmeans=True)
	bpr = plt.boxplot(data_b, positions=np.array(xrange(len(data_b)))*2.0+0.4, sym='', widths=0.6, showmeans=True)
	set_box_color(bpl, '#31a354') # colors are from http://colorbrewer2.org/
	set_box_color(bpr, '#D7191C')

	plt.plot([], c='#31a354', label='Pass')
	plt.plot([], c='#D7191C', label='Fail')
	plt.legend()

	plt.xticks(xrange(0, len(ticks) * 2, 2), ticks, fontsize=12)
	plt.yticks(fontsize=12)
	plt.xlim(-1, len(ticks)*2 - 1)
	plt.grid()
	plt.savefig('runtime-plot.png', bbox_inches='tight')

def get_median(n_num):
	n = len(n_num) 
	n_num.sort() 
	  
	if n % 2 == 0: 
	    median1 = n_num[n//2] 
	    median2 = n_num[n//2 - 1] 
	    median = (median1 + median2)/2
	else: 
	    median = n_num[n//2] 
	return median

def print_rank_info(proj_to_test, test_to_pass, test_to_fail, test_to_first_fail, proj_ranks):
        for proj in proj_to_test.keys():
		all_first_rank = []
                all_fails = []
		for key in proj_to_test[proj]:
			pass_info = test_to_pass.get(key,[])
			fail_info = test_to_fail.get(key,[])
                        if len(pass_info) == 0 or len(fail_info) == 0:
                                continue

			if key in test_to_first_fail:
				all_first_rank.append(test_to_first_fail[key])
                                all_fails.append(float(len(fail_info)) / 5.0)
		mean = sum(all_fails) / len(all_fails)
		median = get_median(all_fails)
                fails = proj_ranks[proj]
                print str.format("{},{},{},{}%,{},{}", proj, len(proj_to_test[proj]), str(len(fails)), int(round(1.0 * len(fails) / len(proj_to_test[proj]), 2) * 100),  str(round(mean,1)), str(round(median,1)))

proj_to_test = {}
tests = set()
test_to_fail = {}
test_to_pass = {}
with open('Tables3and4-Reproducibility-Runtime-anon.csv', 'rb') as csvfile2:
	reader2 = csv.reader(csvfile2, quotechar='"')

	for row in reader2:
		if row[0] == 'Project':
			continue
		tests.add(row[1])
		proj_to_test[row[0]] = proj_to_test.get(row[0],set([])) | set([row[1]])
		if "pass" in row[3]:
			test_to_pass[row[1]] = test_to_pass.get(row[1], []) + [(row[2], row[4])]
		else:
			test_to_fail[row[1]] = test_to_fail.get(row[1], []) + [(row[2], row[4])]

	test_to_first_fail = {}
	for key in tests:
		for (rank, time) in test_to_fail.get(key,[]):
			test_to_first_fail[key] = min(int(rank), int(test_to_first_fail.get(key, 100000)))

	proj_ranks = {}
	for proj in proj_to_test.keys():
		fails = []
		for key in proj_to_test[proj]:
			pass_info = test_to_pass.get(key,[])
			fail_info = test_to_fail.get(key,[])
                        if len(pass_info) == 0 or len(fail_info) == 0:
                                continue

			fails.append(float(len(fail_info)) / 5.0)
                proj_ranks[proj] = fails
        plot_ranks(proj_ranks)
        print "================ Statistics on reproducibility"
        print_rank_info(proj_to_test, test_to_pass, test_to_fail, test_to_first_fail, proj_ranks)
        
        print "================ Statistics on runtime"
	proj_time = {}
	for proj in proj_to_test.keys():
		pass_time = print_time(test_to_pass, proj, proj_to_test[proj], 'pass')
		fail_time = print_time(test_to_fail, proj, proj_to_test[proj], 'fail')
		proj_time[proj] = (pass_time, fail_time)
	plot_time(proj_time)
