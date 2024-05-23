from config import db_config
import pathlib
from pathlib import Path



with open(Path(pathlib.Path.cwd(), 'db_create.txt'), 'w') as writer:
    db = db_config['mysql']
    writer.write("insert each line into your mysql terminal separately by order")
    writer.write('\n\n')
    writer.write(f"CREATE DATABASE {db['database']};\n")
    writer.write(f"USE {db['database']};\n")
    for table in db['tables']:
        writer.write(f"CREATE TABLE {table};\n")
    writer.write(f"CREATE USER '{db['user']}'@'{db['host']}' IDENTIFIED BY '{db['passwd']}';\n")
    writer.write(f"GRANT ALL ON *.* TO '{db['user']}'@'{db['host']}' WITH GRANT OPTION;\n")
    writer.write(f"FLUSH PRIVILEGES;\n")
    writer.write(f"CREATE USER '{db['user2']}'@'{db['host']}' IDENTIFIED BY '{db['passwd']}';\n")
    writer.write(f"GRANT ALL ON *.* TO '{db['user2']}'@'{db['host']}' WITH GRANT OPTION;\n")
    writer.write(f"FLUSH PRIVILEGES;")
    print('файл успешно сгенерирован!')


###mysql -h 127.0.0.1 -u root -p