# instagram image dowbload
This script will download all/provided number of photos from the public instagram account

Usage:

python3 instaimg.py -u "username" -n <number of photos to be saved>(optional, default = all) -s <y or n> (optional)

Sample run:

python3 instaimg.py -u "sushantsinghrajput" -n 40 -s n 
This will run the script in exposed mode i.e. the browser will be visible nd first 40 images will be downloaded from the instagram account "sushantsinghrajput"

python3 instaimg.py -u "sushantsinghrajput"
This will run the script in  stealth i.e. the browser will not be visible and all images(+video thumbnails) will be downloaded from the instagram account "sushantsinghrajput"