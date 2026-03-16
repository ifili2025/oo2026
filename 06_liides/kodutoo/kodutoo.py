from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self):
        self.history = []
    @abstractmethod
    def pay(self, amount, employee):
        pass
    
    @abstractmethod
    def refund(self, amount, employee):
        pass
    def add_to_history(self, action, amount, employee):
        self.history.append({
            'action': action,
            'amount': amount,
            'employee': employee
        })
    def print_history(self):
        if not self.history:
            print("No payment history.")
        else:
            print("Payment history:")
            for record in self.history:
                print(f"{record['action'].capitalize()}: {record['amount']} (employee: {record['employee']})")
class CardPayment(Payment):
    def pay(self,amount,employee):
        print(f"Paid {amount} using cardpayment, served {employee}")
        self.add_to_history('pay', amount, employee)
    def refund(self, amount,employee):
        print(f"Refunded {amount} to card, served {employee} ")
        self.add_to_history('refund', amount, employee)
class CashPayment(Payment):
    def pay(self,amount,employee):
        print(f"Paid {amount} using cashpayment, served {employee}")
        self.add_to_history('pay', amount, employee)
    def refund(self, amount, employee):
        print(f"Refunded {amount} in cash, served {employee}")
        self.add_to_history('refund', amount, employee)
 
payment = CardPayment()
payment.print_history() 
payment.pay(100, 'Igor Filippov')
payment.refund(50, 'Dust Mirage')
payment2 = CashPayment()
payment2.pay(100, 'Nuke Train')
payment2.refund(50, 'Anubis Cache')
payment.print_history()
