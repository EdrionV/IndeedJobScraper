
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Define headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

# Base URL for job search
base_url = "https://www.indeed.com/jobs"
query_params = {
    'q': 'Cyber Security Analyst',
    'l': '',
    'sort': 'date'
}

# Categories for grouping based on post age
def categorize_posting(date_str):
    date_str = date_str.lower()
    if 'just posted' in date_str or 'today' in date_str or '1 day ago' in date_str or '24 hours ago' in date_str:
        return 'Posted Today'
    elif '2 days ago' in date_str:
        return '1–2 Days Ago'
    elif any(day in date_str for day in ['3 days', '4 days', '5 days', '6 days', '7 days']):
        return '3–7 Days Ago'
    elif any(day in date_str for day in ['8 days', '9 days', '10 days', '11 days']):
        return '1–2 Weeks Ago'
    else:
        return 'Older than 2 Weeks'

# Storage
job_data = []

# Scrape first 3 pages (adjust range for more)
for page in range(0, 30, 10):
    print(f"Scraping page {page // 10 + 1}...")
    query_params['start'] = page
    response = requests.get(base_url, headers=headers, params=query_params)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_cards = soup.find_all('div', class_='job_seen_beacon')
    
    for card in job_cards:
        title_tag = card.find('h2', class_='jobTitle')
        company_tag = card.find('span', class_='companyName')
        location_tag = card.find('div', class_='companyLocation')
        date_tag = card.find('span', class_='date')
        link_tag = card.find('a', href=True)

        job_data.append({
            'Job Title': title_tag.text.strip() if title_tag else None,
            'Company': company_tag.text.strip() if company_tag else None,
            'Location': location_tag.text.strip() if location_tag else None,
            'Posted': date_tag.text.strip() if date_tag else None,
            'Category': categorize_posting(date_tag.text.strip()) if date_tag else 'Unknown',
            'Link': "https://indeed.com" + link_tag['href'] if link_tag else None
        })

    time.sleep(1)  # polite delay

# Convert to DataFrame and save
df = pd.DataFrame(job_data)
df.to_excel("Cyber_Security_Analyst_Jobs_Indeed.xlsx", index=False)
print("✅ Scraping complete. Data saved to Cyber_Security_Analyst_Jobs_Indeed.xlsx")
