# Generated by Django 4.0.4 on 2022-04-20 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer'),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.trainer'),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
