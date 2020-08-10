# Web Scraping with Python

## What's Web Scraping?

It's name given to the process of collecting information from web pages, *a.k.a* data mining, or simply the automated web data collecting pipeline.

## Crawler:

Crawler goes from one page to another. It's bigger than a Spyder. 

For example: Google's search engine. The things that you write in the search box, Google will seek it simultaneously in many web pages.

Therefore, it's web navigate looking for relevant information based on specific constraints.

## Spyder:

Spyders follow rules and they're inside the Crawlers. Basically the Crawler will make the search in many web pages whether the Spyder will collect only the information needed.

Then the Crawler is the boss (the one that give the orders) and the Spyder is the employee (the one that obeys).

## Selectors:

Are features that tell the Crawler or Spyder which are the sites so that it can be selected specific parts of the HTML code.

**Most Common:** CSS and XPath

1. CSS: ara patterns to select stylized elements
1. XPath: is a query language for selecting nodes from an XML document

# Scraper

1. creates the Crawler,
1. where you creates at least one Spyder with defined constraints,
1. which will connect to an url or a server,
1. will ask for a request,
1. and the url or server will give you a response with ,the information that you're looking for.