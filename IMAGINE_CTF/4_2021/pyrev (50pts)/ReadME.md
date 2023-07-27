# pyrev!

## Description

* I think it's time for a dis.dis() track...
* [Attachement](https://imaginaryctf.org/r/7F0C-out.txt)

## Solution
Đoạn bytecode tương đối dễ đọc. Hàm nhận tham số n, lần lượt `-=n` với phần tử trong data => chuyển thành `char`. BruceForce tìm tham số n ban đầu.

```
def f(n):
    for x in [0, 6, -17, 14, -21, 25, -23, 5, 15, 2, -12, 11, -1, 6, -4, -12, -6, 9, 8, 5, -3, -3, 6, -6, 4, -18, -6, 26, -2, -18, 20, -17, -9, -4]:
        n -= x
        print(chr(n), end="")
    print()

f(105)

```
* Flag:
```
ictf{bytecode_could_be_easy_as_py}
```