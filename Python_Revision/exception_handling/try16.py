from try15 import underAgeError, overAgeError

def check_eligibility():
        age = int(input('enter your age '))
        if age < 18:
            raise underAgeError
        elif age >= 18 and age <=60:
            print("Yes you are eligible for the test")
        elif age > 60:
            raise overAgeError
        else:
            print("something got error")

try:
     check_eligibility()
except underAgeError as un:
     print(un)
except overAgeError as ov:
     print(ov)
