import os, json

from commands_functions.schema_keys import Keys
from models.table import Table
from outputs.exceptions import *

class Database:
    def __init__(self, database_name = None, schema_data = None):
        self.tables = {}
        if schema_data is not None:
            self.__init_by_schema(schema_data = schema_data)
        elif database_name is not None:
            self.__init_by_name(database_name = database_name)
        else :
            raise WrongInput(message = "the database name and schema data are null")
            
    def __init_by_schema(self, schema_data):
        self.__database_name = schema_data[Keys.DATABASE_NAME]
        for table_schema in schema_data[Keys.TABLES]:
            self.tables[table_schema[Keys.NAME]] = Table(self, table_schema = table_schema)

    def __init_by_name(self, database_name):
        for table_name in os.listdir(self.get_path()):
            self.tables[table_name] = Table(self, table_name = table_name)
        

    def serialize(self):
        os.makedirs(self.get_path(), exist_ok = True)
        self.__serialize_tables()

    def __serialize_tables(self):
        #update tables_metadata dict
        for table in self.tables.values():
            table.serialize()

    def set(self, table_name, row):
        # table = Table(table_name)
        # table.set(row)
        pass
    
    def get(self, table, quiry):
        pass
    
    def delete(self, table, quiry):
        pass
    
    def get_path(self):
        return os.path.join(os.getcwd(), self.__database_name)
    
    def get_name(self):
        return self.__database_name