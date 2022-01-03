class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time_string):
        hour,  minute, second = map(int, time_string.split(':'))
        return hour <= 24 and minute <=59 and second <= 60

    @classmethod
    def from_string(cls,time_string):
        hour,  minute, second = map(int, time_string.split(':'))
        time = cls(hour, minute, second)
        return time

time_string = input()

if Time.is_time_valid(time_string):          # Time. 에서 staticmethod 생각  (객체,인스턴스 선언 X)
    t = Time.from_string(time_string)       # t = 에서 classmethod 생각 (객체,인스턴스 선언 X)
    print(t.hour, t.minute, t.second)

else:
    print("잘못된 시간 형식입니다.")
