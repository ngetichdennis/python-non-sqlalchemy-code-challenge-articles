class Author:
    def __init__(self, name):
        # checking if the name is a string
        if not isinstance(name, str):
            raise TypeError("Author name must be a string")
        # checking if the name is not empty
        if len(name) == 0:
            raise ValueError("Author name cannot be empty")
         # Initialize the name and articles attributes
        self._name = name
        self._articles = []

    @property
     # Getter method for the author's name
    def name(self):
        return self._name

    def articles(self):
        # Method to get the list of articles written by the author
        return self._articles

    def magazines(self):
          # Method to get the list of magazines the author has written for
        return list(set([article.magazine for article in self._articles]))

    def add_article(self, magazine, title):
        # Method to add a new article written by the author
        # Check if the magazine is an instance of Magazine class
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
          # Check if the title is a string and its length is within the specified range
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        # Create a new Article instance and append it to the author's articles list
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article
    def topic_areas(self):
        # Method to get the list of topic areas the author has written about
        if not self._articles:
            return None
        return list(set([article.magazine.category for article in self._articles]))

class Magazine:
    def __init__(self, name, category):
        #initiazlizing magazine objects
        self._name = name
        self._category = category
        self._articles = []
        self._contributors = set()

    @property
    def name(self):
        #getter method for magazine name
        return self._name

    @name.setter
    #setter method for the magazine name
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Magazine name must be a string")
        if not 2 <= len(value) <= 16:
            raise ValueError("Magazine name must be between 2 and 16 characters, inclusive")
        #updating the magazine's name
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
        # Method to add an article to the magazine
        # Check if the article is an instance of Article class
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
        # Count the number of articles written by each author
        authors = {}
        for article in self._articles:
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
                 # Return the authors who have contributed more than 2 articles
        return [author for author, count in authors.items() if count > 2]



class Article:
    all= []
    def __init__(self, author, magazine, title):
        #initiazlizing article objects
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
          # Setter method for the article's author
        # Check if the new_author is an instance of Author class
        if isinstance(new_author, Author):
            self._author.articles().remove(self)
            self._author = new_author
            new_author.articles().append(self)
        else:
            raise ValueError("Author must be an instance of Author class")

    @property
    def magazine(self):
        #getter method for article's magazine
        return self._magazine
    @magazine.setter
    def magazine(self, new_magazine):
         # Setter method for the article's magazine
        # Check if the new_magazine is an instance of Magazine class
        if isinstance(new_magazine, Magazine):
            # Remove the article from the current magazine's articles list
            self._magazine.articles().remove(self)
             # Update the article's magazine
            self._magazine = new_magazine
            # Add the article to the new magazine's articles list
            new_magazine.articles().append(self)
        else:
            raise ValueError("Magazine must be an instance of Magazine class")




