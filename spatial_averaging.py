import cv2
import numpy as np
import matplotlib.pyplot as plt

def spatial_averaging(image_path, kernel_sizes):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    results = []
    for k in kernel_sizes:
        blurred = cv2.blur(img, (k, k))
        results.append((k, blurred))
    return img, results

def main():
    img_path = 'image.png'
    img, results = spatial_averaging(img_path, [3, 10, 20])
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 4, 1), plt.imshow(img, cmap='gray'), plt.title('Original')
    for i, (k, r) in enumerate(results):
        plt.subplot(1, 4, i+2), plt.imshow(r, cmap='gray'), plt.title(f'{k}x{k} Average')
    plt.show()

if __name__ == '__main__':
    main()
