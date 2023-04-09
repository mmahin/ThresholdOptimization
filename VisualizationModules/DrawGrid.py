import matplotlib.pyplot as plt

matrix = [
    [1,1,1,1,0,0,0,0,0,0],
    [1,1,1,1,1,1,0,0,0,0],
    [1,1,1,0,0,0,0,1,1,1],
    [1,0,0,0,0,0,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,1,1,1,0,0],
    [0,0,1,1,1,1,1,0,0,0],
    [0,0,0,0,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0]
]

step1 = 10
step2 = 10
target_threshold1 = 10
target_threshold2 = 10
hotspot_area_restriction = 0.5

min_lat, max_lat = 24.5208, 49.38
min_lon, max_lon = -124.77, -67.06
import numpy as np
# Generate 10 equidistant points along latitude and longitude axis
lat_vals = np.linspace(min_lat, max_lat, 10)
lon_vals = np.linspace(min_lon, max_lon, 10)
lat_labels = []
for count in range(0,len(lat_vals)):
    lat_labels.append( str(round(lat_vals[count], 1))+"|("+str(count+1)+")")

lon_labels = []
for count in range(0,len(lon_vals)):
    lon_labels.append(str(round(lon_vals[count], 1))+"|("+str(count+1)+")")
threshold1_set = []
threshold2_set = []

point_x = []
point_y = []
values = []

count_x = 0
while count_x <= 9:
    count_y = 0
    while count_y <= 9:

        point_y.append(lon_vals[count_x])
        point_x.append(lat_vals[count_y])
        values.append(matrix[count_x][count_y])
        count_y += 1
    count_x += 1



import numpy as np
from scipy.interpolate import griddata
# Create a grid for the data
#xi, yi = np.meshgrid(np.linspace(0,10,10), np.linspace(0,10,10))
#zi = griddata((point_x, point_y), values, (xi, yi), method='cubic')

fig, ax = plt.subplots()
scatter = ax.scatter(point_x, point_y,  c= values,cmap='coolwarm')
#kw = dict(prop="colors", num=10,   fmt="{x:.2f}",
#          func=lambda s: s/100)
#legend2 = ax.legend(*scatter.legend_elements(**kw),
#                    loc='best', bbox_to_anchor=(1.01, 1), title="Interestingness")
#cbar = plt.colorbar(mappable = scatter, ticks = [0,1])
#cbar.ax.set_yticklabels(['0.05','0.10','0.15','0.20','0.25','0.30','0.35','0.40'],fontsize=18)
#cbar.set_label(label=Z_Label, size=28)
#ax.set_xlabel(X_label,size=22)
#ax.set_ylabel(Y_label,size=22)
#ax.tick_params(axis='both', which='major', labelsize=18)
#ax.pcolormesh(xi, yi, zi, cmap='coolwarm', linewidth=0.5, alpha=0.1)
ax.grid(True, linewidth=1, color='gray', alpha=0.5)
ax.grid(True, linewidth=1, color='gray', alpha=0.5, which='major', axis='both', linestyle='-')
ax.set_xticks(lat_vals, rotation=90)
ax.set_xticklabels(lat_labels,rotation=90)
ax.set_yticks(lon_vals)
ax.set_yticklabels(lon_labels)
# Add legend
cbar = plt.colorbar(mappable = scatter, ticks = [0,1])
cbar.set_ticklabels(["$<t$", "$\geq t$"])
ax.set_xlabel('Latitude|(Index)')
ax.set_ylabel('Longitude|(Index)')
#plt.legend(['Points'])
plt.show()