import numpy as np

#1
array = np.array([1, 2, 3, 4, 5])
#2
big_array = np.random.rand(1000)
#.1
print("ອາເລ", array)
print("ຜົນລວມ", np.sum(array))
print("ຄ່າສູງສຸດ", np.max(array))
print("ຄ່າໜ້ອຍສຸດ", np.min(array))
print("ຄ່າສະເລ່ຍ", np.mean(array))
#.2
print("ຂະໜາດອາເລ(ເມກະໄບ):", big_array.nbytes/ 1e6)
print("ຂະໜາດອາເລ(ເມກະໄບ):", big_array)
#data = np.loadtxt("data.text")
#np.savetxt("result.txt", array, delimiter=",")