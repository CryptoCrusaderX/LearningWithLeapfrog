# Polymorphism with Inheritance (method overiding)
class Payment:
    def process_payment(self):
        return "Processing Generic Payment!"


class CreditCardPayment(Payment):
    def process_payment(self):
        return "Processing Credit Card Payment!"


class PayPalPayment(Payment):
    def process_payment(self):
        return "Processing PayPal Payment"


# Polymorphic Function!
def execute_payment(payment_method):
    print(payment_method.process_payment())


credit_card = CreditCardPayment()
paypal = PayPalPayment()

execute_payment(credit_card)
execute_payment(paypal)
