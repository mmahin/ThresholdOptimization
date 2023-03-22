import matplotlib.pyplot as plt
from SubModules.ObtainVariableDataframesAndStateDictionary import getVariableDataframesAndSpatialIndexes
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D

data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

# Bachelor

variable1_name = 'covid_cases_density'
variable2_name = 'bachelor_degree_density_2014_2018'
X_label1 = 'COVID-19 Infection Rate\n Thresholds(t)'
Y_label1 = 'Bachelor Degree Rate\n Thresholds(t\')'
Z_Label1 = 'I({(COVID-19 Infection Rate, t),\n(Bachelor Degree Rate, t\'))})'
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
# Agreement Generation Inputs
steps = 100

# Create thresholds min and gradient
max_variable2 = 65#max(variable2_df['values'])#60#100000#
min_variable2= min(variable2_df['values'])#15#40000#
variable_cutpoint_variable2= (max_variable2 - min_variable2)/steps

max_variable1 = 0.45#max(variable1_df['values'])#0.45#
min_variable1 =  min(variable1_df['values'])#0.15#
variable_cutpoint_variable1 = (max_variable1 - min_variable1)/steps
print(max_variable2, min_variable2, max_variable1, min_variable1)

variable1_thresholds = []
variable2_thresholds = []
variable1_threshold = min_variable1
variable2_threshold = min_variable2
for i in range(steps):
    variable1_thresholds.append(variable1_threshold)
    variable2_thresholds.append(variable2_threshold)
    variable1_threshold += variable_cutpoint_variable1
    variable2_threshold += variable_cutpoint_variable2
print(variable1_thresholds)
print(variable2_thresholds)
Y1, X1 = np.meshgrid(variable2_thresholds, variable1_thresholds)
print(X1,Y1)
path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/TKDE/Agreements/Files/agreementNoAreaRestrictedWithTwoThresholdCovidBachelor.csv"
df = pd.read_csv(path)
data = []
for i in range(len(df['List'])):
    strings = ((df['List'][i].replace("[", "")).replace("]", "")).split(",")
    values = []
    for item in strings:
        values.append(float(item))
    data.append(values)
Z1 = data


path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/TKDE/Agreements/Files/agreementTwoAreaRestrictedWithTwoThresholdCovidBachelor.csv"
df = pd.read_csv(path)
data = []
for i in range(len(df['List'])):
    strings = ((df['List'][i].replace("[", "")).replace("]", "")).split(",")
    values = []
    for item in strings:
        values.append(float(item))
    data.append(values)
Z2 = data

variable3_name = 'covid_cases_density'
variable4_name = 'medianHouseHoldIncome'
X_label2 = 'COVID-19 Infection Rate\n  Thresholds(t)'
Y_label2 = 'Median Income \n Thresholds(t\')'
Z_Label2 = 'I({(COVID-19 Infection Rate, t),\n(Median Income, t\'))})'
variable3_df, variable4_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable3_name, variable4_name)
# Agreement Generation Inputs
steps = 100

# Create thresholds min and gradient
max_variable4 = 100000#max(variable2_df['values'])#60#100000#
min_variable4= min(variable4_df['values'])#15#40000#
variable_cutpoint_variable4= (max_variable4 - min_variable4)/steps

max_variable3 = 0.5#max(variable1_df['values'])#0.45#
min_variable3 =  min(variable3_df['values'])#0.15#
variable_cutpoint_variable3 = (max_variable3 - min_variable3)/steps


variable3_thresholds = []
variable4_thresholds = []
variable3_threshold = min_variable3
variable4_threshold = min_variable4
for i in range(steps):
    variable3_thresholds.append(variable3_threshold)
    variable4_thresholds.append(variable4_threshold)
    variable3_threshold += variable_cutpoint_variable3
    variable4_threshold += variable_cutpoint_variable4

Y2, X2 = np.meshgrid(variable4_thresholds, variable3_thresholds)
path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/TKDE/Agreements/Files/agreementNoAreaRestrictedWithTwoThresholdCovidIncome.csv"
df = pd.read_csv(path)
data = []
for i in range(len(df['List'])):
    strings = ((df['List'][i].replace("[", "")).replace("]", "")).split(",")
    values = []
    for item in strings:
        values.append(float(item))
    data.append(values)
