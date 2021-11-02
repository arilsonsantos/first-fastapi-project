from fastapi import FastAPI, HTTPException
import uvicorn
import movie_data
from models.usuario import Usuario
from models.movie_model import MovieModel

app = FastAPI()

@app.get("/")
def raiz():
    return {"Olá": "Mundo"}

base_de_dados = [
    Usuario(id=1, email="user1@email.com", senha="123"),
    Usuario(id=2, email="user2@email.com", senha="123")
]

@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

@app.get("/usuarios/{id}")
def get_usuario_por_id(id: int):
    # usuario = [x for x in base_de_dados if x.id == id ][0]

    for usuario in base_de_dados:
        if usuario.id == id:
            return usuario

    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.get("/movie/{title}", response_model=MovieModel)
async def movie_search(title: str):
    movie = await movie_data.get_movie(title)

    if not movie:
        raise HTTPException(status_code=404, detail="Filme não encontrado")

    return movie.dict()



if __name__ == "__main__":
    dev = 1
    if dev == 1:
        uvicorn.run('main:app', host="127.0.0.1", port=8000, log_level="info", reload=True, debug=True)