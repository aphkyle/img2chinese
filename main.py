import sys

import numpy as np
from PIL import Image

ok = ''
cmap = ['，', "龙", "龎", "龖", '𪚥']

img = Image.open(sys.argv[1])
img = img.convert('L')
n = int(sys.argv[2])
oaasfsd = (1 - n/100)
img = img.resize(map(int, (img.width * oaasfsd, img.height * oaasfsd))) # downsize n%
img = img.quantize(5)

for eee in np.array(img):
    for ddd in eee:
        ok += cmap[ddd]
    ok += '\n'

print(ok, file=open("test.txt", "w", encoding="utf8"))
img.show()
