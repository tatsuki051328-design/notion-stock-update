import os
import json
from client import get_notion_client

def get_all_database_pages(client, data_source_id):
    pages = []
    while True:
        response = client.data_sources.query(data_source_id=data_source_id)
        pages.extend(response["results"])
        if not response["has_more"]:
            break
    return pages
    
# if __name__ == "__main__":
#     client = get_notion_client()
#     data_sources_id = os.getenv("DATA_SOURCE_ID")
#     pages = get_all_database_pages(client, data_sources_id)
#     print(json.dumps(pages, ensure_ascii=False,indent=2))