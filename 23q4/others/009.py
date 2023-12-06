import numpy as np
import matplotlib.pyplot as plt

N = int(1e4);
D = 2
X = np.random.randn(N, D)
plt.plot(X[:, 0], X[:, 1], '.')
plt.axis('square')
plt.show()
