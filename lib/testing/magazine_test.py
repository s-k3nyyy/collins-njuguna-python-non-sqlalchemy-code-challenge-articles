import pytest
from classes.many_to_many import Article, Author, Magazine

class TestMagazine:
    def test_category_type(self):
        """magazine category is of type str"""
        magazine_1 = Magazine("Vogue", "Fashion")
        assert isinstance(magazine_1.category, str)

        # comment out the next two lines if using Exceptions
        magazine_2 = Magazine("AD", "Architecture")
        magazine_2.category = 2
        assert magazine_2.category == "Architecture"

    def test_category_len(self):
        """magazine category has length greater than 0"""
        magazine_1 = Magazine("Vogue", "Fashion")
        assert magazine_1.category != ""

        # comment out the next three lines if using Exceptions
        magazine_1.category = ""
        assert magazine_1.category == "Fashion"

    def test_has_many_articles(self):
        """magazine has many articles"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author_1.add_article(magazine_1, "How to wear a tutu with style")
        author_1.add_article(magazine_1, "Dating life in NYC")
        author_1.add_article(magazine_2, "2023 Eccentric Design Trends")
        assert len(magazine_1.articles()) == 2

    def test_articles_of_type_articles(self):
        """magazine articles are of type Article"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author_1.add_article(magazine_1, "How to wear a tutu with style")
        author_1.add_article(magazine_1, "Dating life in NYC")
        author_1.add_article(magazine_2, "2023 Eccentric Design Trends")
        assert isinstance(magazine_1.articles()[0], Article)

    def test_has_many_contributors(self):
        """magazine has many contributors"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        author_1.add_article(magazine_1, "How to wear a tutu with style")
        author_2.add_article(magazine_1, "Dating life in NYC")
        assert len(magazine_1.contributors()) == 2

    def test_contributors_of_type_author(self):
        """magazine contributors are of type Author"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        author_1.add_article(magazine_1, "How to wear a tutu with style")
        author_2.add_article(magazine_1, "Dating life in NYC")
        assert isinstance(magazine_1.contributors()[0], Author)

    def test_contributors_are_unique(self):
        """magazine contributors are unique"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        author_1.add_article(magazine_1, "How to wear a tutu with style")
        author_1.add_article(magazine_1, "How to be single and happy")
        author_2.add_article(magazine_1, "Dating life in NYC")
        assert len(set(magazine_1.contributors())) == len(magazine_1.contributors())
        assert len(magazine_1.contributors()) == 2

    def test_article_titles(self):
        """returns list of titles strings of all articles written for that magazine"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        magazine_3 = Magazine("GQ", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")
        Article(author_1, magazine_2, "Carrara Marble is so 2020")
        assert magazine_1.article_titles() == ["How to wear a tutu with style"]

    def test_contributing_authors(self):
        """returns author list who have written more than 2 articles for the magazine"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "How to be single and happy")
        Article(author_1, magazine_1, "Dating life in NYC")
        Article(author_1, magazine_2, "Carrara Marble is so 2020")
        Article(author_2, magazine_2, "2023 Eccentric Design Trends")
        assert author_1 in magazine_1.contributing_authors()

    def test_top_publisher(self):
        """returns the magazine with the most articles"""
        Magazine.all = []
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        assert Magazine.top_publisher() is None

        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "Dating life in NYC")
        Article(author_1, magazine_1, "How to be single and happy")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")
        Article(author_1, magazine_2, "Carrara Marble is so 2020")

        assert Magazine.top_publisher() == magazine_1
        assert isinstance(Magazine.top_publisher(), Magazine)
