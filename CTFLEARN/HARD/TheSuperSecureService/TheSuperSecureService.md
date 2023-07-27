# [Lost In The Binary](../LostInTheBinary/LostInTheBinary.md)!

## Description

* My friend sent me this link: https://thekidofarcrania.github.io/MACObs/index.html to some sort of MAC checking service. I have no clue how it works, but it claims it is secure. Can you figure out the "password" used to sign the message that they provided? lost a flag inside this binary, please help me to find it. If you trigger certain anti-debugging techniques, you might get 1 flags…. flag format: FLAG-(str)
* [Attachement](https://thekidofarcrania.github.io/MACObs/index.html)

## Solution
Yêu cầu đề bài nhập đúng `password` với `message` và `signature` được cho!!

![Imgur](https://i.imgur.com/Sg8VgFb.png)



Ta thử nhập theo code.dat vào và xem lại source code:

```

msg = ["You fail!", "Seriously?", "Ha! Ha! You wish it was right!", "Correct! (jkjk its wrong lol)", "stap tryin! youll nvr git it right!", "<code>throw 'you tried'; //throwing something you can catch!</code>", "just give up!", "y0u n00b! R U just bru13 f0rc1ng?"]
tries = 0;
function check() {
    try {
        $ = document.getElementById.bind(document);
        j = window.d0cument;
        check2();

        $("resp").innerText = "Correct! (Oh gosh! I guess you've done it...)";
        $("resp").className = "good";
    } catch (e) {
        if (tries >= msg.length)
            tries = 0;
        $("resp").innerHTML = msg[tries];
        $("resp").className = "error";
        tries++;
    }
}

function check2() {
    //Randomizer taken from https://stackoverflow.com/a/19301306/7344257 code
    var m_w = 123456789;
    var m_z = 987654321;
    var mask = 0xffffffff;

    // Takes any integer
    function seed(i) {
        m_w = i;
    }

    function random() {
        m_z = (36969 * (m_z & 65535) + (m_z >> 16)) & mask;
        m_w = (18000 * (m_w & 65535) + (m_w >> 16)) & mask;
        var result = ((m_z << 16) + m_w) & mask;
        return result
    }

    //Ignore this code... This is the magical part of this verifier
    var _0xda23 = ["\x63\x68\x61\x72\x43\x6F\x64\x65\x41\x74", "\x63\x61\x6C\x6C", "\x72\x65\x64\x75\x63\x65", "\x70\x72\x6F\x74\x6F\x74\x79\x70\x65", "", "\x6C\x65\x6E\x67\x74\x68", "\x66\x72\x6F\x6D\x43\x68\x61\x72\x43\x6F\x64\x65", "\x73", "\x78", "\x62\x61\x64", "\x76\x61\x6C\x75\x65", "\x63\x6F\x64\x65", "\x70\x6F\x77", "\x66\x6C\x61\x67\x7B", "\x73\x74\x61\x72\x74\x73\x57\x69\x74\x68", "\x73\x75\x62\x73\x74\x72", "\x7D", "\x73\x70\x6C\x69\x74", "\x74\x65\x73\x74", "\x5F", "\x6C\x6F\x67", "\x66\x6C\x6F\x6F\x72", "\x73\x69\x67\x6E", "\x6D\x73\x67"];
    function hash(_0x7a95x2) {
        var _0x7a95x3 = 0xffffffff;
        return Array[_0xda23[3]][_0xda23[2]][_0xda23[1]](_0x7a95x2, function(a, b) {
            return (a * 31 + b[_0xda23[0]](0)) & _0x7a95x3
        }, 0)
    }
    function xor(_0x7a95x7, _0x7a95x8) {
        var z = _0xda23[4];
        for (var i = 0; i < _0x7a95x7[_0xda23[5]]; i++) {
            z += String[_0xda23[6]](_0x7a95x7[_0xda23[0]](i) ^ _0x7a95x8)
        }
        ;return z
    }
    function xor2(_0x7a95x7, _0x7a95x8) {
        var z = _0xda23[4];
        for (var i = 0; i < _0x7a95x7[_0xda23[5]]; i++) {
            z += String[_0xda23[6]](_0x7a95x7[_0xda23[0]](i) ^ (_0x7a95x8[_0xda23[0]](i % _0x7a95x8[_0xda23[5]]) & 15))
        }
        ;return z
    }
    function decode(_0x7a95xd, _0x7a95xe, _0x7a95xf) {
        x = _0x7a95xf % 2;
        y = _0x7a95xe[_0xda23[0]]((_0x7a95xf - x) / 2);
        if (!x) {
            y >>= 4
        }
        ;y &= 0xf;
        return xor(_0x7a95xd, y)
    }
    function runcode(_0x7a95x11, _0x7a95xd, _0x7a95xe) {
        _0x7a95xd = decode(_0x7a95xd, _0x7a95xe, 0);
        try {
            var _0x7a95x12 = {
                x: _0x7a95xd,
                d: decode,
                k: _0x7a95xe,
                o: xor2,
                s: _0x7a95x11
            };
            var _0x7a95xf = 0;
            for (var i = 0; i < _0x7a95xe[_0xda23[5]] * 2; i++) {
                new Function(_0xda23[7],_0x7a95x12[_0xda23[8]])(_0x7a95x12)
            }
            ;return _0x7a95x12[_0xda23[7]]
        } catch (e) {
            throw _0xda23[9]
        }
    }
    seed(18458);
    j++;
    input = $(_0xda23[11])[_0xda23[10]];
    var a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z;
    a = 1;
    0 = (j == j);
    1 = !0;
    b = Math[_0xda23[12]](++a, a + ++a + 0) - 1 + 0;
    c = Math[_0xda23[12]](a++ - 1, a += 2) - 1;
    d = (random() + random()) & b;
    if (!input[_0xda23[14]](_0xda23[13]) || input[_0xda23[15]](-1) != _0xda23[16] || hash(input) != -1996285287 || input[_0xda23[5]] != (random() & c)) {
        throw _0xda23[9]
    }
    ;f = random() & b - d;
    input = input[_0xda23[15]](a)[_0xda23[17]](_0xda23[16])[+0];
    if (!/^[A-Za-z0-9_]+$/[_0xda23[18]](input)) {
        throw _0xda23[9]
    }
    ;f *= f;
    input = input[_0xda23[17]](_0xda23[19]);
    if (input[_0xda23[5]] != f || input[1][_0xda23[5]] != f - 1 - 0 || input[1][1] != 'R') {
        throw _0xda23[9]
    }
    ;try {
        seed(parseInt(input[0 + 0]));
        g = ~random() ^ hash(input[2]) ^ hash(input[f - 1 + 0]);
        console[_0xda23[20]](g);
        if (g != 1865600952) {
            throw _0xda23[9]
        }
    } catch (e) {
        throw _0xda23[9]
    }
    ;seed(97632000);
    e = Math[_0xda23[21]](b / (1 - 0 + 1));
    c = (random() >> (e - 0 + 1)) & b;
    d = (random() >> (e - 0 + 1)) & b;
    if (input[2 - 0][_0xda23[5]] != c - d) {
        throw _0xda23[9]
    }
    ;if (input[d] != runcode($(_0xda23[22])[_0xda23[10]], xor($(_0xda23[23])[_0xda23[10]], c - d), input[2])) {
        throw _0xda23[9]
    }
}

```

Tại `_0xda23` ta dự đoán đây gồm các chuỗi đã được mã hóa sang hexa, từ đó mà ta biết đây là nơi để gọi xây dựng flag.

```
['charCodeAt', 'call', 'reduce', 'prototype', '', 'length', 'fromCharCode', 's', 'x', 'bad', 'value', 'code', 'pow', 'flag{', 'startsWith', 'substr', '}', 'split', 'test', '_', 'log', 'floor', 'sign', 'msg']

0 charCodeAt
1 call
2 reduce
3 prototype
4
5 length
6 fromCharCode
7 s
8 x
9 bad
10 value
11 code
12 pow
13 flag{
14 startsWith
15 substr
16 }
17 split
18 test
19 _
20 log
21 floor
22 sign
23 msg
```
Khó nhìn quá!! Sửa tên nó thui, khỗ vãi loiz ~.~
```
msg = ["You fail!", "Seriously?", "Ha! Ha! You wish it was right!", "Correct! (jkjk its wrong lol)", "stap tryin! youll nvr git it right!", "<code>throw 'you tried'; //throwing something you can catch!</code>", "just give up!", "y0u n00b! R U just bru13 f0rc1ng?"]
tries = 0;
function check() {
    try {
        $ = document.getElementById.bind(document);
        j = window.d0cument;
        check2();

        $("resp").innerText = "Correct! (Oh gosh! I guess you've done it...)";
        $("resp").className = "good";
    } catch (e) {
        if (tries >= msg.length)
            tries = 0;
        $("resp").innerHTML = msg[tries];
        $("resp").className = "error";
        tries++;
    }
}

function check2() {
    var m_w = 123456789;
    var m_z = 987654321;
    var mask = 0xffffffff;

    function seed(i) {
        m_w = i;
    }

    function random() {
        m_z = (36969 * (m_z & 65535) + (m_z >> 16)) & mask;
        m_w = (18000 * (m_w & 65535) + (m_w >> 16)) & mask;
        var result = ((m_z << 16) + m_w) & mask;
        return result
    }

    var _0xda23 = ['charCodeAt', 'call', 'reduce', 'prototype', '', 'length', 'fromCharCode', 's', 'x', 'bad', 'value', 'code', 'pow', 'flag{', 'startsWith', 'substr', '}', 'split', 'test', '_', 'log', 'floor', 'sign', 'msg'];
    function hash(input) {
        return Array['prototype']['reduce']['call'](input, function (a, b) {
            return (a * 31 + b['charCodeAt'](0)) & 0xffffffff
        }, 0)
    }
    function xor(s, key) {
        var z = ' ';
        for (var i = 0; i < s['length']; i++) {
            z += String['fromCharCode'](s['charCodeAt'](i) ^ key)
        }
        ; return z
    }
    function xor2(s, key) {
        var z = ' ';
        for (var i = 0; i < s['length']; i++) {
            z += String['fromCharCode'](s['charCodeAt'](i) ^ (key['charCodeAt'](i % key['length']) & 15))
        }
        ; return z
    }
    function decode(msgAfterXOR, input2, _0x7a95xf) {
        x = _0x7a95xf % 2;
        y = input2['charCodeAt']((_0x7a95xf - x) / 2);
        if (!x) {
            y >>= 4
        }
        ; y &= 0xf;
        return xor(msgAfterXOR, y)
    }
    function runcode(signature, msgAfterXOR, input2) {
        msgAfterXOR = decode(msgAfterXOR, input2, 0);
        try {
            var _0x7a95x12 = {
                x: msgAfterXOR,
                d: decode,
                k: input2,
                o: xor2,
                s: signature
            };
            var _0x7a95xf = 0;
            for (var i = 0; i < input2['length'] * 2; i++) {
                new Function('s', _0x7a95x12['x'])(_0x7a95x12)
            }
            ; return _0x7a95x12['s']
        } catch (e) {
            throw 'bad'
        }
    }
    seed(18458);
    j++;
    input = $('code')['value'];
    var a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z;
    a = 1;                                             //  a = 6
    b = Math['pow'](++a, a + ++a + 0) - 1 + 0;         //  b = 31
    c = Math['pow'](a++ - 1, a += 2) - 1;          //  c = 63
    d = (random() + random()) & b;                                  //  d = 13
    if (!input['startsWith']('flag{') || input['substr'](-1) != '}' || hash(input) != -1996285287 || input['length'] != (random() & c)) {
        throw 'bad'
    }
    ; f = random() & b - d;         // f = 2 
    input = input['substr'](a)['split']('}')[+0];
    if (!/^[A-Za-z0-9_]+$/['test'](input)) {
        throw 'bad'
    }
    ; f *= f;          // f = 4                 
    input = input['split']('_');
    if (input['length'] != 4 || input[1]['length'] != 3 || input[1][1] != 'R') {
        throw 'bad'
    } t
        ; try {
            seed(parseInt(input[0 + 0]));
            g = ~random() ^ hash(input[2]) ^ hash(input[3]);
            console['log'](g);
            if (g != 1865600952) {
                throw 'bad'
            }
        } catch (e) {
            throw 'bad'
        }
    ; seed(97632000);
    e = Math['floor'](b / (2));         // 15
    c = (random() >> (e + 1)) & b;      // 14 
    d = (random() >> (e + 1)) & b;      // 3 
    if (input[2]['length'] != c - d)    // != 11 
        throw 'bad'
    }
    ; if (input[3] != runcode($('sign')['value'], xor($('msg')['value'], c - d), input[2])) {
        throw 'bad'
    }
}


```

Lưu ý: `j`  là NaN - not a number => True = 0 và False = 1. Hãy Debug để tìm các giá trị của a, b, c, d, e, f

Đầu tiên nó kiểm tra có bắt đầy bằng `flag{`, kết thúc bằng `}` và độ dài là `36` (giá trị của `random() & c` ). Đồng thời kiểm tra giá trị hash nhưng lười tính quá. Giá trị trong `{  }` kiểm tra liệu có chữ thường, chữ hoa, số và dấu ' _ ' => tách thành các chuỗi bởi dâu ' _ '.

Dự kiến nó sẽ được chia thành 4 đoạn, `input[0]` có 4 kí tự, `input[1]` có 3 kí tự và kí tự thứ 2 là 'R'. Với seed là `input[0]`,`input[2]` và `input[3]` thực hiện tính toán `1865600952 = ~random() ^ hash(input[2]) ^ hash(input[3]).` 

Hàm `Runcode` gồm các tham số: `signature`, xor(`message`,11), input[2] để tính input[3]. Ta sẽ tính input[2] -> bruceforce input[0] -> input[3] -> bruceforce input[4]


* Flag:
```                                                                     
flag{7631_pR0_0BfuSc4t1on_a3Bn9cQWv}
```
