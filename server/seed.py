from app import app
from config import db
from models import Plant

with app.app_context():
    db.drop_all()
    db.create_all()

    plants = [
        Plant(name="Aloe", image="./images/aloe.jpg", price=11.50, is_in_stock=True),
        Plant(name="Fiddle Leaf Fig", image="./images/fig.jpg", price=45.00, is_in_stock=True),
        Plant(name="Snake Plant", image="./images/snake.jpg", price=22.00, is_in_stock=True),
    ]

    db.session.add_all(plants)
    db.session.commit()
    print("Seeded plants!")
