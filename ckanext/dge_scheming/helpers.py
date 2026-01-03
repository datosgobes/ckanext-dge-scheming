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

import re
from ckanext.scheming.helpers import lang
import ckan.lib.helpers as h
from ckan.plugins.toolkit import (config, _)
import urllib.request, urllib.parse, urllib.error
import urllib.parse
import rfc3987

import ckan.model as model
import ckan.lib.dictization.model_dictize as model_dictize
import ckanext.dge_scheming.constants as ds_constants


import logging
log = logging.getLogger(__name__)


def dge_dataset_form_organization_list():
    """
    Get a list of all active organizations
    """
    context = {'model': model}
    orgs_q = model.Session.query(model.Group) \
        .filter(model.Group.is_organization == True) \
        .filter(model.Group.state == 'active')

    orgs_list = model_dictize.group_list_dictize(orgs_q.all(), context)
    return orgs_list

def dge_dataset_form_value(text):
    """
    :param text: {lang: text} dict or text string

    Convert "language-text" to users' language by looking up
    languag in dict or using _() if not a dict but. If the text
    doesn't exist look for an available text
    """
    if not text:
        return ''

    if hasattr(text, 'get'):
        final_text = ''
        try:
            prefer_lang = lang()
        except:
            prefer_lang = config.get('ckan.locale_default', 'es')
        else:
            try:
                final_text = text[prefer_lang]
            except KeyError:
                pass

        if not final_text:
            locale_order = config.get('ckan.locale_order', '').split()
            for l in locale_order:
                if l in text and text[l]:
                    final_text = text[l]
                    break
        return final_text

    t = _(text)
    if isinstance(t, str):
        return t.decode('utf-8')
    return t

def dge_dataset_form_lang_and_value(text):
    """
    :param text: {lang: text} dict or text string

    Convert "language-text" to users' language by looking up
    languag in dict, if the text
    doesn't exit look for an available text
    """
    if not text:
        return {'': ''}

    if hasattr(text, 'get'):
        final_text = ''
        try:
            prefer_lang = lang()
        except:
            prefer_lang = config.get('ckan.locale_default', 'es')
        else:
            try:
                prefer_lang = str(prefer_lang)
                final_text = text[prefer_lang]
            except KeyError:
                pass

        if not final_text:
            locale_order = config.get('ckan.locale_order', '').split()
            for l in locale_order:
                if l in text and text[l]:
                    final_text = text[l]
                    prefer_lang = l
                    break

        return {prefer_lang: final_text}

    return {'': ''}

def dge_is_url(value):
    '''
    Given a value, raises an RDFParsesException if value is not a complete
    URI.
    A complete URI starts with scheme_name: ([A-Za-z][A-Za-z0-9+.-]*):
    Returns True if argument parses as a http, https or ftp URL
    '''
    if not dge_is_uri(value):
        return False
    else:
        return h.is_url(value)


def dge_is_uri(value):
    '''
    Given a value, raises an RDFParsesException if value is not a complete
    URI.
    A complete URI starts with scheme_name: ([A-Za-z][A-Za-z0-9+.-]*):
    '''
    if not value or value.strip() == '':
        return False
    try:
        url = urllib.parse.urlparse(value)
    except ValueError as e:
        log.info('%s is not a valid URI. Value error %s.' % e)
        return False
    netloc = url.netloc
    if h.is_url(value) and not(netloc and len(netloc) > 0):
        log.info('%s is not a valid URL. Not netloc or netloc length is 0.' % value)
        return False
    else:
        prev_netloc = ''
        while '%' in netloc and prev_netloc != netloc:
            prev_netloc = netloc
            netloc = urllib.parse.unquote(netloc)
    url2 = netloc
    if url.scheme and len(url.scheme) > 0:
        url2 = url.scheme + '://' + netloc
    #log.info('************* url2= %s' % url2)
    if rfc3987.match(url2, rule='URI'):
        return True
    else:
        log.info('% s is not a valid URI.')
        return False


def dge_multiple_field_required(field, lang):
    """
    Return field['required'] or guess based on validators if not present.
    """
    if 'required' in field:
        return field['required']
    if 'required_language' in field and field['required_language'] == lang:
        return True
    return 'not_empty' in field.get('validators', '').split()


