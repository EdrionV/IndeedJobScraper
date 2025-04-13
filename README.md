
# Indeed Cyber Security Job Scraper

This Python project automates the process of scraping **Cyber Security Analyst** job listings from [Indeed.com](https://indeed.com), extracting relevant data, categorizing it by posting age, and saving it into a structured Excel file for further analysis or tracking.

---

## What It Does

- Searches Indeed.com for "Cyber Security Analyst" roles
- Extracts:
  - Job Title
  - Company Name
  - Location
  - Posting Date (e.g., "1 day ago", "3 days ago")
  - Job Link
- Categorizes jobs into:
  - **Posted Today**
  - **1–2 Days Ago**
  - **3–7 Days Ago**
  - **1–2 Weeks Ago**
  - **Older than 2 Weeks**
- Outputs all structured data into an Excel spreadsheet

---

## Technologies Used

- `requests` – to fetch web pages
- `BeautifulSoup` – to parse HTML content
- `pandas` – for data manipulation and export
- `openpyxl` – Excel export engine

---

## How It Automates the Process

1. **Search Query Automation**  
   Sends search requests with parameters like job title, location, and sorting preference.

2. **Page Navigation Loop**  
   Iterates through multiple pages (pagination) of job listings automatically.

3. **HTML Parsing & Data Extraction**  
   Uses `BeautifulSoup` to pull job cards and extract job title, company, and post date.

4. **Categorization Logic**  
   Automatically groups jobs based on the age of the posting using keyword detection.

5. **Excel Export**  
   Converts all results into an Excel file in one click using `pandas`.

---

## Output

Saved file: `Cyber_Security_Analyst_Jobs_Indeed.xlsx`

Each row in the spreadsheet contains:
- Job Title
- Company
- Location
- Posted (raw date)
- Category (e.g., "1–2 Days Ago")
- Direct link to the job post

---

## How to Run

```bash
pip install requests beautifulsoup4 pandas openpyxl
python scrape_indeed_cyber_jobs.py
```

---

## Use Case

This tool is great for:
- Job seekers tracking fresh job posts
- Analysts performing market trend research
- Automating the manual effort of job board searching

---

## Author

**Edrion Ashirvadam** – Cybersecurity Analyst | Threat Researcher
