# Generated by Django 3.0.6 on 2020-05-30 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='시작시간')),
                ('end_time', models.DateTimeField(verbose_name='마감시간')),
                ('title', models.CharField(max_length=50, verbose_name='이벤트 이름')),
                ('description', models.TextField(verbose_name='상세')),
            ],
            options={
                'verbose_name': '이벤트 데이터',
                'verbose_name_plural': '이벤트 데이터',
            },
        ),
    ]
