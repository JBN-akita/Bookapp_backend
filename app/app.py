from fastapi import FastAPI, Depends,Request
import uvicorn
import models
from fastapi.middleware.cors import CORSMiddleware
from models import Books
from settings import Session
from sqlalchemy.orm import Session as AlchemySession



# FastAPIアプリケーションを作成
app = FastAPI()
app.add_middleware(
    CORSMiddleware,#オリジン（ドメイン、ポート、プロトコル)
    allow_origins=["*"],  # 安全な場合には "*" を使わず、必要なオリジンを指定
    allow_credentials=True,
    allow_methods=["*"],#メソッド許可
    allow_headers=["*"],#ヘッダー許可
)

# データベースセッションを取得する関数
def get_db():
    db = Session()
    try:
        yield db#DBセッション呼び出し
    finally:
        db.close()

# 初期化されたデータベースセッションを作成
session = Session()

# ルートエンドポイントへのGETリクエストを処理する関数(test用)
@app.get("/")
async def root():
    return {"message": "test clear!"}

# 書籍一覧取得
@app.get("/list")
def get_list(db: AlchemySession = Depends(get_db)):#データベースにアクセスする

    # Booksテーブルから全件取得するクエリを実行
    LibraryBooks = db.query(Books).all()
    return LibraryBooks


#新規登録
@app.post("/books_regist")
async def books_regist(request:Request,db: Session = Depends(get_db)):

    # jsonデータの取得
    data = await request.json()
    #登録するデータをjson形式で格納
    book_data = models.Books(
        name=data['name'],
        publisher=data['publisher'],
        author=data['author'],
        page_count=data['page_count'],
        published_date=data['published_date'],
        price=data['price'],
        registered_user=data['registered_user']
    )
    #登録処理
    db.add(book_data)
    db.commit()
    #登録okのメッセージを返す
    return "regist_ok"

#更新
@app.post("/books_update/{id}")
async def books_update(id: int, request: Request, db: Session = Depends(get_db)):
        # jsonデータの取得
        data = await request.json()

        # 対象の本を取得
        book = db.query(Books).filter(Books.id == id).first()

        # 本の情報を更新
        book.publisher = data['publisher']
        book.page_count = data['page_count']
        book.published_date = data['published_date']
        book.name = data['name']
        book.author = data['author']
        book.price = data['price']

        # データベースの変更をコミット
        db.add(book)
        db.commit()

        return "update_ok"

#削除
@app.post("/books_delete/{id}")
async def books_delete(id: int, request: Request, db: Session = Depends(get_db)):
    # jsonデータの取得
    data = await request.json()

    db.query(Books).filter(Books.id==id).delete()

    db.commit()

    return "delete_ok"

# FastAPIアプリケーションを実行
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
