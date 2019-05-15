from keras.activations import relu
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.contrib.slim.python.slim.data import dataset

model = Sequential()
model.add(Convolution2D(filters = 32, kernel_size = (3, 3),input_shape = (64, 64, 3),activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Convolution2D(32, 3, 3, activation= 'relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(units = 128, activation = 'relu'))
model.add(Dense(units=1, activation= 'sigmoid'))
model.compile(optimizer = 'adam', loss = 'binary_crossentropy',metrics = ['accuracy'])

train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   shear_range=0.1,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

training_set = train_datagen.flow_from_directory('E://personal//data_science//dataset//ocr//Dataset//training',target_size = (64, 64), batch_size = 32,class_mode = 'binary')
test_set = test_datagen.flow_from_directory('E://personal//data_science//dataset//ocr//Dataset//testing', target_size = (64, 64),batch_size = 32,class_mode = 'binary')
pred=model.fit_generator(training_set,samples_per_epoch = 2000, nb_epoch = 15, validation_data = test_set, nb_val_samples = 200)

print()
print(pred)
