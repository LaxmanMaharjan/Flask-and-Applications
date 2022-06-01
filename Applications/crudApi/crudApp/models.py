from crudApi import db

class User(db.Document):
    user_id = db.StringField(required=True,unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True)

    def __repr__(self):
        return f"<User: {self.first_name}>"
