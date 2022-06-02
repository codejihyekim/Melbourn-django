import random

class Quiz01Calculator:
    def __init__(self, num1, num2, op):
        self.num1 = num1
        self.num2 = num2
        self.op = op

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def did(self):
        return self.num1 / self.num2

    def res(self):
        if self.op == "+":
            return f'{self.add()}'
        elif self.op == "-":
            return f'{self.sub()}'
        elif self.op == "*":
            return f'{self.mul()}'
        elif self.op == "/":
            return f'{self.did()}'


class Quiz02Bmi:
    @staticmethod
    def getBmi(member):
        this = member
        b = this.weight / (this.height * this.height) * 10000
        if b >= 35:
            res = '고도비만'
        elif b >= 30:
            res = '중도비만'
        elif b >= 25:
            res = '경도비만'
        elif b >= 23:
            res = '과체중'
        elif b >= 18.5:
            res = '정상'
        else:
            res = '저체중'
        return res


class Quiz03Grade:

    def __init__(self, name, korscore, engscore, mathscore):
        self.name = name
        self.korscore = korscore
        self.engscore = engscore
        self.mathscore = mathscore

    def sum(self):
        return self.korscore + self.engscore + self.mathscore

    def avg(self):
        return self.sum() / 3

    def pas(self):
        if self.avg() > 80:
            return f'합격'
        else:
            return f'불합격'


class Quiz04GradeAuto(object):
    def __init__(self, name, korscore, engscore, mathscore):
        self.name = name
        self.korscore = korscore
        self.engscore = engscore
        self.mathscore = mathscore

    def sum(self):
        return self.korscore + self.engscore + self.mathscore

    def avg(self):
        return self.sum() / 3

    def getGrade(self):
        pass

    def pas(self):
        if self.avg() > 80:
            return f'합격'
        else:
            return f'불합격'


def myRandom(start, end):
    return random.randint(start, end)


class Quiz05Dice(object):

    @staticmethod
    def cast():
        return myRandom(1, 6)


class Quiz06RandomGenerator(object):
    pass


class Quiz07RandomChoice(object):
    def __init__(self):
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                       "권혜민", "서성민", "조현국", "김한슬", "김진영",
                       '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                       '최민서', '한성수', '김윤섭', '김승현',
                       "강 민", "최건일", "유재혁", "김아름", "장원종"]

    def chooseMember(self):
        ran = myRandom(0, 23)
        return self.members[ran]


class Quiz08Rps(object):

    def __init__(self, user):
        self.user = user
        self.com = myRandom(0, 2)

    def game(self):
        rps = ['가위', '바위', '보']
        score = self.user - self.com
        if score == 0:
            res = f' com:{rps[self.com]} user:{rps[self.user]}으로 비겼습니다.'
        elif score == 1 or score == -2:
            res = f' com:{rps[self.com]} user:{rps[self.user]}으로 이겼습니다.'
        else:
            res = f' com:{rps[self.com]} user:{rps[self.user]}으로 졌습니다.'
        return res


class Quiz09GetPrime(object):
    @staticmethod
    def getPrime():
        num1 = int(input('시작숫자'))
        num2 = int(input('끝숫자'))
        res = ''
        for i in range(num1, num2+1):
            count = 0
            for j in range(1, i+1):
                if i % j == 0:
                    count += 1
            if count <= 2:
                res += str(i) + ' '
        return res


class Quiz10LeapYear(object):
    def __init__(self, year):
        self.year = year

    def leapYear(self):
        if self.year % 4 == 0 and self.year % 10 != 0 or self.year % 400 == 0 :
            res = '윤년입니다.'
        else:
            res = '평년입니다.'
        return res


class Quiz11NumberGolf(object):

    def __init__(self):
        self.comNum = myRandom(1, 100)

    def game(self):
        while 1:
            userNum = int(input('숫자입력'))
            if userNum == self.comNum:
                return '정답입니다.'
            elif userNum > self.comNum:
                print('더 작은 수를 입력하세요')
            elif userNum < self.comNum:
                print('더 큰 수를 입력하세요')
            else:
                print('잘못 입력하셨습니다.')


class Quiz12Lotto(object):

    @staticmethod
    def lotto():

        a = random.sample(range(1, 46), 6)
        a.sort()
        return a


class Quiz13Bank(object): # 이름, 입금, 출금만 구현

    def __init__(self):
        self.total = 0

    def save(self, money):
        self.total += money
        print(f'{money}를 예금하였습니다.')

    def pay(self, money):
        if self.total <= money:
            print(f'잔고가 없습니다.')
            return
        else:
            self.total -= money
            print(f'{money}를 출금하였습니다.')

    def balance(self):

        while 1:
            menu = int(input('0.Exit 1.예금 2.출금 3.잔금'))
            if menu == 0:
                return f'종료'
            elif menu == 1:
                self.save(int(input('금액을 입력해주세요')))
            elif menu == 2:
                self.pay(int(input('금액을 입력해주세요')))
            elif menu == 3:
                print(f'현재 잔금은 {self.total}입니다.')


class Quiz14Gugudan(object): # 책받침구구단
    @staticmethod
    def gugudan():
        res = ''
        for i in range(2, 9, 4):
            for j in range(1, 10):
                for k in range(i, i+4):
                    res += f'{k}*{j}={k*j}'+'\t'
                res += '\n'
            res += '\n'
        return res




