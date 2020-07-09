#!/usr/bin/env python3
import os
import sys
import re
import subprocess

_photosPath = r"/Users/Deepthu/Desktop/videos"

class PhotoMetadata_v2(object):
	def __init__(self):
		super(PhotoMetadata_v2, self).__init__()
		for eachPhoto in [each for each in os.listdir(_photosPath) if each.endswith(".mp4")]:
			photoDate, photoTime = os.path.splitext(eachPhoto)[0][4:].split("_")
			photoDateTime = '{}:{}:{} {}:{}:{}'.format(photoDate[:4], photoDate[4:6], photoDate[6:8], photoTime[:2], photoTime[2:4], photoTime[4:6])
			# command = "/usr/local/bin/exiftool -overwrite_original -AllDates=\"{photoDate}\" \"{photoFile}\"".format(
			# 	photoDate=photoDateTime,
			# 	photoFile='{}/{}'.format(_photosPath, eachPhoto)
			# )
			command = "/usr/local/bin/exiftool -overwrite_original -FileCreateDate=\"{photoDate}\" -FileModifyDate=\"{photoDate}\" -Quicktime:CreateDate=\"{photoDate}\" \"{photoFile}\"".format(
				photoDate=photoDateTime,
				photoFile='{}/{}'.format(_photosPath, eachPhoto)
			)
			subprocess.call([command], shell=True)


if __name__ == '__main__':
	app = PhotoMetadata_v2()