📰 SYNTECXHUB News Aggregator
A smart Python utility that collects, archives, and exports news headlines into interactive reports.

📝 Project Basics: What is this?
A News Aggregator is a tool that "harvests" information from various digital sources and brings it into one place.

What we are doing: Instead of manually checking news sites every hour, we have built an automated pipeline that visits a website, "reads" the headlines like a human would, saves them into a permanent database to avoid duplicates, and finally creates a clean Excel spreadsheet where every headline is a clickable button.

🛠️ Project Modules (How it's Built)
To keep the code clean and professional, we divided the project into four specialized modules:
1. The Scraper (fetcher.py)
Role: The "Eyes" of the project.
What it does: It connects to the internet, downloads the website's code, and uses BeautifulSoup to hunt for specific HTML tags (like <h2> or <a>) that contain headlines.
Logic: It filters out junk text and ensures only actual news titles are collected.

2. The Database (database.py)
Role: The "Memory."
What it does: It uses SQLite (a lightweight database) to store every headline we find.
Logic: It uses the article's URL as a "Primary Key." This means if the script finds the same story twice, the database will automatically ignore the second one, keeping your list clean and unique.

3. The Stylist (exporter.py)
Role: The "Reporter."
What it does: It takes the raw data from the database and uses Pandas and OpenPyXL to build an Excel file.
Logic: It converts plain text links into executable =HYPERLINK formulas, so the final user can click any headline to open the story in a browser.

4. The Brain (main.py)
Role: The "Controller."
What it does: It coordinates the other three modules. It tells the Fetcher to start, hands the data to the Database, and finally triggers the Exporter.

5. Why these specific libraries?
  requests-Connects to the news website and downloads the page content.
  beautifulsoup4-Sifts through the HTML code to find headlines and links.
  pandas-Manages the data in a table format and handles the transfer to Excel.
  openpyxl-The "engine" that allows you to style cells and create clickable hyperlinks.


🚀 How to Run It
Configure: Set your target link in config.py.
Execute: Run python main.py in your terminal.
View: Open the generated .xlsx file to see your clickable news feed.
