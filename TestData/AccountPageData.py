class AccountPageData:

    invalid_address_data = [{"id": "fristname_missing", "firstname": None, "lastname": "Patil",
                             "street-address": "Nagard road near saraswati school", "phone": "9326718923",
                             "city": "Pune", "postcode": "418923", 'state': "Maharashtra"},

                            {"id": "lastname_missing", "firstname": "ABC", "lastname": None,
                             "street-address": "Nagard road near saraswati school", "phone": "9326718923",
                             "city": "Pune", "postcode": "418923", 'state': "Maharashtra"},

                            {"id": "postcode_missing", "firstname": "ABC", "lastname": "Patil",
                             "street-address": "Nagard road near saraswati school", "phone": "9326718923",
                             "city": "Pune", "postcode": None, 'state': "Maharashtra"},

                            {"id": "street_address_missing", "firstname": "ABC", "lastname": "Patil",
                             "street-address": None, "phone": "9326718923",
                             "city": "Pune", "postcode": "418923", 'state': "Maharashtra"},

                            {"id": "city_missing", "firstname": "ABC", "lastname": "Patil",
                             "street-address": "Nagard road near saraswati school", "phone": "9326718923",
                             "city": None, "postcode": "418923", 'state': "Maharashtra"}]