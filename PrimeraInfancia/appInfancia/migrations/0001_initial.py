# Generated by Django 4.0.3 on 2022-03-04 23:38

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
            name='Alertas',
            fields=[
                ('idalertas', models.AutoField(db_column='idAlertas', primary_key=True, serialize=False)),
                ('nombrealerta', models.CharField(blank=True, db_column='NombreAlerta', max_length=50, null=True)),
                ('gradoalerta', models.IntegerField(blank=True, db_column='GradoAlerta', null=True)),
            ],
            options={
                'db_table': 'alertas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('idbitacora', models.AutoField(db_column='idBitacora', primary_key=True, serialize=False)),
                ('fechacreacion', models.DateTimeField(auto_now_add=True, db_column='FechaCreaRemision')),
                ('usuariocrea', models.IntegerField(blank=True, db_column='UsuarioCrea', null=True)),
                ('observacion', models.CharField(blank=True, db_column='Observacion', max_length=500, null=True)),
            ],
            options={
                'db_table': 'bitacora',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Catalagopregunta',
            fields=[
                ('idpregunta', models.AutoField(db_column='idPregunta', primary_key=True, serialize=False)),
                ('enunciado', models.CharField(blank=True, db_column='Enunciado', max_length=250, null=True)),
                ('codigopregunta', models.IntegerField(blank=True, db_column='CodigoPregunta', null=True)),
            ],
            options={
                'db_table': 'catalagopregunta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Catalogorespuestas',
            fields=[
                ('idcatalogorespuestas', models.AutoField(db_column='idCatalogoRespuestas', primary_key=True, serialize=False)),
                ('tiporespuestas', models.CharField(blank=True, db_column='TipoRespuestas', max_length=45, null=True)),
                ('codigorespuestas', models.IntegerField(blank=True, db_column='CodigoRespuestas', null=True)),
                ('rta_otros', models.CharField(blank=True, db_column='Rta_Otros', max_length=150, null=True)),
                ('catapreg_idpregunta', models.ForeignKey(db_column='CataPreg_idPregunta', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.catalagopregunta')),
            ],
            options={
                'db_table': 'catalogorespuestas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CentroZonal',
            fields=[
                ('idcentro_zonal', models.AutoField(db_column='idCentro_Zonal', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=45)),
            ],
            options={
                'db_table': 'centro_zonal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('idmodulo', models.AutoField(db_column='idModulo', primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True, db_column='Fecha')),
            ],
            options={
                'db_table': 'ficha',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Grupoetnico',
            fields=[
                ('idgrupoetnico', models.IntegerField(db_column='idGrupoEtnico', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=100, null=True)),
            ],
            options={
                'db_table': 'grupoetnico',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Grupofocal',
            fields=[
                ('idgrupofocal', models.AutoField(db_column='idGrupoFocal', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=500, null=True)),
            ],
            options={
                'db_table': 'grupofocal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Lengua',
            fields=[
                ('idlengua', models.IntegerField(db_column='idLengua', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
                ('otralengua', models.CharField(blank=True, db_column='OtraLengua', max_length=45, null=True)),
            ],
            options={
                'db_table': 'lengua',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LenguaHasPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'lengua_has_persona',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('codigodane', models.CharField(db_column='CodigoDANE', max_length=45, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=50, null=True)),
            ],
            options={
                'db_table': 'municipios',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('idpais', models.AutoField(db_column='idPais', primary_key=True, serialize=False)),
                ('codigopais', models.CharField(blank=True, db_column='CodigoPais', max_length=3, null=True)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=20, null=True)),
                ('nacionalidad', models.CharField(blank=True, db_column='Nacionalidad', max_length=20, null=True)),
            ],
            options={
                'db_table': 'nacionalidad',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ong',
            fields=[
                ('idong', models.AutoField(db_column='idONG', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=80, null=True)),
                ('nit', models.IntegerField(blank=True, db_column='NIT', null=True)),
                ('digitoverificacion', models.IntegerField(blank=True, db_column='DigitoVerificacion', null=True)),
                ('representantelegal', models.CharField(blank=True, db_column='RepresentanteLegal', max_length=50, null=True)),
                ('direccion', models.CharField(blank=True, db_column='Direccion', max_length=45, null=True)),
                ('telefono', models.IntegerField(blank=True, db_column='Telefono', null=True)),
                ('correo', models.CharField(blank=True, db_column='Correo', max_length=45, null=True)),
            ],
            options={
                'db_table': 'ong',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('idperfilesroles', models.AutoField(db_column='idPerfilesRoles', primary_key=True, serialize=False)),
                ('codigopero', models.IntegerField(blank=True, db_column='CodigoPERO', null=True)),
                ('nombrepero', models.CharField(blank=True, db_column='NombrePERO', max_length=30, null=True)),
                ('usuariocrea', models.IntegerField(blank=True, db_column='UsuarioCrea', null=True)),
                ('usuariomodifica', models.IntegerField(blank=True, db_column='UsuarioModifica', null=True)),
            ],
            options={
                'db_table': 'perfiles',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('idpersona', models.AutoField(db_column='idPersona', primary_key=True, serialize=False)),
                ('no_documento', models.IntegerField(blank=True, db_column='No_Documento', null=True)),
                ('nombres', models.CharField(db_column='Nombres', max_length=50)),
                ('apellidos', models.CharField(db_column='Apellidos', max_length=50)),
                ('telefono', models.CharField(blank=True, db_column='Telefono', max_length=45, null=True)),
                ('correo', models.CharField(blank=True, db_column='Correo', max_length=45, null=True)),
                ('fecha_nacimiento', models.DateField(db_column='Fecha_Nacimiento')),
                ('Lenguas', models.ManyToManyField(through='appInfancia.LenguaHasPersona', to='appInfancia.lengua')),
                ('cz_idcentro_zonal', models.ForeignKey(db_column='CZ_idCentro_Zonal', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.centrozonal')),
                ('cz_mun_codigodane', models.ForeignKey(db_column='CZ_Mun_CodigoDANE', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.municipios')),
            ],
            options={
                'db_table': 'persona',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Regionales',
            fields=[
                ('idregional', models.AutoField(db_column='idRegional', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=45)),
            ],
            options={
                'verbose_name': 'regional',
                'verbose_name_plural': 'regionales',
                'db_table': 'regionales',
                'ordering': ['nombre'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Remision',
            fields=[
                ('idremision', models.AutoField(db_column='idRemision', primary_key=True, serialize=False)),
                ('fechacrearemision', models.DateTimeField(auto_now_add=True, db_column='FechaCreaRemision')),
                ('usucrearemision', models.IntegerField(blank=True, db_column='UsuCreaRemision', null=True)),
                ('observacion', models.CharField(blank=True, db_column='Observacion', max_length=500, null=True)),
                ('codigoremision', models.CharField(blank=True, db_column='CodigoRemision', max_length=10, null=True)),
                ('idcentro_zonal', models.ForeignKey(db_column='idcentro_zonal', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.centrozonal')),
                ('idpersona', models.ForeignKey(db_column='idpersona', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.persona')),
                ('mun_codigodane', models.ForeignKey(db_column='mun_codigodane', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.municipios')),
            ],
            options={
                'db_table': 'remision',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('idsexo', models.IntegerField(db_column='idSexo', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
            ],
            options={
                'db_table': 'sexo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Subdirecciones',
            fields=[
                ('idsubdirecciones', models.AutoField(db_column='idSubDirecciones', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
                ('lider', models.CharField(blank=True, db_column='Lider', max_length=45, null=True)),
                ('direccion', models.CharField(blank=True, db_column='Direccion', max_length=45, null=True)),
                ('telefono', models.CharField(blank=True, db_column='Telefono', max_length=45, null=True)),
                ('correo', models.CharField(blank=True, db_column='Correo', max_length=45, null=True)),
            ],
            options={
                'db_table': 'subdirecciones',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tipodiscapacidad',
            fields=[
                ('idTipodiscapacidad', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'Tipodiscapacidad',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tipoidentificacio',
            fields=[
                ('idtipoidentificacio', models.IntegerField(db_column='idTipoIdentificacio', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
            ],
            options={
                'db_table': 'tipoidentificacio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoModulo',
            fields=[
                ('idtipo_modulo', models.IntegerField(db_column='idTipo_Modulo', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
            ],
            options={
                'db_table': 'tipo_modulo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FichaHasCatalogorespuestas',
            fields=[
                ('ficha_idmodulo', models.OneToOneField(db_column='Ficha_idModulo', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='appInfancia.ficha')),
            ],
            options={
                'db_table': 'ficha_has_catalogorespuestas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Uds',
            fields=[
                ('iduds', models.AutoField(db_column='idUDS', primary_key=True, serialize=False)),
                ('codigocuentame', models.CharField(db_column='CodigoCuentame', max_length=30)),
                ('nombreagenteeducativo', models.CharField(blank=True, db_column='NombreAgenteEducativo', max_length=50, null=True)),
                ('fechacreacion', models.DateTimeField(blank=True, db_column='FechaCreacion', null=True)),
                ('ong_idong', models.ForeignKey(db_column='ONG_idONG', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.ong')),
            ],
            options={
                'db_table': 'uds',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipodiscapacidadHasPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idTipodiscapacidad', models.ForeignKey(db_column='idTipodiscapacidad', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.tipodiscapacidad')),
                ('idcentro_zonal', models.ForeignKey(db_column='idcentro_zonal', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.centrozonal')),
                ('idpersona', models.ForeignKey(db_column='idpersona', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.persona')),
                ('mun_codigodane', models.ForeignKey(db_column='mun_codigodane', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.municipios')),
            ],
            options={
                'db_table': 'Tipodiscapacidad_has_persona',
                'managed': True,
                'unique_together': {('idTipodiscapacidad', 'idpersona', 'idcentro_zonal', 'mun_codigodane')},
            },
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('idseccion', models.AutoField(db_column='idSeccion', primary_key=True, serialize=False)),
                ('nombreseccion', models.CharField(blank=True, db_column='NombreSeccion', max_length=45, null=True)),
                ('tiposeccion', models.CharField(blank=True, db_column='TipoSeccion', max_length=45, null=True)),
                ('idtipo_modulo', models.ForeignKey(db_column='idtipo_modulo', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.tipomodulo')),
            ],
            options={
                'db_table': 'seccion',
                'managed': True,
                'unique_together': {('idseccion', 'idtipo_modulo')},
            },
        ),
        migrations.CreateModel(
            name='Remisioncatalogo',
            fields=[
                ('idremisioncata', models.AutoField(db_column='idremisioncata', primary_key=True, serialize=False)),
                ('codigo', models.CharField(blank=True, db_column='codigo', max_length=10, null=True)),
                ('tipo', models.CharField(blank=True, db_column='Tipo', max_length=50, null=True)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=50, null=True)),
                ('rem_idremision', models.ForeignKey(db_column='Rem_idRemision', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.remision')),
            ],
            options={
                'db_table': 'remisioncatalogo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('idproyectos', models.AutoField(db_column='idProyectos', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
                ('fechafin', models.DateField(blank=True, db_column='FechaFin', null=True)),
                ('fechainicio', models.DateField(blank=True, db_column='FechaInicio', null=True)),
                ('descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=500, null=True)),
                ('no_beneficiarios', models.IntegerField(blank=True, db_column='No_Beneficiarios', null=True)),
                ('tipo_proyecto', models.IntegerField(blank=True, db_column='Tipo_Proyecto', null=True)),
                ('gf_idgrupofocal', models.ForeignKey(db_column='GF_idGrupoFocal', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.grupofocal')),
                ('idsubdirecciones', models.ForeignKey(db_column='idsubdirecciones', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.subdirecciones')),
                ('ong_idong', models.ForeignKey(db_column='ONG_idONG', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.ong')),
            ],
            options={
                'db_table': 'proyectos',
                'managed': True,
                'unique_together': {('idproyectos', 'idsubdirecciones', 'gf_idgrupofocal')},
            },
        ),
        migrations.AddField(
            model_name='persona',
            name='discapacidad',
            field=models.ManyToManyField(through='appInfancia.TipodiscapacidadHasPersona', to='appInfancia.tipodiscapacidad'),
        ),
        migrations.AddField(
            model_name='persona',
            name='ge_idgrupoetnico',
            field=models.OneToOneField(db_column='GE_idGrupoEtnico', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.grupoetnico'),
        ),
        migrations.AddField(
            model_name='persona',
            name='nacionalidad_idpais',
            field=models.ForeignKey(db_column='Nacionalidad_idPais', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.nacionalidad'),
        ),
        migrations.AddField(
            model_name='persona',
            name='sexo_idsexo',
            field=models.OneToOneField(db_column='Sexo_idSexo', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.sexo'),
        ),
        migrations.AddField(
            model_name='persona',
            name='tipoid_idtipoidentificacio',
            field=models.OneToOneField(db_column='TipoId_idTipoIdentificacio', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.tipoidentificacio'),
        ),
        migrations.AddField(
            model_name='municipios',
            name='reg_idregional',
            field=models.ForeignKey(db_column='Reg_idRegional', on_delete=django.db.models.deletion.PROTECT, to='appInfancia.regionales'),
        ),
        migrations.AddField(
            model_name='lenguahaspersona',
            name='idpersona',
            field=models.ForeignKey(db_column='idpersona', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.persona'),
        ),
        migrations.AddField(
            model_name='lenguahaspersona',
            name='len_idlengua',
            field=models.ForeignKey(db_column='Len_idLengua', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.lengua'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='idpersona',
            field=models.ForeignKey(db_column='idpersona', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.persona'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='respuestas',
            field=models.ManyToManyField(through='appInfancia.FichaHasCatalogorespuestas', to='appInfancia.catalogorespuestas'),
        ),
        migrations.AddField(
            model_name='centrozonal',
            name='mun_codigodane',
            field=models.ForeignKey(db_column='Mun_CodigoDANE', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.municipios'),
        ),
        migrations.AddField(
            model_name='catalogorespuestas',
            name='idseccion',
            field=models.ForeignKey(db_column='idseccion', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.seccion'),
        ),
        migrations.AddField(
            model_name='catalogorespuestas',
            name='sec_idtipo_modulo',
            field=models.ForeignKey(db_column='sec_idtipo_modulo', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.tipomodulo'),
        ),
        migrations.AddField(
            model_name='catalagopregunta',
            name='sec_idseccion',
            field=models.ForeignKey(db_column='Sec_idSeccion', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.seccion'),
        ),
        migrations.AddField(
            model_name='catalagopregunta',
            name='sec_idtipo_modulo',
            field=models.ForeignKey(db_column='Sec_idtipo_modulo', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.tipomodulo'),
        ),
        migrations.CreateModel(
            name='BitacoraHasAlertas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_idalertas', models.ForeignKey(db_column='Alert_idAlertas', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.alertas')),
                ('bita_idbitacora', models.ForeignKey(db_column='Bita_idBitacora', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.bitacora')),
            ],
            options={
                'db_table': 'bitacora_has_alertas',
                'managed': True,
                'unique_together': {('bita_idbitacora', 'alert_idalertas')},
            },
        ),
        migrations.AddField(
            model_name='bitacora',
            name='alertas',
            field=models.ManyToManyField(through='appInfancia.BitacoraHasAlertas', to='appInfancia.alertas'),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='idcentro_zonal',
            field=models.ForeignKey(db_column='idcentro_zonal', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.centrozonal'),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='idpersona',
            field=models.ForeignKey(db_column='idpersona', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.persona'),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='mun_codigodane',
            field=models.ForeignKey(db_column='mun_codigodane', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.municipios'),
        ),
        migrations.AlterUniqueTogether(
            name='persona',
            unique_together={('idpersona', 'cz_idcentro_zonal', 'cz_mun_codigodane')},
        ),
        migrations.AlterUniqueTogether(
            name='lenguahaspersona',
            unique_together={('len_idlengua', 'idpersona')},
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_docid', models.CharField(choices=[('1', 'CC'), ('2', 'CE'), ('3', 'PASAPORTE'), ('4', 'NIT')], max_length=1)),
                ('NoDocumento', models.TextField(blank=True, max_length=500)),
                ('FechaNacimiento', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=60)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'funcionario',
                'managed': True,
                'unique_together': {('user', 'name')},
            },
        ),
        migrations.AddField(
            model_name='fichahascatalogorespuestas',
            name='catapreg_idpregunta',
            field=models.ForeignKey(db_column='catapreg_idpregunta', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.catalagopregunta'),
        ),
        migrations.AddField(
            model_name='fichahascatalogorespuestas',
            name='catares_idseccion',
            field=models.ForeignKey(db_column='CataRes_idseccion', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.seccion'),
        ),
        migrations.AddField(
            model_name='fichahascatalogorespuestas',
            name='catares_sec_idtipo_modulo',
            field=models.ForeignKey(db_column='CataRes_sec_idtipo_modulo', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.tipomodulo'),
        ),
        migrations.AddField(
            model_name='fichahascatalogorespuestas',
            name='idcatalogorespuestas',
            field=models.ForeignKey(db_column='idcatalogorespuestas', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.catalogorespuestas'),
        ),
        migrations.AlterUniqueTogether(
            name='centrozonal',
            unique_together={('idcentro_zonal', 'mun_codigodane')},
        ),
        migrations.AlterUniqueTogether(
            name='catalogorespuestas',
            unique_together={('idcatalogorespuestas', 'catapreg_idpregunta', 'idseccion', 'sec_idtipo_modulo')},
        ),
        migrations.AlterUniqueTogether(
            name='catalagopregunta',
            unique_together={('idpregunta', 'sec_idseccion', 'sec_idtipo_modulo')},
        ),
        migrations.AlterUniqueTogether(
            name='bitacora',
            unique_together={('idbitacora', 'idpersona', 'idcentro_zonal', 'mun_codigodane')},
        ),
        migrations.CreateModel(
            name='ProyectosHasUsuario',
            fields=[
                ('idproyectos', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='appInfancia.proyectos')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('idgrupofocal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.grupofocal')),
                ('idsubdirecciones', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.subdirecciones')),
            ],
            options={
                'db_table': 'proyectos_has_usuarios',
                'managed': True,
                'unique_together': {('idproyectos', 'idsubdirecciones', 'idgrupofocal')},
            },
        ),
        migrations.CreateModel(
            name='PersonaHasGrupofocal',
            fields=[
                ('idpersona', models.OneToOneField(db_column='idpersona', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='appInfancia.persona')),
                ('gf_idgrupofocal', models.ForeignKey(db_column='GF_idGrupoFocal', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.grupofocal')),
                ('idcentro_zonal', models.ForeignKey(db_column='idcentro_zonal', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.centrozonal')),
                ('mun_codigodane', models.ForeignKey(db_column='mun_codigodane', on_delete=django.db.models.deletion.DO_NOTHING, to='appInfancia.municipios')),
            ],
            options={
                'db_table': 'persona_has_grupofocal',
                'managed': True,
                'unique_together': {('idpersona', 'mun_codigodane', 'gf_idgrupofocal')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='fichahascatalogorespuestas',
            unique_together={('ficha_idmodulo', 'idcatalogorespuestas', 'catapreg_idpregunta', 'catares_idseccion', 'catares_sec_idtipo_modulo')},
        ),
    ]