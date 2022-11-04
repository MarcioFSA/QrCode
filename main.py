import sys
from datetime import date, datetime
import qrcode

data = datetime.today()
img = qrcode.make(f'Setor de TI {data}')
img.show()
# print(img)

