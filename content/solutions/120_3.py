idxs = zip(min_ids, max_ids)
ratio = 0.0
ratios = []
for y, ids in enumerate(idxs):
    min_id, max_id = ids
    year = y + 1969
    name = pc_inc.loc[min_id].GeoName
    pci_min = pc_inc.loc[min_id, str(year)]
    pci_max = pc_inc.loc[max_id, str(year)]
    r = pci_max / pci_min
    ratios.append(r)
    if r > ratio:
        ratio = r
        max_year = year
print("Maximum relative gap: {} occurred in {}".format(ratio, max_year))
res_df = pandas.DataFrame({'year': range(1969, 2018), 'ratio': ratios})
res_df
