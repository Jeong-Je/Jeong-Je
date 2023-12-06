import feedparser, time

URL = "https://jeongje.vercel.app/feed.xml"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
![header](https://capsule-render.vercel.app/api?type=waving&color=808080&height=300&section=header&text=Jeong%20Je&fontSize=90&fontColor=ffffff&animation=fadeIn&fontAlignY=38&descAlignY=51&descAlign=62)

## 📝 My Blog
<a href="https://jeongje.vercel.app/" target='_blank'><img src="https://img.shields.io/badge/MyBlog-000000?style=flat-square&logo=nextdotjs&logoColor=white"></a>

### 📒 Latest Blog Post
"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"<a href={feed['link']} target='_blank'>{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}</a><br/>\n"

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
