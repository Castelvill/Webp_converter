from PIL import Image
import glob
import os
import sys


where = ""
if len(sys.argv) >= 2:
	where = sys.argv[1] + '\\'

webps = glob.glob(where+'*.webp')


for img in webps:
	im = Image.open(img).convert("RGB")
	im.save(img.split(".")[0]+".bmp")
	os.remove(img)
	
print(f"Updated: {len(webps)}")