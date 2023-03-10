# Coding Allstars Trial Task

This is a trial task for Coding Allstars. Purpose of this task is to crawl [ClassCentral](https://www.classcentral.com)
website and translating English content to Hindi. Then, deploy the application to any web server.


##  Roadmap
In the demo video, HTTrack looked like an easy option for helping to crawl the website, and with more than 5 years of experience with HTTrack, I thought I can do that easily. But, when I started to use 
HTTrack, and it gives me error for every option, I realized that CLI crawl was almost impossible without using antibot tools
or similar libraries. At first, I tried cURL, requests library, and similar tools, but I couldn't get the content of the page.
Then, I listed my options for a better crawl option. There were many options, but I needed a tool which has amazing support and community.
For me, main options were Playwright and Selenium. Selenium is amazing tool but Playwright is powered by Microsoft and ease of use with great community provides many options. Also, it has Python and Node.js support which I use professionally. So, I decided to use Playwright.


## Crawling the Website
When I crawl the homepage and try it in my local server. I realized that they are using webpack and using JS as chunk files. These files are hard to detect in network, so it was another wall to hit in this road. Playwright is providing download option, but I couldn't handle in windowed mode.
So I tried to look alternatives to find all requests for assets. When I monitor the requests and response, only result was a third party tracker file.

Then I went deeper for network activity and I found Chromium project is providing browser tracing. When I log the trace, I found that Chromium is logging everything about rendering, network, and other activities like executions. So, I decided to use this trace to find all assets and download them.

```python
browser.start_tracing(page=page, path="chrome_traces/home.json", categories=["devtools.timeline"])
page.goto("https://www.classcentral.com")
page.wait_for_load_state("load", timeout=0)
browser.stop_tracing()
```
Playwright was providing browser tracing option, and it helped me a lot. To filter results and reduce the log file size, I used `devtools.timeline` keyword argument.


Trace file has many files to crawl, but I didn't need all of them. Because analytics file from Google and other tools were already downloaded from third party URLS. I needed internal files. 
Then I realized that there is a "renderBlocking" option for assets to decide priority. And almost all of them were internal links. So, I saved the trace log for each HTML file and crawled the file to find "renderBlocking" option. The object which has this option was also keeping the url for asset.
And I downloaded assets using this way.

With a simple command below, I found all internal url and wrote them to text file.
```python
link_list = [x.get_attribute("href") for x in page.locator("a").all()]
    with open("temp_data/links.txt", "w", encoding="utf-8") as f:
        for link in link_list:
            f.write(link + "\n")
        f.close()
````
By using list comprehension, I reduced the execution time of the script.

Then I crawled the text file and detected all internal urls starting with slash ("/") character. But some of them were already have the domain, so I decided to add domain to the urls beginning with slash character.

The other challenge was creating directory while protecting the structure for files. So, I decided to read subdirectory of url and create the directories using `os` library recursively.
After creating directory, I downloaded subpages and saved them to their respective folders as well as their trace logs to detect there is any other asset file used in pages.

## Downloading Assets

Downloading the assets was another challenge because Cloudflare was blocking me using CLI tools. When I look at the internet, I found that there were tools to work as proxy and help me to download files. By using ZenRows, I downloaded asset files using `requests` library in Python and also downloaded them to their respective directory.
Assets file was also has duplicate asset links so using `set` data structure helped me find unique links.


## Translating the Content

I tried many options from BeautifulSoup to Playwright, Google Translate CLI tool developed by 3rd party developers and many options. But there were always a problem because Google was blocking me because of the number of requests. Also replacing English text to Hindi would cause links to break. And I realized that I can use Node.js because Playwright is also supporting it and JavaScipt is amazing language for DOM.
So, steps were:

1. Read the HTML file
2. Find all text nodes
3. Translate the text of each node using Playwright
   1. Open Google Translate page
   2. Paste the text
   3. Wait for translation
   4. Get the translated text using copy button on the page
4. Replace the text of each node with translated text
5. Save the file
6. Repeat for all files

Instead of restaring Playwright instance for each text, I started instance in the beginning and just refreshed the page for each node. Also, I excluded elements like script, style, and other elements which doesn't have text (images, links, etc.)

## Deploying the Application

I connected my Netlify account to GitHub and deployed the application. I used Netlify because it is easy to use and has amazing support. Also, it is free for open source projects. Also, it can deploy automatically when I push commit to the repo. For now, it is working without any problem.

## Problems

1. Hindi text is missing for subpages because time was limited and translating each page was time consuming. So, I decided to translate only the home page.
2. Iframes inside subpages are not working because I didn't crawl the iframe urls located in the subpages to prevent deeper crawl.

## Used Libraries / Languages

1. Playwright
2. Python
3. JS
4. Node.js
5. Netlify
6. GitHub
7. requests library for Python
8. JSDOM
9. XMLSerializer

## Conclusion

I want to thank Coding Allstars for this amazing opportunity. I learned a lot from this task and I am sure that I can do better in the future. I am looking forward to hearing from you. Thank you.


Repo for JS operations is [here](https://github.com/furkantaskin/as_task_js)
