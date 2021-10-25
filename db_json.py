import sqlite3
import json


def fetch_data( json_str = False ):
    conn = sqlite3.connect( 'mydb.db' )
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
    db = conn.cursor()

    rows = db.execute('''
    SELECT * from history
    ''').fetchall()

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON

    return rows

# print(fetch_data(json_str=True))