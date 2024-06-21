from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name="Наименование")
    category_description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    product_name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование " "продукта",
    )
    product_description = models.TextField(
        verbose_name="Описание", help_text="Введите описание продукта"
    )
    product_picture = models.ImageField(
        upload_to="picture_product/",
        verbose_name="Изображение",
        help_text="Загрузите фото продукта",
        null=True,
        blank=True,
    )
    product_category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        help_text="Введите цену",
    )

    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )


    def __str__(self):
        return f"{self.product_name}: {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["product_name", "product_category", "price"]
