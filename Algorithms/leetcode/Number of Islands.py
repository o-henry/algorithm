# 섬의 개수를 구하라


Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

Output: 1

---

# 해당 Input은 2차원 배열이다.
# 좌표 값 처럼 (x, y) 형식의 코드를 구현할 수 있다.
  └─ 이중 반복 처리를 통해, 첫번째 순회 값을 y 좌표로, 두번째 순회를 x 좌표로 사용할 수 있다.
# ex. (0, 0) 좌표를 확인하고, (0, 1) , (1, 0) 을 확인하는 식의 코드
  └─ 1 만 섬이므로, 1이 아닐때까지 좌표를 옮겨가며 찾아야한다.
  └─ 따라서 계속 찾아들어가는 DFS를 사용해야 함을 알아야 한다.
  └─ 또, 모양은 그렇지 않지만 그래프 로 생각해야 한다.
  └─ DFS를 써야한다. 이는 즉 그래프로 변화하여 풀이할 수 있는지 확인해보자 라는 생각을 해야한다.
  
---


# 0 이 물이고, 1이 육지다. 1로 연결된 부분이 섬.

1 - 1 - 1 - 1 - 0
|   |   |   |   |
1 - 1 - 0 - 1 - 0
|   |   |   |   |
1 - 1 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 0 - 0 - 0

# 1을 체크하고 상,하,좌,우 에 1이 존재하는지 체크한다.
# 체크 후 확인한 부분을 방문 했다고 체크한다 ( 0으로 바꾼다. )
  └─ 방문 체크를 해야 다시 방문하지 않는다
# 1이 존재하지 않는다면 output 에 1을 추가한다 ( 섬의 개수가 된다 )

# 좌표가 반대인 모양이 나옴

(0,0) - (0,1) - (0,2) - (0,3) - (0,4)
  |       |       |       |       |
(1,0) - (1,1) - (1,2) - (1,3) - (1,4)
  |       |       |       |       |
(2,0) - (2,1) - (2,2) - (2,3) - (2,4)
  |       |       |       |       |
(3,0) - (3,1) - (3,2) - (3,3) - (3,4)

