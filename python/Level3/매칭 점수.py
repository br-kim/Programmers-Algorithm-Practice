# https://programmers.co.kr/learn/courses/30/lessons/42893

import re


def find_link_addr(page):
    result = re.findall('<meta property="og:url" content="([^"]*)"/>', page)
    return result[0]


def find_outer_link(page):
    result = re.findall('<a href="([^"]*)">', page)
    return result


def find_word(word, page):
    page = page.lower()
    word = word.lower()
    result1 = re.findall(f'[a-z]{word}', page)
    result2 = re.findall(f'{word}[a-z]', page)
    result3 = re.findall(f'{word}', page)
    result = len(result3) - (len(result1) + len(result2))
    return result


def solution(word, pages):
    answer = []
    page_score = dict()
    for i in pages:
        link_addr = find_link_addr(i)
        links = find_outer_link(i)
        default_score = find_word(word, i)
        page_score[link_addr] = [default_score, links, 0]

    for page_addr in page_score.keys():
        links = page_score[page_addr][1]
        default_score = page_score[page_addr][0]
        for link in links:
            if link in page_score:
                page_score[link][2] += (default_score / len(links))

    answer = [page_score[page_addr][0] + page_score[page_addr][2]
              for page_addr in page_score.keys()]

    return answer.index(max(answer))


test1 = "blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
                  "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
test2 = "Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
                 "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

testcase = [test1, test2]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test[0], test[1]))
