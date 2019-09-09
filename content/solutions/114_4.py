n = len(lats)
north_max = 0.0
north_id = None
for i in range(n):
    if lons[i] > 0.0:
        if lats[i] > north_max:
            north_max = lats[i]
            north_id = i
print(newlines[1:][north_id])
