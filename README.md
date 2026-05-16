# LinkedIn Job Market Analyzer

A Chrome extension + Python backend application that analyzes LinkedIn job postings to identify the most in-demand skills, tools, certifications, and education requirements for a chosen role.

## Overview

Job seekers often know **what field they want to enter**, but struggle to answer an important question:

**“What skills do employers actually expect for this role?”**

Manually reading dozens of job postings is repetitive, time-consuming, and inefficient.

**LinkedIn Job Market Analyzer** automates this process by extracting job description data from LinkedIn job listings, analyzing the text for relevant requirements, and generating a structured report for the user.

This helps students, career switchers, and professionals understand the market demand for a given role.

## Problem Statement

Suppose someone wants to become:

- Software Engineer
- Data Analyst
- Product Manager
- Machine Learning Engineer

They may not know:

- which programming languages are most requested
- which tools and technologies are commonly required
- whether certifications matter
- expected education qualifications
- role seniority expectations

This project solves that by automatically collecting and analyzing job posting data.

## Solution Architecture

This application uses a **client-server architecture**.

### Frontend (Chrome Extension)

The Chrome extension:

- runs on LinkedIn job pages
- extracts job description text
- waits for dynamic LinkedIn content to load
- sends extracted data to the backend for analysis

### Backend (Python + Flask)

The backend:

- receives scraped job posting text
- analyzes content using keyword-based categorization
- identifies relevant skills and qualifications
- returns structured results
- can generate downloadable Excel reports

## Architecture Flow

```text
User opens LinkedIn Jobs
        ↓
Chrome Extension injects content script
        ↓
Job description text is scraped
        ↓
Data sent to Flask backend via API
        ↓
Python analyzer processes text
        ↓
Skills + requirements categorized
        ↓
Excel report generated
        ↓
User downloads analysis
```

## Features

- LinkedIn job posting scraping
- Automated skill extraction
- Technical skills detection
- Tools and software identification
- Framework/library detection
- Certification extraction
- Education requirement detection
- Role type classification
- Excel report generation
- Chrome extension integration
- Client-server architecture implementation

## Tech Stack

### Frontend

- JavaScript
- Chrome Extensions API
- HTML
- Manifest V3

### Backend

- Python
- Flask
- Flask-CORS
- Regular Expressions
- Excel export utilities

## Project Structure

```text
linkedin-analyser/
│
├── chrome-extension/
│   ├── manifest.json
│   ├── contentScript.js
│   ├── popup.html
│   └── popup.js
│
├── backend/
│   ├── app.py
│   ├── analyzer.py
│   ├── keywords.py
│   ├── exporter.py
│   └── scraper.py
│
└── README.md
```

## Core Components

### `manifest.json`

Configures the Chrome extension:

- LinkedIn page access
- script injection permissions
- backend API communication permissions

### `contentScript.js`

Responsible for:

- detecting when LinkedIn job content loads
- extracting job description text
- sending data to Flask backend

### `app.py`

Flask API server that:

- receives scraped content
- exposes analysis endpoints
- coordinates backend processing

### `analyzer.py`

Processes job descriptions and categorizes keywords into:

- Technical Skills
- Tools & Technologies
- Frameworks & Libraries
- Education
- Certifications
- Role Types

### `keywords.py`

Contains the curated keyword dictionary used for classification.

### `exporter.py`

Generates downloadable Excel reports.

### `scraper.py`

Contains LinkedIn scraping logic for job listings.

## Installation

## 1. Clone the Repository

```bash
git clone https://github.com/ishika-sancheti/linkedin-analyser.git
```

## 2. Backend Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install flask flask-cors requests beautifulsoup4 openpyxl
```

Run the backend:

```bash
python app.py
```

Backend runs at:

```text
http://127.0.0.1:5000
```

## 3. Chrome Extension Setup

Open Chrome:

```text
chrome://extensions/
```

Then:

1. Enable **Developer Mode**
2. Click **Load unpacked**
3. Select the Chrome extension folder

## Usage

1. Start the Flask backend
2. Open LinkedIn Jobs
3. Search for a role (example: Software Engineer)
4. Open job postings
5. Extension extracts job description data
6. Backend analyzes requirements
7. Download Excel report

## Example Insights Generated

The analyzer can identify:

### Technical Skills

- Python
- Java
- SQL
- JavaScript
- Machine Learning

### Tools

- AWS
- Docker
- Kubernetes
- Git
- Jenkins

### Frameworks

- React
- Flask
- Django
- TensorFlow

### Education

- Bachelor's Degree
- Master's Degree
- B.Tech

### Certifications

- AWS Certified Solutions Architect
- PMP
- CISSP

## Challenges Solved

This project addresses practical engineering constraints:

### LinkedIn Anti-Scraping Restrictions

Traditional scraping applications can be blocked.

Solution:

- browser-side extraction via Chrome extension
- backend processing for heavy analysis

### Browser Extension Limitations

Chrome extensions are not ideal for generating complex downloadable files.

Solution:

- delegate processing/export to Python backend

## Learning Outcomes

This project demonstrates:

- browser extension development
- DOM scraping
- asynchronous JavaScript
- Flask API development
- client-server communication
- regex-based NLP
- data processing
- report generation
- software architecture design


## License

MIT License

## Author

**Ishika Sancheti**

GitHub: https://github.com/ishika-sancheti
