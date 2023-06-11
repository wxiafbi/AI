import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import matplotlib.pyplot as plt

# 准备训练数据集
X_train = np.array([[1, 2], [2, 3], [3, 3], [2, 1], [3, 2], [1, 3]])
y_train = np.array([0, 0, 0, 1, 1, 1])

# 构建神经网络模型
model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 编译模型
model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.01))

# 训练模型并保存训练历史
history = model.fit(X_train, y_train, epochs=50, verbose=0)

# 绘制训练历史曲线
print(history.history['loss'])
print(type(history.history['loss']))
plt.plot(history.history['loss'])
plt.plot(X_train, y_train, 'bo')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()
