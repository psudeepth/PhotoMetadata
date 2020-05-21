import sys
import os
import subprocess
from geopy.geocoders import Nominatim


def main(arg):
	for eachPhoto in arg:
		if eachPhoto != __file__:
			filename, ext = os.path.splitext(os.path.basename(eachPhoto))
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


if __name__ == '__main__':
	main(sys.argv)
