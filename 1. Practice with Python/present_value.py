'''
연금의 현재가치 추정

pv = fv / (1+r)^n

fv = pv * (1+r)^n 변형

[형식]
pv(fv, r, n)

[파라미터]
fv : 미래가치
r : 기간별 할인율
n : 총 기간수

'''

def pv(fv, r, n):
    pv = fv / (1+r)**n
    print(pv)