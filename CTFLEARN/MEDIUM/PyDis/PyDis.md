# PyDis!

## Description

* You like python don't you, but do you like dis type of python. This will be helpful: https://docs.python.org/3/library/dis.html
* [Attachement](https://ctflearn.com/challenge/download/976)

## Solution

1. Hàm `func2` thực hiện `return tmp1 ^ tmp2`

2. Hàm `func` thực hiện mở file `"flag.txt"` đọc và lưu và `cipher`. Truyền `cipher` và `biến đếm vòng lặp` và 170 rồi cho hàm `func2` , lưu vào `encrypted_flag.txt`.

Ta có chương trình python được viết lại như sau:
```
def func2(c2, c1):
    tmp1 = c2
    tmp2 = c1
    result = tmp1 ^ tmp2
    return result

def func():
    fp = open('flag.txt')
    cipher = ''

    for i in range(len(fp)):
        result = i ^ fp[i]
        temp = result ^ 170
        cipher += chr(temp)

    print(cipher)
    
    with open('encrypted_flag.txt', 'w') as f:
        f.write(cipher)

func()
```
Vậy thì giải nó thôi
```
data = "éÿîÅËÎÞÃÙóÙÕÎÈÊúèÞÎÜÌÌÕÓÕìùÂéçÆÐþÿñÖËîÿôÿ"
flag = ''.join(chr(ord(c) ^ i ^ 170) for i, c in enumerate(data))
print(flag)

```
* Flag:

```
CTFlearn{Python_Reversing_Is_Pretty_Easy}
```