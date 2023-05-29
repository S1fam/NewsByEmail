import requests
from send_email import send_email

topic = "tesla"
api_key = "YOUR API KEY"  # os.getenv("API_KEY") not working :C
language = "en"

url = f"https://newsapi.org/v2/everything?q={topic}" \
      f"&from=2023-04-28&sortBy=publishedAt&apiKey={api_key}&language={language}"
# parameters - main url, q=tesla, from=2023..., sortBy, apiKey, language

# make request
request = requests.get(url)

# get a dictionary with data
content = request.json()  # makes class dict, request.text would make string as type of content etc

# access the article titles and description

all_articles = ""

for article in content['articles'][0:20]:
    if (article['title'] and article['description']) is not None:
        all_articles = "Subject: Today's news" + "\n" \
                       + all_articles + article["title"] + "\n" \
                       + article["description"] + "\n" \
                       + article["url"] + 2*"\n"


all_articles = all_articles.encode("utf-8")  # encoding into a format, to fix error of:
# UnicodeEncodeError: 'ascii' codec can't encode character '\u2019' in position 209: ordinal not in range(128)

send_email(all_articles)
