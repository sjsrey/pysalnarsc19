import matplotlib.pyplot as plt # make plot larger
fig, axs = plt.subplots(1,2, figsize=(20,10))


tx.plot(column='HR70', scheme='QUANTILES', \
        k=10, cmap='OrRd', linewidth=0.1, ax=axs[0], \
        edgecolor='white', legend=True)

tx.plot(column='HR90', scheme='QUANTILES', \
        k=10, cmap='OrRd', linewidth=0.1, ax=axs[1], \
        edgecolor='white', legend=True)
ax.set_axis_off()
plt.show()
