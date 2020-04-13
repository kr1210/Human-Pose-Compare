# Human-Pose-Compare

## Quick start 
Install Dependencies:
```
pip install -r requirements.txt
```
There is a test video named ```test.mp4``` included with the repo in order to test its working. 
The file called ```lookup.pickle``` contains the sequence of keypoints recorded for ```punch - side``` recorded from ```test.mp4```.

In order to compare ```test.mp4``` with the keypoints recorded in the ```lookup.pickle``` under the label ```punch - side```,run:
```
python start_here.py --activity "punch - side" --video "test.mp4"
```
## Creating New Lookup

There is a file ```key
