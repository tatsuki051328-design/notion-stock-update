import os
from get_pages import get_all_database_pages
from client import get_notion_client

def rollover_stock(client, page):
    current_week_stock = page["properties"]["今週の在庫数"]["number"] or 0
    delivery_stock = page["properties"]["納品量"]["number"] or 0
    new_last_week_stock = current_week_stock + delivery_stock

    return client.pages.update(
        page_id=page["id"],
        properties ={
            "今週の在庫数": {"number": 0},
            "納品量": {"number": 0},
            "先週の在庫数": {"number":  new_last_week_stock}
        }
    )

# if __name__ == "__main__":
#     client = get_notion_client()
#     data_sources_id = os.getenv("DATA_SOURCE_ID")
#     pages = get_all_database_pages(client, data_sources_id)
#     for page in pages:
#         rollover_stock(client, page)