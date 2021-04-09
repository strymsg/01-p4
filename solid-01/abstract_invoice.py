from abc import ABC, abstractmethod

class AbstractInvoice(ABC):
    @abstractmethod
    def __init__(self, seller_id, seller_name, date, number, products=[], buyer=None):
        self.seller_id = seller_id
        self.seller_name = seller_name
        self.date = date
        self.products = products
        self.buyer = buyer
        self.number = number

    @abstractmethod
    def generate_invoice(self):
        d = {
            'seller_id': self.seller_id,
            'seller_name': self.seller_name,
            'products': self.products,
            'buyer': self.buyer,
            'date': self.date,
            'number': self.string
        }
        print(d)
        return d