import xmlrpc.client

url = "http://localhost:8080"
db = "odoo18"
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy("http://localhost:8080/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})


models = xmlrpc.client.ServerProxy("http://localhost:8080/xmlrpc/2/object")

#execute_kw
# Create
new_partner_id = models.execute_kw(db, uid, password,
    'res.partner', 'create',
    [{
        'name': "TEST API CUSTOMER",
        'email': "api.test@example.com",
        'is_company': True
    }])

new_partner_id = 48
# Read
partner_data = models.execute_kw(db, uid, password,
    'res.partner', 'read',
    [[new_partner_id]],
    {'fields': ['name', 'email', 'is_company']})
print(partner_data)

# Write
models.execute_kw(db, uid, password,
    'res.partner', 'write',
    [[new_partner_id], {'name': 'TEST API CUSTOMER Updated'}])
print("Updated.")

# Search
found_ids = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[['name', '=', 'TEST API CUSTOMER Updated']]])
print(f"Found Partner IDs: {found_ids}")

# Name Search
name_matches = models.execute_kw(db, uid, password,
    'res.partner', 'name_search',
    ['TEST API CUSTOMER Updated'])
print(name_matches)

# Field metadata
field_info = models.execute_kw(db, uid, password,
    'res.partner', 'fields_get',
    [],
    {'attributes': ['string', 'help', 'type']})
print(field_info)
print("Field 'email':", field_info['email'])

# DELETE
models.execute_kw(db, uid, password,
    'res.partner', 'unlink',
    [[new_partner_id]])
print("Deleted.")
