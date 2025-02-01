def solution(N):
    # Implement your solution here
    binaryN = ''
    base = 1
    count = 0
    longest = 0
    while base > 0:
        base = int(N/2)
        #print(f'base: {base}')
        R = N % 2
        #print(f'R: {R}')
        binaryN = binaryN + str(R)
        print(f'binaryN: {binaryN}')
        N = base
    
    for indexi in range(0, len(binaryN)):
        if binaryN[indexi] == '1':
            for indexj in range(indexi + 1, len(binaryN)):
                if binaryN[indexj] == '0':
                    count += 1
                elif binaryN[indexj] == '1':
                    if count > longest:
                        longest = count
                    count = 0
                    indexi = indexj
                if indexj == len(binaryN) - 1:
                    break
        
    return longest

print(solution(1376796946))