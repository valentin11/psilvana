from app import db
from models import *

class DataProvider:
    def __init__(self):
        db.create_all()

    def get_user(self, username, password):
        return User.query.filter_by(username=username, password=password).first()

    def get_customers(self):
        customers = Customer.query.all()
        return [cust.serialize for cust in customers]

    def get_customerById(self, id):
        return Customer.query.get(id)

    def new_customer(self, name, phone, strTintas):
        customer = Customer(name, phone)
        db.session.add(customer)
        db.session.flush()
        customer.tintas = self.makeArrayOfTintasObjFromStr(strTintas, customer.id)
        db.session.commit()

    def upd_customer(self, customerId, name, phone, tintas):
        customer = Customer.query.get(customerId)
        customer.name = name
        customer.phone = phone
        self.deleteAllCustomerTintasByCustomerId(customerId)
        customer.tintas = self.makeArrayOfTintasObjFromStr(tintas, customerId)
        db.session.commit()

    def delete_customer(self, customerId):
        customer = Customer.query.get(customerId)
        db.session.delete(customer)
        db.session.commit()


# Aux Functions
    def deleteAllCustomerTintasByCustomerId(self, customerId):
        Tinta.query.filter_by(customerId=customerId).delete()

    def makeArrayOfTintasObjFromStr(self, strTintas, customerId):
        tintasObj = []
        for x, y in self.pairwise(strTintas):
            tintasObj.append(Tinta(x, y, customerId))
        return tintasObj

    def pairwise(self, iterable):
        # s -> (s0, s1), (s2, s3), (s4, s5), ...
        a = iter(iterable)
        return zip(a, a)
