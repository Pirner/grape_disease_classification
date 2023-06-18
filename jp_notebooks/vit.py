import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import glob

import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

from torch import nn
from torch import Tensor
from PIL import Image
from torchvision.transforms import Compose, Resize, ToTensor
from einops import rearrange, reduce, repeat
from einops.layers.torch import Rearrange, Reduce
from torchsummary import summary


def main():
    im_paths = glob.glob(os.path.join(r'C:\data\grape_disease\train', '**/*.JPG'), recursive=True)
    img = Image.open(im_paths[0])

    fig = plt.figure()
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    main()
