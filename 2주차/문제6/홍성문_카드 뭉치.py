def solution(cards1, cards2, goal):
    answer = ''

    for i in goal:
        if cards1 and cards1[0] == i:
            cards1.pop(0)
        elif cards2 and cards2[0] == i:
            cards2.pop(0)
        else:
            return 'No'

    return 'Yes'

#큐는 FIFO

print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))

# 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.3MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.00ms, 10.2MB)
# 테스트 4 〉	통과 (0.00ms, 10.3MB)
# 테스트 5 〉	통과 (0.00ms, 10.1MB)
# 테스트 6 〉	통과 (0.00ms, 10.1MB)
# 테스트 7 〉	통과 (0.00ms, 10.1MB)
# 테스트 8 〉	통과 (0.00ms, 10.4MB)
# 테스트 9 〉	통과 (0.00ms, 10.3MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.1MB)
# 테스트 13 〉	통과 (0.00ms, 10.1MB)
# 테스트 14 〉	통과 (0.01ms, 10.1MB)
# 테스트 15 〉	통과 (0.01ms, 10.1MB)
# 테스트 16 〉	통과 (0.01ms, 10.1MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.1MB)
# 테스트 19 〉	통과 (0.00ms, 10.1MB)
# 테스트 20 〉	통과 (0.00ms, 10.3MB)
# 테스트 21 〉	통과 (0.01ms, 10.2MB)
# 테스트 22 〉	통과 (0.01ms, 10.3MB)
# 테스트 23 〉	통과 (0.00ms, 10.2MB)
# 테스트 24 〉	통과 (0.00ms, 10.3MB)
# 테스트 25 〉	통과 (0.00ms, 10.2MB)
