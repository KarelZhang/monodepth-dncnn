from __future__ import absolute_import, division, print_function

# only keep warnings and errors
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='0'

import numpy as np
import argparse
import re
import time
import tensorflow as tf
import tensorflow.contrib.slim as slim
import scipy.misc
import matplotlib.pyplot as plt


from monodepth_dataloader import *
from average_gradients import *

pred_disp = np.load('disparities.npy')

plt.imsave('1.png', pred_disp[0], cmap='plasma')
