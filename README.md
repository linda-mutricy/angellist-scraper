# Angellist Scraper

This program scrapes [the Angellist Job Collections directories](https://angel.co/job-collections/), making it easier to find names and paste them into a spreadsheet without endlessly scrolling.

### Prerequisites:
```
requests
BeautifulSoup
```

### Running the program:
Download the folder and type the below into your terminal:

```
python3 summarize_lists.py
```

The prompt will ask for a webpage to be scraped:

```
Enter requested URL for scrape:
```

Any link from the [Job Collections landing page](https://angel.co/job-collections/) will work.

After the program runs, navigate to the folder in which `summarize_lists.py` resides. You will see a new file named `[portion of the URL after the last backslash].CSV`, containing the list data in text form.

![Demo](/Demo.png)

### Possible Modifications and Extensions
This webscraper could be adapted to any website where the article is a long-form list with links. Modify line 43 of `summarize_lists.py` to correspond with whichever CSS class name you are interested in.

```
companies = [[h3.find("a").contents[0]] for h3 in html.select("h3[class*='s-h3']")]
```
