from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField("Katigoriya nomi",max_length=200, db_index=True),
        slug = models.SlugField("Katigoriya slug",max_length=200,db_index=True,unique=True)
    )
    img = models.ImageField("Katigriya rasmi", upload_to='cat_imgs/',)

    # def get_absolute_url(self):
    #     return reverse("main:cat_detail", kwargs={"slug": self.slug})
    

    class Meta:
        verbose_name = 'Katigoriya'
        verbose_name_plural = 'Katigoriyalar'

    def __str__(self):
        return self.name

class Article(TranslatableModel):
    translations = TranslatedFields(
        title = models.TextField("Maqola nomi"),
        subtitle = RichTextField(),
        slug = models.SlugField("*")
    )
    category = models.ForeignKey("main.Category", related_name='categoryies' ,on_delete=models.CASCADE)
    author = models.CharField("Maqola aftori", max_length=50)
    date = models.DateField("Joylangan sanasi", auto_now=True,)
    post_views = models.IntegerField(default=0, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("main:art_detail", kwargs={"art": self.slug})

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'


    def __str__(self):
        return self.title
