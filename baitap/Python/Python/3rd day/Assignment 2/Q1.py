import re

text = u"Sau khi dịch covid-19 bùng phát giá dầu giảm còn 10.5%, giá điện giảm 15%, giá khẩu trang tăng 300%"

print("danh sach phan tram giam:")
print(", ".join(re.findall("(?<=giảm)[^\d]+([\d\.]+%)", text)))
print("=======================")
print("danh sach phan tram tang: ")
print(",".join(re.findall("(?<=tăng)[^\d]+([\d\.]+%)", text)))