#  Module for the first small homework

import bs4
import os
import urllib.request
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
from PIL import Image
from scipy import stats


def first_and_second_sub_task():
    """ Function for the first and second subtask """
    working_dir = os.getcwd()
    for file in os.listdir(working_dir):
        if file.endswith(".png"):
            print("Image found: {}".format(file))

            # Sub-task 1.
            image = Image.open(file)
            image.load()
            image_data = np.asarray(image, dtype="int32")

            rgb_channels = {'red': image_data[:, :, 0],
                            'green': image_data[:, :, 1],
                            'blue': image_data[:, :, 2]}

            for color, channel_data in rgb_channels.items():
                print("Channel data of {}: {}".format(color, channel_data))

                # Sub-task 2.
                channel_mean = np.mean(channel_data)
                channel_std = np.std(channel_data)
                print("Mean of {} channel data: {}".format(color, channel_mean))
                print("Standard deviation of {} channel data: {}".format(color, channel_std))

                channel_data_standardized = stats.zscore(channel_data.flatten())
                print("Standardized channel data of {}: {}".format(color, channel_data_standardized))
                print("Mean of {} standardized channel data: {}".format(color, np.mean(channel_data_standardized)))
                print("Standard deviation of {} standardized channel data: {}".format(
                    color, np.std(channel_data_standardized)))

            fig = plt.figure()
            plt.imshow(image)
    plt.show()


def third_subtask():
    # Sub-task 3.
    link = "https://blog.keras.io/the-future-of-deep-learning.html"
    webpage = str(urllib.request.urlopen(link).read())
    soup = bs4.BeautifulSoup(webpage, features="html.parser")
    webpage_text = soup.get_text()
    print("Text of the webpage: {}\n{}".format(link, webpage_text))
    char_list = list(webpage_text)
    ser = pd.Series(char_list)
    ser = ser.str.lower()
    ser = ser[ser.str.isalpha()]
    ser = ser.groupby(ser.values).sum()
    for index, value in ser.items():
        ser[index] = len(value)
    ser = ser.sort_values(ascending=False)

    fig = plt.figure()
    plt.bar(ser.index, ser, width=0.5, color='g')
    plt.show()


def main():
    first_and_second_sub_task()
    third_subtask()


if __name__ == "__main__":
    main()