Z3 = data


path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/TKDE/Agreements/Files/agreementTwoAreaRestrictedWithTwoThresholdCovidIncome.csv"
df = pd.read_csv(path)
data = []
for i in range(len(df['List'])):
    strings = ((df['List'][i].replace("[", "")).replace("]", "")).split(",")
    values = []
    for item in strings:
        values.append(float(item))
    data.append(values)
Z4 = data



import matplotlib.transforms as mtransforms
fig = plt.figure(figsize=plt.figaspect(0.25), constrained_layout=True)
import matplotlib as mpl
ax = fig.add_subplot(1, 2, 1, projection='3d')

mappable = plt.cm.ScalarMappable(cmap=plt.cm.viridis)
mappable.set_array(Z1)
mappable.set_clim(0, 1)
surf1 = ax.plot_surface(X1, Y1, np.array(Z1), cmap='Spectral', norm=mappable.norm, linewidth=0,
                 antialiased=False, cstride=10, rstride=1, alpha=0.5)

from scipy.spatial import ConvexHull
verts = []
x = []
y = []
z = []
for countx in range(len(X2[0])):
    for county in range(len(Y2)):
        if Z2[countx][county] >= 0:
            verts.append([round(X1[countx][0],3),round(Y1[0][county],3),round(Z3[countx][county],3)])
            x.append(round(X1[countx][0],3))
            y.append(round(Y1[0][county],3))
            z.append(round(Z2[countx][county],3))

#print(verts)
#hull = ConvexHull(np.array(verts))
#faces = hull.simplices

#face_indices = []

#face_indices.append([verts.index(tuple(v)) for v in faces])
#verts = [(X2.min(), Y2.min(), 0), (X2.max(), Y2.min(), 0), (X2.max(), Y2.max(), 0), (X2.min(), Y2.max(), 0)]
#poly = Poly3DCollection([verts], alpha=1, facecolor='r')
# Add the polygonal patch to the plot
#ax.add_collection3d(poly)
ax.scatter(x, y, z, c='midnightblue', marker='o',alpha=1, zorder=20)

ax.set_xlabel(X_label1)
ax.set_ylabel(Y_label1)
ax.set_zlabel(Z_Label1)
#ax.view_init(elev=30, azim=120)
ax.set_zlim(0, 1)
ax.set_title("a", fontfamily='serif', loc='left', fontsize='medium')

ax = fig.add_subplot(1, 2, 2, projection='3d')
surf2 = ax.plot_surface(X2, Y2, np.array(Z3), cmap='Spectral', norm=mappable.norm, linewidth=0,
                 antialiased=False, cstride=10, rstride=1, alpha=0.5)

verts = []
x = []
y = []
z = []
for countx in range(len(X2[0])):
    for county in range(len(Y2)):
        if Z2[countx][county] >= 0:
            verts.append([round(X2[countx][0],3),round(Y2[0][county],3),round(Z4[countx][county],3)])
            x.append(round(X2[countx][0],3))
            y.append(round(Y2[0][county],3))
            z.append(round(Z4[countx][county],3))
ax.scatter(x, y, z, c='midnightblue', marker='o',alpha=1, zorder=20)
# Set the tick parameters
ax.tick_params(axis='both', which='major', pad=-1)
ax.set_xlabel(X_label2)
ax.set_ylabel(Y_label2)
ax.set_zlabel(Z_Label2)
ax.set_zlim(0, 1)
ax.set_title("b", fontfamily='serif', loc='left', fontsize='medium')

box = ax.get_position()
box.x0 = box.x0 + 0.125
box.x1 = box.x1 + 0.125
ax.set_position(box)

#fig.colorbar(surf, shrink=0.5, aspect=5)
# ax.set_title('Variables Thresholds vs Agreement Values');

cbar_ax = fig.add_axes([0.85, 0.2, 0.025, 0.7])
fig.colorbar(surf1, cax=cbar_ax)
#fig.colorbar(surf1, orientation="horizontal", shrink=0.5, aspect=5)
fig.tight_layout(pad=1)
plt.show()