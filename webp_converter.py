from PIL import Image
import glob
import os
import sys


where = ""
if len(sys.argv) >= 2:
	where = sys.argv[1] + '\\'

webps = glob.glob(where+'*.webp')
#webps = glob.glob(where+'**/*.webp', recursive=True)

for img in webps:
	im = Image.open(img).convert("RGB")
	im.save(img.split(".webp")[0]+".jpg", jpeg)
	os.remove(img)
	
print(f"Updated: {len(webps)}")
