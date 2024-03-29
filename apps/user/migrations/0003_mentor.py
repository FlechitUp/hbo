# Generated by Django 2.2 on 2019-06-05 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_student2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.User')),
                ('is_mentorizing', models.BooleanField(default=False)),
            ],
            bases=('user.user',),
        ),
    ]
