from marshmallow import fields, Schema

class CategoriaSchema(Schema):
    """Activity schema"""
    
    acti_id = fields.Integer()
    acti_name = fields.String()
    acti_hour = fields.DateTime()
    date = fields.DateTime()
    user_id = fields.Integer()
