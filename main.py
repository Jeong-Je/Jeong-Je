import feedparser, time

URL = "https://jeongje.vercel.app/feed.xml"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
# Jeong Je Son 🖐️

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=castolrz)](https://solved.ac/castolrz/)
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Jeong-Je&layout=compact&theme=ruvbox) <br />
[![Solved.ac프로필](http://mazassumnida.wtf/api/mini/generate_badge?boj=castolrz)](https://solved.ac/castolrz/)

## Skills
![TypeScript](https://img.shields.io/badge/typescript-3178C6.svg?&style=for-the-badge&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-F7DF1E.svg?&style=for-the-badge&logo=javascript&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C.svg?&style=for-the-badge&logo=cplusplus&logoColor=white)
<br />
![Express](https://img.shields.io/badge/Express-000000.svg?&style=for-the-badge&logo=Express&logoColor=white)
![nestjs](https://img.shields.io/badge/NestJS-E0234E.svg?&style=for-the-badge&logo=NestJS&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000.svg?&style=for-the-badge&logo=nextdotjs&logoColor=white)

## My Blog
<a href="https://jeongje.vercel.app/" target='_blank'><img src="https://img.shields.io/badge/myblog-000000?style=for-the-badge&logo=nextdotjs&logoColor=white"></a>
## 📒 Latest Blog Post

"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
