#폰켓몬

num = [3,3,3,2,2,4]

def solution(nums): 
    take_pkm = len(nums)//2
    set_pkm = len(set(nums))

    if take_pkm > set_pkm:
        answer = set_pkm
    else:
        answer = take_pkm
    
    return answer

solution(num)


''' 모범답안 
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
'''