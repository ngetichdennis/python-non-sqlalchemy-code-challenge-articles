class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Author name must be a string")
        if len(name) == 0:
            raise ValueError("Author name cannot be empty")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set([article.magazine for article in self._articles]))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters")

        article = Article(self, magazine, title)
        self._articles.append(article)
        return article
    def topic_areas(self):
        if not self._articles:
            return None
        return list(set([article.magazine.category for article in self._articles]))

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        self._contributors = set()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Magazine name must be a string")
        if not 2 <= len(value) <= 16:
            raise ValueError("Magazine name must be between 2 and 16 characters, inclusive")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Magazine category must be a string")
        if len(value) == 0:
            raise ValueError("Magazine category cannot be empty")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(self._contributors)

    def add_article(self, article):
        if not isinstance(article, Article):
            raise TypeError("Article must be an instance of Article class")
        self._articles.append(article)
        self._contributors.add(article.author)

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        authors = {}
        for article in self._articles:
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        return [author for author, count in authors.items() if count > 2]



class Article:
    all= []
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        author.articles().append(self)
        magazine.add_article(self)
        

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author.articles().remove(self)
            self._author = new_author
            new_author.articles().append(self)
        else:
            raise ValueError("Author must be an instance of Author class")

    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine.articles().remove(self)
            self._magazine = new_magazine
            new_magazine.articles().append(self)
        else:
            raise ValueError("Magazine must be an instance of Magazine class")




