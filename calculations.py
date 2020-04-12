
import tensorflow as tf
import pickle
import cv2
import numpy as np
import posenet
from pose import Pose
from score import Score
from dtaidistance import dtw


class get_Score(object):
	def __init__(self, lookup='lookup.pickle'):
		self.a = Pose()
		self.s = Score()
		self.b = pickle.load(open(lookup, 'rb'))
		self.input_test = []

	def get_action_coords_from_dict(self,action):
			for (k,v) in self.b.items():
				if k==action:
					(model_array,no_of_frames) = (v,v.shape[0])
			return model_array,no_of_frames
	
	def calculate_Score(self,video,action):
		with tf.Session() as sess:
			model_cfg, model_outputs = posenet.load_model(101, sess)
			model_array,j = self.get_action_coords_from_dict(action)
			cap = cv2.VideoCapture(video)
			i = 0
			if cap.isOpened() is False:
				print("error in opening video")
			while cap.isOpened():
				ret_val, image = cap.read()
				if ret_val:         
					input_points= self.a.getpoints(cv2.resize(image,(372,495)),sess,model_cfg,model_outputs)
					input_new_coords = np.asarray(self.a.roi(input_points)[0:34]).reshape(17,2)
					self.input_test.append(input_new_coords)
					i = i + 1
				else:
					break
			cap.release()
			final_score,score_list = self.s.compare(np.asarray(self.input_test),np.asarray(model_array),j,i)
		return final_score,score_list



	
	


