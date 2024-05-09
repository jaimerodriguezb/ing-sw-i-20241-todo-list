from marshmallow import fields, Schema

class ActivitySchema(Schema):
    """Activity schema"""

    name = fields.String()
    hour = fields.DateTime()
    date = fields.DateTime()
    user_id = fields.Integer()
