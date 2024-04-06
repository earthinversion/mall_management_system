from flask import Flask, render_template, request, redirect, url_for
from config import Config
from extensions import db
from models import Purchase

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def index():
    purchases = Purchase.query.all()
    return render_template('index.html', purchases=purchases)

@app.route('/add', methods=['GET', 'POST'])
def add_purchase():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        amount = request.form['amount']
        new_purchase = Purchase(customer_name=customer_name, amount=amount)

        db.session.add(new_purchase)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('add_purchase.html')

@app.route('/purchases')
def purchase_records():
    purchases = Purchase.query.all()
    return render_template('purchase_records.html', purchases=purchases)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
