from extensions import db

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
