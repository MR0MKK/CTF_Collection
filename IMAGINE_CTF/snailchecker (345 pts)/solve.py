import math

def find_n(target_sum):
    n = int(math.log2(target_sum + 1) - 1)
    return n
def sum_of_series(n):
    return 2**(n + 1) + 1

def main():
    data = [1290323666, 1725879542, 1792073930, 1692450534, 1255720158, 1625734874, 1053346506, 1591664324, 1591664350, 2062083806]
    solve_data = [0]*len(data)
    no1 = 2 ** 24
    no2 = 2 ** 16
    no3 = 2 ** 8


    for char1 in range(0x30, 0x7E):
        for char2 in range(0x30, 0x7E):
            for char3 in range(0x30, 0x7E):
                for char4 in range(0x30, 0x7E):
                    value = ((char1) * no1 + (char2) * no2 + (char3) * no3 + (char4) + 1)
                    a = (value - sum_of_series(find_n(value))) * 2
                    if a in data:
                        string = chr(char1) + chr(char2) + chr(char3) + chr(char4)
                        solve_data[data.index(a)]=string[::-1]
    flag ="".join(solve_data)
    print(flag)
if __name__ == "__main__":
    main()
