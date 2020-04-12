
# USAGE : python3 start_here.py --activity "punch - side" --video "test.mp4"

import argparse
from calculations import get_Score



ap = argparse.ArgumentParser()
ap.add_argument("-a", "--activity", required=True,
	help="activity to be scored")
ap.add_argument("-v", "--video", required=True,
	help="video file to be scored against")
ap.add_argument("-l", "--lookup", default="lookup_test.pickle",
	help="The pickle file containing the lookup table")
args = vars(ap.parse_args())



g = get_Score(args["lookup"])

final_score,score_list = g.calculate_Score(args["video"],args["activity"])
print(final_score)
print(score_list)