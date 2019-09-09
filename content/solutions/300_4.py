identical = [i for i, rWi in rW if rWi == qW[i]]
print('{} observation(s) with identical neighbors under Q and R:'.format(len(identical)))
for idx in identical:
    print(idx, rW[idx], qW[idx])
