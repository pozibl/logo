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


def main():
    coords_gen = []
    size = 100
    for i in range(size):
        for j in range(size):
            if not i % 10 and not j % 10 and i == j :
                coords_gen.append([i, j])
        if not i % 10:
            coords_gen.append([i, size - i])
            coords_gen.append([size - i, size - i])
            coords_gen.append([size - i, i])

    line = LineString(coords_gen)

    p = gpd.GeoSeries([LineString(coords_gen[0:i + 1]) for i in range(1, len(coords_gen) - 1)])

    for i, l in enumerate(p):
        ls = gpd.GeoSeries(l)

        fig = ls.plot(color='black')
        ax = fig.set_xlim(0, 100)
        ax = fig.set_ylim(0, 100)
        plt.axis('off')
        plt.savefig(f"logo_{i:>02}.jpg", transparent=True)



if __name__ == '__main__':
	main()
