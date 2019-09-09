import pandas
r8 = Rose(Y, w, k=8)
r8.plot_vectors()
r8.plot()
r8.permute()
table = pandas.DataFrame(data={'counts': r8.counts,
                              'expected': r8.expected_perm,
                              'p-value': r8.p})
table
