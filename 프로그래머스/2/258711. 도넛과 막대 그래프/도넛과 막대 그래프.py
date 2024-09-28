def solution(edges):
    answer = [0, 0, 0, 0]
    in_out = {}
    
    for a, b in edges:
        if not in_out.get(a): in_out[a] = [0, 0]
        if not in_out.get(b): in_out[b] = [0, 0]
        
        in_out[a][1] += 1
        in_out[b][0] += 1
    
    for node, inout_count in in_out.items():
        in_cnt, out_cnt = inout_count
        
        if in_cnt == 0 and out_cnt >= 2:
            answer[0] = node
        elif in_cnt >= 1 and out_cnt == 0:
            answer[2] += 1
        elif in_cnt >= 2 and out_cnt == 2:
            answer[3] += 1
    
    answer[1] = in_out[answer[0]][1] - answer[2] - answer[3]

    return answer