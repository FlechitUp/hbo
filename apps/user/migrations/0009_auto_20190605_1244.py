# Generated by Django 2.2 on 2019-06-05 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20190605_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='team_students',
        ),
        migrations.AddField(
            model_name='students_mentor',
            name='studentB',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentB', to='user.Student2'),
        ),
        migrations.AlterField(
            model_name='students_mentor',
            name='studentA',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentA', to='user.Student2'),
        ),
    ]
