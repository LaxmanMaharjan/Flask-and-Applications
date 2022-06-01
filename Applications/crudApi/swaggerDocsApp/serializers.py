from marshmallow import Schema, fields
from crudApp.serializers import UserSchema

class PostSchema(Schema):
    title = fields.Str()
    content = fields.Str()
    user = fields.Nested(UserSchema)

