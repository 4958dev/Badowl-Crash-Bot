import mysql.connector
from mysql.connector import Error as sqlErr

from config import db_config

import logging



log = logging.getLogger(__name__)



def create_connection_mysql_db(user_name, db_host=db_config["mysql"]["host"], user_password=db_config["mysql"]["passwd"], db_name=db_config['mysql']['database']):
    connection_db = None
    try:
        connection_db = mysql.connector.connect(
            host = db_host,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        connection_db.commit()
    except sqlErr as db_connection_error:
        log.error(db_connection_error, exc_info=True)
        print("Возникла ошибка mySQL: ", db_connection_error)
    return connection_db



sqladmin = create_connection_mysql_db(db_config["mysql"]["user"])
sqleditor = create_connection_mysql_db(db_config["mysql"]["user2"])



#mysql str response clearer
def element_delete_excessives(listing):
    chars_to_remove = ["(", ")", ",", "'"]
    element = str()
    try:
        for element in listing:
            for char in chars_to_remove:
                element = str(element)
                element = element.replace(char, "")
    except:
        pass
    return element



#mysql list response clearer
def list_delete_excessives(listing):
    chars_to_remove = ["(", ")", ",", "'"]
    clear_list = []
    try:
        for element in listing:
            for char in chars_to_remove:
                element = str(element)
                element = element.replace(char, "")
            clear_list.append(element)
    except:
        pass
    return clear_list