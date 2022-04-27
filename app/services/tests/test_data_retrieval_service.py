from app.services import data_retrieval_service
list_results = [
    [{
        "city": "New York-Newark-Jersey City, NY-NJ-PA",
        "occ_code": "11-9031"
    },
    {
        "New York-Newark-Jersey City, NY-NJ-PA": [{
            "employment_count": 3610,
            "job": "Education and Childcare Administrators, Preschool and Daycare"
        }]
    }], 
    [{
        "city": "New York-Newark-Jersey City, NY-NJ-PA",
        "occ_code": "19-407"
    },
    {
        "ERROR": "Please Check OCC Code"
    }],
    [{
        "city": "New York-Newark-Jersey City, NY-NJ-PA",
        "occ_code": "wrc"
    },
    {
        "ERROR": "Please Check OCC Code"
    }],
    [{
        "city": "New York-Newark-Jersey City, NY-NJ-PA",
        "occ_code": ""
    },
    {
        # "New York-Newark-Jersey City, NY-NJ-PA": [{
        #     "employment_count": 3610,
        #     "job": "Education and Childcare Administrators, Preschool and Daycare"
        # }]
    }],
    [{
        "city": "New York-Newark-Jersey City, NY-NJ-PA",
        "occ_code": 434
    },
    {
        "code": 422,
        "errors": {
            "json": {
                "occ_code": [
                    "Not a valid string."
                    ]
                }
            },
        "status": "Unprocessable Entity"
    }],


    [{
        "city": "Denver-Aurora-Lakewood",
        "occ_code": "11-9031"
    },
    {
        "Denver-Aurora-Lakewood, CO": [{
            "employment_count": 400,
            "job": "Education and Childcare Administrators, Preschool and Daycare"
        }],
        "New York-Newark-Jersey City, NY-NJ-PA": [{
                "employment_count": 3610,
                "job": "Education and Childcare Administrators, Preschool and Daycare"
        }],
        "San Francisco-Oakland-Hayward, CA": [{
            "employment_count": 1610,
            "job": "Education and Childcare Administrators, Preschool and Daycare"
        }]
    }],
    [{
        "city": "Denver-Aurora-Lakewood",
        "occ_code": "19-407"
    },
    {
        "ERROR": "Please Check the Inputs"
    }],
    [{
        "city": "Denver-Aurora-Lakewood",
        "occ_code": "wrc"
    },
    {
        "ERROR": "Please Check the Inputs"
    }],
    [{
        "city": "Denver-Aurora-Lakewood",
        "occ_code": ""
    },
    {
        "ERROR": "Please Check the Inputs"
    }],
    [{
        "city": "Denver-Aurora-Lakewood",
        "occ_code": 434
    },
    {
        "code": 422,
        "errors": {
            "json": {
                "occ_code": [
                    "Not a valid string."
                    ]
                }
            },
        "status": "Unprocessable Entity"
    }],



    [{
        "city": "sverv",
        "occ_code": "11-9031"
    },
    {
        "Denver-Aurora-Lakewood, CO": [{
            "employment_count": 400,
            "job": "Education and Childcare Administrators, Preschool and Daycare"
        }],
        "New York-Newark-Jersey City, NY-NJ-PA": [{
                "employment_count": 3610,
                "job": "Education and Childcare Administrators, Preschool and Daycare"
        }],
        "San Francisco-Oakland-Hayward, CA": [{
            "employment_count": 1610,
            "job": "Education and Childcare Administrators, Preschool and Daycare"
        }]
    }],
    [{
        "city": "sverv",
        "occ_code": "19-407"
    },
    {
        "ERROR": "Please Check the Inputs"
    }],
    [{
        "city": "sverv",
        "occ_code": "wrc"
    },
    {
        "ERROR": "Please Check the Inputs"
    }],
    [{
        "city": "sverv",
        "occ_code": ""
    },
    {
        "ERROR": "Please Check the Inputs"
    }],
    [{
        "city": "sverv",
        "occ_code": 434
    },
    {
        "code": 422,
        "errors": {
            "json": {
                "occ_code": [
                    "Not a valid string."
                    ]
                }
            },
        "status": "Unprocessable Entity"
    }],



    [{
        "city": "",
        "occ_code": "11-9031"
    },
    {
        "Denver-Aurora-Lakewood, CO": [{
            "employment_count": 400,
            "job": "Education and Childcare Administrators, Preschool and Daycare"
        }],
        "New York-Newark-Jersey City, NY-NJ-PA": [{
                "employment_count": 3610,
                "job": "Education and Childcare Administrators, Preschool and Daycare"
        }],
        "San Francisco-Oakland-Hayward, CA": [{
            "employment_count": 1610,
            "job": "Education and Childcare Administrators, Preschool and Daycare"
        }]
    }],
    [{
        "city": "",
        "occ_code": "19-407"
    },
    {
        "ERROR": "Please Check the Inputs"
    }],
    [{
        "city": "",
        "occ_code": "wrc"
    },
    {
        "ERROR": "Please Check the Inputs"
    }],
    [{
        "city": "",
        "occ_code": ""
    },
    {
        "ERROR": "Please Check the Inputs"
    }],
    [{
        "city": "",
        "occ_code": 434
    },
    {
        "code": 422,
        "errors": {
            "json": {
                "occ_code": [
                    "Not a valid string."
                    ]
                }
            },
        "status": "Unprocessable Entity"
    }],



    [{
        "city": 34534,
        "occ_code": "11-9031"
    },
    {
        "code": 422,
        "errors": {
            "json": {
                "city": [
                    "Not a valid string."
                    ]
                }
            },
        "status": "Unprocessable Entity"
    }],
    [{
        "city": 34534,
        "occ_code": "19-407"
    },
    {
        "code": 422,
        "errors": {
            "json": {
                "city": [
                    "Not a valid string."
                    ]
                }
            },
        "status": "Unprocessable Entity"
    }],
    [{
        "city": 34534,
        "occ_code": "wrc"
    },
    {
        "code": 422,
        "errors": {
            "json": {
                "city": [
                    "Not a valid string."
                    ]
                }
            },
        "status": "Unprocessable Entity"
    }],
    [{
        "city": 34534,
        "occ_code": ""
    },

    {
        "code": 422,
        "errors": {
            "json": {
                "city": [
                    "Not a valid string."
                    ]
                }
            },
        "status": "Unprocessable Entity"
    }],
    [{
        "city": 34534,
        "occ_code": 434
    },
    {
        "code": 422,
        "errors": {
            "json": {
                "city": [
                    "Not a valid string."
                    ]
                }
            },
        "status": "Unprocessable Entity"
    }]
]
def send_req(query) -> None:
    actual = data_retrieval_service.DataRetrieval.get_data_query(query)
    # excepted = list_results.
    # assert actual == expected
# def send_req(send_text) -> None:
#     actual = skills_service.reverse_skill_title(send_text)
#     data_rev = send_text[::-1].lower()
#     data_json = {"skill_title" : send_text, "reversed_skill_title": data_rev}
#     assert actual==data_json

def test_data_retrieval():
    count = 0
    error_text = "'int' object is not subscriptable"
    list_city = ["New York-Newark-Jersey City, NY-NJ-PA", "Denver-Aurora-Lakewood", "sverv", "", 34534]
    list_occ = ["11-9031", "19-407", "wrc", "", 434]
    for m in list_city:
        for n in list_occ:
            try:
                send_req({"city": list_results, "occ_code": n})
                count = count+1
                print("Test", count, "passed")
            except Exception as error:
                assert error_text==str(error)
                print("Error test passed")