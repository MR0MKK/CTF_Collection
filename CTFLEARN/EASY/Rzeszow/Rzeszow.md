# Rzeszow!

## Description

* This Reversing Challenge is designed to let solvers learn one of the techniques needed to solve my 100 point reversing challenge Rouen. Solve this challenge before Rouen. You may need to extract information from the exe using Ghidra then write a Python script to actually find the flag. Good Luck!
* [Attachement](https://ctflearn.com/challenge/download/1003)

## Solution

1. Using `DIE` , we found it was ELF file. 

       rzeszow: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=d238c7b8f6317abea459bd4c20aeac72c367a7d4, for GNU/Linux 3.2.0, not stripped

2. Using  `IDA64` to analys file



![Imgur](https://i.imgur.com/5kNZKic.png)

![Imgur](https://i.imgur.com/JUOdU1d.png)

![Imgur](https://i.imgur.com/zEp2viy.png)

Đề bài yêu cầu 9 kí tự đầu là `"CTFlearn{"` , kí tự cuối là `"}"`, số lượng kí tự là 20. Lưu ý `v12`,`v13` đều là biến không dấu.

Thực hiện kiểm tra từng kí tự với kí tự đã được mã hóa => dịch ngược nó thôi!!!

```
data = "W8Hj?1VESL^g4xwcvtW%humtEosd$Fq^dXPvi$#sSEe@o618Zl9.5PFrvC%O_E*LB%Igl8qur9SuLAp4MkK#pRzwJHI*Fn9mUs%mGK^RQKO.G*JFJvV%?VJpCpVF9eJuz5&kB!&_VF5DrF?U?jfm&x^9aC7X2(&cGGzbLbOsSOuBeq*ZT%fpc&9riTDO5X%RuTKI@vCqu#CsTAp$Q9WoXJv96.ySdB2EfMK*$NX?.U*aDrfPQQPhFB9cC6y0hMGvbgjBogSux65gTL#Cm9TQt7nTayu9Vr%thh2GnnikE8JnIwlHfreZep^sZ6IrnXT#qu50Lv.Rd_XPDfgwzWcJ3ISjKM!ftRllVyF$?RE_dcJT5&uKZJ!WsqR853uLzcs!8&VyRuTDsiq#6PdmBNlPI$tPi?wZ5$ACCf9yda!OkP.Dc73Nx.Nt1Rj0O.?P!sZDB^d0LN1qXR31!t?OZ#mm7SfZHPO*4gx1J0nyC^d2EKeq^f4h7mSqaIcMv0ZT@G0M"
characters = [chr(i) for i in range(0x20, 0x7E)]
flag = ""

v12 = 0x100000000 - 3
for i in range(10):
    v12 += 3
    for char in characters:
        index = ((v12 - 0x45520FF3) % (v12 - 0x100000000 + ord(char) ** 2 + ord(char) ** 3)) & 0x1FF
        enc_value = data[index]
        
        if enc_value == char:
            flag += char
            print("Value " + str(i) + ": " + char)
            break
            
print("Flag: " + flag)

```

* Flag:

```
CTFlearn{K0nstancja}
```