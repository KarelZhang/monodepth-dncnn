#!/bin/bash
clear
echo ‘start running...’
mode="train"
model_name='depth-dncnn'
data_path='/media/zhangjiaao/data/kitti/'
filenames_file='utils/filenames/neweigen_train_files.txt'
log_directory='tmp'

python monodepth_main.py --mode=$mode --model_name=$model_name --data_path=$data_path --filenames_file=$filenames_file --log_directory=$log_directory
