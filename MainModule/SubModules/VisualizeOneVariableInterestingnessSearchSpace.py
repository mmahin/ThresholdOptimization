import numpy as np
import matplotlib.pyplot as plt

def VisualizeOneVariableInterestingnessSearchSpace(threshold2_values, agreements, X_label, Y_label):
    plt.plot(threshold2_values, agreements)
    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    plt.show()