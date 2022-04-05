from tinydb import TinyDB, Query

db = TinyDB('usuarios.json')
# db.truncate() -> para apagar o db []
# db.insert({"id": 1, "email": "user1@user.com.br", "senha": "123456789"})
# db.insert({"id": 2, "email": "user2@user.com.br", "senha": "987654321"})
# db.insert({"id": 3, "email": "user2@user.com.br", "senha": "987654321"})
# db.insert({"id": 4, "email": "user2@user.com.br", "senha": "987654321"})
# db.insert({"id": 5, "email": "user2@user.com.br", "senha": "987654321"})
# db.insert({"id": 6, "email": "user2@user.com.br", "senha": "987654321"})

User = Query()

# db.remove(User.id == 2)
#  print(db.all())

