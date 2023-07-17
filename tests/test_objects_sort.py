import pytest
from objectSort.objectSort import Movies


def test_by_years(movies_set):
    my_sort = Movies()

    expected = [{'title': 'The Avengers', 'year': 2012, 'genres': ['Action', 'Adventure', 'Sci-Fi']},
                {'title': 'Avatar', 'year': 2009, 'genres': [
                    'Action', 'Adventure', 'Fantasy', 'Sci-Fi']},
                {'title': 'Iron Man', 'year': 2008, 'genres': [
                    'Action', 'Adventure', 'Sci-Fi']},
                {'title': 'Anchorman: The Legend of Ron Burgundy',
                    'year': 2004, 'genres': ['Comedy']},
                {'title': 'A Clockwork Orange', 'year': 1971, 'genres': ['Crime', 'Drama', 'Sci-Fi']}]
    actual = my_sort.movies_sorted_by_year(movies_set)
    assert actual == expected


def test_by_titles(movies_set):
    my_sort = Movies()

    expected = [{'title': 'Anchorman: The Legend of Ron Burgundy', 'year': 2004, 'genres': ['Comedy']},
                {'title': 'Avatar', 'year': 2009, 'genres': [
                    'Action', 'Adventure', 'Fantasy', 'Sci-Fi']},
                {'title': 'The Avengers', 'year': 2012,
                    'genres': ['Action', 'Adventure', 'Sci-Fi']},
                {'title': 'A Clockwork Orange', 'year': 1971,
                    'genres': ['Crime', 'Drama', 'Sci-Fi']},
                {'title': 'Iron Man', 'year': 2008, 'genres': ['Action', 'Adventure', 'Sci-Fi']}]
    actual = my_sort.movies_sorted_by_title(movies_set)
    assert actual == expected


@pytest.fixture
def movies_set():
    return [
        {"title": "The Avengers", "year": 2012,
            "genres": ["Action", "Adventure", "Sci-Fi"]},
        {"title": "Anchorman: The Legend of Ron Burgundy",
            "year": 2004, "genres": ["Comedy"]},
        {"title": "Avatar", "year": 2009, "genres": [
            "Action", "Adventure", "Fantasy", "Sci-Fi"]},
        {"title": "Iron Man", "year": 2008, "genres": [
            "Action", "Adventure", "Sci-Fi"]},
        {"title": "A Clockwork Orange", "year": 1971,
            "genres": ["Crime", "Drama", "Sci-Fi"]}
    ]
