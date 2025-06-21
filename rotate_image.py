import cv2
import matplotlib.pyplot as plt

def rotate_image(image_path):
    img = cv2.imread(image_path)
    h, w = img.shape[:2]
    center = (w // 2, h // 2)

    # Rotate by 45 degrees
    M45 = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated_45 = cv2.warpAffine(img, M45, (w, h))

    # Rotate by 90 degrees
    M90 = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated_90 = cv2.warpAffine(img, M90, (w, h))

    return img, rotated_45, rotated_90

def main():
    img_path = 'image.png'
    original, rot45, rot90 = rotate_image(img_path)
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1), plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB)), plt.title('Original')
    plt.subplot(1, 3, 2), plt.imshow(cv2.cvtColor(rot45, cv2.COLOR_BGR2RGB)), plt.title('Rotated 45°')
    plt.subplot(1, 3, 3), plt.imshow(cv2.cvtColor(rot90, cv2.COLOR_BGR2RGB)), plt.title('Rotated 90°')
    plt.show()

if __name__ == '__main__':
    main()
