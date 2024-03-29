import datetime
from django.db import models
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator, MaxValueValidator, MaxLengthValidator, MinValueValidator


GENRE = (
        ('H', 'Homme'),
        ('F', 'Femme'),
    )
LENGTH_GENRE = 3

METHOD_OF_PAYMENT = (
        ('OM', 'Orange Money'),
        ('MM', 'Moov Money'),
        ('SM', 'Sama Money'),
    )
LENGTH_METHOD_OF_PAYMENT = 10

MODE_TRANSPORT = (
    ('moto', 'Moto'),
    ('vehicule', 'Véhicule'),
)
LENGTH_MODE_TRANSPORT = 20

DEVICE_TYPE = (
    ('iphone', 'iPhone'),
    ('android', 'Android'),
    ('huawei', 'Huawei'),
)
LENGTH_DEVICE_TYPE = 30

PROFESSION = (
    ('etudiant', 'Etudiant'),
    ('fonctionnaire', 'Fonctionnaire'),
    ('commercant', 'Commerçant'),
    ('autre', 'Autre')
)
LENGTH_PROFESSION = 40

REGISTER_TYPE = (
    ('google', 'Google'),
    ('numero', 'Numéro de téléphone'),
    ('email', 'Email'),
)
LENGTH_REGISTER_TYPE = 30

ACCOUNT_TYPE = (
    ('buyer', 'Acheteur'),
    ('seller', 'Vendeur'),
)
LENGTH_ACCOUNT_TYPE = 6

MONTH = (
    ('janvier', 'Janvier'),
    ('fevrier', 'Février'),
    ('mars', 'Mars'),
    ('avril', 'Avril'),
    ('mai', 'Mai'),
    ('juin', 'Juin'),
    ('juillet', 'Juillet'),
    ('aout', 'Aout'),
    ('septembre', 'Septembre'),
    ('octobre', 'Octobre'),
    ('novembre', 'Novembre'),
    ('decembre', 'Décembre'),
)
LENGTH_MONTH = 10

NAME_DAY_OF_BIRTH = (
    ('lun', 'Lundi'),
    ('mar', 'Mardi'),
    ('mer', 'Mercredi'),
    ('jeu', 'Jeudi'),
    ('ven', 'Vendredi'),
    ('sam', 'Samedi'),
    ('dim', 'Dimanche'),
)
LENGTH_NAME_DAY_OF_BIRTH = 3


class Country(models.Model):
    """
        Pays :
            La classe correspondant à un Pays
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Region(models.Model):
    """
        Région :
            La classe correspondant à une région
    """
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, related_name='regions', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Neighborhood(models.Model):
    """
        Quartier :
            La classe correspondant à un quartier
    """
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, related_name='neighborhoods', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class User(models.Model):
    """
        Utilisateur :
            Cette classe concerne tous les utilisateurs de SUGU, les acheteurs, les vendeurs, les livreurs
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    num_tel = PhoneNumberField(region='ML')
    password = models.CharField(validators=[MinLengthValidator(6)], max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        abstract = True


class Buyer(User):
    """
        Acheteur :
            Cette classe représente l'acheteur lui-même
    """


class Seller(Buyer):
    """
        Vendeur :
            Cette classe représente le vendeur lui-même
    """


class Category(models.Model):
    """
        Catégorie :
            Il s'agit de la catégorie dont un produit ou un magasin fait partie
    """
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)  # date de creation de la catégorie
    date_last_updated = models.DateTimeField(auto_now=True)  # date de la dernière modification

    def __str__(self):
        return self.name


class ProfileInfo(models.Model):
    """
        Informations de profile d'un acheteur :
            Cette classe contient l'ensemble deAs informations precis sur le profile de l'acheteur.
    """
    birth_day = models.DateField()
    device_type = models.CharField(choices=DEVICE_TYPE, max_length=LENGTH_DEVICE_TYPE)
    genre = models.CharField(choices=GENRE, max_length=LENGTH_GENRE)
    profession = models.CharField(choices=PROFESSION, max_length=LENGTH_PROFESSION)
    register_type = models.CharField(choices=REGISTER_TYPE, max_length=LENGTH_REGISTER_TYPE)  # c'est m'administrateur
    # qui renseigne ce champ
    method_of_payment = MultiSelectField(choices=METHOD_OF_PAYMENT, max_length=LENGTH_METHOD_OF_PAYMENT)
    account_type = models.CharField(choices=ACCOUNT_TYPE, max_length=LENGTH_ACCOUNT_TYPE)
    register_date = models.DateTimeField(auto_now_add=True)

    buyer = models.OneToOneField(Buyer, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"Information Profile-{self.buyer}"


class DeliveryMan(models.Model):
    """
        Livreur :
            Cette classe fait référence à un livreur de SUGU
    """
    buyer = models.OneToOneField(Buyer, on_delete=models.CASCADE, null=True, blank=True, default=None)
    mode_transport = models.CharField(choices=MODE_TRANSPORT, max_length=10)
    current_geolocation_position = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Livreur-{self.buyer}"


class Address(models.Model):
    """
        Adresse :
            La classe correspondant à une adresse
    """

    name = models.CharField(max_length=20)
    reference = models.CharField(max_length=100)
    geolocation = models.URLField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True,)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True)
    profile_info = models.ForeignKey(ProfileInfo, on_delete=models.CASCADE, blank=True, related_name='addresses')

    def __str__(self):
        return f"{self.name}"


