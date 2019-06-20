# Generated by Django 2.2 on 2019-06-20 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0012_user_last_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('number_phone', models.IntegerField(blank='False', null='True')),
                ('github', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='courses_student',
            name='course',
        ),
        migrations.RemoveField(
            model_name='courses_student',
            name='student2',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='student2',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='students_mentor',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='students_mentor',
            name='program',
        ),
        migrations.RemoveField(
            model_name='students_mentor',
            name='studentA',
        ),
        migrations.RemoveField(
            model_name='students_mentor',
            name='studentB',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Courses_Student',
        ),
        migrations.DeleteModel(
            name='Mentor',
        ),
        migrations.DeleteModel(
            name='Program',
        ),
        migrations.DeleteModel(
            name='Student2',
        ),
        migrations.DeleteModel(
            name='Students_Mentor',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
