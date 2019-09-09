n = len(lats)
west_max = 0.0
west_id = None
for i in southern:
    lon_i = lons[i]
    if lon_i < west_max:
        west_max = lon_i
        west_id = i
print(newlines[1:][west_id])
