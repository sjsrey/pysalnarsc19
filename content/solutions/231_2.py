fig, axs = plt.subplots(1,2, figsize=(20,10))

# use gdf.plot() to create regular choropleth
tx.plot(column='HR70', scheme='quantiles', cmap='RdBu', ax=axs[0])

x = tx['HR70']
y = tx['GI69']
# use vba_choropleth to create Value-by-Alpha Choropleth
vba_choropleth(x, y, tx, rgb_mapclassify=dict(classifier='quantiles'),
               alpha_mapclassify=dict(classifier='quantiles'),
               cmap='RdBu', ax=axs[1])

# set figure style
axs[0].set_title('normal Choropleth HR70')
axs[0].set_axis_off()
axs[1].set_title('Value-by-Alpha Choropleth HR70 and GI69')

# plot
plt.show()


