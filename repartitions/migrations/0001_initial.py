# Generated by Django 2.2.3 on 2019-09-14 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(default='CLOSED', max_length=200)),
                ('even', models.BooleanField(default=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='repartitions.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Proposition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('number_of_places', models.IntegerField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repartitions.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='UserCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='repartitions.Campaign')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='users_campaign', to='repartitions.Category')),
                ('fixed_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='repartitions.Proposition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'campaign')},
            },
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rank', models.IntegerField()),
                ('proposition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repartitions.Proposition')),
                ('user_campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishes', to='repartitions.UserCampaign')),
            ],
        ),
    ]
