import sys
from collections import deque
tc = int(sys.stdin.readline().rstrip())

for _ in range(tc):
    build, rule = map(int, sys.stdin.readline().rstrip().split())
    bt = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    graph = [[] for _ in range(build+1)]
    for t in range(rule):
        a,b = map(int, sys.stdin.readline().rstrip().split())
        graph[b].append(a)

    st = int(sys.stdin.readline().rstrip())
    c = 0
    deq = deque([(c, graph[st])])
    deq2 = deque([(-1, [st])])
    while deq:
        ki = deq.popleft()
        deq2.append(ki)
        if ki[1]==[]:
            break
        si = []
        for kki in ki[1]:
            for kkki in graph[kki]:
                si.append(kkki)
        c+=1
        si = sorted(set(si))
        deq.append((c, si))

    re = 0
    for t in deq2:
        if len(t[1])>1:
            mi=0
            for tt in t[1]:
                mi = max(mi, bt[tt])
            re +=mi

        elif len(t[1]) ==1:
            re +=bt[t[1][0]]

        print(re)
    print("answ")
    print(re)
    print()

