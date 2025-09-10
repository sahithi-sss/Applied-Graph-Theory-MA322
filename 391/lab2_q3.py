from collections import deque

N = int(input())
xs, ys = map(int, input().split(" "))
xt, yt = map(int, input().split(" "))

q = deque()
q.append((xs, ys))

nei = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
visit = set()
moves = 0
isFound = False

while q and not isFound:
    for _ in range(len(q)):
        x, y = q.popleft()

        if (x, y) == (xt, yt):
            isFound = True
            print(moves)
            break

        if (x, y) in visit:
            continue

        visit.add((x, y))

        for dx, dy in nei:
            nx, ny = x + dx, y + dy

            if 1 <= nx <= N and 1 <= ny <= N:
                q.append((nx, ny))
    moves += 1