class Film:
    """
    Clase para representar una película.

    Atributos:
        title: El título de la película.
        description: Una breve descripción de la película.
        release_year: El año en que se lanzó la película.
        language_id: El ID del idioma en el que se habla principalmente la película.
        original_language_id: El ID del idioma en el que se produjo originalmente la película.
        rental_duration: El número de días que un cliente puede alquilar la película.
        rental_rate: La cantidad de dinero que paga un cliente por alquilar la película por día.
        length: La duración de la película en minutos.
        replacement_cost: El costo de reemplazar la película.
        rating: La clasificación de la película, de 1 a 5 estrellas.
        special_features: Una lista de características especiales incluidas en la película.
        last_update: La fecha y hora de la última actualización de la película.
    """

    def __init__(self, film_id=None, title=None, description=None, release_year=None,
                 language_id=None, original_language_id=None, rental_duration=None,
                 rental_rate=None, length=None, replacement_cost=None, rating=None,
                 special_features=None, last_update=None):
        """
        Crea una nueva instancia de la clase Film.

        Args:
            film_id: El ID de la película (obligatorio).
            title: El título de la película.
            description: Una breve descripción de la película.
            release_year: El año en que se lanzó la película.
            language_id: El ID del idioma en el que se habla principalmente la película.
            original_language_id: El ID del idioma en el que se produjo originalmente la película.
            rental_duration: El número de días que un cliente puede alquilar la película.
            rental_rate: La cantidad de dinero que paga un cliente por alquilar la película por día.
            length: La duración de la película en minutos.
            replacement_cost: El costo de reemplazar la película.
            rating: La clasificación de la película, de 1 a 5 estrellas.
            special_features: Una lista de características especiales incluidas en la película.
            last_update: La fecha y hora de la última actualización de la película.
        """
        self.film_id = film_id
        self.title = title
        self.description = description
        self.release_year = release_year
        self.language_id = language_id
        self.original_language_id = original_language_id
        self.rental_duration = rental_duration
        self.rental_rate = rental_rate
        self.length = length
        self.replacement_cost = replacement_cost
        self.rating = rating
        self.special_features = special_features
        self.last_update = last_update

    def __str__(self):
        """
        Devuelve una cadena que representa la película.

        Returns:
            Una cadena que representa la película.
        """
        return self.title
    
    def serialize(self):
        """Serialize object representation
        Returns:
            dict: Object representation
        Note:
            - The last_update attribute is converted to string
            - The special_features attribute is converted to list if it is not
            null in the database. Otherwise, it is converted to None
            - The attributes rental_rate and replacement_cost are converted to 
            int, because the Decimal type may lose precision if we convert 
            it to float
        """
        if self.special_features is not None:
            special_features = list(self.special_features)
        else:
            special_features = None
        return {
            "film_id": self.film_id,
            "title": self.title,
            "description": self.description,
            "release_year": self.release_year,
            "language_id": self.language_id,
            "original_language_id": self.original_language_id,
            "rental_duration": self.rental_duration,
            "rental_rate": int(self.rental_rate*100),
            "length": self.length,
            "replacement_cost": int(self.replacement_cost*100),
            "rating": self.rating,
            "special_features": special_features,
            "last_update": str(self.last_update)
        }