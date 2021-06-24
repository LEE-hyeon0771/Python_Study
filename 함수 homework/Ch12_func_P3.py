'''
분해 : 인자 x좌표, y 좌표, (0,0)으로 부터의 거리, distance()함수, 반환값 존재, 입력값 존재X
패턴인식 : 인자 x,y를 입력받는다.
           (0,0)으로 부터의 거리 공식을 구한다.
           distance()함수를 정의한다.
           반환값을 return 해 주어야 한다.
           입력값은 없다.
추상화 : 인자 x좌표, y좌표를 입력받는다.
         distance함수를 (x^2 + y^2)^1/2 로 return한다.
         반환값이 있으므로 result = distance()로 함수를 호출한다.

알고리즘(의사코드)

def distance():
    return (x^2 + y^2)^1/2

x좌표 입력
y좌표 입력

result = distance()

{result}출력
'''
#자동화


def distance():
    return (x_coord**2 + y_coord**2) ** 0.5

x_coord = int(input("x 좌표 입력: "))
y_coord = int(input("y 좌표 입력: "))

result = distance()

print(f"거리: {result}")

