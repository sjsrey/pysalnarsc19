rel_pov = df.poverty_x / df.poverty_ward
df['rel_pov'] = rel_pov
df.loc[df['rel_pov'].idxmax()]
