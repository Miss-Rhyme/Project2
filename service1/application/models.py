from application import db

class Affirmations(db.Model):
    
    code = db.Column(db.String(10), nullable=False, unique=True)
    affirmation = db.Column(db.String(500), nullable=False, unique=True)

    def __repr__(self):
        return ''.join{[
            'Code: ', str(self.code), '\r\n',
            'Affirmation: ', str(self.affirmation), '\r\n'
        ])



#class Lucky(db.Model):
 #   code = db.Column(db.String(10), nullable=False, unique=True)
#    lucky_fortune = db.Column(db.String(200), nullable=False,unique=True)

 #   def __repr__(self):
 #       return ''.join([
 #           'Code: ', str(self.code), '\r\n',
 #           'Lucky Fortune: ', str(self.lucky_fortune), '\r\n'
 #       ])


#class Unlucky(db.Model):
#    code = db.Column(db.String(10), nullable=False, unique=True)
#    unlucky_fortune = db.Column(db.String(200), nullable=False, unique=True)
#
#    def __repr__(self):
#        return ''.join([
#            'Code: ', str(self.code), '\r\n',
#            'Unlucky Fortune: ', str(self.unlucky_fortune), '\r\n'
#        ])
