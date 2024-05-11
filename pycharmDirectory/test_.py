from itertools import combinations


def make_clu_sentence(sent, k=7):
    words = sent.split()

    # 문장에 있는 단어 수가 k 이하라면 원래 문장 반환
    if len(words) <= k:
        return sent

    clu_list = [' '.join(combo) for combo in combinations(words, k)]

    return clu_list


# 사용 예시
sentence = "This is a sample sentence with several words to test the function."
print(make_clu_sentence(sentence, 3))  # 3개 요소의 부분집합으로 조합을 생성
