# LinkedIn Job Analyser

A Chrome extension that analyses LinkedIn job search results and tells you what skills, tools, frameworks, and qualifications are most in demand for any role automatically.

Search for a role on LinkedIn, and the extension scrapes the top 50 job postings, analyses them, and downloads a ranked CSV report to your computer.

---

## What It Does

When you search for a role on LinkedIn Jobs, the extension:

1. Reads the search keyword from the URL
2. Sends it to a local Flask backend
3. The backend scrapes 50 job postings using LinkedIn's guest API
4. Analyses each posting against a keyword dictionary
5. Consolidates and ranks skills across all 50 jobs
6. Downloads a CSV file with ranked skills by category and company breakdown

---

## Output

The downloaded CSV contains:

- **Technical Skills** — programming languages, methodologies, concepts
- **Tools and Technologies** — cloud platforms, DevOps tools, software
- **Frameworks and Libraries** — React, Django, TensorFlow, etc.
- **Education** — degree requirements
- **Certifications** — required certifications
- **Experience** — role types and levels
- **Companies** — which companies appeared in the 50 results and how many times

Each skill shows how many of the 50 job postings mentioned it, giving you a clear picture of what the market actually wants.

---

## Tech Stack

- **Chrome Extension** — Manifest V3, JavaScript
- **Backend** — Python, Flask, Flask-CORS
- **Scraping** — Requests, BeautifulSoup4
- **Analysis** — Python regex, custom keyword dictionary
- **Export** — Python CSV module

---

## Project Structure

```
linkedin-analyser/
│
├── chrome extension/
│   ├── manifest.json        # Extension configuration
│   ├── contentScript.js     # Reads keyword from LinkedIn URL, triggers download
│   └── background.js        # Handles file download via Chrome Downloads API
│
├── analyzer.py              # Keyword matching and categorisation logic
├── scraper.py               # LinkedIn guest API scraping functions
├── app.py                   # Flask server and consolidation logic
└── keywords.py              # Skill dictionary organised by category
```

---

## Setup

### Prerequisites

- Python 3.x
- Google Chrome
- Anaconda or pip

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/linkedin-analyser.git
cd linkedin-analyser
```

### 2. Install Python dependencies

```bash
pip install flask flask-cors requests beautifulsoup4
```

### 3. Run the Flask backend

```bash
python app.py
```

You should see:
```
Running on http://127.0.0.1:5000
```

### 4. Load the Chrome extension

1. Open Chrome and go to `chrome://extensions`
2. Enable **Developer Mode** in the top right
3. Click **Load unpacked**
4. Select the `chrome extension` folder from this project

### 5. Use it

1. Make sure Flask is running
2. Go to [linkedin.com/jobs](https://linkedin.com/jobs)
3. Search for any role — for example "Software Engineer" or "Data Analyst"
4. Wait approximately 60 seconds while the extension scrapes and analyses 50 jobs
5. A CSV file named `export.csv` will automatically download to your Downloads folder
6. Open it in Excel to see the ranked skill list

---

## Important Notes

**Flask must be running on your machine while using the extension.** This is a local tool — the backend runs on your computer, not on a remote server. Your friends cannot use this without setting up the backend themselves.

**LinkedIn's guest API is used for scraping.** This operates in a grey area of LinkedIn's Terms of Service. Use responsibly and do not make excessive requests.

**Results vary by search.** LinkedIn returns different job postings each time based on your location, filters, and LinkedIn's algorithm. The keyword used in search and your location settings affect which 50 jobs are analysed.

---

## Customising the Keyword Dictionary

Open `keywords.py` to add or modify keywords. The dictionary is organised by category. All keywords must be lowercase. Multi-word keywords like `"machine learning"` are supported.

```python
keywords_list = {
    "Technical Skills": ["python", "java", "machine learning", ...],
    "Tools and Technologies": ["aws", "docker", "kubernetes", ...],
    ...
}
```

---

## Known Limitations

- Short keywords like `"c"` and `"go"` may produce false matches in some job descriptions
- The extension only runs on LinkedIn job search result pages
- Requires Flask to be running locally — not plug and play for end users
- LinkedIn may occasionally block requests if too many are made in quick succession

---

## Built With

This project was built entirely from scratch as a learning exercise — from zero to a working Chrome extension with a Python backend, web scraping, text analysis, and file export.

---

## License

MIT
