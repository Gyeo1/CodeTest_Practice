# 클래스 빈칸채우기 문제
from abc import *


class Book(metaclass=ABCMeta):
    @abstractmethod
    def get_rental_price(self, day):
        pass


## 문제 부분
class ComicBook(Book): #()안에 빈칸 문제: ComicBook은 book을 상속받으니깐 book을 넣어준다.
    def get_rental_price(self, day):#빈칸: 함수 전체를 정의하시오, Book에 있는 그대로를 가져와서 사용한다.
        cost = 500
        day -= 2
        if day > 0:
            cost += 200 * day #빈칸 2: 2일은 기본요금이고 2일 이후부터는 200원씩 주므로 day-2를하고 1이상이면 남은 day*200해주면 된다
        return cost


class Novel(Book):#빈칸: Book 넣기
    def get_rental_price(self, day): # 빈칸: 함수 전체 정의: 마찬가지로 get_rental_price를 구해야되기 때문에 Book의 형태 그대로 사용
        cost = 1000
        day -= 3
        if day > 0:
            cost += 300 * day #빈칸: 소설은 기본 3일은 천원으로 책정, 이후에는 남은 day마다 300원씩 이므로
        return cost


def solution(book_types, day):
    books = []
    for types in book_types:
        if types == "comic":
            books.append(ComicBook())
        elif types == "novel":
            books.append(Novel())

    total_price = 0
    for book in books:
        total_price += book.get_rental_price(day)
    return total_price


###
book_types = ["comic", "comic", "novel"]
day = 4
ret = solution(book_types, day)

print("solution 함수의 반환 값은", ret, "입니다.")
