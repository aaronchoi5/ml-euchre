import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(style="ticks", color_codes=True)

df = pd.read_csv('training_data_180321_1522.csv')
df.info()

# new_sns = sns.load_dataset('new')
g = sns.PairGrid(df, x_vars=['TRUMP','SUM_D','SUM_H','SUM_C','SUM_S'],y_vars=['TRUMP','SUM_D','SUM_H','SUM_C','SUM_S'])

g = g.map_upper(plt.scatter)
g = g.map_lower(sns.kdeplot, cmap="Blues_d")
g = g.map_diag(sns.kdeplot, lw=3, legend=False)
g.savefig("output.png")
