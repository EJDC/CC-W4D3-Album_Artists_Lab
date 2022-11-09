from db.run_sql import run_sql
from models.artist import Artist
# SELECT ALL
def select_all():
    artists = []
    sql ="SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['group_name'], row['id'])
        artists.append(artist)
    return artists

# SAVE
def save(artist):
    sql = """INSERT INTO artists (group_name)
    VALUES (%s) RETURNING *"""

    values = [artist.group_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id 
    return artist 

# SELECT
def select(id):
    artist = None
    sql = """SELECT * FROM artists
    WHERE id=%s"""
    values = [id]
    results = run_sql(sql, values)

    if results: 
        result = results[0]
        artist = Artist(result['group_name'])
        return artist
# Delete

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

# delete single

def delete(id):
    sql = """DELETE FROM artists
    WHERE id=%s"""
    values = [id]
    run_sql(sql, values)

#  UPDATE

def update(artist):
    sql = """UPDATING artists SET (group_name) = (%s) 
    WHERE id=%s"""
    values = [artist.group_name, artist.id]
    run_sql(sql, values)

