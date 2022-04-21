import sys
import numpy
from matplotlib import pyplot

data_range=[250,500,1000,1500,2000]

new_data = []
i=0

for j in data_range:

  filename=str(j)+"_10cm.txt"
  inp_file=open(filename)
  new_data.append([])
  for line in inp_file:  
      val=line.strip()
      single_value=(float(val))
      new_data[i].append(abs(single_value))

  i+=1
  inp_file.close()


filename2="boxplot_10cm.png"
pyplot.boxplot(new_data)#, showfliers=False)
pyplot.xticks([1,2,3,4,5],["250","500","1000","1500","2000"])
pyplot.ylabel('Difference in sea level, m')
pyplot.savefig(filename2,format='png')
pyplot.clf()
