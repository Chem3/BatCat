# Generated by Django 3.1.4 on 2020-12-16 19:28

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
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=10, unique=True)),
                ('longname', models.CharField(blank=True, max_length=20, null=True)),
                ('comments', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'analysis',
                'verbose_name_plural': 'analyses',
                'db_table': 'analysis',
            },
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=10, unique=True)),
                ('longname', models.CharField(blank=True, max_length=20, null=True)),
                ('comments', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'container',
                'verbose_name_plural': 'containers',
                'db_table': 'container',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=10, unique=True)),
                ('longname', models.CharField(blank=True, max_length=20, null=True)),
                ('comments', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'material',
                'verbose_name_plural': 'materials',
                'db_table': 'material',
            },
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=10, unique=True)),
                ('longname', models.CharField(blank=True, max_length=20, null=True)),
                ('comments', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'method',
                'verbose_name_plural': 'methods',
                'db_table': 'method',
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=10, unique=True)),
                ('longname', models.CharField(blank=True, max_length=20, null=True)),
                ('comments', models.CharField(blank=True, max_length=128, null=True)),
                ('unit', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'parameter',
                'verbose_name_plural': 'parameters',
                'db_table': 'parameter',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(blank=True, max_length=64, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
                'db_table': 'persons',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=10, unique=True)),
                ('longname', models.CharField(blank=True, max_length=20, null=True)),
                ('comments', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('barcode', models.CharField(max_length=128, unique=True)),
                ('room', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'shelf',
                'verbose_name_plural': 'shelves',
                'db_table': 'shelf',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=10, unique=True)),
                ('longname', models.CharField(blank=True, max_length=20, null=True)),
                ('comments', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'unit',
                'verbose_name_plural': 'units',
                'db_table': 'unit',
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=10, unique=True)),
                ('longname', models.CharField(blank=True, max_length=20, null=True)),
                ('data', models.FloatField()),
                ('comments', models.CharField(blank=True, max_length=128, null=True)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogue.parameter')),
            ],
            options={
                'verbose_name': 'treatment',
                'verbose_name_plural': 'treatments',
                'db_table': 'treatment',
            },
        ),
        migrations.CreateModel(
            name='StorageUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField()),
                ('entry_content', models.TextField()),
                ('entry_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Storage update',
                'verbose_name_plural': 'Storage updates',
                'db_table': 'Storage Update',
            },
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('date', models.DateField()),
                ('production_time', models.FloatField()),
                ('amount', models.FloatField()),
                ('amount_free', models.FloatField()),
                ('barcode', models.CharField(max_length=128, unique=True)),
                ('inert_handling', models.BooleanField()),
                ('comments', models.CharField(blank=True, max_length=256, null=True)),
                ('static_files', models.CharField(blank=True, max_length=256, null=True)),
                ('analysed_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='analysed_user', to='catalogue.person')),
                ('characterisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalogue.analysis')),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogue.container')),
                ('last_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='last_user', to='catalogue.person')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalogue.material')),
                ('method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalogue.method')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogue.project')),
                ('shelf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogue.shelf')),
            ],
            options={
                'verbose_name': 'sample',
                'verbose_name_plural': 'samples',
                'db_table': 'sample',
            },
        ),
        migrations.AddField(
            model_name='method',
            name='treatments',
            field=models.ManyToManyField(to='catalogue.Treatment'),
        ),
    ]