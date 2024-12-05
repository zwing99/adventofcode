#!/usr/bin/env python

from enum import Enum
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


def is_safe(li):
    diffs = [li[i] - li[i + 1] for i in range(len(li) - 1)]
    pos_li = [3 >= diff > 0 for diff in diffs]
    neg_li = [-3 <= diff < 0 for diff in diffs]
    if all(pos_li):
        return True
    elif all(neg_li):
        return True
    return False


safe_count = 0
for line in lines:
    li = [int(x) for x in line.split()]
    diffs = [li[i] - li[i + 1] for i in range(len(li) - 1)]
    len_diffs = len(diffs)
    pos_li = [3 >= diff > 0 for diff in diffs]
    sum_pos_li = sum(pos_li)
    neg_li = [-3 <= diff < 0 for diff in diffs]
    sum_neg_li = sum(neg_li)
    if is_safe(li):
        safe_count += 1
        continue
    if (
        sum_pos_li == len_diffs - 1
        or sum_pos_li == 1
        or sum_neg_li == len_diffs - 1
        or sum_neg_li == 1
    ):
        safe = False
        for i in range(len(li)):
            li1 = li.copy()
            li1.pop(i)
            if is_safe(li1):
                safe = True
                break
        if safe:
            safe_count += 1
            continue


print(safe_count)

# 655
# 661
