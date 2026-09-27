import os
from client import get_notion_client
from get_pages import get_all_database_pages
from update_page import rollover_stock

def run_cafe_beans_rollover():
    client = get_notion_client()
    data_sources_id = os.getenv("DATA_SOURCE_ID")
    pages = get_all_database_pages(client, data_sources_id)
    for page in pages:
        rollover_stock(client, page)

if __name__ == "__main__":
    run_cafe_beans_rollover()