import cv2
import tensorflow as tf
import numpy as np

def create_cnn_model(input_shape):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

image = cv2.imread('grey.png')
duplicate = cv2.imread('grey.png')
image = np.array(image)
m=len(image)
n=len(image[0])
o=len(image[0][0])

def gaussian(sigma, size):
    kernel=[]
    for i in range(size):
        array=[]
        for j in range(size):
            array.append(0)
        kernel.append(array)
    count=0
    for i in range(size):
        for j in range(size):
            x=i-size//2
            y=j-size//2
            kernel[i][j]=np.exp(-(x**2+y**2)/2*sigma**2)/(2*3.14*sigma**2)
            count+=kernel[i][j]
    for i in range(size):
        for j in range(size):
            kernel[i][j]/=count
    return np.array(kernel)

def get(i, j):
    if i<0 or j<0 or i>=m or j>=n:
        return 0
    return image[i][j][0]

def compareML(p, q, neighbour):
    if q[0]<0 or q[1]<0 or q[0]>=m or q[1]>=n:
        return 0
    matrix1=[]
    for i in range(-neighbour, neighbour+1):
        array=[]
        for j in range(-neighbour, neighbour+1):
            array.append(get(p[0]+i, p[1]+j))
        matrix1.append(array)
    matrix2=[]
    for i in range(-neighbour, neighbour+1):
        array=[]
        for j in range(-neighbour, neighbour+1):
            array.append(get(q[0]+i, q[1]+j))
        matrix2.append(array)
    matrix1=np.array(matrix1)
    matrix2=np.array(matrix2)
    input_shape = (matrix1.shape[0], matrix1.shape[1], 1)
    model = create_cnn_model(input_shape)
    similarity_score = model.predict(np.array([matrix1, matrix2]))
    return similarity_score[0][0]

def compare(p, q, kernel, neighbour):
    if q[0]<0 or q[1]<0 or q[0]>=m or q[1]>=n:
        return 0
    count=0
    for i in range(-neighbour, neighbour+1):
        for j in range(-neighbour, neighbour+1):
            count+=kernel[i+neighbour][j+neighbour]*np.abs(get(p[0]+i, p[1]+j)-get(q[0]+i, q[1]+j))
    return count

def nonLocal(neighbour, search, smoothing, sigma, machineLearning):
    kernel=gaussian(sigma, 2*neighbour+1)
    for i in range(m):
        for j in range(n):
            value=0
            denominator=0
            for a in range(i-search, i+search+1):
                for b in range(j-search, j+search+1):
                    if machineLearning==0:
                        result=compare([i, j], [a, b], kernel, neighbour)
                    else:
                        result=compareML([i, j], [a, b], kernel, neighbour)
                    denominator+=np.exp(-result**2/smoothing**2)
                    value+=get(a, b)*np.exp(-result**2/smoothing**2)
            duplicate[i][j][0]=value/denominator
            duplicate[i][j][1]=value/denominator
            duplicate[i][j][2]=value/denominator

nonLocal(1, 5, 2, 1, 0)
cv2.imwrite("enhanced1.png", duplicate)
nonLocal(1, 5, 2, 1, 1)
cv2.imwrite("enhanced2.png", duplicate)