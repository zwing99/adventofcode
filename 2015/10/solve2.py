#!/usr/bin/env python

from functools import cache
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

line = lines[0]


@cache
def dfs(line, last_cnt, last_chr, depth, max_depth, is_last=False):
    print(line, last_cnt, last_chr, depth)
    if depth == max_depth:
        line = last_cnt * last_chr + line
        if is_last:
            print("foo2", line, len(line), 0, "")
            return len(line), 0, ""
        last_chr = line[-1]
        i = len(line) - 2
        for i in range(len(line) - 2, -1, -1):
            if line[i] != last_chr:
                break
        else:
            i -= 1
        first_set = line[: i + 1]
        last_set = line[i + 1 :]
        # print(line)
        # print(first_set, last_set)
        last_chr = last_set[0] if last_set else ""
        print("foo", line, len(first_set), len(last_set), last_chr)
        return (len(first_set), len(last_set), last_chr)
    j = 0
    l = 0
    cnt = last_cnt
    chr = last_chr
    last_cnt = 0
    last_chr = ""
    while j < len(line):
        if chr == line[j]:
            cnt += 1
        else:
            if cnt:
                a, last_cnt, last_chr = dfs(
                    str(cnt) + chr, last_cnt, last_chr, depth + 1, max_depth
                )
                l += a
            chr = line[j]
            cnt = 1
        j += 1
    if cnt:
        a, last_cnt, last_chr = dfs(
            str(cnt) + chr, last_cnt, last_chr, depth + 1, max_depth, True
        )
        l += a
    # print("bar", line, l, last_cnt, "")
    return l, 0, ""


l, last_cnt, last_chr = dfs(line, 0, "", 1, 40)
print(l, last_cnt, last_chr)

# 45598933
# 126491972
# 492982
