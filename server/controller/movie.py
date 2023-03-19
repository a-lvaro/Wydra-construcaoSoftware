from fastapi import HTTPException
from requests.exceptions import HTTPError
import tmdbsimple as tmdb

from model.schema import Filme
from model.schema import Elenco


class ControladorFilme:
    def get(self, id: int) -> Filme:
        try:
            db_movie = tmdb.Movies(id)

            details = db_movie.info(language="pt-BR")
            credit = db_movie.credits(language="pt-BR")
        except HTTPError:
            raise HTTPException(status_code=404, detail="Filme não existe.")

        diretor = None
        elenco = []

        for member in credit['cast']:
            elenco.append(Elenco(
                nome=member['name'],
                papel=member['character']
            ))

        for member in credit['crew']:
            if member['known_for_department'] == 'Directing':
                diretor = member['name']

        generos = [g['name'] for g in details['genres']]

        movie = Filme(
                id=db_movie.id,
                titulo=details['title'],
                duracao=details['runtime'],
                descricao=details['overview'],
                elenco=elenco,
                diretor=diretor,
                generos=generos
            )

        return movie
