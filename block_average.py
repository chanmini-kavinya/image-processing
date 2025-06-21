import cv2
import numpy as np
import matplotlib.pyplot as plt

def block_average(image_path, block_sizes):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    results = []
    for size in block_sizes:
        h, w = img.shape
        reduced = np.copy(img)
        for i in range(0, h, size):
            for j in range(0, w, size):
                block = img[i:i+size, j:j+size]
                avg = np.mean(block, dtype=np.float32)
                reduced[i:i+size, j:j+size] = avg
        results.append((size, reduced))
    return img, results

def main():
    img_path = 'image.png'
    img, results = block_average(img_path, [3, 5, 7])
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 4, 1), plt.imshow(img, cmap='gray'), plt.title('Original')
    for i, (k, r) in enumerate(results):
        plt.subplot(1, 4, i+2), plt.imshow(r, cmap='gray'), plt.title(f'{k}x{k} Block Avg')
    plt.show()

if __name__ == '__main__':
    main()