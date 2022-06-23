def image2video():
	# 得到图像路径
	files = os.listdir("images/")
	# 对图像排序
	files.sort(key = lambda x: int(x.split(".")[0]))
	# 获取图像宽高
	h, w, _ = cv2.imread("images/" + files[0]).shape	
	# 设置帧数
	fps = 30

	vid = []
	'''
	设置要保存的格式
	mp4:
		mp4v 
	avi:
		xvid
		i420
	'''

	# 保存视频路径和名称
	#save_path = "video/video.mp4"		# 保存视频路径和名称 MP4格式
	save_path = "video/video.avi"		# 保存视频路径和名称 av格式

	# 准备写入视频
	vid = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
	# vid = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'xvid'), fps, (w, h))
	# vid = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'i420'), fps, (w, h))
	
	# 写入
	for file in files:
		img = cv2.imread("images/" + file)
		vid.write(img)
