import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
def PointAndValueVisualizer(point_x,point_y, Values, X_label,Y_label,Z_Label):

    values_upscaled = []
    for item in Values:
        values_upscaled.append(item*1000)
    fig, ax = plt.subplots()

    scatter = ax.scatter(point_x, point_y, s=values_upscaled, marker='o', c= values_upscaled, alpha=1)
    kw = dict(prop="colors", num=10,   fmt="{x:.2f}",
              func=lambda s: s/100)
    #legend2 = ax.legend(*scatter.legend_elements(**kw),
    #                    loc='best', bbox_to_anchor=(1.01, 1), title="Interestingness")
    cbar = plt.colorbar(mappable = scatter, ticks = [50,100,150,200,250,300,350,400])
    cbar.ax.set_yticklabels(['0.05','0.10','0.15','0.20','0.25','0.30','0.35','0.40'],fontsize=18)
    cbar.set_label(label=Z_Label, size=28)
    ax.set_xlabel(X_label,size=22)
    ax.set_ylabel(Y_label,size=22)
    ax.tick_params(axis='both', which='major', labelsize=18)
    plt.show()

def PointAndValueVisualizer2(point_x,point_y, Values, X_label,Y_label,Z_Label):

    values_upscaled = []
    for item in Values:
        values_upscaled.append((item))
    fig, ax = plt.subplots(dpi=80)

    scatter = ax.scatter(point_x, point_y, marker='o', c= 'indigo', alpha=1)
    kw = dict(prop="colors", num=10,   fmt="{x:.2f}",
              func=lambda s: (s/100))
    #legend2 = ax.legend(*scatter.legend_elements(**kw),
    #                    loc='best', bbox_to_anchor=(1.01, 1), title=Z_Label)
    #legend2.set_horizontalalignment('left')
    cbar = plt.colorbar(mappable=scatter, ticks=[0.000])
    cbar.ax.set_yticklabels(['0'], fontsize=22)
    cbar.set_label(label=Z_Label, size=32)
    ax.set_xlabel(X_label,size=26)
    ax.set_ylabel(Y_label,size=26)
    ax.tick_params(axis='both', which='major', labelsize=22)
    plt.show()
'''
import pandas as pd
df = pd.read_csv("C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/GradientSearch/maximasMedianIncomeCoid_100_100.csv")
X_label = 'Covid-19 Infection Rate (t)'
Y_label = 'Median Income(t\')'
Z_Label = '$I_{(Covid-19\ Infection\ Rate , t),(Median\ Income, t\'))}$'
PointAndValueVisualizer(df['t1'],df['t2'],df['I'], X_label,Y_label,Z_Label)
#, label= ["0.05","0.1","0.15","0.20","0.25","0.30","0.35","0.40"]
'''
import geopandas as gpd
from SamplePointGenerationModule.GridHandler import GridGenerator
from AgreementFunction.PolygonAreaCalculation import PolygonArea
from VisualizationModules.HotspotsVisualization import HotspotsVisualiztion
from shapely.ops import unary_union
from SubModules.ObtainVariableDataframesAndStateDictionary import getVariableDataframesAndSpatialIndexes
from SubModules.AssignValuesToGridUsingPointWiseFunctions import AssignValuesToGridUsingPointWiseFunctions
from SubModules.VisualizeTwoVariableInterestingnessSearchSpace import VisualizeTwoVariableInterestingnessSearchSpace
from SubModules.AgreementValueWithTwoAreaConstraintsGeneratorForTwoThresholds import AgreementValueWithTwoAreaConstraintGeneratorForTwoThresholds
from SubModules.AssignValuesToGridUsingPointWiseFunctionWithSpatialIndex import AssignValuesToGridUsingPointWiseFunctionsWithSpatialIndex
from GradientSearch.GradientAscent import gradientAscentForNpoints
data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

#Set Inputs
#data access inputs
variable1_name = 'covid_cases_density'
variable2_name = 'medianHouseHoldIncome'

variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
X_label = 'Covid-19 Infection Rate (t)'
Y_label = 'Median Income(t\')'
Z_Label = '$I_{(Covid-19\ Infection\ Rate , t),(Median\ Income, t\'))}$'
# Grid generation Inputs
grid_row_size = 100
grid_column_size = 100

learning_rate = .1
maximum_iteration = 2000
# Agreement Generation Inputs
step1 = 100
step2 = 100
target_threshold1 = 10
target_threshold2 = 10
hotspot_area_restriction = 0.5

target_threshold1_start = 0.21
target_threshold1_end = 0.45
target_threshold1_cutpoint = (target_threshold1_end - target_threshold1_start )/target_threshold1

target_threshold2_start = 40000
target_threshold2_end = 90000
target_threshold2_cutpoint = (target_threshold2_end - target_threshold2_start )/target_threshold2
threshold1_set = []
threshold2_set = []

point_x = []
point_y = []
values = []

t1 = target_threshold1_start
while t1 <= target_threshold1_end:

    t2 = target_threshold2_start
    while t2 <= target_threshold2_end :
        threshold1_set.append(t1)
        threshold2_set.append(t2)

        t2 += target_threshold2_cutpoint
        point_x.append(t1)
        point_y.append(t2)
        values.append(0)
    t1 += target_threshold1_cutpoint
print(len(point_x),len(point_y))
from PointAndValueVisualizer import PointAndValueVisualizer
PointAndValueVisualizer2(point_x,point_y,values, X_label,Y_label,Z_Label)
