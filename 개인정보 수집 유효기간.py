terms_dict = {}

def solution(today, terms, privacies):
    answer = []

    for term in terms:
        (type, duration) = term.split()
        terms_dict[type] = int(duration)

    y, m, d = map(int, today.split('.'))
    today = (y * 12 + m) * 28 + d
    print(f'오늘 : {today}')

    for i, privacy in enumerate(privacies):
        date, term = privacy.split()

        py, pm, pd = map(int, date.split('.'))
        p_date = (py * 12 + pm + terms_dict[term]) * 28 + pd
        print(f'날짜 : {p_date}')
        if p_date <= today: answer.append(i + 1)

    return answer