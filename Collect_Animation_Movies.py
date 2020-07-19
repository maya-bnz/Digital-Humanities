import csv
from imdb import IMDb
import xlsxwriter

# opening the 'title.basics.tsv.gz' data base
tsv_file = open('data.tsv', encoding='utf-8')
read_tsv = csv.reader(tsv_file, delimiter='\t')

# array to collect animation movies
animation_movies = []
# the following loop is to collect only animation movies from the DB
i=1
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
                # animation_movies.append(line[0])
    print(i)
    i = i+1
print("1933: "+str(animation_movies[1933]))
print("1934: "+str(animation_movies[1934]))
print("1935: "+str(animation_movies[1935]))
tsv_file.close()