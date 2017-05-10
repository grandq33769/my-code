'''
Created on 2017年5月3日

@author: LokHim
'''

import numpy as np
from itertools import product
from PIL import Image
from input_name import FILESET, URLBASE
from input_ellipse import LOCATION_DICT

PADDING_SIZE = 5
SAMPLE_SIZE = 12


def is_overlap(income, origin):
    origin = map(lambda x: x + PADDING_SIZE, list(origin))


def location_of_face(face):
    start_x = face.xcoor - face.minor_axis
    start_y = face.ycoor - face.major_axis
    end_x = face.xcoor + face.minor_axis
    end_y = face.ycoor + face.major_axis
    return (start_x, start_y, end_x, end_y)


def crop_negative(face_list, image, image_size):
    return_list = []
    location_list = []
    width, height = image.size

    for face in face_list:
        bbox = location_of_face(face)
        location_list.append(bbox)

    for x_start, y_start in product(range(0, width, image_size), range(0, height, image_size)):
        rbox = [x_start, y_start, x_start +
                image_size, y_start + image_size]
        if any([is_overlap(rbox, loc) for loc in location_list]):
            pass
    return return_list


def crop_face(face_list, image):
    return_list = []
    for face in face_list:
        bbox = location_of_face(face)
        new = image.rotate(face.angle)
        crop_image = new.crop(bbox)
        return_list.append(crop_image)

    return return_list


total = 0  # 5171
# Crop face image
for filename in FILESET:
    with Image.open(URLBASE + '/' + filename + '.jpg', 'r') as image:
        face_list = LOCATION_DICT[filename]
        croped_list = crop_face(face_list, image)
        file_name = filename.replace('/', '_')
        save_path = URLBASE + '/Input_Data/Positive/' + file_name
        for croped_face in croped_list:
            index = croped_list.index(croped_face)
            str_index = str(index)
            croped_face.save(save_path + '_' + str_index + '.jpg')
            total += 1

print(total)

# Crop background image
total = 0
for filename in FILESET:
    with Image.open(URLBASE + '/' + filename + '.jpg', 'r') as image:
        face_list = LOCATION_DICT[filename]
        croped_list = crop_negative(face_list, image, SAMPLE_SIZE)
        file_name = filename.replace('/', '_')
        save_path = URLBASE + '/Input_Data/Negative/'
        for croped_neg in croped_list:
            str_index = str(total)
            croped_neg.save(save_path + '_' + str_index + '.jpg')
            total += 1

print(total)
