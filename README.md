# ckanext-dge-scheming

`ckanext-dge-scheming` es una extensión para CKAN utilizada en la plataforma [datos.gob.es](https://datos.gob.es/) para ampliar el esquema de metadatos mediante *scheming*.

> [!TIP]
> Guía base y contexto del proyecto: https://github.com/datosgobes/datos.gob.es

## Descripción general

- Añade un plugin CKAN para registrar esquemas de metadatos y *presets* personalizados para los perfiles de aplicación [NTI-RISP (2013)](https://datosgobes.github.io/NTI-RISP/) y [DCAT-AP-ES](https://datosgobes.github.io/DCAT-AP-ES/)

## Requisitos

- Una instancia de CKAN.
- Librerías Python adicionales ([`requirements`](requirements.txt))/[`setup.py.install_requires`](setup.py)
- Requiere [`ckanext-dge-harvest`](https://github.com/datosgobes/ckanext-dge-harvest) y [`ckanext-dge-dataservice`](https://github.com/datosgobes/ckanext-dge-dataservice)

### Compatibilidad

Compatibilidad con versiones de CKAN:

| Versión de CKAN | ¿Compatible?                                                              |
|--------------|-----------------------------------------------------------------------------|
| 2.8          | ❌ No (requiere Python 3+)                                                   |
| 2.9          | ✅ Sí                                                                        |
| 2.10         | ❓ Desconocido                                                               |
| 2.11         | ❓ Desconocido                                                               |

## Instalación

```sh
pip install -r requirements.txt
pip install -e .
```

## Configuración

### Plugins

Activa el plugin en tu configuración de CKAN:

```ini
ckan.plugins = … dge_scheming
```

### Configuración en `ckan.ini`

> [!NOTE]
> La configuración específica de [datos.gob.es](https://datos.gob.es/) está documentada en:
> https://github.com/datosgobes/datos.gob.es/blob/master/docs/202512_datosgobes-ckan-doc_es.pdf (sección 3.11).

La documentación operativa de la plataforma muestra una activación conjunta típica de extensiones:

```ini
ckan.plugins = dge_brokenlinks dge dge_dashboard dge_ga_report dge_ga dcat
dge_harvest dge_nti_rdf_harvester dge_dcat_ap_es_rdf_harvester harvest fluent
scheming_datasets dge_dataservice dge_scheming stats report comments
dge_drupal_users
```

Ejemplo de configuración de esquemas y presets:

```ini
# Esquema para conjuntos de datos y distribuciones, así como ckanext-dge-dataservice con el esquema para servicios de datos
scheming.dataset_schemas =
	ckanext.dge_scheming:nti_dge_dataset.yaml
	ckanext.dge_scheming:nti_dge_dataservice.yaml

# Presets especificos para ckanext-dge-scheming
scheming.presets =
	ckanext.scheming:presets.json
	ckanext.fluent:presets.json
	ckanext.dge_scheming:presets.json
```

## Licencia

Este proyecto se distribuye bajo licencia **GNU Affero General Public License (AGPL) v3.0 o posterior**. Consulta el fichero [LICENSE](LICENSE).
