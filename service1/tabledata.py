from application import db

from application.models import Fortune

db.drop_all() 

db.create_all()

data1 = Fortune(code = "A-1", fortune = "You will have a great day tomorrow")
data2 = Fortune(code = "A-2", fortune = "Oh no, you will step on lego soon! And it will hurt!!!")
data3 = Fortune(code = "A-3", fortune = "Your favourite person will buy you food.")
data4 = Fortune(code = "A-4", fortune = "I see money in your future...it is not yours though.")
data5 = Fortune(code = "B-1", fortune = "You will receive a fortune (cookie)")
data6 = Fortune(code = "B-2", fortune = "Good ideas will soon come to you...like ordering pizza for all.")
data7 = Fortune(code = "B-3", fortune = "Ignore the previous fortune, it lied.")
data8 = Fortune(code = "B-4", fortune = "You will have many friends.. when you have food.")
data9 = Fortune(code = "C-1", fortune = "Some fortune cookies contain no fortune. Sorry.")
data10 = Fortune(code = "C-2", fortune = "Your existence makes some people happy :)")
data11 = Fortune(code = "C-3", fortune = "Stubbing your toe hurts.")
data12 = Fortune(code = "C-4", fortune = "The best kind of TEA is positviTEA")
data13 = Fortune(code = "D-1", fortune = "I cannot help you, for I am just a fortune cookie.")
data14 = Fortune(code = "D-2", fortune = "Mocha is a coffee, not a hot chocolate.")
data15 = Fortune(code = "D-3", fortune = "fortune_cookie.jpg")
data16 = Fortune(code = "D-4", fortune = "You will have a fateful encounter...")

#db.session.add(data)
#db.session.add(data1)

db.session.add_all([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16])

db.session.commit()

