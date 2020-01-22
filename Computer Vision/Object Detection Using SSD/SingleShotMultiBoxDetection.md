## Object Detection

**Single Shot MultiBox Detection (SSD)**


By using SSD, we only need to take one single shot to detect multiple objects within the image, while regional proposal network (RPN) based approaches such as R-CNN series that need two shots, one for generating region proposals, one for detecting the object of each proposal. Thus, SSD is much faster compared with two-shot RPN-based approaches.


SSD300 achieves 74.3% mAP at 59 FPS while SSD500 achieves 76.9% mAP at 22 FPS, which outperforms Faster R-CNN (73.2% mAP at 7 FPS) and YOLOv1 (63.4% mAP at 45 FPS). 

mAP (mean Average precision) is a popular metric in measuring the accuracy of object detectors like Faster R-CNN, SSD, etc. Average precision computes the average precision value for recall value over 0 to 1.

MultiBox’s loss function also combined two critical components that made their way into SSD:
Confidence Loss: this measures how confident the network is of the objectness of the computed bounding box. Categorical cross-entropy is used to compute this loss.
Location Loss: this measures how far away the network’s predicted bounding boxes are from the ground truth ones from the training set. L2-Norm is used here.



**Region-Convolutional Neural Network (R-CNN)**

A few years ago, by exploiting some of the leaps made possible in computer vision via CNNs, researchers developed R-CNNs to deal with the tasks of object detection, localization and classification. Broadly speaking, a R-CNN is a special type of CNN that is able to locate and detect objects in images: the output is generally a set of bounding boxes that closely match each of the detected objects, as well as a class output for each detected object. The image below shows what a typical R-CNN outputs.


**VGG-16 architecture:**


### References:

https://towardsdatascience.com/understanding-ssd-multibox-real-time-object-detection-in-deep-learning-495ef744fab
