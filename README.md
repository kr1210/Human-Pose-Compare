# Human-Pose-Compare
For theory and details on implementation, Please Visit: 
https://medium.com/@krishnarajr319/human-pose-comparison-and-action-scoring-using-deep-learning-opencv-python-c2bdf0ddecba

## Quick start 
Install Dependencies:
```
pip install -r requirements.txt
```
There is a test video named ```test.mp4``` included with the repo in order to test its working. 
The file called ```lookup_test.pickle``` contains the sequence of keypoints recorded for ```punch - side``` recorded from ```test.mp4```.

In order to compare ```test.mp4``` with the keypoints recorded in the ```lookup.pickle``` under the label ```punch - side```,run:
```
python start_here.py --activity "punch - side" --video "test.mp4"
```
## Creating New Lookup

There is a file ```keypoints_from_video.py``` which can be used to create a new lookup table. In order to extract and record keypoints from ```test.mp4```, run:
```
python keypoints_from_video.py --activity "punch - side" --video "test.mp4" --lookup "lookup_new.pickle"/[YOUR_LOOKUP_NAME]
```
Then, in order to use this new lookup, run:
```
python start_here.py --activity "punch - side" --video "test.mp4" --lookup "lookup_new.pickle"/[YOUR_LOOKUP_NAME]
```
### Acknowledgements
The Posenet model used in this repo was implemented  here : https://github.com/rwightman/posenet-python
