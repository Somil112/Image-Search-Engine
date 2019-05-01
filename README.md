# Image-Search-Engine
Implementation of Image Search Engine using Python and OpenCV

## Description for each file:

### colordescriptor.py
  Used to generate the features for each image.

### ime.py:
  This is used to generate the index.csv which stores all the feature scores of the input image.
  In basic terminologies, it is used to train the image search engine given the dataset.
  
### searcher.py
  Helper file for the search.py
  
### search.py
  This file takes input your image and gives the output results.
  
  
## Usage:

    python ime.py --dataset dataset-location-directory --index saved-features.csv
    python search.py --result-path input-path --query abc.jpeg --index saved-features.csv
    
* --dataset : Location of your dataset
* --index : Location and name of the csv file where you'll store the features of all images
* --result-path : Location of your dataset
* --query : Image query


   
    
 
