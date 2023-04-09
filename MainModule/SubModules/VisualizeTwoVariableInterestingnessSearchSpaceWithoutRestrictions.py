import numpy as np
import matplotlib.pyplot as plt

def VisualizeTwoVariableInterestingnessSearchSpaceWithoutRestriction(min_variable1,max_variable1, min_variable2, max_variable2, steps, agreements, X_label, Y_label, Z_Label):
    x = np.linspace(min_variable1, max_variable1, steps)
    y = np.linspace(min_variable2, max_variable2, steps)
    Y, X = np.meshgrid(y, x)
    Z= agreements

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    print(np.shape(X),np.shape(Y),np.shape(np.array(Z)))
    mappable = plt.cm.ScalarMappable(cmap=plt.cm.viridis)
    mappable.set_array(Z)
    mappable.set_clim(0, 1)
    surf = ax.plot_surface(X, Y, np.array(Z), cmap='Spectral', norm=mappable.norm, linewidth=0,
                            antialiased=False, cstride=10, rstride=1, alpha=0.5)
    cbar_ax = fig.add_axes([0.925, 0.15, 0.025, 0.7])
    fig.colorbar(surf, cax=cbar_ax)
    ax.set_xlabel(X_label)
    ax.set_ylabel(Y_label)
    ax.set_zlabel(Z_Label)
    #ax.set_title('Variables Thresholds vs Agreement Values');
    plt.show()