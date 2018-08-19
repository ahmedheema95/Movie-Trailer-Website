import media   # import movie class here
import fresh_tomatoes  # import html and css file

tangled = media.Movie("Tangled",
                      "When the kingdom's most-wanted bandit, Flynn Rider"
                      "(Zachary Levi), hides in a convenient tower, he "
                      "immediately becomes a"
                      "captive of Rapunzel (Mandy Moore), "
                      "the spire's longtime resident"
                      ". Crowned with 70 feet"
                      "of magical golden hair, she has been locked away for"
                      "years and desperately wants freedom"
                      "The feisty teenager strikes a deal with Flynn"
                      "and together they begin a whirlwind adventure.",
                      "https://vignette.wikia.nocookie.net/disney/images/4/"
                      "4b/Tangled_poster_c.jpg/revision/latest?"
                      "cb=20130828020844",
                      "https.://www.youtube.com/watch?v=ip_0CFKTO9E")

up = media.Movie("UP",
                 "Seventy-eight year old Carl Fredricksen travels to"
                 "Paradise Falls in his home equipped with balloons,"
                 "inadvertently taking a young stowaway. ",
                 "https://static.rogerebert.com/uploads/movie/"
                 "movie_poster/up-2009"
                 "/large_zh9DXJhBdHVVaWiDURTipADamcK.jpg",
                 "https://www.youtube.com/watch?v=ORFWdXl_zJ4")

cars = media.Movie("Cars 1",
                   "A hot-shot race-car named Lightning McQueen "
                   "gets waylaid in Radiator Springs"
                   "where he finds the true meaning of friendship and family.",
                   "https://cdn.shopify.com/s/files/1/1909/0103/products"
                   "/Cars1_com_cover_final_SD_530x@2x.jpg?v=1493657671",
                   "https://www.youtube.com/watch?v=SbXIj2T-_uk")

lionking = media.Movie("Lion King 1",
                       "A young lion prince is born in Africa,"
                       "thus making his uncle"
                       "Scar the second in line to the throne."
                       "Scar plots with the"
                       "hyenas to kill King Mufasa and Prince Simba,"
                       "thus making himself King."
                       "The King is killed and Simba is led to believe"
                       "by Scar that it was his fault,"
                       "and so flees the kingdom in shame.",
                       "https://www.movieposter.com/posters/"
                       "archive/main/108/MPW-54063",
                       "https://www.youtube.com/watch?v=4sj1MT05lAA")


nemo = media.Movie("Finding Nemo",
                   "After his son is captured in the Great Barrier"
                   "Reef and taken to Sydney, a timid clownfish sets"
                   "out on a journey to bring him home.",
                   "https://vignette.wikia.nocookie.net/transcripts/"
                   "images/6/66/Disney_and_Pixar%27s_Finding_Nemo_-"
                   "_iTunes_Movie_Poster.jpg/revision/latest?cb="
                   "20170206021216",
                   "https://www.youtube.com/watch?v=2zLkasScy7A")


bolt = media.Movie("Bolt",
                   "The days of canine superstar Bolt (John Travolta)"
                   "are filled with danger and intrigue ..."
                   "until the cameras stop rolling. But Bolt doesn't"
                   "know that he's on a TV show; he thinks his amazing"
                   "powers are real. When Bolt is accidentally shipped"
                   "from his Hollywood soundstage to the mean streets"
                   "of New York, he begins his most-amazing adventure:"
                   "Armed only with his delusions and accompanied by a"
                   "cat and a hamster, he sets out to to find his owner,"
                   "Penny (Miley Cyrus).",
                   "https://vignette.wikia.nocookie.net/disney/images/"
                   "1/1b/Bolt_-_Poster.png/revision/latest?cb=20140902165013",
                   "https://www.youtube.com/watch?v=IBsg00NnzGg")


moana = media.Movie("Moana",
                    "An adventurous teenager sails out on a daring mission"
                    "to save her people. During her journey, Moana meets"
                    "the once-mighty demigod Maui, who guides her in her"
                    "quest to become a master way-finder. Together they"
                    "sail across the open ocean on an action-packed voyage,"
                    "encountering enormous monsters and impossible odds."
                    "Along the way, Moana fulfills the ancient quest of her"
                    "ancestors and discovers the one thing she always sought:"
                    "her own identity.",
                    "https://www.warehouseposters.com/ebaystore/"
                    "farang/moana.jpg",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")
# define an array of movie objects
movies = [tangled, up, cars, lionking, nemo, bolt, moana]
fresh_tomatoes.open_movies_page(movies)  # send array to "open movie" method
