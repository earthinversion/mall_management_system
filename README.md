mkdir world_trade_park_mall
cd world_trade_park_mall
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install Flask Flask-SQLAlchemy


## Application Structure
```
world_trade_park_mall/
    app.py
    models.py
    config.py
    extensions.py
    /templates
        index.html
        add_purchase.html
        purchase_records.html

```