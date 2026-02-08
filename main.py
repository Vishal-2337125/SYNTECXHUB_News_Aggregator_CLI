import config
from fetcher import HeadlineFetcher
from database import DatabaseManager
from exporter import DataExporter

def main():
    fetcher = HeadlineFetcher()
    db = DatabaseManager(config.DB_NAME)

    print(f"[*] Scraping: {config.TARGET_URL}")
    data = fetcher.get_headlines(config.TARGET_URL)
    
    if data:
        new_items = db.save(data)
        print(f"[+] Found {len(data)} headlines. {new_items} were new.")
        
        # Pull all data for export
        full_df = db.get_as_df()
        DataExporter.export_clickable_excel(full_df, config.EXCEL_NAME)
        print(f"[+] Success! Clickable Excel saved as: {config.EXCEL_NAME}")
    else:
        print("[!] No news found. The site might be blocking the request.")

if __name__ == "__main__":
    main()