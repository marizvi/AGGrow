

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestmandi',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
