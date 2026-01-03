# Copyright (C) 2025 Entidad Pública Empresarial Red.es
#
# This file is part of "dge-scheming (datos.gob.es)".
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


ISO_639_LANGUAGE = '^[a-z][a-z][a-z]?[a-z]?$'
FREQUENCY_VALUES = ["days", "weeks", "months",
                    "years", "hours", "minutes", "seconds", "uri"]
DEFAULT_TITLE_FIELD = 'title_translated'
DEFAULT_LANGUAGE = 'es'
MEDIATYPEOREXTENT_IDENTIFIER_KEY = 'mediatypeorextent_identifer'
FORMAT_PREFIX_EDP_IANA = 'https://www.iana.org/assignments/media-types/'
PUBLISHER_URI_KEY = ('publisher_uri',)
LICENSE_KEY = ('license_id',)
DATASET_LICENSE_TMP = ('dataset_license_tmp',)
RESOURCE_KEY = 'resources'
RESOURCE_LICENSE_KEY = 'resource_license'
MEDIA_TYPE_KEY = 'media_type'
ACCESS_URL_KEY = 'access_url'
URL_KEY = 'url'
IDENTIFIER_KEY = ('identifier',)
APPLICATION_PROFILE_KEY = 'application_profile'
DCATAPES_100 = 'dcatapes_100'
NTI = 'nti'
DATOSGOBES_THEME_PREFIX = 'http://datos.gob.es/kos/sector-publico/sector/'
FREQUENCY_EUROPEAN_PREFIX = 'http://publications.europa.eu/resource/authority/frequency/'

# Constants for schema fields choices
NTI_CHOICES_FIELD_LANGUAGE = 'language'
NTI_CHOICES_FIELD_SPATIAL = 'spatial'
NTI_CHOICES_FIELD_THEME = 'theme'
NTI_CHOICES_FIELD_FREQUENCY = 'frequency'
NTI_DCT_LANGUAGES_CHOICES = [
  {
    'label': {
      'en': 'Spanish',
      'es': 'Español',
      'ca': 'Espanyol',
      'gl': 'Español',
      'eu': 'Espainiera',
    },
    'value': 'http://publications.europa.eu/resource/authority/language/SPA'
  },
  {
    'label': {
      'en': 'Catalan',
      'es': 'Catalán',
      'ca': 'Català',
      'gl': 'Catalán',
      'eu': 'Katalana',
    },
    'value': 'http://publications.europa.eu/resource/authority/language/CAT'
  },
  {
    'label': {
      'en': 'Galician',
      'es': 'Gallego',
      'ca': 'Gallec',
      'gl': 'Galego',
      'eu': 'Galegoa',
    },
    'value': 'http://publications.europa.eu/resource/authority/language/GLG'
  },
  {
    'label': {
      'en': 'Basque',
      'es': 'Euskera',
      'ca': 'Eusquera',
      'gl': 'Éuscaro',
      'eu': 'Euskara',
    },
    'value': 'http://publications.europa.eu/resource/authority/language/EUS'
  },
  {
    'label': {
      'en': 'English',
      'es': 'Inglés',
      'ca': 'Anglès',
      'gl': 'Inglés',
      'eu': 'Ingelesa',
    },
    'value': 'http://publications.europa.eu/resource/authority/language/ENG'
  }
]

