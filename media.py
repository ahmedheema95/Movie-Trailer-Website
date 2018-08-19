import webbrowser  # webbrowser module to be able to play youtube videos


class Movie():
    """Define Both Attributes And Mehods Of The Movies Here"""
    def __init__(self, title, storyline, image, youtube):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = youtube
# show_trailer is a method invoked by each instance of the movie class

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
