# Generated by Django 3.1.7 on 2023-01-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiContextInit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BILLING_ID', models.CharField(max_length=250)),
                ('BILLING_NAME', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('BILLING_ORG_NAME', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('BILLING_ORG_CRED', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('BILLING_EMAILADDRESS', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('BILLING_PHONE', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('PAYMENT_TRANS_ID', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('PAYMENT_TRANS_STATUS', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('PAYMENT_TRANS_AMT', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('PAYMENT_TRANS_CURRENCY', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('PAYMENT_DATE', models.CharField(blank=True, default=None, max_length=250, null=True)),
            ],
        ),
    ]