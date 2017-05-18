

### Vehicle Detection Project

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector. 
* Normalize your features and randomize a selection for training and testing.
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

[//]: # (Image References)
[image1]: ./writeup_images/car_not_car.png
[image2]: ./writeup_images/HOG_example.png
[image3]: ./writeup_images/sliding_windows.png
[image4]: ./writeup_images/hot_windows.png
[image5]: ./writeup_images/heat.png
[image6]: ./writeup_images/heat_thresh.png
[image7]: ./writeup_images/output_boxes.png


### Histogram of Oriented Gradients (HOG)

####1. Explain how (and identify where in your code) you extracted HOG features from the training images.

The code for this step is contained in the 6-7th cells of the IPython notebook.

I started by reading in all the `vehicle` and `non-vehicle` images.  Here is an example of one of each of the `vehicle` and `non-vehicle` classes:

![alt text][image2]



####2. Explain how you settled on your final choice of HOG parameters.

Various parameter combinations were used during experimentation. The code for this is in the 5th and 6th cell.

The final parameters were:
    color_space:  YCrCb 
   orientations:  9 
   pix_per_cell:  8 
 cell_per_block:  2 
    hog_channel:  ALL 
   spatial_size:  (32, 32) 
 histogram bins:  32

### Classifier 

####3. Describe how (and identify where in your code) you trained a classifier using your selected HOG features (and color features if you used them).

I trained a linear SVM with the default parameters from the lesson material.  The code for this is in the 8th cell.  The training set was split into a training and test set.  The test set was 10% of the overall feature vector.

Normalization was implemented with the StandardScaler().fit(X) function from sklearn.

### Sliding Window Search

####1. Describe how (and identify where in your code) you implemented a sliding window search.  How did you decide what scales to search and how much to overlap windows?

The code for this is in the 9-10th cell.  The code was mostly taken from the lesson material.  The scaling was from the lesson material and the overlap was determined by experimentation.

![alt text][image3]

####2. Show some examples of test images to demonstrate how your pipeline is working.  What did you do to optimize the performance of your classifier?



### False Positives and Heat Mapping

To reduce the effect of false positive detections, a thresholded heat map was used.

The following image demonstrates two false positive detections.

![alt text][image4]

The following image shows the effect of converting the "hot windows" to a heat map, then the following image shows the result after thresholding.  The code for the heat mapping is in cells 15-17.

![alt text][image5]

![alt text][image6]

The thresholding allows for strong detections to "pass the heat filter" and the false positives to be rejected.

The result of the image pipeline is shown in the following images

![alt text][image7]

---

### Video Implementation

Here's a [link to my video result](https://youtu.be/_9Nu6FPawLk)
 

---

###Discussion

####1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

Problems were encountered in training the classifier.  Parameter tuning proved to be a lengthy task.  99.4% accuracy was obtained after training.

Further problems occurred with the detection of strong false positives.  The Vehicle_Tracker class to store the last 15 window detections. 

The pipeline is likely to fail for environments that do not resemble the training set.  Also, it seems likely the classifier will break-down if presented with city-driving or a very high traffic situation.

Possible improvements to this pipeline in particular might include augmenting the pipeline/classifier with a CNN and additional datasets.

