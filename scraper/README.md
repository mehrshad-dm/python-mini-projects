# Real Python Web Scraper

This is a simple Python web scraping script that:
1. Fetches the HTML content of [realpython.com](https://realpython.com/).
2. Extracts and prints the page title.
3. Extracts and prints text content of elements with the CSS class `.h2`.
4. Extracts and prints the `src` attribute of specific images using a copied CSS selector from the browser's Developer Tools.

---

## Features
- Uses `requests` to retrieve webpage content.
- Uses `BeautifulSoup` (`bs4`) to parse HTML.
- Demonstrates how to:
  - Select elements using `select_one()` and `select()`
  - Extract text content
  - Extract image URLs using a precise CSS selector from the browser.

---

## Installation

Before running the script, install the required dependencies:
```bash
pip install requests beautifulsoup4
```
## CSS Selector for Images

The image selector in the code:
picture = regular_data.select(
    ".h-100 > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > img:nth-child(1)"
)
was intentionally copied directly from Inspect → Copy → Copy Selector in the browser's Developer Tools.
This demonstrates how to locate specific elements on a webpage with precise CSS paths.
