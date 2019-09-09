%%time
points = list(zip(lat, lon))

max_nnd = 0.0
isolated = None
for i, point in enumerate(points):
    j, nnd = nearest_airport(i, points)
    if nnd > max_nnd:
        isolated = i
        neighbor = j
        max_nnd = nnd

print("The most isolated airport is:")
print(data[isolated+1])
print("Its nearest neighbor is:")
print(data[neighbor+1])
print('and the distance separating them is:', max_nnd)
