import datetime

# STEP 1: Add your article URLs here (you can expand this list programmatically later)
urls = [
    "https://khwopajournals.com/index.php/jsce/article/view/4",
    "https://khwopajournals.com/index.php/jsce/article/view/6",
    "https://khwopajournals.com/index.php/jsce/article/view/8",
    "https://khwopajournals.com/index.php/jsce/article/view/10",
    "https://khwopajournals.com/index.php/jsce/article/view/11",
    "https://khwopajournals.com/index.php/jsce/article/view/12",
    "https://khwopajournals.com/index.php/jsce/article/view/13",
    # keep adding article links...
]

# STEP 2: Get today’s date for <lastmod>
today = datetime.date.today().isoformat()

# STEP 3: Build sitemap XML structure
sitemap = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

for url in urls:
    sitemap += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
"""

sitemap += "</urlset>"

# STEP 4: Save to file
with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)

print("✅ sitemap.xml generated successfully!")
