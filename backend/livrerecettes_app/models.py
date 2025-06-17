from django.db import models

class Recette(models.Model):
    """
    Modèle représentant une recette de cuisine.
    """
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    temps_preparation = models.IntegerField(help_text="Temps en minutes", null=True, blank=True)
    temps_cuisson = models.IntegerField(help_text="Temps en minutes", null=True, blank=True)
    nombre_portions = models.IntegerField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date_creation']
