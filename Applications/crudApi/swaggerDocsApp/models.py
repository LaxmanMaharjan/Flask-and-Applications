from crudApi import db
from crudApp.models import User

class Post(db.Document):
    title = db.StringField(required=True, unique=True)
    content = db.StringField(required=True)
    user = db.ReferenceField(User)

    def __repr__(self):
        return f"<Post: {self.title}>"
