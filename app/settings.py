# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # データベース接続情報を定義
# db_user = 'user01'
# db_password = 'pass01'
# db_host = 'localhost'
# db_port = 3306
# db_name = 'restapi'

# # データベース接続用の文字列を作成
# connection_string = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
# engine = create_engine(connection_string, echo=True) 

# # データベースモデルのベースクラスを作成
# Base = declarative_base()
# Base.metadata.create_all(bind=engine)
# # セッションを作成するためのセッションメーカーを作成
# Session = sessionmaker(autocommit=False,autoflush=False,bind=engine)
# #mysqlの記述　db名など命名で変更する↑


#postgresの記述　↓
#import psycopg2←のimportが必要
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL接続情報
db_user = 'postgres'
db_password = 'postgres'
db_host = 'localhost'
db_port = 5432
db_name = 'Bookapp'

# データベース接続用の文字列を作成
connection_string = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_string, echo=True) 

# データベースモデルのベースクラスを作成
Base = declarative_base()

# テーブルを作成
Base.metadata.create_all(bind=engine)

# セッションを作成するためのセッションメーカーを作成
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)