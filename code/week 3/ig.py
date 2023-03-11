pip install alibi[tensorflow]
import tensorflow as tf
from alibi.explainers import IntegratedGradients
from functools import partial



print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)


target_fn=partial(np.argmax, axis=1)

ig=IntegratedGradients(model, target_fn=target_fn)
explanations=ig.explain(arr)


attributions = explanations.attributions
ig = attributions[0]

print(arr.shape)
print(ig.shape)
print(Y.shape)

Write ig result tp file
file = open('ig_train.csv','w')
for item in predictions:
	file.write(str(item)+"\n")
file.close()

 file2 = open('ig_test.csv','w')
for item in predictions2:
	file2.write(str(item)+"\n")
 file2.close()
 
 
from numpy import asarray
from numpy import savetxt
print(ig.reshape(83*3,60))
savetxt('igdata.csv', ig.reshape(83*3,60))