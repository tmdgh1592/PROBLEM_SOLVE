percents = [10, 20, 30, 40]
max_plus, max_emo = -1, -1


def solution(users, emoticons):
    def f(i, comb):
        global max_plus, max_emo

        if len(comb) == len(emoticons):
            now_plus, now_emo = 0, 0
            for user_discount, plus_standard in users:
                user_payment = 0
                for emo_price, emo_discount in comb:
                    if emo_discount >= user_discount:
                        user_payment += emo_price - (emo_price * emo_discount // 100)

                if user_payment >= plus_standard:
                    now_plus += 1
                else:
                    now_emo += user_payment

            if now_plus > max_plus:
                max_plus = now_plus
                max_emo = now_emo
            elif now_plus == max_plus and now_emo > max_emo:
                max_emo = now_emo
            return

        for percent in percents:
            comb.append((emoticons[i], percent))
            f(i + 1, comb)
            comb.pop()

    f(0, [])

    return [max_plus, max_emo]
