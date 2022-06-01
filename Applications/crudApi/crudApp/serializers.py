from marshmallow import Schema, fields, ValidationError, validates
import re

class UserSchema(Schema):
    user_id = fields.Str()
    first_name = fields.Str() 
    last_name = fields.Str() 
    email = fields.Str()

    @validates('email')
    def validate_email(self, value):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.search(regex, value):
            raise ValidationError("Please provide valid email.")

