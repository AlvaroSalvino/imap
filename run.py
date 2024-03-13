from models.connection_options.connection import DBConnectionHandler
from models.repository.usercolecao_repository import usercolecaoRepository


db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()

user_colecao_repository = usercolecaoRepository(db_connection)

response = user_colecao_repository.select_many({"senha": "Malta@2024#"})
print(response)

response2 = usercolecaoRepository.select_one({"nome": "Alvaro"})
print(response2)
