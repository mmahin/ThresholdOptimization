import matplotlib.pyplot as plt

def contourPlot(data, xx,yy):
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))

    # Create an USA state map to visualize clearly the zips
    #path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ACMSIGSPATIAL2020/va_virginia_zip_codes_geo.min.json"
    #fp = path
    #map_df = gpd.read_file(fp)
    #map_df.plot(linewidth=0.8, ax=ax, edgecolor='black', facecolor="none")
    # map_df.plot(linewidth=0.8, ax=ax[1], edgecolor='black', facecolor="none")
    # map_df.plot(linewidth=0.8, ax=ax[1, 0], edgecolor='black', facecolor="none")
    # map_df.plot(linewidth=0.8, ax=ax[1, 1], edgecolor='black', facecolor="none")
    # ctx.add_basemap(ax, zoom=12)
    # Plot the zips

    cfset = ax.contourf(xx, yy, data, levels=[0, 0.8, 1.6, 2.4, 3.2], cmap='coolwarm', alpha=.7)
    cset = ax.contour(xx, yy, data, levels=[0, 0.8, 1.6, 2.4, 3.2], cmap='coolwarm', alpha=.5)
    #
    # cfset = ax[1].contourf(xx, yy, data2,  levels=[0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30], cmap='coolwarm',alpha=.7)
    # cset = ax[1].contour(xx, yy, data2,levels=[0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30], cmap='coolwarm' ,alpha=.5)
    '''
    cfset = ax[1,0].contourf(xx, yy, data3,  levels=[0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30], cmap='coolwarm',alpha=.7)
    cset = ax[1,0].contour(xx, yy, data3,levels=[0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30], cmap='coolwarm' ,alpha=.5)

    cset = ax[1,1].contourf(xx, yy, data4, cmap='coolwarm',alpha=.7)
    cset = ax[1,1].contour(xx, yy, data4,levels=[0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30], cmap='coolwarm' ,alpha=.5)
    '''
    ax.clabel(cset, inline=1, fontsize=10)
    ax.set_adjustable('box')
    ax.autoscale(True)

    # ax[1].clabel(cset, inline=1, fontsize=10)
    # ax[1].set_adjustable('box')
    # ax[1].autoscale(True)
    '''
    ax[1,0].clabel(cset, inline=1, fontsize=10)
    ax[1,0].set_adjustable('box')
    ax[1,0].autoscale(True)

    ax[1,1].clabel(cset, inline=1, fontsize=10)
    ax[1,1].set_adjustable('box')
    ax[1,1].autoscale(True)
    '''
    h1, l1 = cset.legend_elements()
    '''
    labels = []
    for item in l1:
        temp1 = item.split(" = ")
        x = temp1[1].split("$")
        g1 = float(x[0])
        g = round(g1,2)
        #temp = str(g)
        labels.append(g)
    '''
    # ax.legend(h1 , [0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35], loc='center left', bbox_to_anchor=(-0.06, 0.5))
    # ax[1].legend(h1, [0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30], loc='best', bbox_to_anchor=(-0.1, 1))
    '''
    ax[1, 0].legend(h1, [0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30], loc='best', bbox_to_anchor=(-0.1, 1))
    ax[1, 1].legend(h1, [0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30], loc='best', bbox_to_anchor=(-0.1, 1))
    '''
    # ax.set_title(str)
    ax.axis('off')
    # ax[1].set_title(str[1])
    '''
    ax[1, 0].set_title(str[0])
    ax[1, 1].set_title(str[0])
    '''
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    plt.show()