def dge_multiple_uri_field_one_required(field, index):
    """
    Return field['required'] or 
    True if field['required_one'] is true and index is 1
    or guess based on validators if not present.
    """
    if 'required' in field:
        return field['required']
    if 'required_one' in field and field['required_one'] == True and index == 1:
        return True
    return 'not_empty' in field.get('validators', '').split()

def dge_dataset_license_to_distributions_license(context, data_dict):
    '''
    Update resource_license when a dataset is updated
    In DCAT-AP-ES 1.0.0 dataset's dct:license will be stored in every dataset's distribution dct:license
    '''
    from sqlalchemy.orm.attributes import flag_modified
    log.debug('[dge_dataset_license_to_distributions_license]')
    if 'state' not in data_dict:
        model = context['model']
        package = model.Package.get(data_dict['id'])
        for resource in package.resources:
            if 'resource_license' in resource.extras and 'license_id' in data_dict:
                if resource.extras['resource_license'] != data_dict['license_id']:
                    resource.extras['resource_license'] = data_dict['license_id']
                    flag_modified(resource, 'extras')
                    try:
                        model.Session.commit()
                    except Exception as e:
                        log.debug(f'There was an error updating data in resources: {e}')
                        model.Session.rollback()
                        
def dge_get_nti_field_choices(field):
    '''
    :param field: Schema choice field
    
    Return a list of dicts with datos.gob.es NTI-RISP choices for the field specified
    '''
    return ds_constants.NTI_CHOICES_FIELDS[field]

def dge_get_application_profile(dataset_dict):
    '''
    :param datasect_dict: dataset dict
    
    Return a str with the value of dataset application profile
    '''
    application_profile = None
    for data_key in dataset_dict:
        if len(data_key) == 3 and dataset_dict[data_key] == ds_constants.APPLICATION_PROFILE_KEY:
            data_key_index = data_key[1]
            data_profile_value_key = ('extras', data_key_index, 'value')
            application_profile = dataset_dict[data_profile_value_key]
    return application_profile

def dge_is_nti_application_profile(dataset_dict):
    '''
    :param datasect_dict: dataset dict
    
    Return True if dataset application profile is NTI. False otherwise
    '''
    is_nti = False
    for data_key in dataset_dict:
        if len(data_key) == 3 and dataset_dict[data_key] == ds_constants.APPLICATION_PROFILE_KEY:
            data_key_index = data_key[1]
            data_profile_value_key = ('extras', data_key_index, 'value')
            is_nti = True if dataset_dict[data_profile_value_key] == ds_constants.NTI else False
    return is_nti

def dge_is_dcatapes_application_profile(dataset_dict):
    '''
    :param datasect_dict: dataset dict
    
    Return True if dataset application profile is DCATAPES. False otherwise
    '''
    is_dcatapes = False
    for data_key in dataset_dict:
        if len(data_key) == 3 and dataset_dict[data_key] == ds_constants.APPLICATION_PROFILE_KEY:
            data_key_index = data_key[1]
            data_profile_value_key = ('extras', data_key_index, 'value')
            is_dcatapes = True if dataset_dict[data_profile_value_key] == ds_constants.DCATAPES_100 else False
    return is_dcatapes

def dge_is_datosgobes_theme_uri(theme_uri):
    '''
    :param theme_uri: theme uri
    
    Return True if theme uri belongs to datos.gob.es vocabulary. False otherwise
    '''
    return True if theme_uri.startswith(ds_constants.DATOSGOBES_THEME_PREFIX) else False

def dge_parse_frequency_identifier(ftype, fvalue):
    '''
    :param ftype: frequency type
    :param fvalue: frequency value
    
    Return identifier for type and value if exists. 'other' identifier otherwise
    '''
    return ds_constants.FREQUENCY_IDENTIFIERS_OPTIONS.get((ftype, int(fvalue)), ds_constants.FREQUENCY_IDENTIFIER_OTHER)

def dge_scheming_field_nti_required(field):
    """
    :param field: Schema field
    
    Return field['nti_required'] or False if not present.
    """
    if 'nti_required' in field:
        return field['nti_required']
    return False

def dge_get_value_from_nti_identifier(value):
    '''
    :param value: Stored value from Form identifier field
    
    Return the first item if value is a list. Return the value otherwise.
    '''
    if value and isinstance(value, list):
        return value[0]
    return value

def dge_is_list_of_items_field_value(value):
    '''
    :param value: Stored value from Form choices field (spatial, theme)
    
    Return True if value is a list, False otherwise.
    '''
    return (value and isinstance(value, list))