#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: penghuailiang
# @Date  : 2019-09-27

import argparse


def parse_list(str_value):
    if ',' in str_value:
        str_value = str_value.split(',')
    else:
        str_value = [str_value]
    return str_value


parser = argparse.ArgumentParser(description='face')

# ========================== GENERAL PARAMETERS ========================= #
parser.add_argument(
    '--phase',
    dest='phase',
    default='train_imitator',
    help='Specify current phase: train or inference.')
parser.add_argument(
    '--params_cnt',
    dest='params_cnt',
    type=int,
    default=int(95),
    help='count of engine face params')
parser.add_argument(
    '--path_to_dataset',
    dest='path_to_dataset',
    default="../export/trainset_female",
    help='path for database generated by engine')
parser.add_argument(
    '--path_to_testset',
    dest='path_to_testset',
    default="../export/testset_female",
    help='path for testset generated by engine')
parser.add_argument(
    '--path_to_cache',
    dest='path_to_cache',
    default="../export/cache",
    help='path for cache generated by engine')
parser.add_argument(
    '--path_to_inference',
    dest='path_to_inference',
    default="./output/inference",
    help='model path for inference')
parser.add_argument(
    '--path_tensor_log',
    dest='path_tensor_log',
    default="./logs/",
    help='model path for inference')
parser.add_argument(
    '--use_gpu',
    dest='use_gpu',
    type=bool,
    default=bool(True),
    help='manual open gpu mode, if device is supported')
parser.add_argument(
    '--gpuid',
    dest='gpuid',
    type=int,
    default=int(0),
    help='device GPU ID, if use_gpu set True')
parser.add_argument(
    '--udp_port',
    dest='udp_port',
    type=int,
    default=int(5011),
    help='socket port for connecting engine')
parser.add_argument(
    '--lightcnn',
    dest='lightcnn',
    type=str,
    default="./dat/LightCNN_29Layers_V2_checkpoint.pth.tar",
    help='light cnn pre-train model')
parser.add_argument(
    '--parsing_checkpoint',
    dest='parsing_checkpoint',
    type=str,
    default="./dat/79999_iter.pth",
    help='faceparsing trained model')

# ========================= IMITATOR PARAMETERS ========================= #

parser.add_argument(
    '--total_steps',
    dest='total_steps',
    type=int,
    default=int(6e5),
    help='total steps for imitator')
parser.add_argument(
    '--batch_size',
    dest='batch_size',
    type=int,
    default=1,
    help='# images in batch')
parser.add_argument(
    '--prev_freq',
    dest='prev_freq',
    type=int,
    default=1000,
    help='generate preview image when training')
parser.add_argument(
    '--save_freq',
    dest='save_freq',
    type=int,
    default=5000,
    help='Save model every save_freq steps')
parser.add_argument(
    '--learning_rate',
    dest='learning_rate',
    type=float,
    default=0.1,
    help='initial learning rate of imitator')
parser.add_argument(
    '--imitator_model',
    dest='imitator_model',
    type=str,
    default='imitator_550000_cuda.pth',
    help='pre_trained model of imitator')

# ========================= EXTRACTOR PARAMETERS ========================= #
parser.add_argument(
    '--total_extractor_steps',
    dest='total_extractor_steps',
    type=int,
    default=int(2e6),
    help='total number of feature extractor steps')
parser.add_argument(
    '--extractor_learning_rate',
    dest='extractor_learning_rate',
    type=float,
    default=0.02,
    help='initial learning rate of feature extractor')
parser.add_argument(
    '--extractor_prev_freq',
    dest='extractor_prev_freq',
    type=int,
    default=1000,
    help='generate preview image when training')
parser.add_argument(
    '--extractor_save_freq',
    dest='extractor_save_freq',
    type=int,
    default=5000,
    help='Save model every save_freq steps')
parser.add_argument(
    '--extractor_model',
    dest='extractor_model',
    type=str,
    default='extractor_845000_cuda.pth',
    help='pre_trained model of extractor')

# ========================= EVALUATE PARAMETERS ========================= #
parser.add_argument(
    '--total_eval_steps',
    dest='total_eval_steps',
    type=int,
    default=int(1000),
    help='total iterator of evaluate steps')
parser.add_argument(
    '--eval_learning_rate',
    dest='eval_learning_rate',
    type=float,
    default=0.2,
    help='initial learning rate of evaluate')
parser.add_argument(
    '--eval_prev_freq',
    dest='eval_prev_freq',
    type=int,
    default=50,
    help='generate preview image when iterate')
parser.add_argument(
    '--eval_alpha',
    dest='eval_alpha',
    type=float,
    default=1.2,
    help='alpha weight of evaluate balance between l1 & l2')
parser.add_argument(
    '--eval_image',
    dest='eval_image',
    type=str,
    default='../export/testset_female/db_0239_4.jpg',
    help='generate preview image when iterate')
