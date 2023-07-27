# Raspberry!

## Description

* If you want to start learning some assembly language programming to build the skills needed to solve some of the more difficult reversing challenges, then step through the debugger and examine the registers to see how each each letter in the flag is determined to be correct or incorrect. is a beginners Reversing Challenge. It is build with the optimization level set to 0 so that the assembler is more readable. If you are new to reversing, please remember that to solve Reversing challenges you probably need to know some C/C++, Assembler and also some experience with gdb (the gnu debugger). And maybe Ghidra
* [Attachement](https://ctflearn.com/challenge/download/1080)

## Solution

1. Using `DIE` , we found it was ELF file. 

       raspberry: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, with debug_info, not stripped

2. Using  `IDA64` to analys file



![Imgur](https://i.imgur.com/0Uaiwrv.png)

![Imgur](https://i.imgur.com/NT327r4.png)

![Imgur](https://i.imgur.com/v5OlXbg.png)

![Imgur](https://i.imgur.com/hjLqHyE.png)

Hàm `FillInStrings` tạo mảng `strings` 16 phần tử và lưu các chuỗi vào từng phần tử

![Imgur](https://i.imgur.com/wEEQKCr.png)

Quá nhiều tính toán ~.~!!! Mình chả muốn dùng giấy, bút , máy tính để giải bài này đâu!! Code thôi!!

Chương trình nhận tham số chính là Flag, nhận thấy khi ta nhập sai sẽ có các trường hợp sau:
>	Bad Character:

>	Your flag is too long dude!

>	Your flag is too short bruh!

Nếu nhập đúng thì kiểm tra kí tự tiếp theo => quá dễ rồi.

```
import subprocess

file_path = "./Raspberry"
parameter = "CTFlearn{"

characters = [chr(i) for i in range(0x20, 0x80)]

for char in characters:
    new_parameter = parameter + char

    try:
        output = subprocess.check_output([file_path, new_parameter], stderr=subprocess.STDOUT)
        output_str = output.decode('utf-8')
        if "Bad" not in output_str:
            parameter = new_parameter

            if(char == "}"):
                break
    except subprocess.CalledProcessError as e:
        print("Lỗi khi thực thi file ELF:", e.output.decode('utf-8'))

print("Kết quả cuối cùng:", parameter)
```
Do máy hơi yếu nên phải chạy 2 lần và dùng lại các dữ liệu cũ
![Imgur](https://i.imgur.com/CVXmikI.png)

* Flag:

```
CTFlearn{+Fruit123}
```