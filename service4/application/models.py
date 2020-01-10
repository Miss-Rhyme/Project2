from application import db


class Fortune(db.Model):
   ### id = db.Column(db.Integer
    code = db.Column(db.String(10), nullable=False, unique=True, primary_key=True)
    fortune = db.Column(db.String(200), nullable=False,unique=True)

    def __repr__(self):
        return ''.join([
            'Code: ', str(self.code), '\r\n',
            'Fortune: ', str(self.fortune), '\r\n'
        ])

