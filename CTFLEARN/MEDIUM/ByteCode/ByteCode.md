# ByteCode!

## Description

* I dunno what bytecode is. Could you tell me what input of 'checkNum' will return true? The flag is just a 32-bit signed integer as a decimal (nothing else.)
* [Attachement](https://mega.nz/#!qfATFaKR!zaTNExq3Bm1MjJnePjTGQyvnvLX_xZxhbGaMv_ypaxo)

## Solution

1. Đề cho ta file bytecode.txt. Đây là một tập các câu lệnh dành cho Java Virtual Machine, khi thực hiện chương trình java thì bytecode được sinh ra. Nội dung tham khảo [Link](https://en.wikipedia.org/wiki/List_of_Java_bytecode_instructions).  Phân tích nội dung ta được như sau:


![Imgur](https://i.imgur.com/fBqgi3C.png)
    

2. Ta có thể viết lại chương trình thành:

![Imgur](https://i.imgur.com/COvgw0D.png)

Khi thay hết tất cả ta có: `(num << 3) ^ num ^ 525024598 == -889275714` => `(num << 3) ^ num  == -889275714 ^ 525024598`. `-889275714 ^ 525024598` chuyển về cơ số 16 ta được `0xd5b587e8`

Tôi tính làm tay nhưng thôi, code cho vui. Giá trị tìm được là `-1352854872`


```
#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable : 4146)
void BruteForce()
{
    int flag, x1, x2, x3;
    flag = -2147483648; // The biggest negative value of 32bit.
    x3 = 0;
    while (x3 != -889275714)
    {
        x1 = flag << 3;
        x2 = flag ^ 525024598;
        x3 = x1 ^ x2;
        flag += 1;
    }
    printf("%d \n", flag - 1);
}

void main()
{
    BruteForce();
    system("pause");
}
```


* Flag:

```
CTFlearn{-1352854872}
```