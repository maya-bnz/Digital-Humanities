import csv
from imdb import IMDb
import xlsxwriter

# opening the 'title.basics.tsv.gz' data base
tsv_file = open('data.tsv', encoding='utf-8')
read_tsv = csv.reader(tsv_file, delimiter='\t')

# array to collect animation movies
animation_movies = []

# the corpus of words that represent female leading actress movies
key_words = [" she ", "She ", " her ", "Her ", " her", "Princess ", " princess ", "princess", "Queen ", " queen ",
             " queen", " beautiful ", " beautiful" "Beautiful ", " hers ", " hers", "Hers ", " girl ", " girl", "Girl ",
             " woman ", " woman", "Woman ", " she's ", " herself ", " herself"]

# the following loop is to collect only animation movies from the DB
i=0
first_line = True
for line in read_tsv:
    # if i==100000:
    #     break
    if first_line:
        first_line = False
        continue
    title_type = line[1]
    # make sure it is a movie and not a TV show/ Short and ect.
    if title_type == 'movie':
        genres = line[len(line)-1]
        genres = genres.split(',')
        for genre in genres:
            # make sure it is an animation movie
            if genre == 'Animation':
                animation_movies.append(line[0][2:])
    print(i)
    i = i+1
tsv_file.close()

# create the final DB
workbook = xlsxwriter.Workbook('movies_DB.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Movie_ID')
worksheet.write('B1', 'Title')
worksheet.write('C1', 'Country')
worksheet.write('D1', 'Year')
row = 1

# connecting to IMDB
ia = IMDb()

# the following loop does the steps:
# 1. decide if the main character in the movie is a female according to the corpus of key words
# 2. insert the selected movies data to the created DB (xcel file)
j = 0
for movie_id in animation_movies:
    movie = ia.get_movie(movie_id)
    plot = movie.get('plot')
    if plot != None:
        for word in key_words:
            if plot[0].find(word) != -1:
                column = 0
                title = movie.get('title')
                country = movie.get('country')
                year = movie.get('year')
                if (title == None) or (country == None) or (year == None):
                    continue
                content = [movie_id, movie.get('title'), movie.get('country')[0], movie.get('year')]
                for item in content:
                    worksheet.write(row, column, item)
                    column += 1
                row += 1
                break
    print(j)
    j = j+1
workbook.close()
