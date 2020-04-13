import tensorflow as tf
import posenet
import numpy as np

class Pose(object):
	
	def getpoints(self,image_input,sess,model_cfg,model_outputs):
		sum = 0
		pos_temp_data=[]
		output_stride = model_cfg['output_stride']
		input_image, draw_image, output_scale = posenet.read_imgfile(
			image_input, scale_factor=1.0, output_stride=output_stride)

		heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = sess.run(
			model_outputs,
			feed_dict={'image:0': input_image}
		)

		pose_scores, keypoint_scores, keypoint_coords = posenet.decode_multiple_poses(
			heatmaps_result.squeeze(axis=0),
			offsets_result.squeeze(axis=0),
			displacement_fwd_result.squeeze(axis=0),
			displacement_bwd_result.squeeze(axis=0),
			output_stride=output_stride,
			max_pose_detections=1,
			min_pose_score=0.1)

		keypoint_coords *= output_scale

		for pi in range(len(pose_scores)):
			if pose_scores[pi] == 0.:
				break
			for ki, (s, c) in enumerate(zip(keypoint_scores[pi, :], keypoint_coords[pi, :, :])):	
				pos_temp_data.append(c[1])
				pos_temp_data.append(c[0])
			for ki, (s, c) in enumerate(zip(keypoint_scores[pi, :], keypoint_coords[pi, :, :])):
				pos_temp_data.append(s)
				sum = sum + s
			pos_temp_data.append(sum)
		return pos_temp_data


	def getpoints_vis(self,image_input,sess,model_cfg,model_outputs):
		sum = 0
		pos_temp_data=[]
		output_stride = model_cfg['output_stride']
		
		
		input_image, draw_image, output_scale = posenet.read_imgfile(
			image_input, scale_factor=1.0, output_stride=output_stride)

		heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = sess.run(
			model_outputs,
			feed_dict={'image:0': input_image}
		)

		pose_scores, keypoint_scores, keypoint_coords = posenet.decode_multiple_poses(
			heatmaps_result.squeeze(axis=0),
			offsets_result.squeeze(axis=0),
			displacement_fwd_result.squeeze(axis=0),
			displacement_bwd_result.squeeze(axis=0),
			output_stride=output_stride,
			max_pose_detections=1,
			min_pose_score=0.1)

		keypoint_coords *= output_scale

		black_image = np.zeros((draw_image.shape[0],draw_image.shape[1],3),dtype='uint8')

		black_image = posenet.draw_skel_and_kp(1,
					black_image, pose_scores, keypoint_scores, keypoint_coords,
					min_pose_score=0.1, min_part_score=0.0001)
		
		for pi in range(len(pose_scores)):
			if pose_scores[pi] == 0.:
				break
			for ki, (s, c) in enumerate(zip(keypoint_scores[pi, :], keypoint_coords[pi, :, :])):
				
				
				pos_temp_data.append(c[1])
				pos_temp_data.append(c[0])
			for ki, (s, c) in enumerate(zip(keypoint_scores[pi, :], keypoint_coords[pi, :, :])):
				pos_temp_data.append(s)
				sum = sum + s
			pos_temp_data.append(sum)
		
		return pos_temp_data,black_image

	
	def bounding_box(self,coords):

		min_x = 100000 
		min_y = 100000
		max_x = -100000 
		max_y = -100000

		for item in coords:
			if item[0] < min_x:
				min_x = item[0]

			if item[0] > max_x:
				max_x = item[0]

			if item[1] < min_y:
				min_y = item[1]

			if item[1] > max_y:
				max_y = item[1]
		return [(int(min_x),int(min_y)),(int(max_x),int(min_y)),(int(max_x),int(max_y)),(int(min_x),int(max_y))]

	def roi(self,imagepoints):
		coords_new_reshaped = imagepoints[0:34]
		coords_new = np.asarray(coords_new_reshaped).reshape(17,2)
		roi_coords = self.bounding_box(coords_new)
		coords_new = self.get_new_coords(coords_new, roi_coords)
		coords_new = coords_new.reshape(34,)
		coords_new = np.concatenate((coords_new[0:34],imagepoints[34:52]))
		return coords_new

	def get_new_coords(self,coords,fun_bound):
		coords[:,:1] = coords[:,:1] - fun_bound[0][0]
		coords[:,1:2] = coords[:,1:2] - fun_bound[0][1]
		return coords











