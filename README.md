If your RERA scraper uses packages like requests, beautifulsoup4, or pandas, create a file named requirements.txt in your project root:
requests
beautifulsoup4
pandas
openpyxl

# Odisha RERA Project Scraper 🏗️

This Python project scrapes the first 6 projects listed under "Projects Registered" on the Odisha RERA website. It extracts important details like:

- RERA Regd. No
- Project Name
- Promoter Name
- Promoter Address
- GST No

## 🔧 Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
