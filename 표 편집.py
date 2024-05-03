def solution(n, cur, cmds):
    prevs = [i - 1 for i in range(n)]
    nexts = [i + 1 for i in range(n)]
    prevs[0], nexts[-1] = None, None

    stack = []
    for cmd in cmds:
        if cmd[0] == 'U':
            cnt = int(cmd.split()[1])
            for _ in range(cnt):
                cur = prevs[cur]
        elif cmd[0] == 'D':
            cnt = int(cmd.split()[1])
            for _ in range(cnt):
                cur = nexts[cur]
        elif cmd[0] == 'C':
            stack.append(cur)
            prev = prevs[cur]
            next = nexts[cur]
            if prev is not None:
                nexts[prev] = next
            if next is not None:
                prevs[next] = prev
            if next is None:
                cur = prev
            else:
                cur = next
        elif cmd[0] == 'Z':
            restore = stack.pop()
            prev = prevs[restore]
            next = nexts[restore]
            if prev is not None:
                nexts[prev] = restore
            if next is not None:
                prevs[next] = restore

    deleted = set(stack)
    return ''.join(['X' if i in deleted else 'O' for i in range(n)])