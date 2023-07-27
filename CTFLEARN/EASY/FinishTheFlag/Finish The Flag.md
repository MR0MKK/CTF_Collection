# Finish The Flag!

## Description

* I received a strange letter in the mail, when I unfolded the document inside, I discovered this matrix bar code. Can you figure out what it contains?
* [Attachement](https://ctflearn.com/challenge/download/1122)

## Solution

1. Using  `https://zxing.org/w/decode.jspx` to decode QR code, ta có Raw text. Nhìn phát biết ngay phải dùng base64 để decode. Ta được một ELF file, lưu về thôi

![Imgur](https://i.imgur.com/PSgWInp.png)

2. Dùng `IDA` để phân tích chương trình

![Imgur](https://i.imgur.com/7f5CGHi.png)

Chương trình cộng chuỗi `"CTFlearn{"` và một chuỗi cần tính toán => kết quả thu được là `"QR_v30}"`
```
key = [70, 69, 72, 97, 36, 39, 106]
flag = "".join(chr(k ^ 0x17) for k in key)
print(flag)


print("Kết quả cuối cùng:", parameter)
```

* Flag:

```
CTFlearn{QR_v30}
```