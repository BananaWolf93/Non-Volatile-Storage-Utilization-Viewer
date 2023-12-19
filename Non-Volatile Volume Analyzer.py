#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy
import psutil

# The following function searches for available mounted drives and obtains their usage information and stores the data in a dictionary. Finally, the details are then printed.

def disk_use():
    parts = psutil.disk_partitions(all=True)
    storage_dict = {}

    for partition in parts:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            storage_dict[partition.mountpoint] = {
                'Total': usage.total,
                'Used': usage.used,
                'Free': usage.free,
                'Percentage': usage.percent
                }
        except Exception as ex:
            print(f"Error retrieving disk usage for {partition.mountpoint} {ex}")
        
    return storage_dict
    
storage_dict = disk_use()
for mountpoint, info in storage_dict.items():
        print(f"Mountpoint: {mountpoint}")
        print(f"Percentage: {info['Percentage']}%")
        print("-" * 50)

# The following next function utilizes the previously defined dictionary now populated with data to usage with a bar craph to easily visualize these percentages of utilization across all mounted drives on the machine.

def graph(storage_dict):
     mountpoints = list(storage_dict.keys())
     Percentages = [info['Percentage'] for info in storage_dict.values()]

     plt.style.use('ggplot')
     x = numpy.arange(len(mountpoints))
     y = Percentages  

     fig, ax = plt.subplots()

     ax.bar(x, y, width=1, edgecolor="grey", linewidth=0.7)
     ax.set_xticks(x)
     ax.set_xticklabels(mountpoints, rotation=0, ha='right')

    # Set y-axis labels and ticks
     ax.set_yticks(numpy.arange(0, max(Percentages) + 1, 10))

     ax.set_ylabel('Percentage (%)')
     ax.set_title('Disk Usage Percentage')

     plt.tight_layout()
     plt.show()

graph(storage_dict)