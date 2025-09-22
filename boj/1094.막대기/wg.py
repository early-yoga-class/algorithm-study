X = int(input())

stick_lst = [64]
total = sum(stick_lst)

while total != X:
  stick_lst.sort(reverse=True)
  print(stick_lst)
  if total > X:
    stick = stick_lst.pop()
    half = stick // 2
    total -= stick
    if total + half >= X: # 크거나 같다면
      stick_lst.append(half)
      total += half
    else:
      stick_lst.append(half)
      stick_lst.append(half)
      total += (half * 2)
  else:
    break


print(len(stick_lst))