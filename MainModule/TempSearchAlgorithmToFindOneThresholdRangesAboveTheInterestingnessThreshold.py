import pandas as pd

interestingness_df = pd.read_csv("C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/"
                                 "MainModule/Covid-19_median_income_agreements_one_threshold.csv")

thresholds = interestingness_df['thresholds']
agreements = interestingness_df['agreements']
from SubModules.VisualizeOneVariableInterestingnessSearchSpace import VisualizeOneVariableInterestingnessSearchSpace
X_label = 'Median Income(t\')'
Y_label = '$I_{(Covid-19\ Infection\ Rate, 0.3),(Median\ Income, t\'))}$'
VisualizeOneVariableInterestingnessSearchSpace(thresholds, agreements, X_label, Y_label)
inner_ranges = []
max_threshold = max(thresholds)
min_threshold = min(thresholds)
ascending_point = float('-inf')
descending_point = float('-inf')
w = 0.115
for count in range(len(agreements)):
    if agreements[count] >= w and ascending_point == float('-inf'):
        ascending_point = thresholds[count]

    if agreements[count] <= w and ascending_point != float('-inf'):
        descending_point = thresholds[count]
        inner_ranges.append([ascending_point,descending_point])
        ascending_point = float('-inf')
        descending_point = float('-inf')

if ascending_point != float('-inf') and descending_point == float('-inf'):
    descending_point = thresholds[len(agreements)-1]
    inner_ranges.append([ascending_point, descending_point])

print(inner_ranges)