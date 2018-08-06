from app import db
from models import *
from sqlalchemy.exc import IntegrityError

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
        try:
            customer = Customer(name, phone)
            db.session.add(customer)
            db.session.flush()
            customer.tintas = self.makeArrayOfTintasObjFromStr(strTintas, customer.id)
            db.session.commit()
            return ""
        except IntegrityError:
            db.session.rollback()
            return "Something go wrong"

    def upd_customer(self, customerId, name, phone, tintas):
        try:
            customer = Customer.query.get(customerId)
            customer.name = name
            customer.phone = phone
            self.deleteAllCustomerTintasByCustomerId(customerId)
            customer.tintas = self.makeArrayOfTintasObjFromStr(tintas, customerId)
            db.session.commit()
            return ""
        except IntegrityError:
            db.session.rollback()
            return "Something go wrong"

    def delete_customer(self, customerId):
        customer = Customer.query.get(customerId)
        db.session.delete(customer)
        db.session.commit()

    def new_user(self, fullname, username, password):
        try:
            user = User(fullname, username, password)
            db.session.add(user)
            db.session.commit()
            return ""
        except IntegrityError:
            db.session.rollback()
            return "This Username has already exist"


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
