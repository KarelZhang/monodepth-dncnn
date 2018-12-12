#! /bin/bash
clear

echo "start running..."
mode="test"
kitti_data_root="/media/zhangjiaao/data/kitti/"
image_path_file="utils/filenames/new_test_files.txt"
log_dir="tmp/"
model_dir="model/denoise_model_1/model-66400"
encoder="vgg"

python monodepth_main.py --mode=$mode --data_path=$kitti_data_root --filenames_file=$image_path_file --log_directory=$log_dir --checkpoint_path=$model_dir --encoder=$encoder

