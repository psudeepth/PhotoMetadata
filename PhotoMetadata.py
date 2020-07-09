#!/usr/bin/env python3
import os
import sys
import re
import subprocess
from geopy.geocoders import Nominatim

_filenamePattern = re.compile(r"\d{4}-\d{2}-\d{2}_[a-zA-Z]*, [a-zA-Z]*$")


def main(arg):
	result = ""
	for eachPhoto in arg:
		if eachPhoto != __file__:
			filename, ext = os.path.splitext(os.path.basename(eachPhoto))
			if ext == '.jpg':
				if _filenamePattern.search(filename):
					photoDate, location = filename.split("_")
					geolocator = Nominatim(user_agent='PhotoMetadata')
					location = geolocator.geocode(location)
					locationRawData = location.raw
					command = "/usr/local/bin/exiftool -overwrite_original -AllDates=\"{photoDate}\" -GPSLatitude=\"{lat}\" -GPSLongitude=\"{lon}\" \"{photoFile}\"".format(
						photoDate='{} 10:10:10'.format(photoDate.replace("-", ":")),
						lat=locationRawData.get('lat'),
						lon=locationRawData.get('lon'),
						photoFile=eachPhoto
					)
					subprocess.call([command], shell=True)
					result += '{}.{} - Successfully updated the file.\n'.format(filename, ext)
				else:
					result += '{}.{} - Filename does not match with the pattern.\n'.format(filename, ext)
			else:
				result += '{}.{} - Only jpg files accepted.\n'.format(filename, ext)

	print(result)


if __name__ == '__main__':
	main(sys.argv)
