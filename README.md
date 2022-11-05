# SNI-x-KWT-HACKATHON


We will use computer vision to do the recognition and identification of the lions.We will do this by:
1. Isolating region of interest (ROI) from the image.
2. The lion's identity is then estimated using the uniqueness of whisker spot patterns or any other identifiable marks on the lion's face, even the shape of the face.
3. Each lion will then be given a unique identification number or name.
These unique features can be used to filter the lion identity from the database with pattern recognition and finding a match.

We are hoping that this will help with automating the data management process and ultimately with the conservation of lions.


for the model we use sift opencv algorithm to match image features then identify individual lions.
This article goes into the details of the 
 	[sift](https://medium.com/data-breach/introduction-to-sift-scale-invariant-feature-transform-65d7f3a72d40) algorithm
 we are then working on deploying the model on flask so that ita can be used for lion identification.

