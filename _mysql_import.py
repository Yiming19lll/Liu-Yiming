import mysql.connector

def import_to_mysql(schema_path, data_path):
    # 配置 MySQL 连接
    config = {
        'host': 'localhost',         # MySQL 主机
        'user': 'root',     # MySQL 用户名
        'password': 'Lym20040331', # MySQL 密码
        'database': 'my_database'  # 目标数据库
    }

    def execute_sql_file(cursor, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            sql_commands = file.read().split(';')  # 根据 ';' 分割 SQL 语句
            for command in sql_commands:
                if command.strip():  # 跳过空行
                    try:
                        cursor.execute(command)
                    except mysql.connector.Error as e:
                        print(f"Error executing command: {command}\n{e}")

    try:
        # 连接 MySQL
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # 执行 schema.sql 创建表
        print(f"Executing schema.sql: {schema_path}")
        execute_sql_file(cursor, schema_path)

        # 执行 ai_context_insert.sql 插入数据
        print(f"Executing ai_context_insert.sql: {data_path}")
        execute_sql_file(cursor, data_path)

        # 提交事务
        conn.commit()
        print("Data imported successfully!")

    except mysql.connector.Error as e:
        print(f"MySQL error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
