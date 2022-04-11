# Web Scraping, Web harvesting or web data extraction

## Wht is web scraping?
  - Web scraping is a technique to automatically access and extract large amounts of information from a website.


## How to use Web scraping?
  1. Fiest, we need to import some libraries.
```
    import requests
    import urllib.request
    import time
    from bs4 import BeautifulSoup
```
  2. Assign the url of the page to a variable, and using **request** library, request the data from the website.(Here I'll use New York MTA websites)
```
    url = url = 'http://web.mta.info/developers/turnstile.html'
    response = requests.get(url)
```
  3. Using the _BeautifulSoup_ library parse the html, that allow us to use the page tags.
```
    soup = BeautifulSoup(response.text, 'html.parser')
```
  4. Now, we need to find all the anchor tags `<a>`, using the soup method we can select all the anchor tags `soup.find_all('a')`
  5. Now we need to extract the actual link, here all the files start at index 38.

```
    one_a_tag = soup.findAll('a')[36]
    link = one_a_tag['href']
```

  6. Now, to download all the files we can loop through all tags

```
line_count = 1
for one_a_tag in soup.findAll('a'): #'a' tags are for links
    if line_count >= 36: #code for text files starts at line 36
        link = one_a_tag['href']
        download_url = 'http://web.mta.info/developers/'+ link
        urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
        time.sleep(1)
    line_count +=1
```

  7. If you notice above we add some latency `time.sleep(1)` to  pause our code for a second, so that we are not spamming the website with requests. This helps us avoid getting flagged as a spammer.

## How to scrap websites without getting blocked?
  1. Respect Robots.txt
     * Robots.text shows rules for scraping such as:
       * frequently you can scrape
       * which pages allow scraping and and which ones you can’t. 
  2. Make the crawling slower, do not slam the server, treat websites nicely
     * Web scraping fetch data very fast, so the make the site easy to detect scrapers.
     * You should add some delay between each request to avoid blocking.
     * Too many requests wll make the website unresponsive.
  3. Do not follow the same crawling pattern
     * Humans generally will not perform repetitive tasks as they browse through a site with random actions.
     * Web scraping bots have the same crawling pattern, because they are programmed that way.
     * if the site have intelligent anti-crawling mechanisms, it is easy to detect spiders and block them.
  4. Make requests through Proxies and rotate them as needed
     * When we scraping the IP address can be seen, and the site can what we are doing.
     * Multiple requests come from the same IP wll led you to get block.
     * Creating a pool of IPs using some tools can help us to not be detected and do multiple requests to the same site.
     * We can use one of these tools to change the IP address:
       * TOR Browser
       * VPNs
       * Free Proxies
       * Shared Proxies
       * Private Proxies
  5. Rotate User Agents and corresponding HTTP Request Headers between requests
     * User-agent is a tool that tell the server which web browser is being used. 
     * Every request made from a web browser contains a user-agent header and using the same user-agent consistently leads to the detection of a bot.
  6. Use a headless browser like Puppeteer, Selenium or Playwright
     * When we scraping we are not using a web browser for visiting the website, we are using libraries.
     * These libraries can not run JavaScript codes, so the website check if the client (web browser) can run a block of JavaScript code or not, if it can't run it, it detect that we are scraping. 

## What sre web scraping techniques?
  1. Human copy-and-paste
  2. Text pattern matching
  3. HTTP programming
  4. HTML parsing
  5. DOM parsing
  6. Vertical aggregation
  7. Semantic annotation recognizing
  8. Computer vision web-page analysis



---
### Resource
  - [wikipedia](https://en.wikipedia.org/wiki/Web_scraping)
  - [medium](https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460)
  - [scrape hero](https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/)