from hello.domains import Member
from hello.models1 import Quiz01Calculator, Quiz02Bmi, Quiz05Dice, Quiz08Rps, Quiz10LeapYear, Quiz03Grade, \
    Quiz07RandomChoice, Quiz12Lotto, Quiz13Bank, Quiz14Gugudan, Quiz11NumberGolf, Quiz09GetPrime

if __name__ == '__main__':
    while 1:
        menu = input('0.계산기\n 1.BMI\n 2.주사위\n 3.가위바위보\n 4.윤년\n '
                     '5.성적표\n 6.멤버선택\n 7.로또\n 8.입출금\n 9.구구단\n 10.숫자맞추기\n '
                     '11.소수\n 12.버블\n 13.삽입\n 14.선택\n 15.퀵\n 16.병합\n'
                     '17.매직\n 18.지그재그\n 19.직각별\n 20.정삼각형\n 21.예약\n 22.리스트'
                     '23.튜플 24.딕셔너리 25 26 27 28 29 30')
        if menu == '0': # 계산기
            q0 = Quiz01Calculator(int(input('첫번째 수')), int(input('두번째 수')), input('연산자'))
            print(f'{q0.num1} {q0.op} {q0.num2} = {q0.res()}')
        elif menu == '1': # BMI
            member = Member()
            q1 = Quiz02Bmi()
            member.name = input('이름: ')
            member.height = float(input('키: '))
            member.weight = float(input('몸무게: '))
            res = q1.getBmi(member)
            print(f'{member.name}님의 BMI는 {res}입니다.')
        elif menu == '2': # 주사위
            q2 = Quiz05Dice()
            print(f'결과: {Quiz05Dice.cast()}')
        elif menu == '3': #가위바위보
            q3 = Quiz08Rps(int(input('가위: 1 바위: 2 보: 3')))
            print(f'{q3.game()}')
        elif menu == '4': #성적표
            q4 = Quiz10LeapYear(int(input('년도 입력')))
            print(f'입력한 년도는 {q4.leapYear()}')
        elif menu == '5':
            q5 = Quiz03Grade(input('이름'), int(input('국어')), int(input('영어')), int(input('수학')))
            print(f'{q5.name}님의 총점: {q5.sum()} 평균: {q5.avg()}으로 {q5.pas()}입니다.')
        elif menu == '6': #멤버선택
            q6 = Quiz07RandomChoice()
            print(f'결과: {q6.chooseMember()}')
        elif menu == '7': #로또
            q7 = Quiz12Lotto()
            print(f'로또 결과: {q7.lotto()}')
        elif menu == '8': #입출금
            q8 = Quiz13Bank()
            print(q8.balance())
        elif menu == '9': #구구단
            q9 = Quiz14Gugudan()
            print(f'{q9.gugudan()}')
        elif menu == '10': # 숫자맞추기
            q10 = Quiz11NumberGolf()
            print(f'결과: {q10.game()}')
        elif menu == '11': #소수
            q11 = Quiz09GetPrime()
            print(f'결과: {q11.getPrime()}')

