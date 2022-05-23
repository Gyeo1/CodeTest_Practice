from abc import *


class DeliveryStore(metaclass=ABCMeta):
    @abstractmethod
    def set_order_list(self, order_list):
        pass

    @abstractmethod
    def get_total_price(self):
        pass


class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class PizzaStore(DeliveryStore):  # 1번 빈칸 해설 => DeliveryStore를 상속받는다는 것을 뜻함
    def __init__(self):
        menu_names = ["Cheese", "Potato", "Shrimp", "Pineapple", "Meatball"]
        menu_prices = [11100, 12600, 13300, 21000, 19500];
        self.menu_list = []
        for i in range(5):
            self.menu_list.append(Food(menu_names[i], menu_prices[i]))

        self.order_list = []

    def set_order_list(self, order_list): #두번째 빈칸 set_order_list를 작성
        for order in order_list:
            self.order_list.append(order)

    def get_total_price(self): #세번째 빈칸 get_total_price를 작성
        total_price = 0
        for order in self.order_list:
            for menu in self.menu_list:
                if order == menu.name:
                    total_price += menu.price
        return total_price


def solution(order_list):
    delivery_store = PizzaStore()

    delivery_store.set_order_list(order_list)
    total_price = delivery_store.get_total_price()
    return total_price


order_list = ["Cheese", "Pineapple", "Meatball"]
ret = solution(order_list)

print("solution 함수의 반환 값은", ret, "입니다.")
