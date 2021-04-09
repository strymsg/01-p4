from abc import ABC, abstractmethod
from abstract_invoice import AbstractInvoice

class PhysicialInvoice(AbstractInvoice):
    def __init__(self, seller_id, seller_name, date, number,
                 physical_id, branch_location, products=[], buyer=None, ):
        self.physical_id = physical_id
        self.branch_location = branch_location
        # overriding __init__
        self.seller_id = seller_id
        self.seller_name = seller_name
        self.date = date
        self.products = products
        self.buyer = buyer
        self.number = number
        #AbstractInvoice.__init__(self, seller_id, seller_name, date, number, products, buyer)

    def generate_invoice(self):
        print('PHYSICAL INVOICE')
        d = {
            'seller_id': self.seller_id,
            'seller_name': self.seller_name,
            'products': self.products,
            'buyer': self.buyer,
            'date': self.date,
            'number': self.number,
            'physical_id': self.physical_id,
            'branch_location': self.branch_location
        }
        print(d)
        return d

    def print_copy(self):
        print('Physical Invoice')
        d = {
            'seller_id': self.seller_id,
            'seller_name': self.seller_name,
            'products': self.products,
            'buyer': self.buyer,
            'date': self.date,
            'number': self.number,
            'physical_id': self.physical_id,
            'branch_location': self.branch_location
        }
        for k,v in d.items():
            print(f' {k}: {v}')


class DigitalInvoice(AbstractInvoice):
    def __init__(self, seller_id, seller_name, date, number,
                 online_id, verification_url, products=[], buyer=None, ):
        self.online_id = online_id
        self.verification_url = verification_url
        # overriding __init__
        self.seller_id = seller_id
        self.seller_name = seller_name
        self.date = date
        self.products = products
        self.buyer = buyer
        self.number = number

    def generate_invoice(self):
        print('DIGITAL INVOICE')
        d = {
            'seller_id': self.seller_id,
            'seller_name': self.seller_name,
            'products': self.products,
            'buyer': self.buyer,
            'date': self.date,
            'number': self.number,
            'online_id': self.online_id,
            'verification_url': self.verification_url
        }
        print(d)
        return d

    def verify(self):
        pass