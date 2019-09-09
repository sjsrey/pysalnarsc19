import numpy
numpy.random.seed(1234)
lisa = esda.Moran_Local(df["median_pri"], wq)
f, axs = plt.subplots(1, 3, figsize=(16, 3))
for i, ax in zip([0.05, 0.01, 0.001], axs):
    esdaplot.lisa_cluster(lisa, df, p=i, ax=ax)
    ax.set_title(f"Significance level = {i}")

wr = lp.weights.Rook.from_dataframe(df)
lisa_r = esda.Moran_Local(df["median_pri"], wr)
f, axs = plt.subplots(1, 3, figsize=(16, 3))
for i, ax in zip([0.05, 0.01, 0.001], axs):
    esdaplot.lisa_cluster(lisa_r, df, p=i, ax=ax)
    ax.set_title(f"Significance level = {i}")
    
w4 = lp.weights.distance.KNN.from_dataframe(df, k=4)
lisa_4 = esda.Moran_Local(df["median_pri"], w4)
f, axs = plt.subplots(1, 3, figsize=(16, 3))
for i, ax in zip([0.05, 0.01, 0.001], axs):
    esdaplot.lisa_cluster(lisa_4, df, p=i, ax=ax)
    ax.set_title(f"Significance level = {i}")
