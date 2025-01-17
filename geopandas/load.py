import os
import timeit
import geopandas
import pandas as pd

wd = os.getcwd()
vec = os.path.join(wd, "data", "points.gpkg")

t_list = [None] * 10
for i in range(10):
    tic = timeit.default_timer()

    gdf = geopandas.read_file(vec)

    toc = timeit.default_timer()
    t_list[i] = round(toc - tic, 2)
    
df = {'task': ['load'] * 10, 'package': ['geopandas'] * 10, 'time': t_list}
df = pd.DataFrame.from_dict(df)
if not os.path.isdir('results'): os.mkdir('results')
savepath = os.path.join('results', 'load-geopandas.csv')
df.to_csv(savepath, index = False, decimal = ',', sep = ';')
