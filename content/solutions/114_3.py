n = len(lats)
south_min = 0.0
south_id = None
for i in range(n):
    if lons[i] < 0.0:
        if lats[i] < south_min:
            south_min = lats[i]
            south_id = i
print(newlines[1:][south_id])
