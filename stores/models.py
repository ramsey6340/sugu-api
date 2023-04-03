from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)  # date de creation de la catégorie
    date_last_updated = models.DateTimeField(auto_now=True)  # date de la dernière modification

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    is_up_to_date = models.BooleanField(default=True)  # pour savoir si oui ou non le magasin est à jour
    # dans son payement mentuel
    size = models.IntegerField(default=5)  # la taille du magasin, le nombre de produit maximal que le magasin peut
    # contenir
    is_popular = models.BooleanField(default=False)  # un magasin est concideré comme populaire si son nombre d'abonnée
    # atteint un certain nombre
    description = models.TextField(max_length=300, blank=True)
    more_precision = models.CharField(max_length=40, default="")  # pour ajouter plus de precision de la par du vendeur
    # pour localiser sont magasin. Par exemple: "Près de la grande mosquée de Bamako",
    # "Près de l'hopital Gabriel Touré", etc
    num_tel1 = models.IntegerField()
    num_tel2 = models.IntegerField(null=True)
    email = models.EmailField(null=True)

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)  # date de creation de la sous catégorie
    date_last_updated = models.DateTimeField(auto_now=True)  # date de la dernière modification

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)  # date de creation de la sous catégorie
    date_last_updated = models.DateTimeField(auto_now=True)  # date de la dernière modification
    nb_like = models.IntegerField(default=0)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    is_popular = models.BooleanField()

    categories = models.ManyToManyField(Category)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')

    class Genre(models.TextChoices):
        HOMME = 'homme'
        FEMME = 'femme'

    genre = models.CharField(choices=Genre.choices, max_length=5)

    def __str__(self):
        return self.name
