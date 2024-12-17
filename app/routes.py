from flask import Blueprint, render_template, request, redirect, url_for, flash
from .firebase import get_table_data  # Assuming you have a function to get table data

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('signin.html')

@main_bp.route('/submit', methods=['POST'])
def submit():
    table_number = request.form['table_number']
    if table_number:
        table_data = get_table_data(table_number)  # Get table data from Firebase
        
        if table_data is None:
            flash("Table number does not exist!")  # Show error if table doesn't exist
            return redirect(url_for('main.home'))
        
        if table_data['is_occupied']:
            flash("Table is already occupied.", "message")  # Show error if table is occupied
            return redirect(url_for('main.home'))
        
        # If table is not occupied, redirect to the dashboard
        return redirect(url_for('main.dashboard', table_number=table_number))

    flash("Please enter a table number.")
    return redirect(url_for('main.home'))

from flask import render_template
from .firebase import get_table_data  # Assuming this is your function to get data

@main_bp.route('/dashboard/<table_number>')
def dashboard(table_number):
    table_data = get_table_data(table_number)  # Fetch the data for the table
    if table_data is None:
        return render_template('error.html', message="Table not found")
    return render_template('dashboard.html', table_number=table_number, table_data=table_data)

