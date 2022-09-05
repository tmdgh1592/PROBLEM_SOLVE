from bisect import bisect_left


def solution(n, plans, clients):
    answer = []

    for i in range(len(clients)):
        client = clients[i]
        # 이용 데이터, 이용 부가서비스
        client_data, *client_services = map(int, client.split())
        
        min_data = 10000000
        flag = True
        
        for plan in plans:
            plan_data = int(plan.split()[0])
            if client_data <= plan_data:
                if min_data > plan_data:
                    min_data = plan_data
                    flag = False
        
        if flag:
            answer
        
        print(min_data)
                

    return answer


def convert_data(clients):
    data = []
    for client in clients:
        data.append(list(map(int, client.split()))[0])
    return data
