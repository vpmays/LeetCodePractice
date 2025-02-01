def solution(S):
    # Implement your solution here

    removeable = ["AB", "BA", "CD", "DC"]
    newS = S
    indexi = 0
    indexj = 1

    while indexj < len(newS):
        #print(f'S[indexi] + S[indexj]: {newS[indexi] + newS[indexj]}')
        if (newS[indexi] + newS[indexj] in removeable):
            newS = newS[:indexi] + newS[indexj+1:]
            #print(newS)
            indexi = 0
            indexj = 1
            #print(f'indexi: {indexi}')
            #print(f'indexj: {indexj}')
        else:
            indexi += 1
            indexj += 1

    return newS

print(solution('ABCBACDDADAAABAAC'))