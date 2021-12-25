# 다시

"""
청소하는 영역 개수 구하기

왼쪽 방향부터 탐색
a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

로봇 청소기 좌표 (r, c) 
[N, E, S, W]
[0, 1, 2, 3]

nx = [-1, 0, 1, 0]
ny = [0, 1, 0, -1]
1은 벽, 0은 빈칸

1. 벽에 닿는(행렬의 끝) 경우 
"""

N, M = map(int, input().split())
r, c, d = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]


nx = [-1, 0, 1, 0]
ny = [0, 1, 0, -1]


def solution():
    ret = 0

    for i in range(N):
        for j in range(M):
            if area[r][c] == 0:  # 현재위치
                ret += 1

    return ret


solution()
