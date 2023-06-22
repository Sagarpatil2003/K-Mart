from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_product_category'),
        ('central', '0006_remove_websitesetting_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitesetting',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product_category'),
        ),
    ]
