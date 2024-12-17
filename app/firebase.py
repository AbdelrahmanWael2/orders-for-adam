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



# Example function to simulate fetching paginated items from a database with 12 items
def get_items(page=1, per_page=10):
    items = [
        {'name': 'Item 1', 'description': 'Description 1', 'price': 10, 'image_url': 'path/to/image1.jpg'},
        {'name': 'Item 2', 'description': 'Description 2', 'price': 20, 'image_url': 'path/to/image2.jpg'},
        {'name': 'Item 3', 'description': 'Description 3', 'price': 30, 'image_url': 'path/to/image3.jpg'},
        {'name': 'Item 4', 'description': 'Description 4', 'price': 40, 'image_url': 'path/to/image4.jpg'},
        {'name': 'Item 5', 'description': 'Description 5', 'price': 50, 'image_url': 'path/to/image5.jpg'},
        {'name': 'Item 6', 'description': 'Description 6', 'price': 60, 'image_url': 'path/to/image6.jpg'},
        {'name': 'Item 7', 'description': 'Description 7', 'price': 70, 'image_url': 'path/to/image7.jpg'},
        {'name': 'Item 8', 'description': 'Description 8', 'price': 80, 'image_url': 'path/to/image8.jpg'},
        {'name': 'Item 9', 'description': 'Description 9', 'price': 90, 'image_url': 'path/to/image9.jpg'},
        {'name': 'Item 10', 'description': 'Description 10', 'price': 100, 'image_url': 'path/to/image10.jpg'},
        {'name': 'Item 11', 'description': 'Description 11', 'price': 110, 'image_url': 'path/to/image11.jpg'},
        {'name': 'Item 12', 'description': 'Description 12', 'price': 120, 'image_url': 'path/to/image12.jpg'}
    ]
    
    # Return items for the current page, with 10 items per page
    start = (page - 1) * per_page
    end = start + per_page
    return items[start:end]
