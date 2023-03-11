def row(before):
  kernel = np.ones(5)/5
  after = np.convolve(before,kernel,mode="same")
  return after


def country(before):
  after = np.empty((3,60))
  for i in range(3):
    after[i,0:60] = row(before[i])
  return after



xavg = np.empty((83,3,60))
yavg = np.empty((83,1,60))
igavg = np.empty((83,3,60))

for i in range(83):
  xavg[i,0:3,0:83] = country(arr[i])

for i in range(83):
  igavg[i,0:3,0:83] = country(ig[i])


for i in range(83):
  yavg[i,0:1,0:83] = row(np.squeeze(Y[i]))


xavg = xavg.reshape(83,60,3)
yavg = yavg.reshape(83,60,1)
igavg = igavg.reshape(83,60,3)


x_per_year = np.hsplit(xavg,60)
y_per_year = np.hsplit(yavg,60)
ig_per_year = np.hsplit(igavg,60)


for i in range(60):
  x_per_year[i] = x_per_year[i].reshape(83,3)
  y_per_year[i] = y_per_year[i].reshape(83,1)
  ig_per_year[i] = ig_per_year[i].reshape(83,3)


combine = np.empty((83*60,7))
for i in range(60):
  data_per_year = np.array(np.concatenate((np.stack((x_per_year[i],ig_per_year[i]),axis=2).reshape(83,6),y_per_year[i]),axis=1))
  for j in range(83):
    combine[i*83+j,0:7] = data_per_year[j]

print(combine[0])


savetxt('combinedata.csv', combine)