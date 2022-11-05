# pip install opencv-python -U
# pip install gdown
# gdown --id 1IQ90jtnITrrcBWsFjF8jkFXF7LAxDqLF



import matplotlib.pyplot as plt
def show_images(images, figsize=(20,10), columns = 5):
  plt.figure(figsize=figsize)
  for i, image in enumerate(images):
      plt.subplot(len(images) / columns + 1, columns, i + 1)
      plt.imshow(image)


import os
IMAGE_PATH="/content/drive/MyDrive/lions"
file_names=os.listdir(IMAGE_PATH)
print(f"number of images: {len(file_names)}")


import cv2
import numpy as np
from PIL import Image
from os import listdir
import pickle as pk
import math
from tqdm import tqdm
sift = cv2.SIFT_create(nfeatures=500)

def resize_img_to_array(img):
    height,width=img.size
    if height*width>2000*2000:
        k=math.sqrt(height*width/(2000*2000))
        img=img.resize(
            (round(height/k),round(width/k)), 
            Image.ANTIALIAS
        )
    img_array = np.array(img)
    return img_array

def calculate_descr(img):
    eps=1e-7
    img=resize_img_to_array(img)
    key_points, descriptors = sift.detectAndCompute(img, None)
    if descriptors is None:
      return (None,None)
    descriptors /= (descriptors.sum(axis=1, keepdims=True) + eps) #RootSift
    descriptors = np.sqrt(descriptors)    #RootSift
    return (key_points,descriptors)

IMAGES_PATH="/content/drive/MyDrive/lions"
file_names=listdir(IMAGES_PATH)
all_image_features=[]
for file_name in tqdm(file_names):
    img = Image.open(IMAGES_PATH+"/"+file_name)
    keyp,descs=calculate_descr(img)
    if descs is None:
        continue
    if descs.shape[0]==1:
        continue
    all_image_features.append({"descs":descs,"file_name":file_name})
pk.dump(all_image_features, open("all_image_features.pkl","wb"))


import numpy as np
from PIL import Image
query_image_pillow=Image.open(f'{IMAGES_PATH}/LE.jpg')
query_image_features=calculate_descr(query_image_pillow)[1]
show_images([np.array(query_image_pillow)])
print(query_image_features.shape)

time
res=sift_reverse_search(query_image_pillow)
print(res)

found_images=[]
for file_name in res:
    found_images.append(np.array(Image.open(IMAGES_PATH+"/"+file_name)))
show_images(np.array(found_images))

crop_rectangle = (100, 100, 400, 400)
query_image_cropped = query_image_pillow.crop(crop_rectangle)
res2=sift_reverse_search(query_image_cropped)
show_images([np.array(query_image_cropped)])
found_images_2=[]
for file_name in res2:
    found_images_2.append(np.array(Image.open(IMAGES_PATH+"/"+file_name)))
show_images(np.array(found_images_2))


