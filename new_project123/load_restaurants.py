import csv
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_project123.settings')
django.setup()

from app.models import Restaurant

# Path to CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), 'restaurants.csv')

# Load data from CSV
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Restaurant.objects.create(
            name=row['restaurant_name'],
            zone=row['location'],
            table_size=int(row['table_size']),
            table_count=int(row['table_count'])
        )

print("Restaurants loaded successfully.")