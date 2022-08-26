import numpy as np
import matplotlib.pyplot as plt

def VisualizeTwoVariableInterestingnessSearchSpace(threshold1_values, threshold2_values, agreements, X_label, Y_label, Z_Label):
    x = threshold1_values
    y = threshold2_values
    Y, X = np.meshgrid(y, x)
    Z= agreements

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    print(np.shape(X),np.shape(Y),np.shape(np.array(Z)))
    surf = ax.plot_surface(X, Y, np.array(Z), rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.set_xlabel(X_label)
    ax.set_ylabel(Y_label)
    ax.set_zlabel(Z_Label)
    #ax.set_title('Variables Thresholds vs Agreement Values');
    plt.show()