from newspaper import Article 

#News article from the star
url = 'https://www.thestar.com.my/news/nation/2019/06/18/17-students-arrested-in-private-party-op-at-posh-condo-in-kl/'
article = Article(url)
article.download()

#To parse the article 
article.parse() 

#To extract title 
print("Article's Title:")
print(article.title)
print("\n")

#To extract text
print("Article's Text:")
print(article.text)
print("\n")

article.nlp()

#To extract summary 
print("Article's Summary:") 
print(article.summary) 
print("\n")

#To extract keywords
print("Article's Keywords:") 
print(article.keywords)

#Chinese newspaper
from newspaper import Article 

#News article from the sinchew (Chinese Newspaper)
url = 'https://www.sinchew.com.my/content/content_2058387.html'
chinese_article = Article(url, language='zh')
chinese_article.download()

#To parse the article 
chinese_article.parse() 

#To extract title 
print("Article's Title:")
print(chinese_article.title)
print("\n")

#To extract text
print("Article's Text:")
print(chinese_article.text) 


chinese_article.nlp()

#To extract summary 
print("Article's Summary:") 
print(chinese_article.summary) 
print("\n")

#To extract keywords
print("Article's Keywords:") 
print(chinese_article.keywords)
