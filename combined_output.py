import sys
import numpy
from matplotlib import pyplot
import os, os.path
import glob
import statistics

# In this file we calculate statistics for different distances,
# create scatter plots for separate pairs and the total one,
# make histograms for separate pairs and total 
# and make a boxplot for single distance



dir_range=[0,1,2,3,4,5,6,7,8,9]
#dir_range=[0]
filename3="./statistics.txt"
out_file=open(filename3,"w+")

total_diff = []
total_stats = []
total_sea_level = []
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
    filename4 = ".500km/pair" + str(j) + "/waterlevel"+str(i)+".txt"
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
      total_sea_level.append(single_value2) 
    inp_file.close()
    inp_file4.close()

  total_values=numpy.arange(N_of_values)

#Scatter
  filename2="./scatter_total_" + str(j) + ".png"
  pyplot.scatter(z_int, new_data,s=10.)
  pyplot.xlabel("Sea level")
  pyplot.ylabel("Difference in sea level, m")
  pyplot.savefig(filename2,format='png')
  pyplot.clf()

#Histogram
  filename5="./histogram_" + str(j) + ".png"
  pyplot.hist(new_data,bins = 100, range=[-0.05,0.05])
  pyplot.ylabel("Number of points in selected range")
  pyplot.xlabel("Difference in sea level, m")
  pyplot.savefig(filename5,format='png')
  pyplot.clf()


#For statistics
  strn1="mean value =" + str(statistics.mean(for_stats))
  out_file.write(strn1+" \n")
  strn2="standard deviation = " + str(statistics.stdev(new_data))
  out_file.write(strn2+" \n")

strn1="mean value, total =" + str(statistics.mean(total_stats))
out_file.write(strn1+" \n")
strn2="standard deviation, total= " + str(statistics.stdev(total_diff))
out_file.write(strn2+" \n")


#Combined outputs
filename6="histogram_500km_range_3cm.png"
pyplot.hist(total_diff,bins = 100, range=[-0.03,0.03])
pyplot.ylabel("Number of points in selected range")
pyplot.xlabel("Difference in sea level, m")
#pyplot.title("Distance 500 km")
pyplot.savefig(filename6,format='png')
pyplot.clf()

filename7="boxplot_500km.png"
pyplot.boxplot(total_diff, showfliers=False)
pyplot.savefig(filename7,format='png')
pyplot.clf()
  
filename8="./scatter_all_500km" + ".png"
pyplot.scatter(total_sea_level, total_diff,s=10.)
pyplot.xlim(-1.5,1.5)
pyplot.xlabel("Sea level")
pyplot.ylabel("Difference in sea level, m")
pyplot.savefig(filename8,format='png')
pyplot.clf()
