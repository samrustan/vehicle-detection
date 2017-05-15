import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#image = mpimg.imread('bbox-example-image.jpg')
image = mpimg.imread('temp-matching-example-2.jpg')
templist = ['cutout1.jpg', 'cutout2.jpg', 'cutout3.jpg',
            'cutout4.jpg', 'cutout5.jpg', 'cutout6.jpg']

# Here is your draw_boxes function from the previous exercise
def draw_boxes(img, bboxes, color=(0, 0, 255), thick=6):
    # Make a copy of the image
    imcopy = np.copy(img)
    # Iterate through the bounding boxes
    for bbox in bboxes:
        # Draw a rectangle given bbox coordinates
        cv2.rectangle(imcopy, bbox[0], bbox[1], color, thick)
    # Return the image copy with boxes drawn
    return imcopy
    
    
# Define a function that takes an image and a list of templates as inputs
# then searches the image and returns the a list of bounding boxes 
# for matched templates
def find_matches(img, template_list):
    # Make a copy of the image to draw on
    # Define an empty list to take bbox coords
    bbox_list = []
    # Iterate through template list
    for tempo in template_list:
        # Read in templates one by one
        tmpl = cv2.imread(tempo)
        # Use cv2.matchTemplate() to search the image\
        found = cv2.matchTemplate(img, tmpl, cv2.TM_CCOEFF_NORMED)
        # Use cv2.minMaxLoc() to extract the location of the best match
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(found)
        # Determine bounding box corners for the match
        w, h = (tmpl.shape[1], tmpl.shape[0])
        if cv2.TM_CCOEFF_NORMED in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            upper_left = min_loc
        else:
            upper_left = max_loc
        
        lower_right = (upper_left[0] + w, upper_left[1] + h)
        bbox_list.append((upper_left, lower_right))
        # Return the list of bounding boxes
    return bbox_list

bboxes = find_matches(image, templist)
result = draw_boxes(image, bboxes)
plt.imshow(result)