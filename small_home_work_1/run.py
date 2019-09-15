#  Module for the first small homework

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


def main():
    image = Image.open("image_1.png")
    image.load()
    image_data = np.asarray(image, dtype="int32")

    # plt.imshow(image)
    # plt.show()

    red_channel = image_data[:, :, 0]
    green_channel = image_data[:, :, 1]
    blue_channel = image_data[:, :, 2]

    red_mean = np.mean(red_channel)
    green_mean = np.mean(green_channel)
    blue_mean = np.mean(blue_channel)

    red_std = np.std(red_channel)
    green_std = np.std(green_channel)
    blue_std = np.std(blue_channel)

    red_standardized = stats.zscore(red_channel.flatten())
    green_standardized = stats.zscore(green_channel.flatten())
    blue_standardized = stats.zscore(blue_channel.flatten())

    print(np.mean(red_standardized))
    print(np.mean(green_standardized))
    print(np.mean(blue_standardized))

    print(np.std(red_standardized))
    print(np.std(green_standardized))
    print(np.std(blue_standardized))


if __name__ == "__main__":
    main()
