n = int(input())


def solution(n):
    cnt = 0

    while n >= 0:
        if n % 5 == 0:
            cnt += n // 5
            print(cnt)
            break
        n -= 3
        cnt += 1
    else:
        print(-1)


print(solution(n))
