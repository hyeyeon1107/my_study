
class Member:
    def __init__(self, name):
        self.name = name

    def fee(self):
        return 10000

class Student(Member):
    def fee(self):
        return 7000

m = Member("지수")
s = Student("하준")
print(m.name, m.fee())
print(s.name, s.fee())


class Parcel:
    def __init__(self, item):
        self.item = item

    def message(self):
        return (f"{self.item} 3일 뒤 도착")

class Quick(Parcel):
    def message(self):
        return (f"{self.item} 내일 도착")

p = Parcel("책")
q = Quick("우산")
print(p.message())
print(q.message())