def solution(s: str):
    num_list = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    for num_s, num_d in num_list.items():
        s = s.replace(num_s, num_d)
        
    return int(s)
