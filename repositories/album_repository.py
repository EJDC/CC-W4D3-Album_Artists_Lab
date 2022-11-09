from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository

# SELECT ALL
def select_all():
    albums = []
    sql ="SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], artist, row['genre'], row['id'])
        albums.append(album)
    return albums

# SAVE
def save(album):
    sql = """INSERT INTO albums (title, artist_id, genre)
    VALUES (%s,%s,%s) RETURNING *"""

    values = [album.title, album.artist_id.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id 
    return album 

# SELECT
def select(id):
    album = None
    sql = """SELECT * FROM albums
    WHERE id=%s"""
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0] 
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], artist, result['genre'], result['id'])
        return album
# Delete

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

# delete single

def delete(id):
    sql = """DELETE FROM albums
    WHERE id=%s"""
    values = [id]
    run_sql(sql, values)

#  UPDATE

def update(album):
    sql = """UPDATE albums SET (title, artist_id, genre) = (%s,%s,%s) 
    WHERE id=%s"""
    values = [album.title, album.artist_id.id, album.genre, album.id]
    run_sql(sql, values)


def album_by_artist(id):
    sql = """SELECT * FROM albums
    WHERE artist_id = (%s)"""
    values = [id]
    run_sql(sql, values)
