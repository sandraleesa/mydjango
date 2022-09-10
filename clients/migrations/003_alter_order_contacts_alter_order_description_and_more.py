from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_order_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='contacts',
            field=models.CharField(help_text='Введите Ваш номер телефона, адрес электронной почты или социальной сети', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, help_text='Вы можете добавить описание', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(help_text='Введите Ваше имя', max_length=255),
        ),
    ]