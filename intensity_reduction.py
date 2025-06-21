import cv2
import numpy as np
import matplotlib.pyplot as plt

def reduce_intensity_levels(image_path, levels):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    factor = 256 // levels
    reduced_img = (img // factor) * factor
    return img, reduced_img

def main():
    img_path = 'image.png'
    original, reduced = reduce_intensity_levels(img_path, 2)

    plt.subplot(1, 2, 1), plt.imshow(original, cmap='gray'), plt.title('Original')
    plt.subplot(1, 2, 2), plt.imshow(reduced, cmap='gray'), plt.title('Reduced to 2 levels')
    plt.show()

if __name__ == '__main__':
    main()