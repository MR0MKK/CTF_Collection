import math
O = [00, 0x52, 0x00, 0x0e, 0x00, 0x00, 0x01, 0x76, 0x37, 0x1d, 0x1f, 0x47, 0xf3, 0x40, 0x1d, 0x31, 0x7b, 0xed, 0x73, 0x71, 0x00, 0x06, 0x0c, 0x07, 0x11, 0x00, 0x3f, 0x3f, 0x3f, 0x3f, 0x3f, 0x42, 0x76, 0x21, 0x67, 0x72, 0x25, 0x49, 0x70, 0x21, 0x66, 0x2f, 0x47, 0x30, 0x6f, 0x70, 0x38, 0x70, 0x48, 0x48, 0x50, 0x35, 0x31, 0x5f, 0x7a, 0x49, 0x5f, 0x6b, 0x47, 0x3f, 0x3f, 0x3f, 0x3f,
     0x3f, 0x3f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x31, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x92, 0x84, 0x6c, 0x41, 0x17, 0xa8, 0x6c, 0x2b, 0xb3, 0x5d, 0x68, 0x60, 0xf5, 0x1f, 0x01, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

stack = []

a = 0


def Add_Value(arr, values):
    values = values[::-1]
    for value in values:
        arr.append(value)
    return 37


def Assign_Value(arr, index, value):
    arr[index] = value


def Clear_Stack(arr):
    arr.clear()


my_functions = [
    # () -> O[4] < O[3] ? e(3, 0) : e(25),
    lambda: Add_Value(
        stack, [3, 0]) if O[4] < O[3] else Add_Value(stack, [25]),
    # () -> O[20] = O[0],
    lambda: Assign_Value(O, 20, O[0]),
    # () -> {aa.clear();return 0;},
    lambda: Clear_Stack(stack),
    # () -> e(16, 9, O[O[1] - 1], 25, 5, 19) + (O[5] = (byte)(6 + O[4])),
    lambda: Add_Value(stack, [16, 9, O[O[1]-1], 25, 5, 19]
                      ) + Assign_Value(O, 5, (6 + O[4])),
    # () -> O[81] += (O[5] - 103 == 0 ? 5 : 0),
    lambda: Assign_Value(O, 81, O[81] + 5) if O[5] - \
    103 == 0 else Assign_Value(O, 81, O[81]),
    # () -> O[6 + O[4]] = O[5],
    lambda: Assign_Value(O, 6 + O[4], O[5]),
    # () -> O[O[1] - 1] ^= O[4],
    lambda: Assign_Value(O, O[1] - 1, O[O[1] - 1] ^ O[4]),
    # () -> e(25, 39, 24, 47, 9),
    lambda: Add_Value(stack, [25, 39, 24, 47, 9]),
    # () -> e(18, 22, 16, 50, 45, 36),
    lambda: Add_Value(stack, [18, 22, 16, 50, 45, 36]),
    # () -> O[O[1]++] = O[5],
    lambda: Assign_Value(O, Assign_Value(
        O, 1, O[1]+1), O[5]), Assign_Value(O, 1, O[1]+1),
    # () -> O[25]++,
    lambda: Assign_Value(O, 25, O[25] + 1),
    # () -> O[25] / 3 - 1,
    lambda: Assign_Value(O, 25, O[25] / 3 - 1),
    # () -> e(24,  25, 48, 9, 7),
    lambda: Add_Value(stack, [24,  25, 48, 9, 7]),
    # () -> e(37, 26, 35, 44, 27, 33, 18, 22, 16, 4),
    lambda: Add_Value(stack, [37, 26, 35, 44, 27, 33, 18, 22, 16, 4]),
    # () -> O[25],
    lambda: Assign_Value(O, 25, O[25]),
    # () -> e(44, 27, 9, 0),
    lambda: Add_Value(stack, [44, 27, 9, 0]),
    # () -> O[5] = O[O[5]],
    lambda: Assign_Value(O, 5, O[O[5]]),
    # () -> O[4] == 0 ? e(41, 24, 28, 30, 23, 25, 20, 9) : e(25, 20, 9),
    lambda: Add_Value(stack, [41, 24, 28, 30, 23, 25, 20, 9]
                      ) if O[4] == 0 else Add_Value(stack, [25, 20, 9]),
    # () -> O[80],
    lambda: Assign_Value(O, 80, O[80]),
    # () -> O[4]++,
    lambda: Assign_Value(O, 4, O[4] + 1),
    # lambda: a.byteValue() - ((a = a.shiftRight(8)).equals(6) ? 6 : 37) + e(22),
    lambda: a & 0xFF - (6 if a >> 8 == 6 else 37) + Add_Value(stack, [22]),
    # lambda: O[5] -= O[2],
    lambda: Assign_Value(O, 5, O[5] - O[2]),
    # lambda: O[5] = O[0],
    lambda: Assign_Value(O, 5, O[0]),
    # lambda: (a = a.modPow(b(107, 3), b(93, 14))).byteValue(),

    # lambda: O[2] = O[0],
    lambda: Assign_Value(O, 2, O[0]),
    # lambda: O[5] = O[--O[1]],
    lambda: Assign_Value(O, 1, O[1]-1), Assign_Value(O, 5, O[1]),
    # lambda: 5,
    lambda: 5,
    # lambda: O[4] = O[0],
    lambda: Assign_Value(O, 4, O[0]),
    # lambda: O[2]--,
    lambda: Assign_Value(O, 2, O[2]-1),
    # lambda: O[25] < O[3] ? e(46, 10, 29) : e(2),
    lambda: Add_Value(stack, [46, 10, 29]
                      ) if O[25] < O[3] else Add_Value(stack, [2]),
    # lambda: (O[2] >= 0 ? e(22, 47, 16, 38, 28, 30) : e()) - 31,
    lambda: (Add_Value(stack, [22, 47, 16, 38, 28, 30])
             if O[2] >= 0 else Add_Value(stack, [])) - 31,
    # lambda: 58 - (O[25] % 3 == 0 ? e(22, 11, 24, 47, 16, 15) : e()),
    lambda: 58 - Add_Value(stack, [22, 11, 24, 47, 16, 15]
                           ) if O[25] % 3 == 0 else Add_Value(stack, []),
    # lambda: O[5] == 0 ? 0 : (O[81] = 1) - 1,
    lambda: Assign_Value(O, 81, 1) - 1 if O[5] == 0 else 0,
    # lambda: (O[4] < O[3] ? e(24, 43, 47, 16, 34, 19, 33) : e()) - 31,
    lambda: Add_Value(stack, [24, 43, 47, 16, 34, 19, 33]
                      ) if O[4] < O[3] else Add_Value(stack, []) - 31,
    # lambda: e(24, 21, 32),
    lambda: Add_Value(stack, [24, 21, 32]),
    # lambda: O[81] = O[0],
    lambda: Assign_Value(O, 81, O[0]),
    # lambda: e(24, 46, 22, 48, 26, 24, 21, 18, 24, 47, 40) - 26,
    lambda: Add_Value(stack, [24, 46, 22, 48, 26,
                      24, 21, 18, 24, 47, 40]) - 26,
    # lambda: O[25] < O[3] ? e(8, 10, 31, 37) : e(),
    lambda: Add_Value(stack, [8, 10, 31, 37]
                      ) if O[25] < O[3] else Add_Value(stack, []),
    # lambda: (a = a.shiftLeft(8).add(b(O[5] & 0xFF))).byteValue(),
    lambda: (a >> 8+(O[5] & 0xFF))*0xFF,
    # lambda: 45,
    lambda: 45,
    # lambda: O[80] = O[5],
    lambda: Assign_Value(O, 80, O[5]),
    # lambda: O[3],
    lambda: Assign_Value(O, 3, O[3]),
    # lambda: O[O[1]++] = O[0],
    lambda: Assign_Value(O, O[1], O[0]), lambda: Assign_Value(O, 1, O[1]+1),
    # lambda: O[5] = O[4],
    lambda: Assign_Value(O, 5, O[4]),
    # lambda: 0,
    lambda: 0,
    # lambda: O[5] == 63 ? e(29) : e(39),
    lambda: Add_Value(stack, [29]) if O[5] == 63 else Add_Value(stack, [39]),
    # lambda: in.nextLine().length() % 2,

    # lambda: O[5] += O[2],
    lambda: Assign_Value(O, 5, O[5] + O[2]),
    # lambda: O[5] *= O[2],
    lambda: Assign_Value(O, 5, O[5] * O[2]),
    # lambda: e(O[5]),
    lambda: Add_Value(stack, O[5]),
    # lambda: O[O[25] + 6] -= (O[O[25] + 66] = O[5]) + O[80],
    lambda: Assign_Value(O, O[25] + 66, O[5]), Assign_Value(O,
                                                            O[25] + 6, O[O[25] + 6] - O[O[25] + 66]-O[80]),
]
