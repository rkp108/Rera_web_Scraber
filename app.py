rom selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up headless browser
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# Project and promoter URLs
project_urls = [
    "----------------------",
    "----------------------"
]

promoter_urls = [
    "----------------------",
    "----------------------"
]

# Helper function
def get_text(label):
    try:
        return driver.find_element(By.XPATH, f"//label[contains(text(), '{label}')]/following-sibling::strong").text.strip()
    except:
        return "N/A"

def switch_to_promoter():
    try:
        driver.find_element(By.XPATH, "//a[contains(text(),'Promoter Details')]").click()
        time.sleep(1)
    except:
        pass

# Scraping and combining data
projects = []
for i in range(6):
    driver.get(project_urls[i])
    time.sleep(1.5)
    pname = get_text("Project Name")
    rera = get_text("RERA Regd. No.")

    driver.get(promoter_urls[i])
    time.sleep(1.5)
    switch_to_promoter()
    prom_name = get_text("Company Name")
    prom_addr = get_text("Registered Office Address")
    gst = get_text("GST No.")

    projects.append({
        "Project Name": pname,
        "RERA No.": rera,
        "Promoter Name": prom_name,
        "Office Address": prom_addr,
        "GST No.": gst
    })

driver.quit()

# Generate HTML Table
html = """
<html>
<head><title>Projects Registered</title></head>
<body>
<h2>Projects Registered </h2>
<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th style="border: 1px solid black; padding: 8px;">S.No</th>
      <th style="border: 1px solid black; padding: 8px;">Project Name</th>
      <th style="border: 1px solid black; padding: 8px;">RERA No.</th>
      <th style="border: 1px solid black; padding: 8px;">Promoter Name</th>
      <th style="border: 1px solid black; padding: 8px;">Office Address</th>
      <th style="border: 1px solid black; padding: 8px;">GST No.</th>
    </tr>
  </thead>
  <tbody>
"""

for idx, p in enumerate(projects, start=1):
    html += f"""
    <tr>
      <td style="border: 1px solid black; padding: 8px;">{idx}</td>
      <td style="border: 1px solid black; padding: 8px;">{p['Project Name']}</td>
      <td style="border: 1px solid black; padding: 8px;">{p['RERA No.']}</td>
      <td style="border: 1px solid black; padding: 8px;">{p['Promoter Name']}</td>
      <td style="border: 1px solid black; padding: 8px;">{p['Office Address']}</td>
      <td style="border: 1px solid black; padding: 8px;">{p['GST No.']}</td>
    </tr>
    """

html += """
  </tbody>
</table>
</body>
</html>
"""

# Save to HTML file
with open("Projects Registered.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ HTML file 'Projects Registered.html' has been created successfully.")
