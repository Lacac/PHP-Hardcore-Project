from datetime import datetime
import peewee

db = peewee.SqliteDatabase("baiviet.db")

class Artical(peewee.Model):
    Title = peewee.CharField()
    Auther = peewee.CharField()
    Brief = peewee.CharField()
    Content = peewee.CharField()
    Publish = peewee.CharField()

    class Meta:
        database = db

try:
    Artical.create_table()
except:
    print('Artical table already exist')

artical1 = Artical(Title='First artical', Auther='Jony English', Brief='this is a brief of the artical', Content='hello world', Publish=datetime.now())
artical2 = Artical(Title='Second artical', Auther='Jony English', Brief='this is a brief of the artical', Content='hello world 2', Publish=datetime.now())
artical3 = Artical(Title='Third artical', Auther='Jony English', Brief='this is a brief of the artical', Content='hello world 3', Publish=datetime.now())
artical4 = Artical(Title='Fourth artical', Auther='Jony English', Brief='this is a brief of the artical', Content='hello world 4', Publish=datetime.now())
artical5 = Artical(Title='Fifth artical', Auther='Jony English', Brief='this is a brief of the artical', Content='hello world 5', Publish=datetime.now())

artical1.save()
artical2.save()
artical3.save()
artical4.save()
artical5.save()

print('===================using select===================')
rows = Artical.select()
for row in rows:
    print("Title: {} | Auther: {} | Brief: {} | Content: {} | Publish: {}".format(row.Title, row.Auther, row.Brief, row.Content, row.Publish))

print('===================using get===================')
result = Artical.get(Artical.Title == 'Second artical')
print("Title: {} | Auther: {} | Brief: {} | Content: {} | Publish: {}".format(result.Title, result.Auther, result.Brief, result.Content, result.Publish))
