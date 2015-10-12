import webbrowser

class Movie():
    
    # Initialize move class and define the parameters.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):


        # Define parameters (Movie Title, Movie description, Poster and Youtube trailer
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    # Define function to open Youtube browser
    def show_trailer(self): 
        webbrowser.open(self.trailer_youtube_url)
