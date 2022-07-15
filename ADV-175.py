# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 18:42:20 2022

@author: anees
"""

import matplotlib .pyplot as plt
import psutil as p
app_name_list = []
app_percent_list = []
count = 0
for process in p.process_iter():
  count = count + 1
  if count <= 6:
    name = process.name()
    cpu_usage = p.cpu_percent()
    print('name : ', name,'-- cpu_usage : ', cpu_usage)
    app_name_list.append(name)
    app_percent_list.append(cpu_usage)

plt.figure(figsize=(15,7))
plt.xlabel("Application")
plt.ylabel("CPU Usage")
plt.bar(app_name_list, app_percent_list,width=0.6 ,color=("purple","green","red","blue","orange","pink"))
plt.show()