import marshmallow as ma

class EmploymentInputSchema(ma.Schema):
    msa_id = ma.fields.Int()
    city = ma.fields.String()
    occ_code = ma.fields.String()