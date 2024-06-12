class Page:
    def __init__(self, idx, basic, link, score):
        self.idx = idx
        self.basic = basic
        self.link = link
        self.score = score


def solution(word, pages):
    wsize = len(word)
    pagehash = {}
    pagelist = []
    word = word.lower()
    for idx, s in enumerate(pages):
        s = s.lower()
        mid = -1
        posl = posr = 0
        while mid < 0:
            posl = s.find('<meta', posl + 1)
            posr = s.find('>', posl)
            mid = s.find('https://', posl, posr)
        posr = s.find('\"', mid)
        url = s[mid:posr]

        posl = s.find('<body>', posr)
        basic = 0
        start = posl
        while True:
            start = s.find(word, start + 1)
            if start == -1:
                break
            if not s[start - 1].isalpha() and not s[start + wsize].isalpha():
                basic += 1

        link = 0
        start = posl
        while True:
            start = s.find('<a href', start + 1)
            if start == -1:
                break
            link += 1

        pagehash[url] = idx
        pagelist.append(Page(idx, basic, link, basic))

    for i, s in enumerate(pages):
        posl = posr = 0
        while True:
            posl = s.find('<a href', posr)
            if posl == -1:
                break
            posl = s.find('https://', posl)
            posr = s.find('\"', posl)
            url = s[posl:posr]
            if url in pagehash:
                idx = pagehash[url]
                pagelist[idx].score += pagelist[i].basic / pagelist[i].link

    score = answer = -1
    for page in pagelist:
        if page.score > score:
            score = page.score
            answer = page.idx

    return answer