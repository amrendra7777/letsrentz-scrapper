import requests
import time

def fetch_properties():
    """
    Fetches rental property listings from LetsRentz using pagination.
    Returns a list of dictionaries containing structured property data.
    """

    base_url = "https://www.letsrentz.com/filteredProperties"

    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "Referer": "https://www.letsrentz.com/propertysearch/Flat-for-rent-in-Sector-79-Sahibzada-Ajit-Singh-Nagar-Punjab-140308-India/1/30.678061/76.7113748",
        "X-Requested-With": "XMLHttpRequest",
    }

    furnishing_map = {1: "Furnished", 2: "Semi Furnished", 3: "Unfurnished"}
    all_listings = []

    listings_per_page = 12
    pages_to_scrape = 5  # Change this to 216 for a full scrape

    for page in range(pages_to_scrape):
        offset = page * listings_per_page

        params = {
            "property_type_ids[]": "3",  # Property type 3 = Flat
            "offset": str(offset),
            "min_rent": "0",
            "max_rent": "500000",
            "sortBy": "distance",
            "minimumPhotoCount": "0",
            "sortByOrder": "asc",
            "lati": "30.678061",
            "longi": "76.7113748",
            "user_id": "",
            "listed_by": "",
            "livin_couple_allowed": "",
            "fully_independent": "",
            "student_allowed": "",
            "owner_free": "",
            "is_prime": "",
            "rent_negotiable": "",
            "pet_friendly": "",
            "gated_society": "",
            "address": "Sector 79 Sahibzada Ajit Singh Nagar Punjab 140308 India"
        }

        try:
            response = requests.get(base_url, params=params, headers=headers)
            data = response.json()
        except Exception:
            continue  # Skip this page on error

        if not data.get("status") or not data.get("data"):
            continue  # Skip if no results found

        for item in data["data"]:
            all_listings.append({
                "id": item["id"],
                "title": item.get("description", ""),
                "price": item["rent"],
                "bhk": f'{item.get("bedroom", 0)} BHK',
                "address": item.get("full_address", ""),
                "furnishing": furnishing_map.get(item.get("furnished_id", 0), "Unknown"),
                "area": f'{item.get("squarefeet", 0)} Sq.ft',
                "listed_by": item["user_detail"].get("user_type", "unknown"),
                "contact": item["user_detail"].get("phone_number", "NA")
            })

        time.sleep(1)  # Add delay to prevent hitting rate limits

    return all_listings
