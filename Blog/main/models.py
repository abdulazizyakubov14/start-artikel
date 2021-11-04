from django.db import models

# Create your models here.
from parler.models import TranslatableModel, TranslatedFields
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Category(models.Model):
    name = models.CharField('Katigoriya Nomi',max_length=150)
    slug = models.SlugField('*',max_length=150, unique=True)
    
    class Meta:
        verbose_name = 'Katigoriya'
        verbose_name_plural = 'Katigoriyalar'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:category_detail', kwargs={'category_slug':self.slug})

class Article(models.Model):
    title = models.TextField("Maqola nomi")
    subtitle = RichTextField()
    slug = models.SlugField("*")
    img = models.ImageField("Rasm", upload_to='cat_imgs/',blank=True,null=True)
    category = models.ForeignKey("main.Category", related_name='categoryies' ,on_delete=models.CASCADE)
    author = models.CharField("Maqola aftori", max_length=50)
    date = models.DateField("Joylangan sanasi", auto_now=True,)
    # post_views = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'


    def __str__(self):
        return self.title
