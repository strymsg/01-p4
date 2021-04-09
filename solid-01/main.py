from product import Product
from abstract_invoice import AbstractInvoice
from buyer import Buyer
from invoices import PhysicialInvoice, DigitalInvoice

if __name__ == '__main__':
    # creating some samples
    p1 = Product(name='capucino', description='A cup of coffe', price=12.5)
    p2 = Product(name='blue mountain', description='A cup of coffe', price=14.5)
    p3 = Product(name='expresso', description='3 cup of coffe', price=22)

    b1 = Buyer(buyer_id='C881841', buyer_name='Juan Morales')
    b2 = Buyer(buyer_id='D254151', buyer_name='Maria Ramos')
    b3 = Buyer(buyer_id='N88751', buyer_name='Ester Perwz')

    pi1 = PhysicialInvoice(seller_id='S-5151',
                           seller_name='Tokki Coffe',
                           products=[p1,p2],
                           buyer=b1,
                           date='03-21-2021',
                           number='AAAA332',
                           physical_id='PCCCC1',
                           branch_location='Asturias Avenune #541')

    pi1.generate_invoice()
    print()
    pd1 = DigitalInvoice(seller_id='S-5151',
                        seller_name='Grand Parris Coffe',
                        products=[p3],
                        buyer=b2,
                        date='03-20-2021',
                        number='CCCCCCCCC7722',
                         online_id='C81851/6515610512312-31231243',
                         verification_url='https://harddw.com/verify/C81851/6515610512312-31231243')
    pd1.generate_invoice()