"""
1 ~ 10까지의 경우를 만들 수 있다.

1->1
2->1 
3->1
4->(2->1) 
5->(4->2->1)
6->(2->1)
7->(6->2->1)
8->(4->2->1)
9->(3->1)
10->(9->3->1)

11->(10->9->3->1)
12->(6->2->1)
13->(12->6->2->1)
14->(7->6->2->1)
15->(5->4->2->1)

점화식이 필요하다.
"""

N = int(input())
cnt = 0

[1, 1, 1, 2, 3, 2, 3, 3, 2, 3]


print(cnt)
