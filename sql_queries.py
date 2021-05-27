# DROP TABLES
#try:
#    songplay_table_drop = "DROP table songplays"
#except:
#    print ("Error dropping songplay table")
#
#try:
#    user_table_drop = "DROP table users"
#except:
#    print("Error dropping users table")
#
#try:
#    song_table_drop = "DROP table songs"
#except:
#    print("Error dropping songs table")
    
    
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = "CREATE TABLE IF NOT EXISTS songplays (songplay_id int, start_time int, user_id int, level int, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent int)"

user_table_create = """CREATE TABLE IF NOT EXISTS users (user_id int, first_name varchar, last_name varchar, gender varchar, level int)"""

song_table_create = """CREATE TABLE IF NOT EXISTS songs (song_id varchar, title varchar, artist_id varchar, year int, duration float)"""

artist_table_create = """CREATE TABLE IF NOT EXISTS artists (artist_id varchar, name varchar, location varchar, latitude int, longitude int)"""

time_table_create = """CREATE TABLE IF NOT EXISTS time (start_time int, hour int, day int, week int, month int, year int, weekday varchar)"""

# INSERT RECORDS

songplay_table_insert = """INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

user_table_insert = """INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s, %s)"""

song_table_insert = """INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
"""

artist_table_insert = """INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)"""


time_table_insert = """INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)"""

# FIND SONGS

song_select = """ SELECT * FROM songs """

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]