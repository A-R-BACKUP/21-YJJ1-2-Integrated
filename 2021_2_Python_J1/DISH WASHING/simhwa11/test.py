import numpy as np          # 난수생성기 호출을 위해 numpy import
import matplotlib.pyplot as plt         # 그래프 작성을 위한 matplotlib import

# rigX = 25 + 6 * np.random.randn(1000, 1)
# rigY = (25 + 6 * np.random.randn(1000, 1)) + np.random.randn(1000, 1)
#
# print(rigX)
# print('------------------')
# print(rigY)
test_a = np.array([4, 9], np.float)
test_b = np.array([2, 2], np.float)

print(test_a + test_b)
print(test_a - test_b)
print(test_a * test_b)
print(test_a / test_b)