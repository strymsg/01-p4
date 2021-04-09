class Buyer:
    def __init__(self, buyer_id, buyer_name):
        self.buyer_id = buyer_id
        self.buyer_name = buyer_name

    def show(self):
        print('Buyer:')
        print(f' Buyer id: {self.buyer_id}')
        print(f" Buyer's name: {self.buyer_name}")