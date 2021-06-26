# OpenCV with Python in 4 Hours
Notes and code used in my [**Python and OpenCV course**](https://youtu.be/oXlwWbU8l2o) on [freeCodeCamp.org](http://freecodecamp.org). You can find me on [Twitter](https://twitter.com/jasmcaus) for more info on courses I'm working on currently.


## Important Updates:
`caer.train_val_split()` is a deprecated feature in [`caer`](https://github.com/jasmcaus/caer/). Use `sklearn.model_selection.train_test_split()` instead. See [#9](https://github.com/jasmcaus/opencv-course/issues/9) for more details.


# Course Outline (with timestamps)
## 1. Installation
Besides installing OpenCV, we cover the installation of the following package:

[**`Caer`**](https://github.com/jasmcaus/caer/) is a *lightweight, high-performance* Vision library for high-performance AI research. It simplifies your approach towards Computer Vision by abstracting away unnecessary boilerplate code giving you the **flexibility** to quickly prototype deep learning models and research ideas. 
```bash
$ pip install caer
```


## 2. Basic Concepts:
- Reading Images and Video ([0:04:12](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=252s))
- Resizing and Rescaling Images and Video Frames ([0:12:57](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=777s))
- Drawing Shapes and Placing text on images ([0:20:21](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=1221s))
- 5 Essential Methods in OpenCV ([0:31:55](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=1915s))
- Image Transformations ([0:44:13](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=2653s))
- Contour Detection ([0:57:06](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=3426s))
    
## 3. Advanced Concepts:
- Switching between Colour Spaces (RGB, BGR, Grayscale, HSV and L*a*b) ([1:12:53](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=4373s))
- Splitting and Merging Colour Channels ([1:23:10](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=4990s))
- Blurring ([1:31:03](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=5463s))
- BITWISE operations ([1:44:27](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=6267s))
- Masking ([1:53:06](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=6786s))
- Histogram Computation ([2:01:43](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=7303s))
- Thresholding/Binarizing Images ([2:15:22](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=8122s))
- Advanced Edge Detection ([2:26:27](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=8787s))
    
## 4. Face Detection and Recognition
- Face Detection using Haar Cascades ([2:35:25](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=9325s))
- Face Recognition using OpenCV's LBPHFaceRecognizer algorithm ([2:49:05](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=10145s))
    
## 5. Capstone: Deep Computer Vision
- Building a Deep Computer Vision model to classify between the characters in the popular TV series The Simpsons ([3:11:57](https://www.youtube.com/watch?v=x3c8w2ruhjs&t=11517s))

# Credits
The images in the [Photos](https://github.com/jasmcaus/opencv-course/tree/master/Resources/Photos) and [Videos](https://github.com/jasmcaus/opencv-course/tree/master/Resources/Videos) folders were downloaded from [Unsplash](http://unsplash.com) and [Pixabay](http://pixabay.com), unless otherwise mentioned.


The images in the [Faces](https://github.com/jasmcaus/opencv-course/tree/master/Resources/Faces) folder were procurred from a [repo](https://www.kaggle.com/dansbecker/5-celebrity-faces-dataset) on Kaggle.