class Cart(models.Model):
    """
        Panier :
            Cette classe représente le panier de l'acheteur
    """
    total_nb_products = models.IntegerField()
    total_price = models.IntegerField()  # prix total de l'ensemble des commandes dans le panier
    buyer = models.OneToOneField(Buyer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Panier-{self.buyer}"


class Store(models.Model):
    """
        Magasin ou Boutique :
            Il s'agit de la classe d'une Boutique
    """
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    is_up_to_date = models.BooleanField(default=True)  # pour savoir si oui ou non le magasin est à jour
    # dans son payement mensuel
    size = models.IntegerField(default=5)  # la taille du magasin, le nombre de produits maximal que le magasin peut
    # contenir
    is_popular = models.BooleanField(default=False)  # un magasin est concideré comme populaire si son nombre d'abonnées
    # atteint un certain nombre
    description = models.TextField(max_length=300, blank=True)
    more_precision = models.CharField(max_length=40, blank=True)  # pour ajouter plus de precision de la par du vendeur
    # Pour localiser son magasin. Par exemple : "Près de la grande mosquée de Bamako",
    # "Près de l'hôpital Gabriel Touré", etc
    num_tel1 = PhoneNumberField(region='ML')
    num_tel2 = PhoneNumberField(region='ML', blank=True)
    email = models.EmailField(null=True, blank=True)

    categories = models.ManyToManyField(Category)
    seller = models.OneToOneField(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """
        Sous-Catégorie :
            Il s'agit de la sous-catégorie dont un produit fait partie
    """
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)  # date de creation de la sous catégorie
    date_last_updated = models.DateTimeField(auto_now=True)  # date de la dernière modification

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
        Produit :
            Il s'agit de produit que le vendeur mettra dans son magasin
    """
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
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, related_name='products')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products', default=None)

    genre = MultiSelectField(choices=GENRE, max_length=LENGTH_GENRE)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    """
        Promotion :
            Il s'agit de promotion que le vendeur à fait sur son produit
    """
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    new_price = models.IntegerField()

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Promotion-{self.seller}-{self.product}"


class ProductHistory(models.Model):
    """
        Historique des produits visités :
            Il s'agit de la liste des produits que l'acheteur a consulté. Il s'agit de son historique
    """
    total_nb_product = models.IntegerField(default=0)
    buyer = models.OneToOneField(Buyer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"Historique-{self.buyer}"


class Order(models.Model):
    """
        Commande :
            Cette classe représente les commandes de l'acheteur. Ces commandes peuvent être inactives (elle se
            trouve encore dans le panier), elles peuvent être actives (l'acheteur a décidé de payer le produit), dans cette
            dernière, elle n'est plus dans le panier et fait partie de la liste des commandes.
    """
    nb_copies = models.IntegerField()  # nombre d'exemplaires
    total_price = models.IntegerField()  # prix total de cette unique commande
    active = models.BooleanField(default=False)  # pour savoir si la commande a été payé ou non
    delete = models.BooleanField(default=False)  # pour savoir si la commande a été supprimer de la liste

    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    method_of_payment = models.CharField(choices=METHOD_OF_PAYMENT, max_length=LENGTH_METHOD_OF_PAYMENT)

    def __str__(self):
        return f"Commande-{self.buyer}-{self.product}"


class Delivery(models.Model):
    approximate_duration = models.DurationField()
    actuel_duration = models.DurationField(null=True, blank=True)
    delivered = models.BooleanField(default=False)  # pour savoir si la livraison a bien été faite
    delivery_price = models.IntegerField()
    QR_code = models.URLField(null=True, blank=True)

    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    delivery_man = models.ForeignKey(DeliveryMan, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Livraison-{self.delivery_man}-{self.order}"


class Comment(models.Model):
    """
        Commentaire :
            Cette classe abstraite représente les commentaires d'un acheteur par rapport à un magasin ou un produit
    """
    comment = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Commentaire-{self.buyer}-{self.date}"

    class Meta:
        abstract = True


class Like(models.Model):
    """
        Aimer :
            Cette classe abstraite représente un like d'un acheteur vis-à-vis d'un produit ou un magasin
    """
    date = models.DateTimeField(auto_now_add=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Like-{self.buyer}-{self.date}"

    class Meta:
        abstract = True


class Follow(models.Model):
    """
        Abonné et Abonnement :
            Cette classe représente les abonnements d'un acheteur et les abonnés d'un acheteur
    """
    date = models.DateTimeField(auto_now_add=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f"Follow-{self.buyer}-{self.store}-{self.date}"


class CommentStore(Comment):
    """
        Commentaire par rapport à un magasin ou boutique :
            Cette classe représente la classe de commentaire d'un magasin
    """
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


class CommentProduct(Comment):
    """
        Commentaire par rapport à un produit :
            Cette classe représente la classe de commentaire d'un produit
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class LikeStore(Like):
    """
        Aimer un magasin :
            Cette classe représente le like d'un acheteur vis-à-vis d'un magasin
    """
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


class LikeProduct(Like):
    """
        Aimer un produit :
            Cette classe représente le like d'un acheteur vis-à-vis d'un produit
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class TargetedAdvertising(models.Model):

    """
        Publicité ciblée :
            Il s'agit d'une classe permettant aux vendeurs de faire des publicités ciblée
    """
    nb_buyers = models.IntegerField(default=10)
    start_day = models.DateTimeField()
    end_day = models.DateTimeField()
    min_age = models.IntegerField(null=True)
    max_age = models.IntegerField(null=True)
    first_name_list = models.CharField(blank=True, null=True, max_length=10)  # La liste des prenoms.
    # On lui demandera de les séparer par une virgule (,) ainsi on fera un Split pour récupérer les noms sous forme
    # de liste.
    last_name_list = models.CharField(blank=True, null=True, max_length=10)
    first_name_startswith = models.CharField(blank=True, null=True, max_length=10)  # Liste de caractères
    # pour les debuts de prénom
    last_name_startswith = models.CharField(blank=True, null=True, max_length=10)  # Liste de caractères
    # pour les debuts de nom
    nb_follower = models.IntegerField(null=True, blank=True)  # nombre d'abonnés
    nb_following = models.IntegerField(null=True, blank=True)  # nombre d'abonnements
    year_of_birth = models.IntegerField(
        validators=[MinValueValidator(1923), MaxValueValidator(datetime.date.today().year)], null=True, blank=True
    )
    month_of_birth = models.CharField(choices=MONTH, max_length=10, null=True, blank=True)
    day_of_birth = models.IntegerField(null=True, validators=[MaxValueValidator(31), MinValueValidator(1)], blank=True)
    name_day_of_birth = MultiSelectField(choices=NAME_DAY_OF_BIRTH, null=True, max_length=LENGTH_NAME_DAY_OF_BIRTH, blank=True)
    follow_me = models.BooleanField(null=True, blank=True)
    categories = models.ManyToManyField(Category)
    genre = MultiSelectField(choices=GENRE, default=['H', 'F'], max_length=LENGTH_GENRE)
    device_type = MultiSelectField(
        choices=DEVICE_TYPE, default=['iphone', 'android', 'huawei'], max_length=LENGTH_DEVICE_TYPE
    )
    profession = MultiSelectField(
        choices=PROFESSION, default=['etudiant', 'fonctionnaire', 'commercant'], max_length=LENGTH_PROFESSION
    )
    register_type = MultiSelectField(
        choices=REGISTER_TYPE, default=['google', 'numero', 'email'], max_length=LENGTH_REGISTER_TYPE
    )
    method_of_payment = MultiSelectField(
        choices=METHOD_OF_PAYMENT, default=['OM', 'MM', 'SM'], max_length=LENGTH_METHOD_OF_PAYMENT
    )
    account_type = models.CharField(choices=ACCOUNT_TYPE, default=['buyer'], max_length=LENGTH_ACCOUNT_TYPE)

    seller = models.OneToOneField(Seller, on_delete=models.CASCADE)
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
    countries = models.ManyToManyField(Country, default=None)
    regions = models.ManyToManyField(Region, default=None)
    neighborhoods = models.ManyToManyField(Neighborhood, default=None)

    def __str__(self):
        return f"Publicité-{self.seller}-{self.store}"

