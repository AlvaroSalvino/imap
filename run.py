from pymongo.server_api import ServerApi
from models.connection_options.connection import DBConnectionHandler
from models.repository.usercolecao_repository import usercolecaoRepository

db_hande = DBConnectionHandler()
db_hande.connect_to_db()
db_connection = db_hande.get_db_connection()

user_colecao_Repository = usercolecaoRepository(db_connection)

user_colecao_Repository.select_many()

