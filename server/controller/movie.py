from fastapi import HTTPException
import tmdb3

from model.schema import Filme
from model.schema import Elenco


class ControladorFilme:
    def get(self, id: int) -> Filme:
        try:
            db_movie = tmdb3.Movie(id)
        except tmdb3.TMDBHTTPError:
            raise HTTPException(status=404, detail="Filme não existe.")

        elenco = []
        for member in db_movie.cast:
            elenco.append(Elenco(nome=member.name, papel=member.character))

        diretor = None
        for member in db_movie.crew:
            if member.job == 'Director':
                diretor = member.name

        generos = [g.name for g in db_movie.genres]

        movie = Filme(
                id=db_movie.id,
                titulo=db_movie.title,
                duracao=db_movie.runtime,
                descricao=db_movie.overview,
                elenco=elenco,
                diretor=diretor,
                generos=generos
            )

        return movie
