from django import forms
from .models import Pelicula, Genero


class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ["nombre", "descripcion"]

        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ejemplo: Acción"
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Descripción del género"
                }
            ),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()

        if not nombre:
            raise forms.ValidationError(
                "El nombre del género es obligatorio."
            )

        return nombre


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = [
            "titulo",
            "sinopsis",
            "anio",
            "duracion",
            "imagen",
            "generos",
        ]

        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Título de la película"
                }
            ),
            "sinopsis": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Sinopsis de la película"
                }
            ),
            "anio": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Año"
                }
            ),
            "duracion": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Duración en minutos"
                }
            ),
            "imagen": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://..."
                }
            ),
            "generos": forms.CheckboxSelectMultiple(),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data["titulo"].strip()

        if not titulo:
            raise forms.ValidationError(
                "El título de la película es obligatorio."
            )

        return titulo

    def clean_sinopsis(self):
        sinopsis = self.cleaned_data["sinopsis"].strip()

        if not sinopsis:
            raise forms.ValidationError(
                "La sinopsis de la película es obligatoria."
            )

        return sinopsis