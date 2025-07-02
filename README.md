# 🏠 LetsRentz Property Scraper

A Python-based web scraping project to extract rental listings from [LetsRentz](https://www.letsrentz.com), a dynamic property portal. The scraped data is stored in a PostgreSQL database and can be exported to a CSV for further analysis or reporting.

---

## 📌 Features

- Scrapes real-time rental property data via API
- Handles pagination to collect multiple pages of listings
- Stores data in a structured PostgreSQL table
- Exports data to a clean CSV file
- Built with modular Python scripts

---

## 🚀 Tech Stack

- **Python 3.x**
- **Requests** for HTTP requests
- **psycopg2** for PostgreSQL integration
- **CSV** module for data export
- **PostgreSQL** as the database
- **Virtualenv** for dependency isolation

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/amrendra7777/letsrentz-scrapper.git
cd letsrentz-scrapper

### 2. Edit the save_to_postgres.py and generate_csv.py file and replace the password of the database with your own password.
