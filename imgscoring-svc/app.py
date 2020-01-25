from flask import Flask, jsonify, make_response, request
import cv2
import numpy as np
from face import face_det
from grey import grey_scale
app = Flask(__name__)


@app.route("/imageScoring/score", methods=["POST"])
def imagescoring_score():
	# input
	file = request.files['yoyo']
	print('Posted file: %s' % (file))
	buf = file.read()
	#use numpy to construct an array from the bytes
	buf_array = np.fromstring(buf, dtype='uint8')
	img = cv2.imdecode(buf_array, 1)
	kordinat = face_det(img)
	abu = grey_scale(img)
	# print(img)
	# process something...
	resp_body = {
		'saturation': abu,
		'faceCoordinates': kordinat.tolist()
	}
	res = make_response(jsonify(resp_body), 200)
	return res
