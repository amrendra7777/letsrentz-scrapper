import psycopg2
from scrape_properties import fetch_properties

def save_to_postgres(data):
    """
    Connects to a PostgreSQL database, creates a table if it doesn't exist,
    and inserts the scraped property data into the table.
    """
    conn = psycopg2.connect(
        dbname="letsrentz",
        user="postgres",
        password="amrendra",  # Replace with your actual PostgreSQL password
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Create the listings table if it does not already exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS listings (
            id INTEGER PRIMARY KEY,
            title TEXT,
            price INTEGER,
            bhk TEXT,
            address TEXT,
            furnishing TEXT,
            area TEXT,
            listed_by TEXT,
            contact TEXT
        )
    """)

    # Insert each property record into the table
    for item in data:
        cur.execute("""
            INSERT INTO listings (id, title, price, bhk, address, furnishing, area, listed_by, contact)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """, (
            item["id"], item["title"], item["price"], item["bhk"],
            item["address"], item["furnishing"], item["area"],
            item["listed_by"], item["contact"]
        ))

    conn.commit()
    print("Data successfully saved to PostgreSQL")

    # Close the cursor and connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    # Fetch property listings and store them in the database
    data = fetch_properties()
    print(f"Fetched {len(data)} items")
    save_to_postgres(data)
