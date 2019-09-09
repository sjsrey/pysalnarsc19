bad_ids = []
for idx in knn4:
    #print(idx)
    i , weights = idx
    if knn4[i] != knn4_bad[i]:
        bad_ids.append(i)
print('There are: {} bad neighbor sets'.format(len(bad_ids)))
print(bad_ids)
