def solve(a):

  if a == 0:
    return 0

  resp = 1/(2 + solve(a-1))
  return resp

n = float(input())
ans = 1+solve(n)
print("{:.10f}".format(ans))
