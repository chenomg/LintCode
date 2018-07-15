#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: Trailing_Zeros.py
#          Desc: Write an algorithm which computes the number of trailing zeros in n factorial.
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-07-15 00:54:03
#       History:
# =============================================================================
'''
from time import time, ctime


class Trailing_Zeros(object):
    def factorial_slow(self, n):
        """
        递归函数计算最后一位是否为零，为零的话继续往前一位计算
        """
        print('factorial_slow begining at: {}'.format(ctime()))
        t_start = time()
        total_list = (i for i in range(1, n + 1))
        factorial = 1
        for item in total_list:
            factorial *= item
        t_end = time()
        t_del = t_end - t_start
        factorial_str = str(factorial)
        trailing_zeros = 0
        for i in factorial_str[::-1]:
            if not int(i):
                trailing_zeros += 1
            else:
                break
        # print(factorial)
        print('factorial_slow ending at: {}'.format(ctime()))
        print('time costed: {}s'.format(t_del))
        print('trailing_zero num: {}'.format(trailing_zeros))

    def get_trail_zeros(self, num):
        n = 0
        for i in str(num)[::-1]:
            if not int(i):
                n += 1
            else:
                return n

    def get_2_5(self, num):
        count_2 = 0
        count_5 = 0
        for i in str(num)[::-1]:
            if int(i):
                if not int(i) % 2:
                    count_2 = int(i) // 2
                    return [count_2, count_5]
                elif not int(i) % 5:
                    count_5 = int(i) // 5
                    return [count_2, count_5]
                else:
                    return [count_2, count_5]

    def factorial_fast(self, n):
        """
        递归函数计算最后一位是否为零，为零的话继续往前一位计算
        """
        print('factorial_fast begining at: {}'.format(ctime()))
        t_start = time()
        total_list = (i for i in range(1, n + 1))
        # 计算尾数为零的总零数
        trailing_zeros = 0
        count_2_5 = [0, 0]
        for i in total_list:
            trailing_zeros += self.get_trail_zeros(i)
            count_2_5[0] += self.get_2_5(i)[0]
            count_2_5[1] += self.get_2_5(i)[1]
        if count_2_5[0] > count_2_5[1]:
            min_2_5 = count_2_5[1]
        else:
            min_2_5 = count_2_5[0]
        trailing_zeros += min_2_5
        t_end = time()
        t_del = t_end - t_start
        print('factorial_fast ending at: {}'.format(ctime()))
        print('time costed: {}s'.format(t_del))
        print('trailing_zero num: {}'.format(trailing_zeros))
        return trailing_zeros


def main():
    Solution = Trailing_Zeros()
    Solution.factorial_fast(123456)
    Solution.factorial_slow(123456)


if __name__ == "__main__":
    main()
