def solution(lottos, win_nums):
    convert = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    count_0 = lottos.count(0)
    min_num = 0
    
    for num in lottos:
        if num in win_nums:
            min_num += 1
    
    return (convert[count_0 + min_num], convert[min_num])