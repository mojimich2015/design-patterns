from abc import ABCMeta, abstractmethod


# Subject
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


# Real Subject
class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __get_account(self):
        self.account = self.card
        return self.account

    def __check_balance(self):
        print("Bank:: Will check if the account: ", self.__get_account(), "has enough money or not")
        return True

    def set_card(self, card):
        self.card = card

    def do_pay(self):
        if self.__check_balance():
            print("Bank:: The price is payed")
            return True
        else:
            print("Bank:: Not enough money")
            return False


# Proxy
class Card(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy:: Enter bank card number: ")
        self.bank.set_card(card)
        return self.bank.do_pay()


# Client
class You:
    def __init__(self):
        print("You:: I want a shirt")
        self.card = Card()
        self.isPurchased = None

    def pay(self):
        self.isPurchased = self.card.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("You:: I've bought a shirt")
        else:
            print("You:: I didn't have enough money")


you = You()
you.pay()
