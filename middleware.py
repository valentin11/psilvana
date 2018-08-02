from flask import render_template, redirect, url_for, request, jsonify
from data_provider import DataProvider
from flask_login import login_user, logout_user, current_user
from forms import *
import json

dataProvider = DataProvider()

# Web page logic
def page_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = dataProvider.get_user(username, password)
        if user is None:
            form.username.errors.append('Incorrect Username or Password.')
            form.password.errors.append('Incorrect Username or Password.')
        else:
            login_user(user)
            return redirect(url_for('customers'))
    return render_template('login.html', form=form)

def page_customers():
    #if (not current_user.is_authenticated):
    #    return redirect(url_for('login'))

    customers = dataProvider.get_customers()
    return render_template('customers.html', customers=customers)

def page_new_customer():
    if request.method == 'POST':
        dataProvider.new_customer(request.form['fullName'], request.form['mobilePhone'], (request.form['tintas']).split(','))
        return jsonify({"status": "OK"})

    form = CustomerForm()
    return render_template('customer.html', mode="ADD", jsonMode=json.dumps("ADD"), form=form, tintas=[])

def page_see_customer(id):
    customer = dataProvider.get_customerById(id)
    form = CustomerForm()
    form.fullName.render_kw = {'disabled': 'disabled'}
    form.mobilePhone.render_kw = {'disabled': 'disabled'}
    form.fullName.data = customer.name
    form.mobilePhone.data = customer.phone
    return render_template('customer.html', mode="SEE", form=form, tintas=customer.tintas)

def page_edit_customer(id):
    if request.method == 'PUT':
        dataProvider.upd_customer(id, request.form['fullName'], request.form['mobilePhone'], (request.form['tintas']).split(','))
        return jsonify({"status": "OK"})

    customer = dataProvider.get_customerById(id)
    form = CustomerForm()
    form.fullName.data = customer.name
    form.mobilePhone.data = customer.phone
    return render_template('customer.html', mode="UPD", jsonMode=json.dumps("UPD"), id=id, form=form, tintas=customer.tintas)

def page_delete_customer(id):
    dataProvider.delete_customer(id)
    return jsonify({"status": "OK"})

def page_register():
    return render_template('register.html')

def page_logout():
    logout_user()
    return redirect(url_for('login'))
