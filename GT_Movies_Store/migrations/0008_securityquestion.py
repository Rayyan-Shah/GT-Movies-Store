# Generated by Django 4.2.18 on 2025-02-04 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GT_Movies_Store', '0007_movie_price_cart_cartitem_order_orderitem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(choices=[('pet', 'What was the name of your first pet?'), ('school', 'What was the name of your first school?'), ('city', 'In what city were you born?')], max_length=50)),
                ('answer', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='security_question', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
