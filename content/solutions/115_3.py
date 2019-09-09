%%time
points = list(zip(lon, lat))

import pysal

tree = pysal.lib.cg.kdtree.KDTree(points, distance_metric='Arc',
                          radius=pysal.lib.cg.RADIUS_EARTH_MILES)

dists, ids = tree.query(points, 2)
id_mnn = numpy.argmax(dists[:,1])
print(data[id_mnn+1])
print('nndist: ', dists[id_mnn,1])
