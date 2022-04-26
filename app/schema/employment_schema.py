import marshmallow as ma

class EmploymentInputSchema(ma.Schema):
    msa_id = ma.fields.Int()
    city = ma.fields.String()
    occ_code = ma.fields.String()


class EmploymentOutputSchema(ma.Schema):
    job = ma.fields.String()
    employment_count = ma.fields.Int()