# Code for "TSM: Temporal Shift Module for Efficient Video Understanding"
# arXiv:1811.08383
# Ji Lin*, Chuang Gan, Song Han
# {jilin, songhan}@mit.edu, ganchuang@csail.mit.edu

import os


def return_bb_dataset_cropped(modality):
    filename_categories = 'datasets_tsm/bb-dataset-cropped/category.txt'
    if modality == 'RGB':
        prefix = 'img_{:03d}.jpg'
        root_data = 'datasets_tsm/bb-dataset-cropped/images'
        filename_imglist_train = 'datasets_tsm/bb-dataset-cropped/train.txt'
        filename_imglist_val = 'datasets_tsm/bb-dataset-cropped/val.txt'
    else:
        raise NotImplementedError('no such modality:' + modality)
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix


def return_bb_dataset_cropped_upper(modality):
    filename_categories = 'datasets_tsm/bb-dataset-cropped-upper/category.txt'
    if modality == 'RGB':
        prefix = 'img_{:03d}.jpg'
        root_data = 'datasets_tsm/bb-dataset-cropped-upper/images'
        filename_imglist_train = 'datasets_tsm/bb-dataset-cropped-upper/train.txt'
        filename_imglist_val = 'datasets_tsm/bb-dataset-cropped-upper/val.txt'
    else:
        raise NotImplementedError('no such modality:' + modality)
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix


def return_yanchai(modality):
    filename_categories = 'datasets_tsm/yanchai_23072024/category.txt'
    if modality == 'RGB':
        prefix = 'img_{:03d}.jpg'
        root_data = 'datasets_tsm/yanchai_23072024/images'
        filename_imglist_train = 'datasets_tsm/yanchai_23072024/train.txt'
        filename_imglist_val = 'datasets_tsm/yanchai_23072024/val.txt'
    else:
        raise NotImplementedError('no such modality:' + modality)
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix


def return_combine(modality):
    filename_categories = 'datasets_tsm/combined_ogcio_yanchai_06082024/category.txt'
    if modality == 'RGB':
        prefix = 'img_{:03d}.jpg'
        root_data = 'datasets_tsm/combined_ogcio_yanchai_06082024/images'
        filename_imglist_train = 'datasets_tsm/combined_ogcio_yanchai_06082024/train.txt'
        filename_imglist_val = 'datasets_tsm/combined_ogcio_yanchai_06082024/val.txt'
    else:
        raise NotImplementedError('no such modality:' + modality)
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix


def return_dataset(dataset, modality):
    dict_single = {'bb-dataset-cropped': return_bb_dataset_cropped,
                   'bb-dataset-cropped-upper': return_bb_dataset_cropped_upper,
                   'yanchai': return_yanchai,
                   'combine': return_combine}
    if dataset in dict_single:
        file_categories, file_imglist_train, file_imglist_val, root_data, prefix = dict_single[dataset](modality)
    else:
        raise ValueError('Unknown dataset ' + dataset)

    if isinstance(file_categories, str):
        with open(file_categories) as f:
            lines = f.readlines()
        categories = [item.rstrip() for item in lines]
    else:  # number of categories
        categories = [None] * file_categories
    n_class = len(categories)
    print('{}: {} classes'.format(dataset, n_class))
    return n_class, file_imglist_train, file_imglist_val, root_data, prefix
