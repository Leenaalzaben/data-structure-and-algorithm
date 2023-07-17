import re
class Movies():
    '''
    A class to arrange movies based on different criterias. 
    
    '''
    def __init__(self):
        pass


    def movies_sorted_by_year(self,movies) :
        '''
        A method to Sort movies by year in dscending order
        args:list of objects
        retuns: ordered list of object based on the most recent years
        '''
        ordered_movies=sorted(movies, key=lambda x: x["year"],reverse=True)
        return ordered_movies


    def movies_sorted_by_title (self,movies):
        '''
        A method Sorts movies by title while ignoring leading "A"s, "An"s, or "The"s
        args:list of objects
        retuns: ordered list of object based on the alphabits
        '''
        ignore_prefix = r'^(A|An|The)\s'  
        ordered_movies=sorted(movies, key=lambda x: re.sub(ignore_prefix, '', x["title"], flags=re.IGNORECASE))
        return ordered_movies

        

