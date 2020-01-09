from application import db

from application.models import Fortune

db.drop_all() 

db.create_all()

data = Fortune(code = "A1", fortune = "You will have a fateful encounter")
data1 = Fortune(code = "A2", fortune = "You will have a great day tomorrow")


db.session.add(data)
db.session.add(data1)

db.session.commit()

