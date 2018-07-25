from enum import Enum

Month = Enum('Month', ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))

for name, member in Month.__members__.item():
    print(name, '=>', member, ',', member.value)

