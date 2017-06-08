'''
Created on 2017年6月7日

@author: LokHim
'''
from keras.models import load_model, Model
from llh.Python.keras.face_regonition.model import *

MODEL = Sequential()

MODEL.add(Conv2D(64, (5, 5), padding='same',
                 input_shape=X_TRAIN.shape[1:]))
MODEL.add(Activation('relu'))
MODEL.add(MaxPooling2D(pool_size=(3, 3), strides=2))
MODEL.add(Flatten())
MODEL.add(Dense(128))
MODEL.add(Activation('tanh'))
# Concatenate 12-net result
IMPORT_NET = load_model('12-net.h5')
NET12 = Model(inputs=IMPORT_NET.input,
              outputs=IMPORT_NET.get_layer(index=6).output)
# TODO:Concatenate the NET12 to fully-connected layer for softmax

MODEL.add(Dense(NUM_CLASSES))
MODEL.add(Activation('softmax'))

# initiate RMSprop optimizer
OPT = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)

# Let's train the model using RMSprop
MODEL.compile(loss='categorical_crossentropy',
              optimizer=OPT,
              metrics=['accuracy'])


HISTORY = MODEL.fit(X_TRAIN, Y_TRAIN,
                    batch_size=BATCH_SIZE,
                    epochs=EPOCHS,
                    validation_data=(X_TEST, Y_TEST),
                    shuffle=True)

SCORE = MODEL.evaluate(X_TEST, Y_TEST, verbose=0)

print('Test loss:', SCORE[0])
print('Test accuracy:', SCORE[1])

MODEL.save('12-net.h5')
