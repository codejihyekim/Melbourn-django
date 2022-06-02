
import random
from hello import Member
from hello.domains import my100, myRandom, members

class Quiz10:

    def quiz10bubble(self) -> str:
        arr = []
        for i in range(0, 10):
            a = my100()
            if a not in arr:
                arr.append(a)
        for i in range(0, len(arr)):
            for j in range(0, len(arr)-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f'버블정렬: {arr}')


    def quiz11insertion(self) -> str:
        arr = []
        for i in range(0, 10):
            a = my100()
            if a not in arr:
                arr.append(a)
        for i in range(1, len(arr)):
            temp = i
            while temp > 0 and arr[temp-1] > arr[temp]:
                arr[temp-1], arr[temp] = arr[temp], arr[temp -1]
                temp -= 1
        print(f'삽입정렬: {arr}')



    def quiz12selection(self) -> str:
        arr = []
        for i in range(0, 10):
            a = my100()
            if a not in arr:
                arr.append(a)
        for i in range(0, len(arr)-1):
            min = i
            for j in range(i+1, len(arr)):
                if arr[min] > arr[j]:
                    min = j
            arr[min], arr[i] = arr[i], arr[min]
        print(f'선택정렬: {arr}')


    # https://seongonion.tistory.com/37
    def quiz13quick(self) -> str: return None

    def quiz14merge(self) -> str: return None

    def quiz15magic(self) -> str: return None

    def quiz16zigzag(self) -> str: return None

    def quiz17prime(self):
        num = random.sample(range(1, 10), 2)
        num.sort()
        res = ''
        for i in range(num[0], num[1]+1):
            count = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    count += 1
            if count <= 2:
                res += str(i) + ' '
        print(res)
        if res == '':
            print(f'{num[0]}과 {num[1]} 사이에는 소수가 없습니다.')


    def quiz18golf(self):
        comNum = myRandom(1, 100)
        while 1:
            userNum = myRandom(1, 100)
            if userNum == comNum:
                print('정답입니다.')
                return
            elif userNum > comNum:
                print('더 작은 수를 입력하세요')
            elif userNum < comNum:
                print('더 큰 수를 입력하세요')
            else:
                print('잘못 입력하셨습니다.')

    def quiz19booking(self) -> str:
        size = 10
        seats = ["0","0","0","0","0","0","0","0","0","0"]
        while 1:
            print("----------------")
            for i in range(0, size):
                print((i+1))
            print('\n----------------')
            print('원하는 좌석번호를 입력(종료 0): ')
            s = myRandom(0, 10)
            print(s)
            if s == 0:
                break
            elif seats[s-1]== "0":
                seats[s-1] = "1"
                print('예약되었습니다.')
            else:
                print('이미 예약 된 자리입니다.')
        return None