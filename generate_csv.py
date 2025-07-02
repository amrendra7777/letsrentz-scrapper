import csv
import psycopg2

def export_csv():
    """
    Connects to the PostgreSQL database, fetches all records from the listings table,
    and exports the data into a CSV file.
    """
    conn = psycopg2.connect(
        dbname="letsrentz",
        user="postgres",
        password="amrendra",  # Replace with your actual PostgreSQL password
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Fetch all records from the listings table
    cur.execute("SELECT * FROM listings")
    rows = cur.fetchall()

    # Extract column names from the cursor description
    headers = [desc[0] for desc in cur.description]

    # Write the data into a CSV file
    with open("letsrentz_data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    # Close database resources
    cur.close()
    conn.close()

    print("CSV file successfully generated: letsrentz_data.csv")


if __name__ == "__main__":
    export_csv()
