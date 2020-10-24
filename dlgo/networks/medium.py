# © 2020 지성. all rights reserved.
# <llllllllll@kakao.com>
# MIT License

from tensorflow.keras.layers import Dense, Activation, Flatten
from tensorflow.keras.layers import Conv2D, ZeroPadding2D

def layers(input_shape):
    return [
        ZeroPadding2D((2, 2), input_shape=input_shape, data_format='channels_first'),
        Conv2D(64, (5, 5), padding='valid', data_format='channels_first'),
        Activation('relu'),

        ZeroPadding2D((2, 2), data_format='channels_first'),
        Conv2D(64, (5, 5), data_format='channels_first'),
        Activation('relu'),

        ZeroPadding2D((1, 1), data_format='channels_first'),
        Conv2D(64, (3, 3), data_format='channels_first'),
        Activation('relu'),

        ZeroPadding2D((1, 1), data_format='channels_first'),
        Conv2D(64, (3, 3), data_format='channels_first'),
        Activation('relu'),

        ZeroPadding2D((1, 1), data_format='channels_first'),
        Conv2D(64, (3, 3), data_format='channels_first'),
        Activation('relu'),

        Flatten(),
        Dense(512),
        Activation('relu'),
    ]