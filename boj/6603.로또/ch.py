import itertools
import sys
from collections import deque


while 1:
    input_list = deque(list(map(int, input().split())))

    if input_list[0] == 0: break

    # 6 < k < 13
    k = input_list.popleft()
    result = list(itertools.combinations(input_list, 6))

    for el in result:
        print(" ".join([str(num) for num in el]))
    print()
