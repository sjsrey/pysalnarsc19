n = len(lats)
northern = [i for i in range(n) if i not in southern]
west_max = 0.0
west_id = None
for i in northern:
    lon_i = lons[i]
    if lon_i < west_max:
        west_max = lon_i
        west_id = i
print(newlines[1:][west_id])
