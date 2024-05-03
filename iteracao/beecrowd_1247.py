def solve(d,vf,vg):

    h = (144+d*d)**(1/2)
    tguarda = h/vg
    tfugini = 12/vf
    if tguarda > tfugini:
        ans = 'N'
    else:
        ans = 'S'
    return ans

while True:
    try:
        a,b,c = (int(x) for x in input().split())
        ans = solve(a,b,c)
        print(ans)
    except EOFError:
        break
