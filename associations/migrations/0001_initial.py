# Generated by Django 2.1.1 on 2018-09-29 23:55

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
            name='Association',
            fields=[
                ('id', models.SlugField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(null=True, upload_to='associations/logos/')),
                ('is_hidden_1A', models.BooleanField(default=False, verbose_name='Cachée aux 1A')),
                ('rank', models.IntegerField(default=0, help_text="Ordre d'apparition dans la liste des associations (ordre alphabétique pour les valeurs égales)")),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('starts_at', models.DateTimeField(auto_now_add=True)),
                ('ends_at', models.DateTimeField(auto_now_add=True)),
                ('max_choice_number', models.PositiveIntegerField(default=1)),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='associations.Association')),
                ('registered_voters', models.ManyToManyField(related_name='allow_to_vote', to=settings.AUTH_USER_MODEL)),
                ('voters', models.ManyToManyField(related_name='has_voted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('starts_at', models.DateTimeField(auto_now_add=True)),
                ('ends_at', models.DateTimeField(auto_now_add=True)),
                ('place', models.TextField()),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='associations.Association')),
                ('participants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('FUNDED', 'Versé'), ('REFUNDED', 'Remboursé')], default='FUNDED', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=200, null=True)),
                ('is_admin_group', models.BooleanField(default=False)),
                ('static_page', models.BooleanField(default=False)),
                ('news', models.BooleanField(default=False)),
                ('marketplace', models.BooleanField(default=False)),
                ('library', models.BooleanField(default=False)),
                ('vote', models.BooleanField(default=False)),
                ('events', models.BooleanField(default=False)),
                ('members', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.SlugField(max_length=200, primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_date', models.DateTimeField(auto_now=True)),
                ('expected_return_date', models.DateTimeField(null=True)),
                ('real_return_date', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('ORDERED', 'Commandé'), ('VALIDATED', 'Validé'), ('DELIVERED', 'Délivré'), ('CANCELLED', 'Annulé'), ('RETURNED', 'Rendu')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Marketplace',
            fields=[
                ('id', models.SlugField(max_length=200, primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(blank=True, default=None, null=True)),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='associations.Association')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewsPhoto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='associations.News')),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='')),
                ('comment', models.TextField()),
                ('number_left', models.PositiveIntegerField(default=1)),
                ('still_in_the_catalogue', models.BooleanField(default=True)),
                ('orderable_online', models.BooleanField(default=True)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='associations.Library')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('ORDERED', 'Commandé'), ('VALIDATED', 'Validé'), ('DELIVERED', 'Délivré'), ('CANCELLED', 'Annulé'), ('REFUNDED', 'Remboursé')], max_length=200)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(blank=True, default=None, null=True)),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='associations.Association')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='')),
                ('comment', models.TextField(null=True)),
                ('number_left', models.IntegerField(default=-1)),
                ('still_in_the_catalogue', models.BooleanField(default=True)),
                ('orderable_online', models.BooleanField(default=True)),
                ('marketplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='associations.Marketplace')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='VoteChoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='associations.Election')),
            ],
        ),
        migrations.AddField(
            model_name='vote',
            name='choices',
            field=models.ManyToManyField(to='associations.VoteChoice'),
        ),
        migrations.AddField(
            model_name='vote',
            name='election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='associations.Election'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='associations.Product'),
        ),
        migrations.AddField(
            model_name='loan',
            name='object',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='associations.Object'),
        ),
        migrations.AddField(
            model_name='loan',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='funding',
            name='marketplace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fundings', to='associations.Marketplace'),
        ),
        migrations.AddField(
            model_name='funding',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='file',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='associations.Page'),
        ),
        migrations.AddField(
            model_name='association',
            name='groups',
            field=models.ManyToManyField(blank=True, to='associations.Group'),
        ),
        migrations.AddField(
            model_name='association',
            name='library',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='associations.Library'),
        ),
        migrations.AddField(
            model_name='association',
            name='marketplace',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='association', to='associations.Marketplace'),
        ),
        migrations.AddField(
            model_name='association',
            name='publication',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='associations.Publication'),
        ),
    ]
