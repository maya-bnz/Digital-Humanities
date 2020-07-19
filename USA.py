import csv
from imdb import IMDb
import xlsxwriter

# opening the 'title.basics.tsv.gz' data base
tsv_file = open('data.tsv', encoding='utf-8')
read_tsv = csv.reader(tsv_file, delimiter='\t')

# array to collect animation movies
animation_movies = []

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
workbook = xlsxwriter.Workbook('USA_DB.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Movie_ID')
worksheet.write('B1', 'Title')
worksheet.write('C1', 'Year')
row = 1

# connecting to IMDB
ia = IMDb()

j = 0
for movie_id in animation_movies:
    movie = ia.get_movie(movie_id)
    country = movie.get('country')
    if country == None:
        continue
    if country[0] == "United States":
        content = [movie_id, movie.get('title'), movie.get('year')]
        column = 0
        for item in content:
            worksheet.write(row, column, item)
            column += 1
        row += 1
    print(j)
    j = j + 1
workbook.close()