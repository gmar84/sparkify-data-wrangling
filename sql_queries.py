# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("CREATE table songplays (songplay_id serial primary key, start_time timestamp, user_id int, level text, song_id text, artist_id text, session_id varchar, location text, user_agent text);")

user_table_create = ("CREATE TABLE users (user_id int primary key not null, first_name varchar, last_name varchar, gender varchar(1), level varchar(4));")

song_table_create = ("CREATE TABLE songs (song_id varchar(18) primary key not null, title text, artist_id varchar(18), year int, duration float);")

artist_table_create = ("CREATE TABLE artists (artist_id varchar(18) primary key not null, artist_name text, artist_location text, artist_latitude float(5), artist_longitude float(5));")

time_table_create = ("CREATE TABLE time (start_time time primary key not null, hour int, day varchar(9), week int, month int, year int, weekday int);")

# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (songplay_id) DO NOTHING")

user_table_insert = ("INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level")

song_table_insert = ("INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)")

artist_table_insert = ("INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING")


time_table_insert = ("INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES(%s, %s, %s, %s, %s, %s, %s)")

# FIND SONGS
# get the song ID and artist ID by querying the songs and artists tables to find matches based on song title, artist name, and song duration time

song_select = ("SELECT songs.song_id, songs.artist_id FROM songs LEFT JOIN songplays ON songs.song_id = songplays.song_id")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]