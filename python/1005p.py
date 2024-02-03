from collections import deque
import sys

def find_min_time_to_build(rules, build_times, target):
    # 건물의 개수
    n = len(build_times)
    # 진입 차수 배열
    in_degree = [0] * (n + 1)
    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    # 건설 시간
    time_needed = [0] * (n + 1)

    # 진입 차수와 그래프 구성
    for x, y in rules:
        graph[x].append(y)
        in_degree[y] += 1

    # 건설 시간 초기화
    for i in range(1, n + 1):
        time_needed[i] = build_times[i-1]

    # 위상 정렬
    q = deque()
    # 진입 차수가 0인 건물 찾기
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    # 위상 정렬 실행
    while q:
        now = q.popleft()
        for next in graph[now]:
            # 최소 시작 시간 업데이트
            time_needed[next] = max(time_needed[next], time_needed[now] + build_times[next-1])
            in_degree[next] -= 1
            if in_degree[next] == 0:
                q.append(next)

    # 목표 건물 건설 완료 시간 반환
    return time_needed[target]

tc = int(sys.stdin.readline().rstrip())

for _ in range(tc):
    build, rule = map(int, sys.stdin.readline().rstrip().split())
    bt =list(map(int, sys.stdin.readline().rstrip().split()))
    rules = []
    for t in range(rule):
        a,b = map(int, sys.stdin.readline().rstrip().split())
        rules.append((a,b))

    target = int(sys.stdin.readline().rstrip())
    print(find_min_time_to_build(rules, bt, target))