DATOSGOB_DCT_SPATIAL_CHOICES = [
  {
    "label": {
      "es": "Espa\u00F1a",
      "en": "Spain",
      "ca": "Espa\u00F1a",
      "gl": "Espa\u00F1a",
      "eu": "Espa\u00F1a"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Pais/Espa\u00F1a"
  },
  {
    "label": {
      "es": "Andaluc\u00EDa",
      "en": "Andaluc\u00EDa",
      "ca": "Andaluc\u00EDa",
      "gl": "Andaluc\u00EDa",
      "eu": "Andaluc\u00EDa"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Andalucia"
  },
  {
    "label": {
      "es": "Almer\u00EDa",
      "en": "Almer\u00EDa",
      "ca": "Almer\u00EDa",
      "gl": "Almer\u00EDa",
      "eu": "Almer\u00EDa"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Almeria"
  },
  {
    "label": {
      "es": "C\u00E1diz",
      "en": "C\u00E1diz",
      "ca": "C\u00E1diz",
      "gl": "C\u00E1diz",
      "eu": "C\u00E1diz"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Cadiz"
  },
  {
    "label": {
      "es": "C\u00F3rdoba",
      "en": "C\u00F3rdoba",
      "ca": "C\u00F3rdoba",
      "gl": "C\u00F3rdoba",
      "eu": "C\u00F3rdoba"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Cordoba"
  },
  {
    "label": {
      "es": "Granada",
      "en": "Granada",
      "ca": "Granada",
      "gl": "Granada",
      "eu": "Granada"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Granada"
  },
  {
    "label": {
      "es": "Huelva",
      "en": "Huelva",
      "ca": "Huelva",
      "gl": "Huelva",
      "eu": "Huelva"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Huelva"
  },
  {
    "label": {
      "es": "Ja\u00E9n",
      "en": "Ja\u00E9n",
      "ca": "Ja\u00E9n",
      "gl": "Ja\u00E9n",
      "eu": "Ja\u00E9n"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Jaen"
  },
  {
    "label": {
      "es": "M\u00E1laga",
      "en": "M\u00E1laga",
      "ca": "M\u00E1laga",
      "gl": "M\u00E1laga",
      "eu": "M\u00E1laga"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Malaga"
  },
  {
    "label": {
      "es": "Sevilla",
      "en": "Sevilla",
      "ca": "Sevilla",
      "gl": "Sevilla",
      "eu": "Sevilla"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Sevilla"
  },
  {
    "label": {
      "es": "Arag\u00F3n",
      "en": "Arag\u00F3n",
      "ca": "Arag\u00F3n",
      "gl": "Arag\u00F3n",
      "eu": "Arag\u00F3n"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Aragon"
  },
  {
    "label": {
      "es": "Huesca",
      "en": "Huesca",
      "ca": "Huesca",
      "gl": "Huesca",
      "eu": "Huesca"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Huesca"
  },
  {
    "label": {
      "es": "Teruel",
      "en": "Teruel",
      "ca": "Teruel",
      "gl": "Teruel",
      "eu": "Teruel"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Teruel"
  },
  {
    "label": {
      "es": "Zaragoza",
      "en": "Zaragoza",
      "ca": "Zaragoza",
      "gl": "Zaragoza",
      "eu": "Zaragoza"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Zaragoza"
  },
  {
    "label": {
      "es": "Principado de Asturias",
      "en": "Principado de Asturias",
      "ca": "Principado de Asturias",
      "gl": "Principado de Asturias",
      "eu": "Principado de Asturias"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Principado-Asturias"
  },
  {
    "label": {
      "es": "Asturias",
      "en": "Asturias",
      "ca": "Asturias",
      "gl": "Asturias",
      "eu": "Asturias"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Asturias"
  },
  {
    "label": {
      "es": "Illes Balears",
      "en": "Illes Balears",
      "ca": "Illes Balears",
      "gl": "Illes Balears",
      "eu": "Illes Balears"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Illes-Balears"
  },
  {
    "label": {
      "es": "Provincia de Illes Balears",
      "en": "Provincia de Illes Balears",
      "ca": "Provincia de Illes Balears",
      "gl": "Provincia de Illes Balears",
      "eu": "Provincia de Illes Balears"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Illes-Balears"
  },
  {
    "label": {
      "es": "Canarias",
      "en": "Canarias",
      "ca": "Canarias",
      "gl": "Canarias",
      "eu": "Canarias"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Canarias"
  },
  {
    "label": {
      "es": "Las Palmas",
      "en": "Las Palmas",
      "ca": "Las Palmas",
      "gl": "Las Palmas",
      "eu": "Las Palmas"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Las-Palmas"
  },
  {
    "label": {
      "es": "Santa Cruz de Tenerife",
      "en": "Santa Cruz de Tenerife",
      "ca": "Santa Cruz de Tenerife",
      "gl": "Santa Cruz de Tenerife",
      "eu": "Santa Cruz de Tenerife"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Santa-Cruz-Tenerife"
  },
  {
    "label": {
      "es": "Cantabria",
      "en": "Cantabria",
      "ca": "Cantabria",
      "gl": "Cantabria",
      "eu": "Cantabria"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Cantabria"
  },
  {
    "label": {
      "es": "Provincia de Cantabria",
      "en": "Provincia de Cantabria",
      "ca": "Provincia de Cantabria",
      "gl": "Provincia de Cantabria",
      "eu": "Provincia de Cantabria"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Cantabria"
  },
  {
    "label": {
      "es": "Castilla y Le\u00F3n",
      "en": "Castilla y Le\u00F3n",
      "ca": "Castilla y Le\u00F3n",
      "gl": "Castilla y Le\u00F3n",
      "eu": "Castilla y Le\u00F3n"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Castilla-Leon"
  },
  {
    "label": {
      "es": "\u00C1vila",
      "en": "\u00C1vila",
      "ca": "\u00C1vila",
      "gl": "\u00C1vila",
      "eu": "\u00C1vila"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Avila"
  },
  {
    "label": {
      "es": "Burgos",
      "en": "Burgos",
      "ca": "Burgos",
      "gl": "Burgos",
      "eu": "Burgos"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Burgos"
  },
  {
    "label": {
      "es": "Le\u00F3n",
      "en": "Le\u00F3n",
      "ca": "Le\u00F3n",
      "gl": "Le\u00F3n",
      "eu": "Le\u00F3n"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Leon"
  },
  {
    "label": {
      "es": "Palencia",
      "en": "Palencia",
      "ca": "Palencia",
      "gl": "Palencia",
      "eu": "Palencia"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Palencia"
  },
  {
    "label": {
      "es": "Salamanca",
      "en": "Salamanca",
      "ca": "Salamanca",
      "gl": "Salamanca",
      "eu": "Salamanca"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Salamanca"
  },
  {
    "label": {
      "es": "Segovia",
      "en": "Segovia",
      "ca": "Segovia",
      "gl": "Segovia",
      "eu": "Segovia"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Segovia"
  },
  {
    "label": {
      "es": "Soria",
      "en": "Soria",
      "ca": "Soria",
      "gl": "Soria",
      "eu": "Soria"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Soria"
  },
  {
    "label": {
      "es": "Valladolid",
      "en": "Valladolid",
      "ca": "Valladolid",
      "gl": "Valladolid",
      "eu": "Valladolid"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Valladolid"
  },
  {
    "label": {
      "es": "Zamora",
      "en": "Zamora",
      "ca": "Zamora",
      "gl": "Zamora",
      "eu": "Zamora"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Zamora"
  },
  {
    "label": {
      "es": "Castilla-La Mancha",
      "en": "Castilla-La Mancha",
      "ca": "Castilla-La Mancha",
      "gl": "Castilla-La Mancha",
      "eu": "Castilla-La Mancha"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Castilla-La-Mancha"
  },
  {
    "label": {
      "es": "Albacete",
      "en": "Albacete",
      "ca": "Albacete",
      "gl": "Albacete",
      "eu": "Albacete"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Albacete"
  },
  {
    "label": {
      "es": "Ciudad Real",
      "en": "Ciudad Real",
      "ca": "Ciudad Real",
      "gl": "Ciudad Real",
      "eu": "Ciudad Real"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Ciudad-Real"
  },
  {
    "label": {
      "es": "Cuenca",
      "en": "Cuenca",
      "ca": "Cuenca",
      "gl": "Cuenca",
      "eu": "Cuenca"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Cuenca"
  },
  {
    "label": {
      "es": "Guadalajara",
      "en": "Guadalajara",
      "ca": "Guadalajara",
      "gl": "Guadalajara",
      "eu": "Guadalajara"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Guadalajara"
  },
  {
    "label": {
      "es": "Toledo",
      "en": "Toledo",
      "ca": "Toledo",
      "gl": "Toledo",
      "eu": "Toledo"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Toledo"
  },
  {
    "label": {
      "es": "Catalu\u00F1a",
      "en": "Catalu\u00F1a",
      "ca": "Catalu\u00F1a",
      "gl": "Catalu\u00F1a",
      "eu": "Catalu\u00F1a"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Cataluna"
  },
  {
    "label": {
      "es": "Barcelona",
      "en": "Barcelona",
      "ca": "Barcelona",
      "gl": "Barcelona",
      "eu": "Barcelona"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Barcelona"
  },
  {
    "label": {
      "es": "Girona",
      "en": "Girona",
      "ca": "Girona",
      "gl": "Girona",
      "eu": "Girona"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Girona"
  },
  {
    "label": {
      "es": "Lleida",
      "en": "Lleida",
      "ca": "Lleida",
      "gl": "Lleida",
      "eu": "Lleida"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Lleida"
  },
  {
    "label": {
      "es": "Tarragona",
      "en": "Tarragona",
      "ca": "Tarragona",
      "gl": "Tarragona",
      "eu": "Tarragona"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Tarragona"
  },
  {
    "label": {
      "es": "Comunitat Valenciana",
      "en": "Comunitat Valenciana",
      "ca": "Comunitat Valenciana",
      "gl": "Comunitat Valenciana",
      "eu": "Comunitat Valenciana"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Comunitat-Valenciana"
  },
  {
    "label": {
      "es": "Alicante",
      "en": "Alicante",
      "ca": "Alicante",
      "gl": "Alicante",
      "eu": "Alicante"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Alicante"
  },
  {
    "label": {
      "es": "Castell\u00F3n",
      "en": "Castell\u00F3n",
      "ca": "Castell\u00F3n",
      "gl": "Castell\u00F3n",
      "eu": "Castell\u00F3n"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Castellon"
  },
  {
    "label": {
      "es": "Valencia",
      "en": "Valencia",
      "ca": "Valencia",
      "gl": "Valencia",
      "eu": "Valencia"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Valencia"
  },
  {
    "label": {
      "es": "Extremadura",
      "en": "Extremadura",
      "ca": "Extremadura",
      "gl": "Extremadura",
      "eu": "Extremadura"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Extremadura"
  },
  {
    "label": {
      "es": "Badajoz",
      "en": "Badajoz",
      "ca": "Badajoz",
      "gl": "Badajoz",
      "eu": "Badajoz"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Badajoz"
  },
  {
    "label": {
      "es": "C\u00E1ceres",
      "en": "C\u00E1ceres",
      "ca": "C\u00E1ceres",
      "gl": "C\u00E1ceres",
      "eu": "C\u00E1ceres"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Caceres"
  },
  {
    "label": {
      "es": "Galicia",
      "en": "Galicia",
      "ca": "Galicia",
      "gl": "Galicia",
      "eu": "Galicia"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Galicia"
  },
  {
    "label": {
      "es": "A Coru\u00F1a",
      "en": "A Coru\u00F1a",
      "ca": "A Coru\u00F1a",
      "gl": "A Coru\u00F1a",
      "eu": "A Coru\u00F1a"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/A-Coruna"
  },
  {
    "label": {
      "es": "Lugo",
      "en": "Lugo",
      "ca": "Lugo",
      "gl": "Lugo",
      "eu": "Lugo"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Lugo"
  },
  {
    "label": {
      "es": "Ourense",
      "en": "Ourense",
      "ca": "Ourense",
      "gl": "Ourense",
      "eu": "Ourense"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Ourense"
  },
  {
    "label": {
      "es": "Pontevedra",
      "en": "Pontevedra",
      "ca": "Pontevedra",
      "gl": "Pontevedra",
      "eu": "Pontevedra"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Pontevedra"
  },
  {
    "label": {
      "es": "Comunidad de Madrid",
      "en": "Comunidad de Madrid",
      "ca": "Comunidad de Madrid",
      "gl": "Comunidad de Madrid",
      "eu": "Comunidad de Madrid"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Comunidad-Madrid"
  },
  {
    "label": {
      "es": "Madrid",
      "en": "Madrid",
      "ca": "Madrid",
      "gl": "Madrid",
      "eu": "Madrid"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Madrid"
  },
  {
    "label": {
      "es": "Regi\u00F3n de Murcia",
      "en": "Regi\u00F3n de Murcia",
      "ca": "Regi\u00F3n de Murcia",
      "gl": "Regi\u00F3n de Murcia",
      "eu": "Regi\u00F3n de Murcia"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Region-Murcia"
  },
  {
    "label": {
      "es": "Murcia",
      "en": "Murcia",
      "ca": "Murcia",
      "gl": "Murcia",
      "eu": "Murcia"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Murcia"
  },
  {
    "label": {
      "es": "C. Foral de Navarra",
      "en": "C. Foral de Navarra",
      "ca": "C. Foral de Navarra",
      "gl": "C. Foral de Navarra",
      "eu": "C. Foral de Navarra"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Comunidad-Foral-Navarra"
  },
  {
    "label": {
      "es": "Navarra",
      "en": "Navarra",
      "ca": "Navarra",
      "gl": "Navarra",
      "eu": "Navarra"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Navarra"
  },
  {
    "label": {
      "es": "Pa\u00EDs Vasco",
      "en": "Pa\u00EDs Vasco",
      "ca": "Pa\u00EDs Vasco",
      "gl": "Pa\u00EDs Vasco",
      "eu": "Pa\u00EDs Vasco"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Pais-Vasco"
  },
  {
    "label": {
      "es": "\u00C1lava",
      "en": "\u00C1lava",
      "ca": "\u00C1lava",
      "gl": "\u00C1lava",
      "eu": "\u00C1lava"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Alava"
  },
  {
    "label": {
      "es": "Guip\u00FAzcoa",
      "en": "Guip\u00FAzcoa",
      "ca": "Guip\u00FAzcoa",
      "gl": "Guip\u00FAzcoa",
      "eu": "Guip\u00FAzcoa"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Guipuzcoa"
  },
  {
    "label": {
      "es": "Vizcaya",
      "en": "Vizcaya",
      "ca": "Vizcaya",
      "gl": "Vizcaya",
      "eu": "Vizcaya"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Vizcaya"
  },
  {
    "label": {
      "es": "La Rioja",
      "en": "La Rioja",
      "ca": "La Rioja",
      "gl": "La Rioja",
      "eu": "La Rioja"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/La-Rioja"
  },
  {
    "label": {
      "es": "Provincia de La Rioja",
      "en": "Provincia de La Rioja",
      "ca": "Provincia de La Rioja",
      "gl": "Provincia de La Rioja",
      "eu": "Provincia de La Rioja"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/La-Rioja"
  },
  {
    "label": {
      "es": "Ceuta",
      "en": "Ceuta",
      "ca": "Ceuta",
      "gl": "Ceuta",
      "eu": "Ceuta"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Ceuta"
  },
  {
    "label": {
      "es": "Provincia de Ceuta",
      "en": "Provincia de Ceuta",
      "ca": "Provincia de Ceuta",
      "gl": "Provincia de Ceuta",
      "eu": "Provincia de Ceuta"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Ceuta"
  },
  {
    "label": {
      "es": "Melilla",
      "en": "Melilla",
      "ca": "Melilla",
      "gl": "Melilla",
      "eu": "Melilla"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Autonomia/Melilla"
  },
  {
    "label": {
      "es": "Provincia de Melilla",
      "en": "Provincia de Melilla",
      "ca": "Provincia de Melilla",
      "gl": "Provincia de Melilla",
      "eu": "Provincia de Melilla"
    },
    "value": "http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Melilla"
  }
]

DATOSGOB_DCT_THEME_CHOICES = [
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/ciencia-tecnologia",
    "notation": "ciencia-tecnologia",
    "label": {
      "en": "Science and technology",
      "es": "Ciencia y tecnolog\u00EDa",
      "ca": "Ci\u00E8ncia i tecnologia",
      "gl": "Ciencia e tecnolox\u00EDa",
      "eu": "Zientzia eta teknologia"
    },
    "description": {
      "en": "",
      "es": "Incluye: Innovaci\u00F3n, Investigaci\u00F3n, I/u002BD/u002BI, Telecomunicaciones, Inernet y Sociedad de la Informaci\u00F3n.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/TECH"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/comercio",
    "notation": "comercio",
    "label": {
      "en": "Commerce",
      "es": "Comercio",
      "ca": "Comer\u00E7",
      "gl": "Comercio",
      "eu": "Merkataritza"
    },
    "description": {
      "en": "",
      "es": "Incluye: Consumo.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/ECON"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/cultura-ocio",
    "notation": "cultura-ocio",
    "label": {
      "en": "Culture and leisure",
      "es": "Cultura y ocio",
      "ca": "Cultura i lleure",
      "gl": "Cultura e lecer",
      "eu": "Kultura eta aisia"
    },
    "description": {
      "en": "",
      "es": "Incluye: Tiempo libre.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/EDUC"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/demografia",
    "notation": "demografia",
    "label": {
      "en": "Demography",
      "es": "Demograf\u00EDa",
      "ca": "Demografia",
      "gl": "Demograf\u00EDa",
      "eu": "Demografia"
    },
    "description": {
      "en": "",
      "es": "Incluye: Inmigraci\u00F3n y Emigraci\u00F3n, Familia, Mujeres, Infancia, Mayores, Padr\u00F3n.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/SOCI"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/deporte",
    "notation": "deporte",
    "label": {
      "en": "Sport",
      "es": "Deporte",
      "ca": "Esport",
      "gl": "Deporte",
      "eu": "Kirola"
    },
    "description": {
      "en": "",
      "es": "Incluye: Instalaciones deportivas, Federaciones, Competiciones.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/EDUC"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/economia",
    "notation": "economia",
    "label": {
      "en": "Economy",
      "es": "Econom\u00EDa",
      "ca": "Economia",
      "gl": "Econom\u00EDa",
      "eu": "Ekonomia"
    },
    "description": {
      "en": "",
      "es": "Incluye: Deuda, Moneda y Banca y finanzas.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/ECON"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/educacion",
    "notation": "educacion",
    "label": {
      "en": "Education",
      "es": "Educaci\u00F3n",
      "ca": "Educaci\u00F3",
      "gl": "Educaci\u00F3n",
      "eu": "Hezkuntza"
    },
    "description": {
      "en": "",
      "es": "Incluye: Formaci\u00F3n.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/EDUC"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/empleo",
    "notation": "empleo",
    "label": {
      "en": "Employment",
      "es": "Empleo",
      "ca": "Ocupaci\u00F3",
      "gl": "Emprego",
      "eu": "Enplegua"
    },
    "description": {
      "en": "",
      "es": "Incluye: Trabajo, Mercado laboral.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/ECON"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/energia",
    "notation": "energia",
    "label": {
      "en": "Energy",
      "es": "Energ\u00EDa",
      "ca": "Energia",
      "gl": "Enerx\u00EDa",
      "eu": "Energia"
    },
    "description": {
      "en": "",
      "es": "Incluye: Fuentes renovables.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/ENER"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/hacienda",
    "notation": "hacienda",
    "label": {
      "en": "Treasury",
      "es": "Hacienda",
      "ca": "Hisenda",
      "gl": "Facenda",
      "eu": "Ogasuna"
    },
    "description": {
      "en": "",
      "es": "Incluye: Impuestos.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/GOVE"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/industria",
    "notation": "industria",
    "label": {
      "en": "Industry",
      "es": "Industria",
      "ca": "Ind\u00FAstria",
      "gl": "Industria",
      "eu": "Industria"
    },
    "description": {
      "en": "",
      "es": "Incluye: Miner\u00EDa.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/ECON"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/legislacion-justicia",
    "notation": "legislacion-justicia",
    "label": {
      "en": "Legislation and justice",
      "es": "Legislaci\u00F3n y justicia",
      "ca": "Legislaci\u00F3 i just\u00EDcia",
      "gl": "Lexislaci\u00F3n e xustiza",
      "eu": "Legegintza eta justizia"
    },
    "description": {
      "en": "",
      "es": "Incluye: Registros.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/JUST"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/medio-ambiente",
    "notation": "medio-ambiente",
    "label": {
      "en": "Environment",
      "es": "Medio ambiente",
      "ca": "Medi ambient",
      "gl": "Medio ambiente",
      "eu": "Ingurumena"
    },
    "description": {
      "en": "",
      "es": "Incluye: Meteorolog\u00EDa, Geograf\u00EDa, Conservaci\u00F3n fauna y flora.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/ENVI"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/medio-rural-pesca",
    "notation": "medio-rural-pesca",
    "label": {
      "en": "Rural environment",
      "es": "Medio Rural",
      "ca": "Medi rural",
      "gl": "Medio rural",
      "eu": "Nekazaritza"
    },
    "description": {
      "en": "",
      "es": "Incluye: Agricultura, Ganader\u00EDa, Pesca y Silvicultura.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/AGRI"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/salud",
    "notation": "salud",
    "label": {
      "en": "Healthcare",
      "es": "Salud",
      "ca": "Salut",
      "gl": "Sa\u00FAde",
      "eu": "Osasuna"
    },
    "description": {
      "en": "",
      "es": "Incluye: Sanidad.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/HEAL"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/sector-publico",
    "notation": "sector-publico",
    "label": {
      "en": "Public sector",
      "es": "Sector p\u00FAblico",
      "ca": "Sector p\u00FAblic",
      "gl": "Sector p\u00FAblico",
      "eu": "Sektore publikoa"
    },
    "description": {
      "en": "",
      "es": "Incluye: Presupuestos, Organigrama institucional, Legislaci\u00F3n interna, Funci\u00F3n p\u00FAblica.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/GOVE"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/seguridad",
    "notation": "seguridad",
    "label": {
      "en": "Security",
      "es": "Seguridad",
      "ca": "Seguretat",
      "gl": "Seguridade",
      "eu": "Segurtasuna"
    },
    "description": {
      "en": "",
      "es": "Incluye: Protecci\u00F3n civil, Defensa.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/JUST"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/sociedad-bienestar",
    "notation": "sociedad-bienestar",
    "label": {
      "en": "Society and welfare",
      "es": "Sociedad y bienestar",
      "ca": "Societat i benestar",
      "gl": "Sociedade e benestar",
      "eu": "Gizartea eta ongizatea"
    },
    "description": {
      "en": "",
      "es": "Incluye: Participaci\u00F3n ciudadana, Marginaci\u00F3n, Envejecimiento Activo, Autonom\u00EDa personal y Dependencia, Invalidez, Jubilaci\u00F3n, Seguros y Pensiones, Prestaciones y Subvenciones.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/SOCI"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/transporte",
    "notation": "transporte",
    "label": {
      "en": "Transport",
      "es": "Transporte",
      "ca": "Transport",
      "gl": "Transporte",
      "eu": "Garraioa"
    },
    "description": {
      "en": "",
      "es": "Incluye: Comunicaciones y Tr/u00E1fico.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/TRAN"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/turismo",
    "notation": "turismo",
    "label": {
      "en": "Tourism",
      "es": "Turismo",
      "ca": "Turisme",
      "gl": "Turismo",
      "eu": "Turismoa"
    },
    "description": {
      "en": "",
      "es": "Incluye: Alojamientos, Hosteler\u00EDa, Gastronom\u00EDa.",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/ECON"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/urbanismo-infraestructuras",
    "notation": "urbanismo-infraestructuras",
    "label": {
      "en": "Town planning and infrastructures",
      "es": "Urbanismo e infraestructuras",
      "ca": "Urbanisme i infraestructures",
      "gl": "Urbanismo e infraestruturas",
      "eu": "Hirigintza eta azpiegiturak"
    },
    "description": {
      "en": "",
      "es": "Incluye: Saneamiento p\u00FAblico, Construcci\u00F3n (infraestructuras, equipamientos p\u00FAblicos).",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/REGI"
  },
  {
    "value": "http://datos.gob.es/kos/sector-publico/sector/vivienda",
    "notation": "vivienda",
    "label": {
      "en": "Housing",
      "es": "Vivienda",
      "ca": "Habitatge",
      "gl": "Vivenda",
      "eu": "Etxebizitza"
    },
    "description": {
      "en": "",
      "es": "Incluye: Mercado inmobiliario, Construcci\u00F3n (viviendas).",
      "ca": "",
      "gl": "",
      "eu": ""
    },
    "dcat_ap": "http://publications.europa.eu/resource/authority/data-theme/REGI"
  }
]

# Frequency constants
FREQUENCY_STANDARD_LABELS = [
    {
        'label': {
            'en': 'Bidecennial',
            'es': 'Cada veinte años',
            'ca': 'Cada vint anys',
            'gl': 'Cada vinte anos',
            'eu': 'Hogei urtean behin'
        },
        'value': 'bidecennial'
    },
    {
        'label': {
            'en': 'Tridecennial',
            'es': 'Cada treinta años',
            'ca': 'Cada trenta anys',
            'gl': 'Cada trinta anos',
            'eu': 'Hiru hamarkadaro'
        },
        'value': 'tridecennial'
    },
    {
        'label': {
            'en': 'Bihourly',
            'es': 'Cada dos horas',
            'ca': 'Cada dues hores',
            'gl': 'Cada dúas horas',
            'eu': 'Bi orduro behin'
        },
        'value': 'bihourly'
    },
    {
        'label': {
            'en': 'Trihourly',
            'es': 'Cada tres horas',
            'ca': 'Cada tres hores',
            'gl': 'Cada tres horas',
            'eu': 'Hiru ordutik behin'
        },
        'value': 'trihourly'
    },
    {
        'label': {
            'en': 'Other',
            'es': 'Otro',
            'ca': 'Altre',
            'gl': 'Outro',
            'eu': 'Beste'
        },
        'value': 'other'
    },
    {
        'label': {
            'en': 'Weekly',
            'es': 'Semanal',
            'ca': 'Setmanal',
            'gl': 'Semanal',
            'eu': 'Asteko'
        },
        'value': 'weekly'
    },
    {
        'label': {
            'en': 'As needed',
            'es': 'En función de las necesidades',
            'ca': 'En funció de les necessitats',
            'gl': 'En función das necesidades',
            'eu': 'Beharretan oinarrituta'
        },
        'value': 'as_needed'
    },
    {
        'label': {
            'en': 'Not planned',
            'es': 'No previsto',
            'ca': 'No previst',
            'gl': 'Non previsto',
            'eu': 'Aurreikusi gabe'
        },
        'value': 'not_planned'
    },
    {
        'label': {
            'en': 'Hourly',
            'es': 'Cada hora',
            'ca': 'Cada hora',
            'gl': 'Cada hora',
            'eu': 'Orduro'
        },
        'value': 'hourly'
    },
    {
        'label': {
            'en': 'Quadrennial',
            'es': 'Cada cuatro años',
            'ca': 'Cada quatre anys',
            'gl': 'Cada catro anos',
            'eu': 'Lau urtez behin'
        },
        'value': 'quadrennial'
    },
    {
        'label': {
            'en': 'Quinquennial',
            'es': 'Cada cinco años',
            'ca': 'Cada cinc anys',
            'gl': 'Cada cinco anos',
            'eu': 'Bost urterik behin'
        },
        'value': 'quinquennial'
    },
    {
        'label': {
            'en': 'Decennial',
            'es': 'Cada diez años',
            'ca': 'Cada deu anys',
            'gl': 'Cada dez anos',
            'eu': 'Hamabost urterik behin'
        },
        'value': 'decennial'
    },
    {
        'label': {
            'en': 'Semiweekly',
            'es': 'Bisemanal',
            'ca': 'Bisemanal',
            'gl': 'Bisemanal',
            'eu': 'Bisemanal'
        },
        'value': 'weekly_2'
    },
    {
        'label': {
            'en': 'Three times a week',
            'es': 'Tres veces por semana',
            'ca': 'Tres vegades per setmana',
            'gl': 'Tres veces por semana',
            'eu': 'Astero hiru aldiz'
        },
        'value': 'weekly_3'
    },
    {
        'label': {
            'en': 'Unknown',
            'es': 'Desconocido',
            'ca': 'Desconegut',
            'gl': 'Descoñecido',
            'eu': 'Ezezaguna'
        },
        'value': 'unknown'
    },
    {
        'label': {
            'en': 'Continuously updated',
            'es': 'Continuamente actualizada',
            'ca': 'Continuament actualitzada',
            'gl': 'Continuamente actualizada',
            'eu': 'Etengabe eguneratua'
        },
        'value': 'update_cont'
    },
    {
        'label': {
            'en': 'Quarterly',
            'es': 'Trimestral',
            'ca': 'Trimestral',
            'gl': 'Trimestral',
            'eu': 'Hiruhilabetekoa'
        },
        'value': 'quarterly'
    },
    {
        'label': {
            'en': 'Every five minutes',
            'es': 'Cada cinco minutos',
            'ca': 'Cada cinc minuts',
            'gl': 'Cada cinco minutos',
            'eu': 'Bost minuturo'
        },
        'value': '5min'
    },
    {
        'label': {
            'en': 'Triennial',
            'es': 'Trienal',
            'ca': 'Triennal',
            'gl': 'Trienal',
            'eu': 'Hirugarren urtekoa'
        },
        'value': 'triennial'
    },
    {
        'label': {
            'en': 'Never',
            'es': 'Nunca',
            'ca': 'Mai',
            'gl': 'Nunca',
            'eu': 'Inoiz'
        },
        'value': 'never'
    },
    {
        'label': {
            'en': 'Provisional data',
            'es': 'Datos provisionales',
            'ca': 'Dades provisionals',
            'gl': 'Datos provisionais',
            'eu': 'Datu provizionalak'
        },
        'value': 'op_datpro'
    },
    {
        'label': {
            'en': 'Semimonthly',
            'es': 'Bimensual',
            'ca': 'Bimensual',
            'gl': 'Bimensual',
            'eu': 'Bi hilean behin'
        },
        'value': 'monthly_2'
    },
    {
        'label': {
            'en': 'Three times a month',
            'es': 'Tres veces por mes',
            'ca': 'Tres vegades al mes',
            'gl': 'Tres veces ao mes',
            'eu': 'Hilean hiru aldiz'
        },
        'value': 'monthly_3'
    },
    {
        'label': {
            'en': 'Irregular',
            'es': 'Irregular',
            'ca': 'Irregular',
            'gl': 'Irregular',
            'eu': 'Irregulaarra'
        },
        'value': 'irreg'
    },
    {
        'label': {
            'en': 'Monthly',
            'es': 'Mensual',
            'ca': 'Mensual',
            'gl': 'Mensual',
            'eu': 'Hileko'
        },
        'value': 'monthly'
    },
    {
        'label': {
            'en': 'Daily',
            'es': 'Diario',
            'ca': 'Diari',
            'gl': 'Diario',
            'eu': 'Egunkari'
        },
        'value': 'daily'
    },
    {
        'label': {
            'en': 'Twice a day',
            'es': 'Dos veces al día',
            'ca': 'Dues vegades al dia',
            'gl': 'Dúas veces ao día',
            'eu': 'Bi aldiz egunean'
        },
        'value': 'daily_2'
    },
    {
        'label': {
            'en': 'Biweekly',
            'es': 'Quincenal',
            'ca': 'Quinzenal',
            'gl': 'Quincenal',
            'eu': 'Bi astez behin'
        },
        'value': 'biweekly'
    },
    {
        'label': {
            'en': 'Continuous',
            'es': 'Continuo',
            'ca': 'Continu',
            'gl': 'Continuo',
            'eu': 'Jarraitua'
        },
        'value': 'cont'
    },
    {
        'label': {
            'en': 'Biennial',
            'es': 'Bienal',
            'ca': 'Biennal',
            'gl': 'Bianual',
            'eu': 'Bienala'
        },
        'value': 'biennial'
    },
    {
        'label': {
            'en': 'Bimonthly',
            'es': 'Bimestral',
            'ca': 'Bimestral',
            'gl': 'Bimestral',
            'eu': 'Bi hilabetekoa'
        },
        'value': 'bimonthly'
    },
    {
        'label': {
            'en': 'Semiannual',
            'es': 'Semestral',
            'ca': 'Semestral',
            'gl': 'Semestral',
            'eu': 'Sei hilean behin'
        },
        'value': 'annual_2'
    },
    {
        'label': {
            'en': 'Three times a year',
            'es': 'Cuatrimestral',
            'ca': 'Quadrimestral',
            'gl': 'Cuatrimestral',
            'eu': 'Laugarren hilekoa'
        },
        'value': 'annual_3'
    },
    {
        'label': {
            'en': 'Annual',
            'es': 'Anual',
            'ca': 'Anual',
            'gl': 'Anual',
            'eu': 'Urtero'
        },
        'value': 'annual'
    },
    {
        'label': {
            'en': 'Every thirty minutes',
            'es': 'Cada treinta minutos',
            'ca': 'Cada trenta minuts',
            'gl': 'Cada trinta minutos',
            'eu': 'Hogei minuturo'
        },
        'value': '30min'
    },
    {
        'label': {
            'en': 'Every minute',
            'es': 'Cada minuto',
            'ca': 'Cada minut',
            'gl': 'Cada minuto',
            'eu': 'Minutu bakoitzean'
        },
        'value': '1min'
    },
    {
        'label': {
            'en': 'Every twelve hours',
            'es': 'Cada doce horas',
            'ca': 'Cada dotze hores',
            'gl': 'Cada doce horas',
            'eu': 'Hamaika orduro'
        },
        'value': '12hrs'
    },
    {
        'label': {
            'en': 'Every fifteen minutes',
            'es': 'Cada quince minutos',
            'ca': 'Cada quinze minuts',
            'gl': 'Cada quince minutos',
            'eu': 'Hamar hamar minuturo'
        },
        'value': '15min'
    },
    {
        'label': {
            'en': 'Every ten minutes',
            'es': 'Cada diez minutos',
            'ca': 'Cada deu minuts',
            'gl': 'Cada dez minutos',
            'eu': 'Hamar minuturo'
        },
        'value': '10min'
    }
]

FREQUENCY_STANDARD_LABELS_DEFAULT = {
    'en': 'Other',
    'es': 'Otro',
    'ca': 'Altre',
    'gl': 'Outro',
    'eu': 'Beste'
}

UNDEFINED_FORMAT_LABELS = {
    'en': 'Undefined',
    'es': 'Indefinido',
    'ca': 'Indefinit',
    'gl': 'Indefinido',
    'eu': 'Zehaztugabea'
}

NTI_CHOICES_FIELDS = {
  NTI_CHOICES_FIELD_LANGUAGE: NTI_DCT_LANGUAGES_CHOICES,
  NTI_CHOICES_FIELD_SPATIAL: DATOSGOB_DCT_SPATIAL_CHOICES,
  NTI_CHOICES_FIELD_THEME: DATOSGOB_DCT_THEME_CHOICES,
  NTI_CHOICES_FIELD_FREQUENCY: FREQUENCY_STANDARD_LABELS
}

FREQUENCY_IDENTIFIER_BIDECENNIAL = 'bidecennial'
FREQUENCY_IDENTIFIER_TRIDECENNIAL = 'tridecennial'
FREQUENCY_IDENTIFIER_BIHOURLY = 'bihourly'
FREQUENCY_IDENTIFIER_TRIHOURLY = 'trihourly'
FREQUENCY_IDENTIFIER_OTHER = 'other'
FREQUENCY_IDENTIFIER_WEEKLY = 'weekly'
FREQUENCY_IDENTIFIER_NOT_PLANNED = 'not_planned'
FREQUENCY_IDENTIFIER_AS_NEEDED = 'as_needed'
FREQUENCY_IDENTIFIER_5MIN = '5min'
FREQUENCY_IDENTIFIER_30MIN = '30min'
FREQUENCY_IDENTIFIER_HOURLY = 'hourly'
FREQUENCY_IDENTIFIER_QUADRENNIAL = 'quadrennial'
FREQUENCY_IDENTIFIER_QUINQUENNIAL = 'quinquennial'
FREQUENCY_IDENTIFIER_DECENNIAL = 'decennial'
FREQUENCY_IDENTIFIER_1MIN = '1min'
FREQUENCY_IDENTIFIER_15MIN = '15min'
FREQUENCY_IDENTIFIER_WEEKLY_2 = 'weekly_2'
FREQUENCY_IDENTIFIER_WEEKLY_3 = 'weekly_3'
FREQUENCY_IDENTIFIER_12HRS = '12hrs'
FREQUENCY_IDENTIFIER_UNKNOWN = 'unknown'
FREQUENCY_IDENTIFIER_10MIN = '10min'
FREQUENCY_IDENTIFIER_UPDATE_CONT = 'update_cont'
FREQUENCY_IDENTIFIER_QUARTERLY = 'quarterly'
FREQUENCY_IDENTIFIER_TRIENNIAL = 'triennial'
FREQUENCY_IDENTIFIER_NEVER = 'never'
FREQUENCY_IDENTIFIER_OP_DATPRO = 'op_datpro'
FREQUENCY_IDENTIFIER_MONTHLY_2 = 'monthly_2'
FREQUENCY_IDENTIFIER_MONTHLY_3 = 'monthly_3'
FREQUENCY_IDENTIFIER_IRREG = 'irreg'
FREQUENCY_IDENTIFIER_MONTHLY = 'monthly'
FREQUENCY_IDENTIFIER_DAILY = 'daily'
FREQUENCY_IDENTIFIER_DAILY_2 = 'daily_2'
FREQUENCY_IDENTIFIER_BIWEEKLY = 'biweekly'
FREQUENCY_IDENTIFIER_CONT = 'cont'
FREQUENCY_IDENTIFIER_BIENNIAL = 'biennial'
FREQUENCY_IDENTIFIER_BIMONTHLY = 'bimonthly'
FREQUENCY_IDENTIFIER_ANNUAL_2 = 'annual_2'
FREQUENCY_IDENTIFIER_ANNUAL_3 = 'annual_3'
FREQUENCY_IDENTIFIER_ANNUAL = 'annual'

FREQUENCY_IDENTIFIERS = [
    FREQUENCY_IDENTIFIER_BIDECENNIAL,
    FREQUENCY_IDENTIFIER_TRIDECENNIAL,
    FREQUENCY_IDENTIFIER_BIHOURLY,
    FREQUENCY_IDENTIFIER_TRIHOURLY,
    FREQUENCY_IDENTIFIER_OTHER,
    FREQUENCY_IDENTIFIER_WEEKLY,
    FREQUENCY_IDENTIFIER_NOT_PLANNED,
    FREQUENCY_IDENTIFIER_AS_NEEDED,
    FREQUENCY_IDENTIFIER_5MIN,
    FREQUENCY_IDENTIFIER_30MIN,
    FREQUENCY_IDENTIFIER_HOURLY,
    FREQUENCY_IDENTIFIER_QUADRENNIAL,
    FREQUENCY_IDENTIFIER_QUINQUENNIAL,
    FREQUENCY_IDENTIFIER_DECENNIAL,
    FREQUENCY_IDENTIFIER_1MIN,
    FREQUENCY_IDENTIFIER_15MIN,
    FREQUENCY_IDENTIFIER_WEEKLY_2,
    FREQUENCY_IDENTIFIER_WEEKLY_3,
    FREQUENCY_IDENTIFIER_12HRS,
    FREQUENCY_IDENTIFIER_UNKNOWN,
    FREQUENCY_IDENTIFIER_10MIN,
    FREQUENCY_IDENTIFIER_UPDATE_CONT,
    FREQUENCY_IDENTIFIER_QUARTERLY,
    FREQUENCY_IDENTIFIER_TRIENNIAL,
    FREQUENCY_IDENTIFIER_NEVER,
    FREQUENCY_IDENTIFIER_OP_DATPRO,
    FREQUENCY_IDENTIFIER_MONTHLY_2,
    FREQUENCY_IDENTIFIER_MONTHLY_3,
    FREQUENCY_IDENTIFIER_IRREG,
    FREQUENCY_IDENTIFIER_MONTHLY,
    FREQUENCY_IDENTIFIER_DAILY,
    FREQUENCY_IDENTIFIER_DAILY_2,
    FREQUENCY_IDENTIFIER_BIWEEKLY,
    FREQUENCY_IDENTIFIER_CONT,
    FREQUENCY_IDENTIFIER_BIENNIAL,
    FREQUENCY_IDENTIFIER_BIMONTHLY,
    FREQUENCY_IDENTIFIER_ANNUAL_2,
    FREQUENCY_IDENTIFIER_ANNUAL_3,
    FREQUENCY_IDENTIFIER_ANNUAL
]

FREQUENCY_IDENTIFIERS_OPTIONS = {
    ('years', 1): FREQUENCY_IDENTIFIER_ANNUAL,
    ('years', 2): FREQUENCY_IDENTIFIER_BIENNIAL,
    ('years', 3): FREQUENCY_IDENTIFIER_TRIENNIAL,
    ('years', 4): FREQUENCY_IDENTIFIER_QUADRENNIAL,
    ('years', 5): FREQUENCY_IDENTIFIER_QUINQUENNIAL,
    ('years', 10): FREQUENCY_IDENTIFIER_DECENNIAL,
    ('years', 20): FREQUENCY_IDENTIFIER_BIDECENNIAL,
    ('years', 30): FREQUENCY_IDENTIFIER_TRIDECENNIAL,
    ('years', 0): FREQUENCY_IDENTIFIER_CONT,
    ('months', 1): FREQUENCY_IDENTIFIER_MONTHLY,
    ('months', 2): FREQUENCY_IDENTIFIER_BIMONTHLY,
    ('months', 3): FREQUENCY_IDENTIFIER_QUARTERLY,
    ('months', 4): FREQUENCY_IDENTIFIER_ANNUAL_3,
    ('months', 6): FREQUENCY_IDENTIFIER_ANNUAL_2,
    ('months', 12): FREQUENCY_IDENTIFIER_ANNUAL,
    ('months', 24): FREQUENCY_IDENTIFIER_BIENNIAL,
    ('months', 36): FREQUENCY_IDENTIFIER_TRIENNIAL,
    ('months', 48): FREQUENCY_IDENTIFIER_QUADRENNIAL,
    ('months', 60): FREQUENCY_IDENTIFIER_QUINQUENNIAL,
    ('months', 120): FREQUENCY_IDENTIFIER_DECENNIAL,
    ('months', 240): FREQUENCY_IDENTIFIER_BIDECENNIAL,
    ('months', 360): FREQUENCY_IDENTIFIER_TRIDECENNIAL,
    ('months', 0): FREQUENCY_IDENTIFIER_CONT,
    ('weeks', 1): FREQUENCY_IDENTIFIER_WEEKLY,
    ('weeks', 2): FREQUENCY_IDENTIFIER_BIWEEKLY,
    ('weeks', 4): FREQUENCY_IDENTIFIER_MONTHLY,
    ('weeks', 0): FREQUENCY_IDENTIFIER_CONT,
    ('days', 1): FREQUENCY_IDENTIFIER_DAILY,
    ('days', 7): FREQUENCY_IDENTIFIER_WEEKLY,
    ('days', 15): FREQUENCY_IDENTIFIER_BIWEEKLY,
    ('days', 30): FREQUENCY_IDENTIFIER_MONTHLY,
    ('days', 31): FREQUENCY_IDENTIFIER_MONTHLY,
    ('days', 60): FREQUENCY_IDENTIFIER_BIMONTHLY,
    ('days', 90): FREQUENCY_IDENTIFIER_QUARTERLY,
    ('days', 120): FREQUENCY_IDENTIFIER_ANNUAL_3,
    ('days', 180): FREQUENCY_IDENTIFIER_ANNUAL_2,
    ('days', 365): FREQUENCY_IDENTIFIER_ANNUAL,
    ('days', 0): FREQUENCY_IDENTIFIER_CONT,
    ('hours', 1): FREQUENCY_IDENTIFIER_HOURLY,
    ('hours', 2): FREQUENCY_IDENTIFIER_BIHOURLY,
    ('hours', 3): FREQUENCY_IDENTIFIER_TRIHOURLY,
    ('hours', 12): FREQUENCY_IDENTIFIER_12HRS,
    ('hours', 24): FREQUENCY_IDENTIFIER_DAILY,
    ('hours', 0): FREQUENCY_IDENTIFIER_CONT,
    ('minutes', 1): FREQUENCY_IDENTIFIER_1MIN,
    ('minutes', 5): FREQUENCY_IDENTIFIER_5MIN,
    ('minutes', 10): FREQUENCY_IDENTIFIER_10MIN,
    ('minutes', 15): FREQUENCY_IDENTIFIER_15MIN,
    ('minutes', 30): FREQUENCY_IDENTIFIER_30MIN,
    ('minutes', 60): FREQUENCY_IDENTIFIER_HOURLY,
    ('minutes', 120): FREQUENCY_IDENTIFIER_BIHOURLY,
    ('minutes', 180): FREQUENCY_IDENTIFIER_TRIHOURLY,
    ('minutes', 0): FREQUENCY_IDENTIFIER_CONT,
    ('seconds', 60): FREQUENCY_IDENTIFIER_1MIN,
    ('seconds', 1): FREQUENCY_IDENTIFIER_CONT,
    ('seconds', 0): FREQUENCY_IDENTIFIER_CONT
}