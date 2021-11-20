import peliculaDAO

db = 'pelicula'
col = 'pelicula'

r = peliculaDAO.select_all(db, col)
for r in r:
    print(r)

r = peliculaDAO.select_by(db, col, {'name': 'Chuky'})
for r in r:
    print(r)