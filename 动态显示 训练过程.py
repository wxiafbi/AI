import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from tqdm import tqdm


# 准备训练数据集
X_train = np.array([[1, 2], [2, 3], [3, 3], [2, 1], [3, 2], [1, 3]])
y_train = np.array([0, 0, 0, 1, 1, 1])

# 构建神经网络模型
model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 编译模型
model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.01))

# 训练模型并动态显示训练过程
for epoch in tqdm(range(50)):
    model.fit(X_train, y_train, epochs=1, verbose=0)
    loss = model.evaluate(X_train, y_train, verbose=0)
    tqdm.write("Epoch {}: loss = {:.4f}".format(epoch + 1, loss))