import sys
import numpy
from matplotlib import pyplot
import os, os.path
import glob
import statistics

# Here we combine all inputs from different pairs
# for boxplot
# Currently it is set to use only data with difference in 
# sea level more than 10cm

dir_range=[0,1,2,3,4,5,6,7,8,9]

total_diff = []
total_stats = []
new_diff = []
for j in dir_range:

  DIR = "./500km/pair"+str(j)
  N_of_files=int(len(glob.glob1(DIR,"*.txt"))/2)

  new_data = []
  z_int = []
  for_stats = []
  N_of_values = 0
  for i in range (1,N_of_files):
    filename = "./500km/pair" + str(j) + "/scatter_plot_data"+str(i)+".txt"
    inp_file=open(filename)
    filename4 = "./500km/pair" + str(j) + "/waterlevel"+str(i)+".txt"
    inp_file4=open(filename4)
  
    for line in inp_file:
      N_of_values += 1
      val=line.strip()
      single_value=(float(val))
      new_data.append(single_value)
      total_diff.append(single_value)
      for_stats.append(abs(single_value))
      total_stats.append(abs(single_value))
    for line2 in inp_file4:
      val2=line2.strip()
      single_value2=(float(val2))
      z_int.append(single_value2)
    
    inp_file.close()
    inp_file4.close()
  total_values=numpy.arange(N_of_values)


# Remove next 3 lines to use complete set of data
  for i in range(0, N_of_values):
    if (abs(total_diff[i]) > 0.1):
      new_diff.append(abs(total_diff[i]))

print("number of points in the selection", len(new_diff))


filename7="boxplot_500km.png"
pyplot.boxplot(new_diff, showfliers=False)
pyplot.savefig(filename7,format='png')
pyplot.clf()

out_file2=open("500_10cm.txt","w+")
for i in (new_diff):
  strn3=str(i)
  out_file2.write(strn3+" \n")
