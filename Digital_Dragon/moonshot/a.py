def main():
    v18 = 0
    v27 = 1
    v26 = 0x1010101
    v25 = 0x2020202
    v24 = 0x4040404
    v23 = 0x8080808
    v22 = 0x10101010
    v21 = 0x20202020
    v20 = 0x40404040
    v19 = 0x80808080

    for i in range(64):
        j = (i >> 0) & 1
        k = (i >> 1) & 1
        m = (i >> 2) & 1
        n = (i >> 3) & 1
        ii = (i >> 4) & 1
        jj = (i >> 5) & 1
        kk = (i >> 6) & 1

        # print("I'm thinking of a number between negative infinity and infinity...")
        v18 = 1#int(input())

        if v27 == (v19 & v20 & v21 & v22 & v23 & v24 & v25 & v26):
            print("flag{")
        elif v26 == v25:
            print("r3d_h3rr1ng")
        elif v25 == v24:
            print("}")
        if (v27 & v18) != 0:
            v3 = v26 if j else 0
            v4 = v25 if k else 0
            v5 = v4 | v3
            v6 = v24 if m else 0
            v7 = v6 | v5
            v8 = v23 if n else 0
            v9 = v8 | v7
            v10 = v22 if ii else 0
            v11 = v10 | v9
            v12 = v21 if jj else 0
            v13 = v12 | v11
            v14 = v20 if kk else 0
            v15 = v14 | v13
            v16 = v19 if ii else 0
            if v16 != 0:
                print(i,hex(v15),hex(v16),hex(v15 | v16))
            if (v27 | v18) == (v15 | v16):
                return
            if (v18+1) > 3:
                return


if __name__ == "__main__":
    main()

