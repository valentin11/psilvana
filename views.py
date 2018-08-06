from app import app, login_manager
from middleware import *
from flask_login import login_required

@app.route('/login', methods=['GET', 'POST'])
def login():
    return page_login()

@app.route('/customers/', methods=['GET'])
@login_required
def customers():
    return page_customers()

@app.route('/customer/', methods=['GET', 'POST'])
@login_required
def newCustomer():
    return page_new_customer()

@app.route('/customer/<int:id>/', methods=['GET', 'PUT'])
@login_required
def editCustomer(id):
    return page_edit_customer(id)

@app.route('/see-customer/<int:id>/', methods=['GET'])
@login_required
def seeCustomer(id):
    return page_see_customer(id)

@app.route('/customer/<int:id>/', methods=['DELETE'])
@login_required
def deleteCustomer(id):
    return page_delete_customer(id)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    return page_register()

@app.route('/logout/', methods=['GET'])
@login_required
def logout():
    return page_logout()
