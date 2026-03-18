# Step03_Example.py

"""
    회원 한명의 정보는 번호, 이름, 주소 로 이루어 있다.
    그리고 그러한 회원이 여러명이다.
    여러명의 회원 목록을 하나의 묶음으로(하나의 data) 로 순서대로 관리하고 싶다면...
"""

# 3명의 회원정보를 각각 dict 에 담은 다음 그 dict 를 list 에 담는 코드를 작성해서 쳇팅창에 보내 보세요.
mem1 = {"num":1, "name":"김구라", "addr":"노량진"}
mem2 = {"num":2, "name":"해골", "addr":"노량진"}
mem3 = {"num":3, "name":"원숭이", "addr":"동물원"}
# dict 3 개를 list 에 담기 
members = [mem1, mem2, mem3]

a = members
b = members[0]
c = members[0]["num"]
d = members[0]["name"]

print("종료됩니다.")

