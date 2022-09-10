from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='contacts',
            field=models.CharField(help_text='Номер телефона, адрес электронной почты или социальной сети', max_length=255),
        ),
    ]