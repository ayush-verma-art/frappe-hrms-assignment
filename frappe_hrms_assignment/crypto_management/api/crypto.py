import frappe
import requests
from datetime import datetime

# API to fetch and store data
COINS = {
    "bitcoin": "BTC",
    "ethereum": "ETH"
}

@frappe.whitelist()
def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    params = {
        "ids": ",".join(COINS.keys()),
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        frappe.throw("Failed to fetch crypto prices")

    data = response.json()

    created_records = []

    for coin, symbol in COINS.items():
        rate = data.get(coin, {}).get("usd")

        if not rate:
            continue

        doc = frappe.get_doc({
            "doctype": "Crypto Prices",
            "cryptocurrency_name": coin.title(),
            "symbol": symbol,
            "rate": rate,
            "timestamp": datetime.now(),
            "date": datetime.today().date()
        })

        doc.insert(ignore_permissions=True)
        created_records.append(doc.name)

    return {
        "status": "success",
        "records_created": created_records
    }

# API to get paginated data
@frappe.whitelist(allow_guest=True)
def get_crypto_prices(page=1, page_size=10):
    page = int(page)
    page_size = int(page_size)

    # offset calculate
    offset = (page - 1) * page_size

    # total records
    total = frappe.db.count("Crypto Prices")

    # data fetch
    data = frappe.get_all(
        "Crypto Prices",
        fields=["name", "cryptocurrency_name", "symbol", "rate", "timestamp", "date"],
        order_by="timestamp desc",
        limit_start=offset,
        limit_page_length=page_size
    )

    return {
        "status": "success",
        "page": page,
        "page_size": page_size,
        "total_records": total,
        "total_pages": (total // page_size) + (1 if total % page_size else 0),
        "data": data
    }