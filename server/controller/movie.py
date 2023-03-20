from fastapi import HTTPException
from requests.exceptions import HTTPError
from typing import List

import tmdbsimple as tmdb

from model.schema import Filme


class ControladorFilme:
    def get(self, id: int) -> Filme:
        try:
            # Obtem o filme através da API TMDB
            db_movie = tmdb.Movies(id)

            info = db_movie.info(language="pt-BR")
        except HTTPError:
            raise HTTPException(status_code=404, detail="Filme não existe.")

        movie = convert(info)
        return movie

    def get_by_titulo(self, titulo: str, page=1) -> List[Filme]:
        search = tmdb.Search()
        response = search.movie(query=titulo, page=page)
        movies = []

        # Converte cada filme da lista
        for result in response['results']:
            # Temos o titulo e a descrição mas para obter
            # o elenco e generos precisamos fazer outro request
            # TODO: Fazer isso de um jeito mais eficiente
            movie = convert(result)
            movies.append(movie)

        return movies


# Função auxiliar para converter um filme no formato
# da API tmdb para uma entidade Filme
def convert(info) -> Filme:
    # Obtem os generos
    categoria = [g['name'] for g in info['genres']]

    # Cria uma entidade da classe filme
    movie = Filme(
            id=info['id'],
            titulo=info['title'],
            duracao=info['runtime'],
            descricao=info['overview'],
            categoria=categoria
        )

    return movie
