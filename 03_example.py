
def ageCalculator(y, m, d):
    '''Age Calculator using Python'''
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print('Your age is: ', age)


y = int(input('Enter your Birh Year: '))
m = int(input('Enter your Birh Mounth: '))
d = int(input('Enter your Birh Day: '))

ageCalculator(y, m, d)


