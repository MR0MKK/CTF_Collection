# Rotterdam!

## Description

* The flag is encoded using xor, add, sub, mul and div operations. The flag kernel is of the form a_b_c_d_e where each letter corresponds to a short word. Each word is based on a single math operation. There is a function GetTData used to retrieve constants used to hide the flag via math operations. There is no need to step into GetTData... when the function returns the constant is in the rax register.
* [Attachement](https://ctflearn.com/challenge/download/1076)

## Solution

Using `DIE` , we found it was ELF file.

        Rotterdam: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, not stripped
    
Dùng `IDA` để phân tích chương trình, bài này bao gồm có khá nhiều bước. `Flag` sẽ có 64 kí tự - công việc dài đây!!!! Việc phân tích data trong file là bất khả thi nên mình chỉ Debug từ từ thôi!!! 

Lưu ý quan trọng: 

-   Trong bài dùng rất nhiều `RAX`,`RBX`, và ta cần Debug để biết giá trị `RAX`,`RBX` để dùng. 
-   Tất cả giá trị lưu trong thanh ghi đều ở dạng Little Endian nên phải đảo chuỗi

Step 1: Tham số lưu vào RAX và chương trình tạo RBX

![Imgur](https://i.imgur.com/l8PIBkS.png)
```
RBX = 0x2A460D92F5A1F504
XOR_value = 0x4B227FF781D59A56
value = hex(RBX^XOR_value)
print(bytes.fromhex(value[2:]).decode('utf-8')[::-1])

#Rotterda
```

Step 2: Kiểm tra kí tự tiếp theo có là `"_"`

![Imgur](https://i.imgur.com/dASmlyp.png)

Step 3: Tham số lưu vào RBX và chương trình tạo RAX. Sau đó kiểm tra kí tự tiếp theo có là `"_"`

![Imgur](https://i.imgur.com/j0pX2wv.png)

![Imgur](https://i.imgur.com/gLG39Ml.png)
```
RAX = 0xE2F2CEF6
ADD_value = 0x15764FF46
value = hex(ADD_value-RAX)
print(bytes.fromhex(value[2:]).decode('utf-8')[::-1])

#P0rt
```


Step 4: Dữ liệu được nhập lưu vào `RCX` và chương trình tạo `RAX`, `RBX`. Kiểm ta `RCX & RAX > RBX & RAX`. Cần thực hiện `AND 0xFFFFFFFFFF` nhưng tôi bỏ qua. 

-   Đây là ảnh khi chưa `AND 0xFFFFFFFFFF`

![Imgur](https://i.imgur.com/pnizPRR.png)

-   Đây là ảnh khi đã `AND 0xFFFFFFFFFF`

![Imgur](https://i.imgur.com/5xiDYhq.png)

![Imgur](https://i.imgur.com/5YGEgJo.png)

```
RBX = 0x4D998C32FF
SUB_value = 0x17D4A53553
value = hex(SUB_value+RBX)
print(bytes.fromhex(value[2:]).decode('utf-8')[::-1])

#Rh1ne
```

Step 5: Dữ liệu được nhập lưu vào `RAX` và `mul RBX`. Giá trị sẽ được lưu vào `RAX`, do tràn số nên dữ liệu tràn lưu ở `RDX`. Lưu ý `00000000004013B8 mov     rax, 037F7D400A77B9BEh`

![Imgur](https://i.imgur.com/Yqb69tX.png)

![Imgur](https://i.imgur.com/z6uI89S.png)

```
RBX = 0xDEB4FA4D998C32FF
MUL_value = 0x6A87544938037F7D400A77B9BE
value = hex(int(MUL_value/RBX))
print(value)
print(bytes.fromhex(value[2:]).decode('utf-8')[::-1])

#Bl1tz
```

Step 6: Dữ liệu được nhập lưu vào `RCX` và chương trình tạo `RBX`. Thương được lưu vào RAX, số dư lưu vào RDX.


![Imgur](https://i.imgur.com/livrtcX.png)

```
RBX = 0x1F6FF5218C40DE9C
DIV_value = 0x4F5352
MOLDULE_vaule = 0x55930DBBE
value = (hex(int((RBX-MOLDULE_vaule)/DIV_value)))
print(bytes.fromhex(value[2:]).decode('utf-8')[::-1])

#W1tte
```

* Flag:

```
CTFlearn{Rotterda_P0rt_Rh1ne_Bl1tz_W1tte}
```