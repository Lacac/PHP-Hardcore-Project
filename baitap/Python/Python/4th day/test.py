import sys
from string import ascii_lowercase, ascii_uppercase

password = "8jjdKHch67152HJdnksiP"
test = ascii_lowercase + ascii_uppercase + "1234567890"

if(len(sys.argv) == 1 or len(sys.argv) > 4):
    sys.exit("test.py <Host> <Cookie> <Time delay>")

try:
    URL = sys.argv[1]
    COOKIE = dict(item.split("=") for item in sys.argv[2].split("; "))
    TIME_DELAY = int(sys.argv[3])
except:
    sys.exit("test.py <Host> <Cookie> <Time delay>")

print(URL.split("://")[1])
print(COOKIE)
print(type(TIME_DELAY))

for i in range(1,20):
    COOKIE['TrackingId'] = i
    print(COOKIE['TrackingId'])

length = len(test)
mid = int(length / 2)
first = test[0]
last = test[-1]

# for i in range(1, length + 1):
#     pass

print('a' >'A')