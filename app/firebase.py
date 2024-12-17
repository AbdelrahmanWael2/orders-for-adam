import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./firebase_config.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_table_data(table_number):
    table_ref = db.collection('tables').document(table_number)
    table_ref.set({
        'status': 'open',
        'order': 'None'
    })

def get_table_data(table_number):
    # Reference to the specific document for the table in Firestore
    table_ref = db.collection('restaurant_tables').document(str(table_number))
    
    # Get the document
    table_doc = table_ref.get()

    if table_doc.exists:
        # Return the table data as a dictionary
        return table_doc.to_dict()
    else:
        # If table does not exist, return None
        return None

def add_sample_data():
    # Reference to Firestore collection (restaurant_tables)
    tables_ref = db.collection('restaurant_tables')

    # Sample data for tables
    sample_tables = [
        {'table_number': 1, 'is_occupied': False, 'order_status': 'open'},
        {'table_number': 2, 'is_occupied': True, 'order_status': 'processing'},
        {'table_number': 3, 'is_occupied': False, 'order_status': 'open'},
        {'table_number': 4, 'is_occupied': True, 'order_status': 'delivered'},
        {'table_number': 5, 'is_occupied': False, 'order_status': 'open'},
    ]

    # Add sample tables to Firestore
    for table in sample_tables:
        table_ref = tables_ref.document(str(table['table_number']))
        table_ref.set(table)

    print("Sample data added successfully!")

#  add sample data
add_sample_data()
