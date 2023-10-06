import feedparser, time

URL = "https://jeongje.vercel.app/feed.xml"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
![header](https://capsule-render.vercel.app/api?type=waving&color=808080&height=300&section=header&text=Jeong%20Je&fontSize=90&fontColor=ffffff&animation=fadeIn&fontAlignY=38&descAlignY=51&descAlign=62)
## 📚 Tech Stack 

  ![C++](https://img.shields.io/badge/C++-00599C.svg?&style=flat-square&logo=cplusplus&logoColor=white)
  ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6.svg?&style=flat-square&logo=typescript&logoColor=white)
  ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E.svg?&style=flat-square&logo=javascript&logoColor=white)
   <br />
  ![nodedotjs](https://img.shields.io/badge/Node.js-339933.svg?&style=flat-square&logo=nodedotjs&logoColor=white)
  ![Express](https://img.shields.io/badge/Express-000000.svg?&style=flat-square&logo=Express&logoColor=white)
  ![nestjs](https://img.shields.io/badge/NestJS-E0234E.svg?&style=flat-square&logo=NestJS&logoColor=white)
  ![Next.js](https://img.shields.io/badge/Next.js-000000.svg?&style=flat-square&logo=nextdotjs&logoColor=white)
  ![React](https://img.shields.io/badge/React-61DAFB.svg?&style=flat-square&logo=react&logoColor=white)
  <br />
  ![postgresql](https://img.shields.io/badge/PostgreSQL-4169E1.svg?&style=flat-square&logo=postgresql&logoColor=white)
  ![mysql](https://img.shields.io/badge/MySQL-4479A1.svg?&style=flat-square&logo=mysql&logoColor=white)
  ![mongodb](https://img.shields.io/badge/MongoDB-47A248.svg?&style=flat-square&logo=mongodb&logoColor=white)


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
