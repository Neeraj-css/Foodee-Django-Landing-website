from django.db import models

# Create your models here.

class Header(models.Model):
    Title = models.CharField(max_length=50)
    Author_Name = models.CharField(max_length=50)
    Link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Header"
        verbose_name_plural = "Header"

    def __str__(self):
        return self.Title

class About_Us(models.Model):
    Firstcharacter = models.CharField(max_length=1, null=False)
    Paragraph = models.CharField(max_length=1000)
    Get_in_touch = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

class Quote(models.Model):
    Quote = models.CharField(max_length=300)
    Quote_author = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quote"

    def __str__(self):
        return self.Quote_author

class Food_type(models.Model):
    Food_image = models.ImageField(upload_to='image/Food_type')
    Food_title = models.CharField(max_length=100)
    Food_description = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Food Type"
        verbose_name_plural = "Food Type"

    def __str__(self):
        return self.Food_title

class Food_bg(models.Model):
    Food_Background = models.ImageField(upload_to='image/Food_Background')

    class Meta:
        verbose_name = "Food Background"
        verbose_name_plural = "Food Background"

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Food Category"
        verbose_name_plural = "Food Category"

    def __str__(self):
        return self.name

class Food_item(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        verbose_name = "Food Item"
        verbose_name_plural = "Food Item"

    def __str__(self):
        return self.name

class Event(models.Model):
    Event_title = models.CharField(max_length=200)
    Event_date = models.DateField()
    Event_description = models.TextField()
    Event_link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Event"

    def __str__(self):
        return self.Event_title


class Reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    occation = models.CharField(max_length=255)
    date = models.DateField()  # Change to DateField to store in YYYY-MM-DD format
    time = models.CharField(max_length=7)  # Storing time as "HHMM AM/PM"
    message = models.TextField(default='Please Call Back')

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservation"

    def __str__(self):
        return f"Reservation for {self.name} on {self.date}"

class Slide(models.Model):
    image = models.ImageField(upload_to='slides/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description or f'Slide {self.pk}'