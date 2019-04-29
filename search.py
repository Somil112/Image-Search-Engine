# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:04:07 2019

@author: Somil
"""

from colordescriptor import ColorDescriptor
from searcher import Searcher
import argparse
import cv2


ap = argparse.ArgumentParser()

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
    help = "Path to where the computed index is stored")
ap.add_argument("-q", "--query", required = True,
    help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
    help = "Path to the result path")
args = vars(ap.parse_args())
 

cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread(args["query"])
features = cd.describe(query)
 
# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)
 
# display the query
cv2.imshow("Query", query)

print(results)
print(args)
# loop over the results
print("Similar Images Recognized from best to worst")
for (score, resultID) in results:
    # load the result image and display it
    print("Image name: ",resultID)
    # result = cv2.imread('img' + "\\" + resultID)    
    # cv2.imshow('Results', result)
    # cv2.waitKey(0)
