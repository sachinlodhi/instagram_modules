
# instagram image dowbload
This script will download all/provided number of photos from the public instagram account

Usage:

python3 instaimg.py -u "username" -n <number of photos to be saved>(optional, default = all) -s <y or n> (optional)

Sample run:

python3 instaimg.py -u "sushantsinghrajput" -n 40 -s n 
This will run the script in exposed mode i.e. the browser will be visible nd first 40 images will be downloaded from the instagram account "sushantsinghrajput"

python3 instaimg.py -u "sushantsinghrajput"
This will run the script in  stealth i.e. the browser will not be visible and all images(+video thumbnails) will be downloaded from the instagram account "sushantsinghrajput"

Dependencies:
1) Driver(GeckoDriver/Chrome Driver)
2) Selenium
3) Python3 (recommended)

Note: While using in terminal use python3 not python or it may cause some unwanter error.



Caution : This script is for educational and research purposes only. I am not liable for any damage done by exploiting this. User of this program must take permission from the instagram or instagram account owner for the actual use.
