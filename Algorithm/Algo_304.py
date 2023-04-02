from typing import Any, Sequence

def binary_search(a: Sequence, key: Any) -> int:
    ptr_L = 0
    ptr_R = len(a) - 1
    
    while True:
        ptr_C = (ptr_L + ptr_R) // 2
        
        if a[ptr_C] == key:
            return ptr_C
        elif a[ptr_C] < key:
            ptr_L = ptr_C + 1
        else:
            ptr_R = ptr_C - 1
        
        if ptr_L > ptr_R:
            break
    return -1

if __name__ == "__main__":
    num = int(input('원소 수를 입력하세요 >> '))
    x = [None] * num
    
    print('배열 데이터를 오름차순으로 입력하세요.')
    
    x[0] = int(input('x[0] >> '))
    
    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}] >> '))
            if x[i] >= x[i - 1]:
                break
    
    key = int(input('검색할 값을 입력하세요 >> '))
    index = binary_search(x, key)
    
    if index == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{index}]에 있습니다.')