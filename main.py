import sys
from datetime import date
import qrcode

data = date.today()
img = qrcode.make(f'Setor de TI {data}')
img.show()
# print(img)

