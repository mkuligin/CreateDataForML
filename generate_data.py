import csv
import random

# Define the column ranges based on the provided example data
columns = {
    'duration': (2, 80),
    'src_bytes': (150, 25200),
    'dst_bytes': (100, 4000),
    'wrong_fragment': (0, 1),
    'urgent': (0, 0),
    'hot': (0, 5),
    'num_failed_logins': (0, 7),
    'count': (2, 60),
    'label': ['normal', 'attack']
}

def generate_row():
    """Generate a single row of test data within the specified bounds."""
    row = {
        'duration': random.randint(*columns['duration']),
        'src_bytes': random.randint(*columns['src_bytes']),
        'dst_bytes': random.randint(*columns['dst_bytes']),
        'wrong_fragment': random.randint(*columns['wrong_fragment']),
        'urgent': random.randint(*columns['urgent']),
        'hot': random.randint(*columns['hot']),
        'num_failed_logins': random.randint(*columns['num_failed_logins']),
        'count': random.randint(*columns['count']),
        'label': random.choice(columns['label'])
    }
    return row

def generate_dataset(num_rows=1000):
    """Generate a dataset with the specified number of rows."""
    data = [generate_row() for _ in range(num_rows)]
    return data

def save_to_csv(data, filename='network_traffic.csv'):
    """Save the generated data to a CSV file."""
    fieldnames = ['duration', 'src_bytes', 'dst_bytes', 'wrong_fragment', 
                  'urgent', 'hot', 'num_failed_logins', 'count', 'label']
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Generated {len(data)} rows and saved to {filename}")

if __name__ == '__main__':
    # Set seed for reproducibility (optional)
    random.seed(42)
    
    # Generate and save the dataset
    data = generate_dataset(1000)
    save_to_csv(data, 'network_traffic.csv')
