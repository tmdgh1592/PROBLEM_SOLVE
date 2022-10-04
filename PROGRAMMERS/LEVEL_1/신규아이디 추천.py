def solution(new_id):
    new_id = new_id.lower()
    stack = []
    for ch in new_id:
        if ch.isalnum() or ch == '-' or ch =='_' or ch =='.':
            stack.append(ch)
    new_id = ''.join(stack)
    stack.clear()
    for i in range(len(new_id) - 1):
        if new_id[i] == '.' and new_id[i+1] == '.': continue
        else: stack.append(new_id[i])
    stack.append(new_id[-1])
    new_id = ''.join(stack)
    while new_id and new_id[0] == '.':
        new_id = new_id[1:]
    while new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) == 0: new_id = 'a'
    if len(new_id) >= 16: new_id = new_id[:15]
    while new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    
    return new_id

print(solution("123_.def"))