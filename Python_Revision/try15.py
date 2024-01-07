class underAgeError(Exception):
    def __init__(self,msgg='age is under 18'):
        self.msg = msgg
    def __str__(self):
        return self.msg
    

class overAgeError(Exception):
    def __init__(self,msgg='age is above 60'):
        self.msg = msgg
    def __str__(self):
        return self.msg


