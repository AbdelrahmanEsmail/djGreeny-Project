

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

# code

from products.models import Product, Brand, Category
import random
from faker import Faker

def seed_category(n):
    fake = Faker()
    images = ['1.png', '2.png', '3.png', '4.png', '5.png',
    '6.png', '7.png', '8.png', '9.png','10.png',
    '11.png', '12.png', '13.png', '14.png','15.png',
    '16.png', '17.png', '18.png', '19.png', '20.png',
    '21.png', '22.png', '23.png', '24.png']
    for _ in range(n):
        name = fake.name()
        image = f"category/{images[random.randint(0, 23)]}"
        Category.objects.create(
            name=name,
            image=image
        )


def seed_brand(n):
    fake = Faker()
    images = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png']
    for _ in range(n):
        name = fake.name()
        image = f"brands/{images[random.randint(0, 5)]}"
        Brand.objects.create(
            name=name,
            image=image,
            category=Category.objects.get(id=random.randint(26,35 ))
        )


def seed_products(n):
    fake = Faker()
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg',
    '6.jpg', '7.jpg', '8.jpg', '9.jpg','10.jpg',
    '11.jpg', '12.jpg', '13.jpg', '14.jpg','15.jpg',
    '16.jpg', '17.jpg', '18.jpg']
    flag_type = ['New', 'Feature', 'Sale']
    for _ in range(n):
        name = fake.name()
        subtitle = fake.text(max_nb_chars=500)
        sku = random.randint(1000, 100000)
        description = fake.text(max_nb_chars=10000)
        price = round(random.uniform(20.99, 99.99), 2)
        image = f"products/{images[random.randint(0, 17)]}"
        flag = flag_type[random.randint(0, 2)]
        quantity = random.randint(1, 100)

        Product.objects.create(
            name=name,
            subtitle=subtitle,
            sku=sku,
            price=price,
            desc=description,
            flag=flag,
            quantity=quantity,
            image=image,
            brand=Brand.objects.get(id=random.randint(30,40)),
            category=Category.objects.get(id=random.randint(26,35)),
        )


# seed_category(10)
# seed_brand(10)
seed_products(1000)
