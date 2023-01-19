'''
51p
NPV = 순 현재가치 -> 모든 편익의 현재가치에서 모든 비용의 현재가치 차감
현금 유입은 플러스로, 현금 유출은 마이너스로 표기하면 NPV는 모든 현금 흐름의 현재가치를 더하면 됨

pv = fv / (1+r)^n 이용

def NPV(rate, cashflows)

파라미터
rate = r
cashflows = 리스트 형식의 현금 흐름

'''

def NPV(rate, cashflows):
    
    total = 0.0
    
    for i in range(0, len(cashflows)):
        total += cashflows[i] / (1 + rate)**i
    
    return total

# 주어진 현금흐름에 대해 그 NPV를 0으로 만드는 할인율(r) 구하는 함수    
# def NPV_zero(r, cashFlows):
    
#     while(r < 1.0):
#         r += 0.000001
#         npv_zero = NPV_zero(r, cashFlows)
        
#         if (abs(npv_zero) <= 0.0001):
#             print("NPV를 0으로 만드는 할인율 : {}".format(r))

def main():
    
    # NPV 함수 이용
    rate = 0.035
    cashflows = [-100, -30, 10, 40, 50, 45, 20]
    
    print("r: {} \ncashflows: {}\n".format(rate, cashflows))
    
    res = NPV(rate, cashflows)
    
    print("########## result of NPV ##########")
    print("NPV = {}".format(res))
    print("###################################\n")
    
    # NPV 함수 이용해 주어진 현금흐름에 대해 그 NPV를 0으로 만드는 할인율(r) 구하기
    r = 0
    cashFlows = (550, -500, -500, -500, 1000)
    
    print("cashFlows: {} 일때".format(cashFlows))
    
    while(r < 1.0):
        r += 0.000001
        npv_zero = NPV(r, cashFlows)
        
        if (abs(npv_zero) <= 0.0001):
            print("NPV를 0으로 만드는 할인율 : {}".format(r))
    

if __name__ == '__main__':
    main()
