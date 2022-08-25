n,m = (int(x) for x in input().split())

while n > 0 and m > 0:

    tickets = {}

    for i in range(1,n+1):
        tickets[i] = 0

    rolezeiros = [int(x) for x in input().split()]

    for i in range(0,m):
        ticket_entregue = rolezeiros[i]
        tickets[ticket_entregue]+=1

    ans = 0
    for t in tickets:
        if tickets[t] > 1:
            ans+=1

    print(ans)

    n,m = (int(x) for x in input().split())


