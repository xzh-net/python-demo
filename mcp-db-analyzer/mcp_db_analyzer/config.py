"""
数据库配置文件
"""

# 数据库 A 配置
DB_A = {
    "host": "192.168.31.161",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "geo"
}

# 数据库 B 配置
DB_B = {
    "host": "192.168.31.161",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "iam_identity"
}

# 数据库映射
DATABASES = {
    "A": DB_A,
    "B": DB_B
}