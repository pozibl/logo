"""
Code to create the logo for pozibl


We want to create a recursive square.


Starting with a example coordinate sequence like

coords = [[0,0], [0,100], [100,100], [100,0], [2,2], [2,98], [98,98], [98,2], [4,4]]

It wasn't initially clear how to do this.

So start by making a few loops and adjusting till we get something similar
"""

from shapely.geometry import LineString, Polygon
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely import box


def main():
    coords_gen = []
    size = 100
    for i in range(size):
        if not i % 10:
            coords_gen.append([i, i])
            coords_gen.append([i, size - i])
            coords_gen.append([size - i, size - i])
            coords_gen.append([size - i, i])

    line = LineString(coords_gen)

    p = gpd.GeoSeries([LineString(coords_gen[0:i + 1]) for i in range(1, len(coords_gen) - 1)])

    for i, l in enumerate(p):
        ls = gpd.GeoSeries(l)

        fig = ls.plot(color='black')
        ax = fig.set_xlim(-50, 150)
        ax = fig.set_ylim(-50, 150)
        plt.axis('off')
        plt.savefig(f"logo_white{i:>02}.jpg", transparent=True)

        ax = ls.plot(color='white')
        xMin, yMin, xMax, yMax = ls.total_bounds
        bbox = gpd.GeoDataFrame(geometry=[box(xMin-50, yMin-50, xMax+50, yMax+50)], crs=ls.crs)
        fig = bbox.plot(ax=ax, color="black", zorder=0)
        fig.set_facecolor('red')
        plt.axis('off')
        plt.savefig(f"logo_black{i:>02}.jpg", transparent=False)



if __name__ == '__main__':
	main()
