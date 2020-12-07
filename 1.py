import sys
import os
from PIL import Image ,ImageChops
img1=Image.open("nassir1.jpg")
img2=Image.open("nassir.jpg")
diff=ImageChops.difference(img1,img2)
if diff.getbbox():
	diff.show()
	sys.stdout.write('voila la difference  ')
    
else :
	sys.stdout.write('cest le meme person  ')