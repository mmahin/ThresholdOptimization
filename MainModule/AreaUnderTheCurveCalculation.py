import pandas as pd
from SamplePointGenerationModule.GridHandler import GridGenerator



#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidUnemployment.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidTemperature.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidPrecipitation.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidPoverty.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidPopulation.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidMedianIncome.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidHousehold.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidEmplTransportation.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidEmplService.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidEmplMining.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidEmplManufacturing.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidEmplInformation.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidEmplGovernment.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidEmplFire.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidEmplConstruction.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidEmplAgriculture.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidDeath.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidBachelor.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidEmplTrade.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedWithTwoThresholdBachlorIncome.csv")

#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/TwoThresholdsTwolimit/agreementTwoAreaRestrictedWithTwoThresholdBachelorIncome-5-0.csv")

#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/TwoThresholdsTwolimit/agreementTwoAreaRestrictedWithTwoThresholdBachelorEmplService-50-0.csv")#
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/TwoThresholdsTwolimit/agreementTwoAreaRestrictedWithTwoThresholdBachelorEmplFire-50-0.csv")
#df = pd.read_csv(
#    "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/TwoThresholdsTwolimit/agreementTwoAreaRestrictedWithTwoThresholdUmemploymentPovert-50-0.csv")
#df = pd.read_csv(
#    "/Agreements/TwoThresholdsTwolimit/agreementTwoAreaRestrictedWithTwoThresholdBachlorIncome.csv")
files = ["agreementTwoAreaRestrictedWithTwoThresholdBachelorEmplFire-50-10.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdBachelorEmplService-50-10.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdBachlorIncome.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidBachlor.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidDeath.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidEmplAgriculture.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidEmplConstruction.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidEmplFire.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidEmplInformation.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidEmplMining.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidEmplService.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidEmplTrade.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidEmplTransportation.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidIncome.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidPoverty.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidPrecipitation.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidTemperature.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidTEmplGovernment.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidTEmplManufacturing.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidUnemployment.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdUmemploymentPovert-50-10.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdIncomePoverty-50-10.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdBachelorPoverty-50-10.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidHousehold.csv",
         "agreementTwoAreaRestrictedWithTwoThresholdCovidPopulation.csv"]

var1_mins = [0, 0, 0, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
             0.03, 0.03, 0.03, 0.03, 1, 22679, 0, 0.03, 0.03]
var1_maxs = [78, 78, 78, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32,
             1.32, 1.32, 1.32, 1.32, 18, 136191, 78, 1.32, 1.32]
var2_mins = [0, 5, 22679, 0, 0, 0, 0, 0, 0, 0, 5, 1, 2, 22679, 3, 0, 34, 0, 0, 1, 3, 3, 3, 0, 0]
var2_maxs = [21, 82, 136191, 78, 0.012, 60, 22, 21, 17, 42, 82, 35, 24, 136191, 56, 6, 78, 32, 50, 18,
             56, 56, 56, 37106, 69468]
for count in range(len(files)):
    print("\n", files[count], "\n")
    path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/TwoThresholdsTwolimit/" + \
           files[count]
    df = pd.read_csv(path)
    minx = var1_mins[count]
    maxx = var1_maxs[count]
    miny = var2_mins[count]
    maxy = var2_maxs[count]
    matrix = []
    for i in range(len(df['List'])):
        strings = ((df['List'][i].replace("[", "")).replace("]", "")).split(",")
        values = []
        for item in strings:
            values.append(float(item))
        matrix.append(values)

    matrix2 = []

    for item in matrix:

        count = 0
        for i in range(len(item), 100):
            item.insert(count, 0)
            count += 1
        matrix2.append(item)
    count = 0

    for i in range(len(matrix), 100):
        vec = [0]*len(matrix2[0])
        matrix2.insert(count,vec)
        count += 1
    total_sum = 0
    loc_x = 0
    loc_y = 0
    count_x = 0

    max_val = 0
    for item in matrix2:
        count_y = 0
        for element in item:
            if element > 0:
                total_sum += element
                if element > max_val:
                    max_val = element
                    loc_x = count_x
                    loc_y = count_y
            count_y += 1
        count_x += 1

    print("Area Under The Curve for Whole SPace:",round(total_sum/10000,6))

    total_sum2 = 0
    count = 0
    for item in matrix:
        for element in item:
            if element >= 0:
                total_sum2 += element
                count += 1
    print("Area Under The Curve for restricted Space:",round(total_sum2/count,6))
    mat = matrix2
    print(len(matrix2),len(matrix2[0]))
    x_axis_size = 100
    y_axis_size = 100
    threshold = 0.001




    grid, grid_matrix = GridGenerator(minx, maxx, miny, maxy, x_axis_size, y_axis_size)

    total_sum2 = 0
    count = 0
    count_x = 0
    xs = []
    ys = []
    for item in matrix2:
        count_y = 0
        for element in item:
            if element > 0:
                xs.append((grid_matrix[count_x ][count_y]).x)
                ys.append((grid_matrix[count_x ][count_y ]).y)
                if count_x == loc_x and count_y == loc_y:
                    print("maximas",(grid_matrix[count_x ][count_y]).x, (grid_matrix[count_x ][count_y]).y,max_val)
                total_sum2 += element
                count += 1
            count_y += 1
        count_x += 1
    print("Biggher boundary", round(total_sum2/count,3),round(min(xs),4),round(max(xs),4),round(min(ys),4),round(max(ys),4))