rom selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up headless browser
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# Project and promoter URLs
project_urls = [
    "https://rera.odisha.gov.in/projects/project-details/VTJGc2RHVmtYMSs1MzhtY0xoLzhqRDk3MmpFVXBsVGczSzJFcXhMazRZdzNRREdQc3grcmpRMDd3R2EzZXo2U0lia1hUYmlwQTJyVTFZcTIyb3RQYXFqNytHblBZTzlZRklNclpNenJMWGM9",
    "https://rera.odisha.gov.in/projects/project-details/VTJGc2RHVmtYMSs1eVdsUFZiT0VoN0hyQXZkZFpPdG53VkxGMjRkZEFUd085bTNkMmZXN0J4d3NlTERDT01qRjlSbFRNSjVvZVI4NGdKb2NIZWduN3ZwcmQ5aUtua09sQXB3eG9COUM5bGM9",
    "https://rera.odisha.gov.in/projects/project-details/VTJGc2RHVmtYMTgyei9GWE14WGV6blhlVDhGQWJVckNlbjZFTkllNHJ5VmhNY2tIbDNhdHozTjRET1NidXlNWmJOZVQrbnhKOU1mSSs5WE5rQ3JXc0kvOEgxYVlMNjdEbDBUYkpuREV6T1E9",
    "https://rera.odisha.gov.in/projects/project-details/VTJGc2RHVmtYMS9CMmwxVlVNZFZtRWwyNXpMeXBrZjhOQ1F6dTI2d0RsTGxjdGR3Uzl4U0hXczIxckV6eGExazhRLytTZC9hb0VpbXRhMDZwZkdld3hZNVdqVFhzQmpxNnVpL1hGK25PT0E9",
    "https://rera.odisha.gov.in/projects/project-details/VTJGc2RHVmtYMTgyZjFHUmxjcndZN29ZM1dmbUhyQVZHSE5iVkViU1RoaGorQzY5OHh1OGNxVkFWUkxyaVB1VXJOYjdLOGU0RFIzdnNOMVVVT21KSjJ6Mlh3UHZBU3o2YzloczN3dDFBNDA9",
    "https://rera.odisha.gov.in/projects/project-details/VTJGc2RHVmtYMSs4VVJaaFRWRmZ0OVNQQ2xmM0R1Zk14K1JNdnRqYUxLLzNRekxUN1pwU1UzTjFrS00yUUpLdkV5UjBna0I1dG8wWHluVFVLWjNLSGxlNFFBbTdlWmxhbHJYYldURmZWdjg9"
]

promoter_urls = [
    "https://rera.odisha.gov.in/projects/project-details/VTJGc2RHVmtYMTg2enlxdnFtVW1KREFMcU95Y3lFVm5ta09jWlNtdytDVndWTWVaWUNTVnlmbmd1M2FiUjQyK3JvNHlUSGVZaFlEbzU3WkN5WjVDS0VMYnVRdjgvTHlJMFFjcWN5RklIR1k9",
    "https://rera.odisha.gov.in/projects/project-details/VTJGc2RHVmtYMStaek42d1FVYkNxNW52MWk2MWIreGZqK3dDUXNrZDRnVDU4M1pjbVJCOGI2ZWtnNEhxc2U4Z3ovS1l4RnYycGJndmdwRUlUOGRYNk85aDNSeVlPV2g1QWk2cjFNL2x5Wjg9",
    "https://rera.odisha.gov.in/projects/project-details/VTJGc2RHVmtYMTlWRnJiNm5TMkNDMUFOY1VUM01YWnpjZE9DZmpaQ2RRVUFUSnBFa0NCVHBvdkIvOEZsUkEvRUkveiswS3dBd2N5bk5qNDMyYkZMdUw4KzNndWxuNENjUVdWTjNIZjNjdjA9",
    "https://rera.odisha.gov.in/projects/project-details/VTJGc2RHVmtYMTlJZFZ2VndQdDVlT083TTJiZlRZdnYzK1FlVXV0KzQyMWRQRWpKTXNta00wSzRuV2JxdHhZNG1PN3JhWUFMcjZ5cmUzOWU0R25LdjNmR3VMOFBaZHg1M0NsWmcxbUNZTVk9",
    "https://rera.odisha.gov.in/projects/project-details/VTJGc2RHVmtYMSsvRjlONk91cVRiTnVlRG5DODVhSjlaeTd4LzQ4OVJmU0piYWFRMldyRkxIQU14clZQdkp1bjV5dGw0bHFQb1JCUjZwbEpOMnJhTExpYTBVeEYrdVh0ai8yN1VVOG9kWmc9",
    "https://rera.odisha.gov.in/projects/project-details/VTJGc2RHVmtYMTlDTm82M1NTWEVTSU5Kc1RvQXNEdUZVOG5laEV4SG5raUlPTGp2anRNYUJBUXBrall2bDRuM00wcnFGZ0t1blhJSjlSam1RZWJtRVFiNU8rQm5qMjJIQWxzZk02OWJDaTQ9"
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
