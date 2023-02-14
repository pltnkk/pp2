from datetime import datetime

def withoutmic(data):
    return data.replace(microsecond = 0)

data = datetime.now()

muew = withoutmic(data)
print("With microseconds: ", data)
print("Without microseonds: ", withoutmic(muew))
