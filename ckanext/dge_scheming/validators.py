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

# -*- coding: utf-8 -*-
import json
import logging
import re
import urllib.request, urllib.parse, urllib.error
import urllib.parse
import six
import datetime

import ckan.authz as authz
import ckan.lib.helpers as h
import ckan.lib.munge as munge
import ckan.lib.navl.dictization_functions as df
import ckan.model as model
import ckan.plugins.toolkit as toolkit
import ckanext.dge_scheming.helpers as dh
import ckanext.dge_scheming.constants as ds_constants
from dateutil.parser import parse as parse_date
from ckan.logic.validators import tag_string_convert
from ckan.plugins.toolkit import missing, Invalid, StopOnError, _
from ckantoolkit import get_validator
from ckan.plugins.toolkit import config
from ckanext.scheming.helpers import (
    scheming_field_choices)
from ckanext.fluent.validators import (
    _validate_single_tag, BCP_47_LANGUAGE)
from ckanext.fluent.helpers import (
    fluent_form_languages, fluent_alternate_languages)
from ckanext.scheming.validation import (
    scheming_validator, validators_from_string, validate_date_inputs)
from ckanext.dcat.validators import is_year, is_year_month, is_date

log = logging.getLogger(__name__)

not_empty = get_validator('not_empty')
ignore_missing = get_validator('ignore_missing')
ignore_empty = get_validator('ignore_empty')
tag_length_validator = get_validator('tag_length_validator')
tag_name_validator = get_validator('tag_name_validator')
netloc_re = re.compile('^(?:([^:]*)[:]([^@]*)@)?([^:]*)(?:[:](\d+))?$')

all_validators = {}


def register_validator(fn):
    """
    collect validator functions into ckanext.scheming.all_helpers dict
    """
    all_validators[fn.__name__] = fn
    return fn

def scheming_validator(fn):
    """
    Decorate a validator for using with scheming.
    """
    fn.is_a_scheming_validator = True
    return fn


"""
FIELD TYPE URL
"""


@scheming_validator
def uri_text(field, schema):
    required = field.get('required', False)
    nti_required = field.get('nti_required', False)
    header = '[uri_text VALIDATOR]'
    def validator(key, data, errors, context):
        log.debug('{} validating. Key: {} required: {}'.format(header, key, required))
                
        value = data[key]
    
        is_url = False
        if ('is_url' in field):
            is_url = field['is_url']
        
        if value is not missing:
            if value:
                if is_url and not dh.dge_is_url(value):
                    errors[key].append(_('the URL format is not valid'))
                else:
                    if not is_url and not dh.dge_is_uri(value):
                        errors[key].append(_('the URI format is not valid'))
                        
                if key == ds_constants.LICENSE_KEY:
                    data[ds_constants.DATASET_LICENSE_TMP] = value
                
                return

        # 3. separate fields
        extras = data.get(('__extras',), {})
        if key in extras:
            value = extras[key]

            if is_url and not dh.dge_is_url(value):
                errors[key].append(_('the URL format is not valid'))
            else:
                if not is_url and not dh.dge_is_uri(value):
                    errors[key].append(_('the URI format is not valid'))
            return
        
        if len(key) == 3 and key[0] == ds_constants.RESOURCE_KEY:
            resource_license_key = (ds_constants.RESOURCE_KEY, key[1], ds_constants.RESOURCE_LICENSE_KEY)
            if key == resource_license_key and ds_constants.DATASET_LICENSE_TMP in data:
                if data[ds_constants.DATASET_LICENSE_TMP] is not None and data[ds_constants.DATASET_LICENSE_TMP] is not missing:
                    dataset_license_tmp = data[ds_constants.DATASET_LICENSE_TMP]
                    data[resource_license_key] = dataset_license_tmp

        if required or (nti_required and not dh.dge_is_dcatapes_application_profile(data)):
            not_empty(key, data, errors, context)
        else:
            ignore_missing(key, data, errors, context)
            ignore_empty(key, data, errors, context)

    return validator


def uri_text_output(value):
    return value


"""
FIELD TYPE MULTIPLE URL
"""


@scheming_validator
def multiple_uri_text(field, schema):
    required_one = field['required_one'] if 'required_one' in field else False
    header = '[multiple_uri_text VALIDATOR]'
    def validator(key, data, errors, context):
        """
        Accept repeating text input in the following forms
        and convert to a json list for storage:
        1. a list of strings, eg.
           ["http://url1", "http://url2"]
        2. a single string value to allow single text fields to be
           migrated to repeating text
           "http://url1"
        3. separate fields per language (for form submissions):
           fieldname-0 = "http://url1"
           fieldname-1 = "http://url2"
        """
        log.debug('{} validating. Key: {} required_one: {}'.format(header, key, required_one))
        
        # just in case there was an error before that validator
        if errors[key]:
            return
        
        is_dcatapes = dh.dge_is_dcatapes_application_profile(data) if key == ds_constants.IDENTIFIER_KEY else False
               
        if len(key) == 3 and key[0] == ds_constants.RESOURCE_KEY:
            access_url_key = (ds_constants.RESOURCE_KEY, key[1], ds_constants.ACCESS_URL_KEY)
            if key == access_url_key:
                url_key = (ds_constants.RESOURCE_KEY, key[1], ds_constants.URL_KEY)
                resource_url = data[url_key]
                if resource_url:
                    data[key] = [resource_url]
        
        value = data[key]

        is_url = False
        if ('is_url' in field):
            is_url = field['is_url']
        
        # 1. list of strings or 2. single string
        if value is not missing:
            if isinstance(value, str):
                value = [value]
            if not isinstance(value, list):
                errors[key].append(_('Expecting list of strings'))
                return

            out = []
            
            for element in value:
                # In DCAT-AP-ES 1.0.0 identifier doesn't have to be an URI
                if key != ds_constants.IDENTIFIER_KEY or (key == ds_constants.IDENTIFIER_KEY and not is_dcatapes):
                    if not isinstance(element, str):
                        errors[key].append(_('Invalid type for repeating url text: %r')
                                        % element)
                        continue
                        type(i)
                    try:
                        if not isinstance(element, str):
                            element = element.decode('utf-8')
                        if element:
                            if is_url and not dh.dge_is_url(element):
                                errors[key].append(
                                    _('The URL format is not valid'))
                            else:
                                if not is_url and not dh.dge_is_uri(element):
                                    errors[key].append(
                                        _('The URI format is not valid'))

                    except UnicodeDecodeError:
                        errors[key]. append(_('Invalid encoding for "%s" value')
                                            % lang)
                        continue
                out.append(element)
            
            if required_one and len(out) == 0:
                errors[key] = [_('Missing value')]

            if not errors[key]:
                data[key] = json.dumps(out)
            return

        # 3. separate fields
        found = {}
        prefix = key[-1] + '-'
        extras = data.get(key[:-1] + ('__extras',), {})

        # Validation
        url_errors = False
        
        index = -1
        for name, text in extras.items():
            if not name.startswith(prefix):
                continue
            if not text:
                continue
            index = name.split('-', 1)[1]
            if text is not missing:
                if is_url and not dh.dge_is_url(text):
                    url_errors = True
                    name_error = key[:-1] + (name,)
                    errors[name_error] = [
                        _('The URL format for "%s" is not valid') % text]
                else:
                    if not is_url and not dh.dge_is_uri(text):
                        url_errors = True
                        name_error = key[:-1] + (name,)
                        errors[name_error] = [
                            _('The URI format for "%s" is not valid') % text]
            elif required_one and index == 1:
                name_error = key[:-1] + (name,)
                errors[name_error] = [_('Missing value')]
        
        if required_one and index == -1:
            errors[key] = [_('Missing value')]
            
        if url_errors:
            return

        for name, text in extras.items():
            if not name.startswith(prefix):
                continue
            if not text:
                continue
            index = name.split('-', 1)[1]
            try:
                index = int(index)
            except ValueError:
                continue
            found[index] = text

        out = [found[i] for i in sorted(found)]
        
        # Avoiding storing empty lists
        if out and len(out) > 0:
            data[key] = json.dumps(out)
          
        # Ignoring missing or empty if not required
        if not required_one:
            ignore_missing(key, data, errors, context)
            ignore_empty(key, data, errors, context)

    return validator


def multiple_uri_text_output(value):
    """
    Return stored json representation as a list, if
    value is already a list just pass it through.
    """
    if isinstance(value, list):
        return value
    if value is None:
        return []
    try:
        return json.loads(value)
    except ValueError:
        return [value]


"""
FIELD TYPE DATE FREQUENCY
"""


@scheming_validator
def date_frequency(field, schema):
    header = '[date_frequency VALIDATOR]'
    def validator(key, data, errors, context):
        """
        JSON with frequency and value information
        """
        log.debug('{} validating. Key: {}'.format(header, key))
        # just in case there was an error before that validator
        if errors[key]:
            return

        value = data[key]

        # 1. list of strings or 2. single string
        if value is not missing:
            if isinstance(value, str):
                try:
                    value = json.loads(value)
                except ValueError:
                    errors[key].append(_('Failed to decode JSON string'))
                    return
                except UnicodeDecodeError:
                    errors[key].append(_('Invalid encoding for JSON string'))
                    return
            if not isinstance(value, dict):
                errors[key].append(_('Expecting JSON object'))
                return

            if not 'type' in value or not 'value' in value:
                errors[key].append(
                    _('The JSON object must contain type and value keys'))
                return

            frequency_type = value['type']
            frequency_value = value['value']
            
            if frequency_type and frequency_value is not None:
                if not frequency_type in ds_constants.FREQUENCY_VALUES:
                    errors[key] = [_('The frequency type is no allowed')]
                try:
                    int(frequency_value)
                except ValueError:
                    errors[key] = [_('The frequency value is not an integer')]
            else:
                if frequency_type and frequency_value == None:
                    errors[key] = [_('The frequency value is mandatory')]
                if frequency_value is not None and not frequency_type:
                    errors[key] = [_('The frequency type is mandatory')]
                if field.get('required') and frequency_value == None and not frequency_type:
                    not_empty(key, data, errors, context)

            if not errors[key]:
                if frequency_value is not None and frequency_type:
                    frequency_uri = value['uri'] if 'uri' in value and value['uri'] else ''
                    # Adding identifier
                    frequency_identifier = ''
                    if frequency_uri:
                        frequency_identifier = frequency_uri[len(ds_constants.FREQUENCY_EUROPEAN_PREFIX):].lower()
                    else:
                        frequency_identifier = dh.dge_parse_frequency_identifier(frequency_type, frequency_value)
                    if not frequency_identifier in ds_constants.FREQUENCY_IDENTIFIERS:
                        frequency_identifier = ds_constants.FREQUENCY_IDENTIFIER_OTHER
                    out = {'type': frequency_type, 'value': frequency_value, 'uri': frequency_uri, 'identifier': frequency_identifier}
                    data[key] = json.dumps(out)
                else:
                    data[key] = None
            return

        # 3. separate fields
        found = {}
        prefix = key[-1] + '-'
        extras = data.get(key[:-1] + ('__extras',), {})

        # Form validations
        frequency_type = extras.get(prefix + 'type')
        frequency_value = extras.get(prefix + 'value')

        if frequency_type and frequency_value:
            if not frequency_type in ds_constants.FREQUENCY_VALUES:
                errors[key] = [_('The frequency type is no allowed')]
            try:
                int(frequency_value)
            except ValueError:
                errors[key] = [_('The frequency value is not an integer')]
        else:
            if frequency_type and not frequency_value:
                errors[key] = [_('The frequency value is mandatory')]
            if frequency_value and not frequency_type:
                errors[key] = [_('The frequency type is mandatory')]
            if field.get('required') and not frequency_value and not frequency_type:
                not_empty(key, data, errors, context)

        # With errors we finish
        if errors[key]:
            return

        # transform to JSON
        if frequency_value and frequency_type:
            # Adding identifier
            frequency_identifier = ''
            frequency_identifier = dh.dge_parse_frequency_identifier(frequency_type, frequency_value)
            if not frequency_identifier in ds_constants.FREQUENCY_IDENTIFIERS:
                frequency_identifier = ds_constants.FREQUENCY_IDENTIFIER_OTHER
            out = {'type': frequency_type, 'value': frequency_value, 'uri': '', 'identifier': frequency_identifier}
            data[key] = json.dumps(out)
        else:
            data[key] = None

    return validator


def date_frequency_output(value):
    """
    Return stored json representation as a dict, if
    value is already a dict just pass it through.
    """
    if isinstance(value, dict):
        return value
    if value is None:
        return {}
    try:
        return json.loads(value)
    except ValueError:
        return {}


"""
FIELD URL FROM MULTILANGUAGE TITLE
"""


@scheming_validator
def multilanguage_url(field, schema):
    def validator(key, data, errors, context):
        if errors[key]:
            return

        value = data[key]
        if value is not missing:
            dir3 = _get_dir3(data, key)
            log.debug(
                    '[multilanguage_url] key %s, value %s, dir3 %s', key, value, dir3)
            if value:
                if dir3 and dir3 not in value:
                    _dir3 = (dir3 + '-') if dir3 else ''
                    data[key] = munge.munge_title_to_name(_dir3 + value)
                    log.debug('[multilanguage_url] Created name "%s" from dir3 %s and value %s',
                              data[key], dir3 or '', value)
                return
            else:
                output = {}

                prefix = field['autogeneration_field']
                if not prefix:
                    prefix = ds_constants.DEFAULT_TITLE_FIELD

                log.debug(
                    '[multilanguage_url] Creating field using the field %s', prefix)

                prefix = prefix + '-'

                extras = data.get(key[:-1] + ('__extras',), {})

                locale_default = config.get('ckan.locale_default', 'es')
                if locale_default:
                    title_lang = prefix + locale_default

                    if title_lang in extras and extras[title_lang]:
                        dataset_title = extras[title_lang]
                        _dir3 = (dir3 + '-') if dir3 else ''
                        data[key] = munge.munge_title_to_name(
                            _dir3 + dataset_title)

                        log.debug('[multilanguage_url] Created name "%s" for package from language %s',
                                  data[key], locale_default)
                    return

                locale_order = config.get('ckan.locale_order', '').split()
                for l in locale_order:
                    title_lang = prefix + l
                    if title_lang in extras and extras[title_lang]:
                        dataset_title = extras[title_lang]

                        # Generate title prefix
                        dir3 = _get_dir3(data)
                        if dir3:
                            dataset_title = dir3 + '-' + dataset_title

                        data[key] = munge.munge_title_to_name(dataset_title)

                        log.debug('[multilanguage_url] Created name "%s" for package from language %s',
                                  data[key], l)
                        break

    def _get_organization(data, key):
        organization = None
        field_prefix = field['organization_field']
        organization_prefix = field['organization_prefix']
        extras = data.get(key[:-1] + ('__extras',), {})
        publisher_id = data.get((field_prefix,))
        if not publisher_id and field_prefix in extras:
            publisher_id = extras[field_prefix]

        if publisher_id and organization_prefix:
            organization = h.get_organization(publisher_id)
            if not organization:
                organization = toolkit.get_action('dge_organization_publisher')(
                    {'model': model}, {'id': publisher_id})
        return organization

    def _get_dir3(data, key):
        organization_prefix = field['organization_prefix']
        organization = _get_organization(data, key)
        log.debug('[_get_dir3]  organization_prefix %s organization  %s', organization_prefix, organization)
        if organization and organization['extras']:
            for extra in organization['extras']:
                if extra['key'] == organization_prefix and extra['state'] == 'active':
                    return extra['value'].lower()
                    break

    def _get_dir3_history(data, key):
        dir3_history = []
        organization_prefix = field['organization_prefix']
        organization = _get_organization(data, key)
        organization_id = organization['id'] if 'id' in list(organization.keys(
        )) else None

        if organization and organization_id:
            result = model.Session.execute("""SELECT distinct value FROM group_extra_revision
            WHERE group_id = '{organization_id}'
            AND "key" = '{organization_prefix}'""".format(organization_id=organization_id, organization_prefix=organization_prefix))
            if result:
                for value in result:
                    dir3_history.append(value[0].lower())
        return dir3_history

    return validator


"""
FIELD TYPE DATE PERIOD
"""


@scheming_validator
def date_period(field, schema):
    required = field.get('required', False)
    header = '[date_period VALIDATOR]'
    def validator(key, data, errors, context):
        """
        1. a JSON with dates, eg.
           {"1": {"to": "2016-05-28T00:00:00", "from": "2016-05-11T00:00:00"}}
        2. separate fields per date and time (for form submissions):
           fieldname-from-date-1 = "2012-09-11"
           fieldname-from-time-1 = "11:00"
           fieldname-from-date-2 = "2014-03-03"
           fieldname-from-time-2 = "09:45"
        """
        log.debug('{} validating. Key: {} required: {}'.format(header, key, required))
        
        # just in case there was an error before that validator
        if errors[key]:
            return
        
        value = data[key]

        # 1. json
        if value is not missing:
            if isinstance(value, str):
                try:
                    value = json.loads(value)
                except ValueError as e:
                    errors[key].append(
                        _('Invalid field structure, it is not a valid JSON'))
                    return
            if not isinstance(value, dict):
                errors[key].append(_('Expecting valid JSON value'))
                return

            out = {}
            for element in sorted(value):
                dates = value.get(element)
                with_date = False
                if 'from' in dates:
                    try:
                        date = validate_date(dates['from'])
                        with_date = True
                    except (TypeError, ValueError) as e:
                        errors[key].append(
                            _('From value: Date format incorrect'))
                        continue
                if 'to' in dates:
                    try:
                        date = validate_date(dates['to'])
                        with_date = True
                    except (TypeError, ValueError) as e:
                        errors[key].append(
                            _('To value: Date format incorrect'))
                        continue

                if not with_date:
                    errors[key].append(_('Date period without from and to'))
                    continue
                out[str(element)] = dates

            if not errors[key]:
                data[key] = json.dumps(out)

            return

        # 3. separate fields
        found = {}
        short_prefix = key[-1] + '-'
        prefix = key[-1] + '-date-'
        extras = data.get(key[:-1] + ('__extras',), {})

        datetime_errors = False
        valid_indexes = []
        for name, text in extras.items():
            if not name.startswith(prefix):
                continue
            if not text:
                continue

            datetime = text
            # Get time if exists
            index = name.split('-')[-1]
            type_field = name.split('-')[-2]
            time_value = extras.get(
                short_prefix + 'time-' + type_field + '-' + index)
            # Add the time
            if time_value:
                datetime = text + ' ' + time_value

            # Create datetime and validation
            try:
                date = h.date_str_to_datetime(datetime)
                valid_indexes.append(index)
            except (TypeError, ValueError) as e:
                errors[key].append(_('Date time format incorrect'))
                datetime_errors = True

        if datetime_errors:
            return

        valid_indexes = sorted(list(set(valid_indexes)))
        new_index = 1
        for index in valid_indexes:
            period = {}

            # Get from
            date_from_value = extras.get(short_prefix + 'date-from-' + index)
            if date_from_value:
                datetime = date_from_value
                time_from_value = extras.get(
                    short_prefix + 'time-from-' + index)
                if time_from_value:
                    datetime = date_from_value + " " + time_from_value
                try:
                    date = h.date_str_to_datetime(datetime)
                    period['from'] = date.strftime("%Y-%m-%dT%H:%M:%S")
                except (TypeError, ValueError) as e:
                    continue

            date_to_value = extras.get(short_prefix + 'date-to-' + index)
            if date_to_value:
                datetime = date_to_value
                time_to_value = extras.get(short_prefix + 'time-to-' + index)
                if time_to_value:
                    datetime = date_to_value + " " + time_to_value
                try:
                    date = h.date_str_to_datetime(datetime)
                    period['to'] = date.strftime("%Y-%m-%dT%H:%M:%S")
                except (TypeError, ValueError) as e:
                    continue

            if period:
                found[new_index] = period
                # only adds 1 to the new index with good periods
                new_index = new_index + 1

        out = {}
        for i in sorted(found):
            out[i] = found[i]
        
        # Avoiding storing empty dict
        if out and len(out) > 0:
            data[key] = json.dumps(out)
        
        # Ignoring missing or empty if not required
        if not required:
            ignore_missing(key, data, errors, context)
            ignore_empty(key, data, errors, context)

    return validator


def date_period_output(value):
    """
    Return stored json representation as a dict, if
    value is already a dict just pass it through.
    """
    if isinstance(value, dict):
        return value
    if value is None or isinstance(value, list):
        return {}
    try:
        return json.loads(value)
    except ValueError:
        return {}


"""
VALIDATOR FOR FLUENT TEXT
"""


def multiple_one_value(key, data, errors, context):
    header = '[multiple_one_value VALIDATOR]'
    log.debug('{} validating. Key: {}'.format(header, key))
    if errors[key]:
        return

    values = []
    languages = []
    value = data[key]
    if value is not missing:
        if isinstance(value, str):
            try:
                value = json.loads(value)
            except ValueError:
                errors[key].append(_('Failed to decode JSON string'))
                return
            except UnicodeDecodeError:
                errors[key].append(_('Invalid encoding for JSON string'))
                return
        if not isinstance(value, dict):
            errors[key].append(_('Expecting JSON object'))
            return

        for lang, text in value.items():
            try:
                m = re.match(ds_constants.ISO_639_LANGUAGE, lang)
            except TypeError:
                errors[key].append(_('Invalid type for language code: %r')
                                   % lang)
                continue

            languages += [lang]
            if not isinstance(text, str):
                errors[key].append(_('Invalid type for "%s" value') % lang)
                continue
            if isinstance(text, str) or isinstance(text, str):
                try:
                    if text.strip():
                        values += [lang]
                except UnicodeDecodeError:
                    errors[key].append(_('Invalid encoding for "%s" value')
                                       % lang)

        if not values:
            for lang in languages:
                errors[key[:-1] + (key[-1] + '-' + lang,)
                       ] = [_('Missing value')]

        return

    prefix = key[-1] + '-'
    extras = data.get(key[:-1] + ('__extras',), {})

    for name, text in extras.items():
        if not isinstance(name, str) or not name.startswith(prefix):
            continue

        lang = name.split('-', 1)[1]
        m = re.match(ds_constants.ISO_639_LANGUAGE, lang)
        if not m:
            errors[name] = [_('Invalid language code: "%s"') % lang]
            values = None
            continue

        languages += [lang]
        if text:
            name_key = name.split('-', 1)[0]
            if name_key == ds_constants.DEFAULT_TITLE_FIELD and lang == ds_constants.DEFAULT_LANGUAGE:
                data[('title',)] = text
            values += [lang]

    if not values:
        for lang in languages:
            errors[key[:-1] + (key[-1] + '-' + lang,)] = [_('Missing value')]


"""
Multiple tags validator
"""


@scheming_validator
def multiple_tags(field, *args):
    header = '[multiple_tags validator]'
    log.debug('{} decorator.'.format(header))

    def validator(key, data, errors, context):
        log.debug('{} validating.'.format(header))
        tags = []
        for lang in field['fluent_form_placeholder']:
            key_lang = 'tag_string-' + lang
            data[key_lang] = [ti.strip()
                              for ti in data[('__extras',)].get(key_lang, '').split(',')
                              if ti.strip()]
            tags += data[key_lang]
            tag_string_convert(key_lang, data, errors, context)

        data[key] = ','.join(tags)
        log.debug('{} done validating. data[key]: {}'.format(
            header, data[key]))

    return validator


"""
CHECK REQUIRED LANGUAGE
"""


@scheming_validator
def multiple_required_language(field, schema):
    header = '[multiple_required_language VALIDATOR]'
    def validator(key, data, errors, context):
        log.debug('{} validating. Key: {}'.format(header, key))
        if errors[key]:
            return

        values = []
        languages = []

        required_language = field['required_language']
        if not required_language:
            required_language = config.get('ckan.locale_default', 'es')

        required_field = field.get('required')
        if not required_field:
            required_field = False

        value = data[key]
        if value is not missing:
            if isinstance(value, str):
                try:
                    value = json.loads(value)
                except ValueError:
                    errors[key].append(_('Failed to decode JSON string'))
                    return
                except UnicodeDecodeError:
                    errors[key].append(_('Invalid encoding for JSON string'))
                    return
            if not isinstance(value, dict):
                errors[key].append(_('Expecting JSON object'))
                return

            for lang, text in value.items():
                try:
                    m = re.match(ds_constants.ISO_639_LANGUAGE, lang)
                except TypeError:
                    errors[key].append(_('Invalid type for language code: %r')
                                       % lang)
                    continue

                # Register the language
                languages += [lang]
                if not isinstance(text, str):
                    errors[key].append(_('Invalid type for "%s" value') % lang)
                    continue
                if isinstance(text, str) or isinstance(text, str):
                    try:
                        # Not register empty values
                        if text.strip():
                            values += [lang]
                    except UnicodeDecodeError:
                        errors[key].append(_('Invalid encoding for "%s" value')
                                           % lang)

            if values and not required_language in values:
                errors[key[:-1] + (key[-1] + '-' + required_language,)
                       ] = [_('Missing required language value')]
            else:
                if not values and required_field:
                    errors[key[:-1] + (key[-1] + '-' + required_language,)
                           ] = [_('Missing required language value')]

            return

        prefix = key[-1] + '-'
        extras = data.get(key[:-1] + ('__extras',), {})

        for name, text in extras.items():
            if not isinstance(name, str) or not name.startswith(prefix):
                continue

            lang = name.split('-', 1)[1]
            m = re.match(ds_constants.ISO_639_LANGUAGE, lang)
            if not m:
                errors[name] = [_('Invalid language code: "%s"') % lang]
                values = None
                continue

            languages += [lang]
            if text:
                values += [lang]

        if values and not required_language in values:
            errors[key[:-1] + (key[-1] + '-' + required_language,)
                   ] = [_('Missing required language value')]
        else:
            if not values and required_field:
                errors[key[:-1] + (key[-1] + '-' + required_language,)
                       ] = [_('Missing required language value')]

    return validator


"""
VALIDATOR FOR PUBLISHER FIELD
"""


@scheming_validator
def select_organization(field, schema):
    organization_prefix = field['organization_prefix']
    publisher_uri_prefix = field['publisher_uri_prefix']
    header = '[select_organization VALIDATOR]'
    def validator(key, data, errors, context):
        log.debug('{} validating. Key: {}'.format(header, key))
        value = data.get(key)
        
        if value is missing or value is None:
            if not authz.check_config_permission('create_unowned_dataset'):
                raise Invalid(_('A organization must be supplied'))
            data.pop(key, None)
            raise df.StopOnError

        model = context['model']
        user = context['user']
        user = model.User.get(user)
        if value == '':
            if not authz.check_config_permission('create_unowned_dataset'):
                raise Invalid(_('A organization must be supplied'))
            return

        group = model.Group.get(value)
        if not group:
            raise Invalid(_('Organization does not exist'))
        group_id = group.id
        organization = h.get_organization(group.id)
        org_dir3 = None
        if not organization:
                organization = toolkit.get_action('dge_organization_publisher')(
                    {'model': model}, {'id': group.id})
        if organization and organization['extras']:
            for extra in organization['extras']:
                if extra['key'] == organization_prefix and extra['state'] == 'active':
                    org_dir3 = extra['value'].upper()
                    
        if org_dir3:
            data[ds_constants.PUBLISHER_URI_KEY] = publisher_uri_prefix + org_dir3
        else:
            raise Invalid(_('Organization does not exist or is not active'))
        
        data[key] = group_id
                

    return validator


"""
PACKAGE VALIDATOR TO AVOID SPECIAL CHARS SCRIPTING
"""


@scheming_validator
def tags_html_detected(field, schema):
    from bs4 import BeautifulSoup

    def validator(key, data, errors, context):
        if errors[key] or 'resources' in str(data):
            return

        value = data.get(key)
        languages = []
        prefix = key[0]

        extras = data.get(('__extras',), {})

        for name, text in extras.items():
            if not name.startswith(prefix):
                continue
            if text:
                soup = BeautifulSoup(text, 'html.parser')
                if len(soup.find_all()) > 0 and name.split('-')[0] == prefix:
                    language = config.get('ckan.locale_order')
                    suffix = name.split('-')[1]
                    if suffix in language:
                        errors[(prefix + '-' + suffix,)
                               ] = ['Contiene tag(s) HTML']
                    else:
                        errors[(prefix,)] = ['Contiene tag(s) HTML']

        if value is not missing:
            soup = BeautifulSoup(value, 'html.parser')
            if len(soup.find_all()) > 0:
                errors[key].append('Contiene tag(s) HTML')

    return validator


"""
PACKAGE VALIDATOR TO ENCODE SPECIAL CHARS
"""


@scheming_validator
def url_encode(field, schema):
    def validator(key, data, errors, context):
        value = data[key]

        if value is not missing:
            value = _url_encode(value)
        data[key] = value

    return validator


def _url_encode(url):

    unquote_url = urllib.parse.unquote((url).encode('utf-8'))
    unquote = urllib.parse.unquote((unquote_url).decode('utf-8'))
    parsed_url = urllib.parse.urlparse(unquote.encode('utf-8').strip())

    netloc_m = netloc_re.match(parsed_url.netloc)
    username, password, host, port = (
        urllib.parse.quote(g) if g else g for g in netloc_m.groups())
    netloc = ('{}:{}@'.format(username, password) if username and password else '') + \
        host + (':' + port if port else '')

    path = urllib.parse.quote(parsed_url.path)

    query = [(k, urllib.parse.quote(v)) for k, v in urllib.parse.parse_qsl(
        parsed_url.query.replace(';', urllib.parse.quote(';')), keep_blank_values=True)]
    query = '&'.join(
        [qi[0] + ('=' + qi[1] if qi[1] else '') for qi in query])

    return urllib.parse.urlunparse((parsed_url.scheme, netloc, path,
                                parsed_url.params, query, parsed_url.fragment))


"""
PACKAGE VALIDATOR TO ENCODE SPECIAL CHARS
"""


@scheming_validator
def multiple_url_encode(field, schema):
    def validator(key, data, errors, context):
        value = json.loads(data[key])

        log.debug('[multiple_url_encode] values "%s"', value)

        if not isinstance(value, list):
            raise Exception()

        value = json.dumps([_url_encode(url) for url in value])

        data[key] = value

    return validator

"""
PACKAGE VALIDATOR TO ENSURE ONE OF THE REQUIRED SUBFIELDS IS INCLUDED
"""

@scheming_validator
def at_least_one_required(field, schema):
    required_list = field['required_list'] if 'required_list' in field else False
    header = '[at_least_one_required VALIDATOR]'
    def validator(key, data, errors, context):
        """
        Check if one of the subfields in required_list is at least included
        """
        log.debug('{} validating. Key: {}'.format(header, key))
        value = data[key]
        
        if value is not missing:
            if isinstance(value, str):
                try:
                    value = json.loads(value)
                except ValueError:
                    errors[key].append(_('Failed to decode JSON string'))
                    return
                except UnicodeDecodeError:
                    errors[key].append(_('Invalid encoding for JSON string'))
                    return
            if not isinstance(value, dict):
                errors[key].append(_('Expecting JSON object'))
                return
            
            has_at_least_one_required = any(value.get(required_item) for required_item in required_list)
            if not has_at_least_one_required:
                errors[key].append(_('At least of of the following subfields must be included: has_email, has_url'))

    return validator

"""
RESOURCE VALIDATOR TO TRANSFORM NTI FORMAT VALUES INTO MEDIA_TYPE
"""

@scheming_validator
def format_to_media_type(field, schema):
    header = '[format_to_media_type VALIDATOR]'
    def validator(key, data, errors, context):
        """
        Obtaining the format value and store it in extra media_type as an IANA URI if NTI Profile
        """
        log.debug('{} validating. Key: {}'.format(header, key))
        
        for data_key in data:
            if len(data_key) == 3 and data[data_key] == ds_constants.APPLICATION_PROFILE_KEY:
                data_key_index = data_key[1]
                data_profile_value_key = ('extras', data_key_index, 'value')
                if data[data_profile_value_key] == ds_constants.DCATAPES_100:
                    break
        
        value = data[key]
        if value is not missing:
            if isinstance(value, str):
                if len(key) == 3 and key[0] == ds_constants.RESOURCE_KEY:
                    media_type_key = (ds_constants.RESOURCE_KEY, key[1], ds_constants.MEDIA_TYPE_KEY)
                    if media_type_key in data:
                        if data[media_type_key] is None or data[media_type_key] is missing:
                            data[media_type_key] = ds_constants.FORMAT_PREFIX_EDP_IANA + value
        
    return validator

"""
MULTILANGUAGE_TAGS
OVERWRITES CKANEXT-FLUENT 'FLUENT_TAGS' VALIDATOR IN ORDER TO LET MISSING OR EMPTY FIELDS IF NOT REQUIRED
"""

@scheming_validator
def multilanguage_tags(field, schema):
    """
    Accept multilingual lists of tags in the following forms
    and convert to a json string for storage.

    1. a multilingual dict of lists of tag strings, eg.

       {"en": ["big", "large"], "fr": ["grande"]}

    2. separate fields per language with comma-separated values
       (for form submissions)

       fieldname-en = "big,large"
       fieldname-fr = "grande"

    Validation of each tag is performed with validators
    tag_length_validator and tag_name_validator. When using
    ckanext-scheming these may be overridden with the
    "tag_validators" field value
    """
    required = field.get('required', False)
    header = '[multilanguage_tags VALIDATOR]'
    required_langs = []
    alternate_langs = {}
    if field and field.get('required'):
        required_langs = fluent_form_languages(field, schema=schema)
        alternate_langs = fluent_alternate_languages(field, schema=schema)

    tag_validators = [tag_length_validator, tag_name_validator]
    if field and 'tag_validators' in field:
        tag_validators = validators_from_string(
            field['tag_validators'], field, schema)

    def validator(key, data, errors, context):
        log.debug('{} validating. Key: {} required: {}'.format(header, key, required))
        
        # just in case there was an error before that validator
        if errors[key]:
            return

        value = data[key]
        # 1. dict of lists of tag strings
        if value is not missing:
            if not isinstance(value, dict):
                errors[key].append(_('expecting JSON object'))
                return

            for lang, keys in value.items():
                try:
                    m = re.match(BCP_47_LANGUAGE, lang)
                except TypeError:
                    errors[key].append(_('invalid type for language code: %r')
                        % lang)
                    continue
                if not m:
                    errors[key].append(_('invalid language code: "%s"') % lang)
                    continue
                if not isinstance(keys, list):
                    errors[key].append(_('invalid type for "%s" value') % lang)
                    continue
                out = []
                for i, v in enumerate(keys):
                    if not isinstance(v, six.string_types):
                        errors[key].append(
                            _('invalid type for "{lang}" value item {num}').format(
                                lang=lang, num=i))
                        continue

                    if isinstance(v, str):
                        try:
                            out.append(v if six.PY3 else v.decode(
                                'utf-8'))
                        except UnicodeDecodeError:
                            errors[key]. append(_(
                                'expected UTF-8 encoding for '
                                '"{lang}" value item {num}').format(
                                    lang=lang, num=i))
                    else:
                        out.append(v)

                tags = []
                errs = []
                for tag in out:
                    newtag, tagerrs = _validate_single_tag(tag, tag_validators)
                    errs.extend(tagerrs)
                    tags.append(newtag)
                if errs:
                    errors[key].extend(errs)
                value[lang] = tags

            for lang in required_langs:
                if value.get(lang) or any(
                        value.get(l) for l in alternate_langs.get(lang, [])):
                    continue
                errors[key].append(_('Required language "%s" missing') % lang)

            if not errors[key]:
                data[key] = json.dumps(value)
            return

        # 2. separate fields
        output = {}
        prefix = key[-1] + '-'
        extras = data.get(key[:-1] + ('__extras',), {})

        for name, text in extras.items():
            if not name.startswith(prefix):
                continue
            lang = name.split('-', 1)[1]
            m = re.match(BCP_47_LANGUAGE, lang)
            if not m:
                errors[name] = [_('invalid language code: "%s"') % lang]
                output = None
                continue

            if not isinstance(text, six.string_types):
                errors[name].append(_('invalid type'))
                continue

            if isinstance(text, str):
                try:
                    text = text if six.PY3 else text.decode(
                        'utf-8')
                except UnicodeDecodeError:
                    errors[name].append(_('expected UTF-8 encoding'))
                    continue

            if output is not None and text:
                tags = []
                errs = []
                for tag in text.split(','):
                    newtag, tagerrs = _validate_single_tag(tag, tag_validators)
                    errs.extend(tagerrs)
                    tags.append(newtag)
                output[lang] = tags
                if errs:
                    errors[key[:-1] + (name,)] = errs

        for lang in required_langs:
            if extras.get(prefix + lang) or any(
                    extras.get(prefix + l) for l in alternate_langs.get(lang, [])):
                continue
            errors[key[:-1] + (key[-1] + '-' + lang,)] = [_('Missing value')]
            output = None

        if output is None:
            return

        for lang in output:
            del extras[prefix + lang]
        
        # Avoiding storing empty dict
        if output and len(output) > 0:
            data[key] = json.dumps(output)
        
        # Ignoring missing or empty if not required
        if not required:
            ignore_missing(key, data, errors, context)
            ignore_empty(key, data, errors, context)

    return validator


"""
MULTIPLE_THEME_CHOICE
OVERWRITES CKANEXT-SCHEMING 'SCHEMING_MULTIPLE_CHOICE' VALIDATOR IN ORDER TO LET:
    - MISSING OR EMPTY FIELDS IF NOT REQUIRED
    - VOCABULARY http://inspire.ec.europa.eu/theme URIs
    - VOCABULARY http://publications.europa.eu/resource/authority/data-theme/ URIs
"""

@scheming_validator
@register_validator
def multiple_theme_choice(field, schema):
    required = field.get('required', False)
    header = '[multiple_theme_choice VALIDATOR]'
    theme_choice_order = [c['value'] for c in ds_constants.DATOSGOB_DCT_THEME_CHOICES]
    theme_choice_values = set(theme_choice_order)

    def validator(key, data, errors, context):
        log.debug('{} validating. Key: {} required: {}'.format(header, key, required))
        # if there was an error before calling our validator
        # don't bother with our validation
        if errors[key]:
            return
        
        # If updating or adding new distributions to an existing dataset
        if data[key] is missing and ('__junk',) in data:
            junk = data.get(('__junk',), {})
            junk_dict_list = {}
            for junk_key, junk_value in junk.items():
                if isinstance(junk_key, tuple) and len(junk_key) == 3:
                    base, index, subfield = junk_key
                    if base == 'theme':
                        if index not in junk_dict_list:
                            junk_dict_list[index] = {}
                        junk_dict_list[index][subfield] = junk_value
            junk_dict_list = [v for _, v in sorted(junk_dict_list.items())]
            data[key] = json.dumps(junk_dict_list)
            del data[('__junk',)]
            return
        
        if not required:
            ignore_missing(key, data, errors, context)
            ignore_empty(key, data, errors, context)

        value = data[key]
        extras = data.get(key[:-1] + ('__extras',), {})
        
        if value is not missing:
            if extras:
                # If creating new dataset and before adding distributions
                ckan_phase = extras['_ckan_phase'] if '_ckan_phase' in extras else None
                dataset_state = data[('state',)] if ('state',) in data else None
                if ckan_phase == 'dataset_new_1' or dataset_state == 'draft':
                    if isinstance(value, str) and not value.startswith('['):
                        value = [value]
                    if isinstance(value, list):
                        data[key] = json.dumps(value)
                    return
            
            if isinstance(value, six.string_types):
                value = [value]
            elif not isinstance(value, list):
                errors[key].append(_('expecting list of strings'))
                return
        else:
            value = []

        choice_values = theme_choice_values
        if not choice_values:
            choice_order = [
                choice.get('value')
                for choice in scheming_field_choices(field) or [] if choice.get('value')
            ]
            choice_values = set(choice_order)

        is_dcatapes = dh.dge_is_dcatapes_application_profile(data)
        
        selected = set()
        vocabularies_uris = []
        for element in value:
            is_datosgobes_uri = True
            if is_dcatapes:
                is_datosgobes_uri = dh.dge_is_datosgobes_theme_uri(element)
            if is_datosgobes_uri:
                if element in choice_values:
                    selected.add(element)
                    continue
                errors[key].append(_('unexpected choice "%s"') % element)
            else:
                vocabularies_uris.append(element)

        if not errors[key]:
            datosgobes_themes_list = [v for v in (theme_choice_order if theme_choice_values else choice_order) if v in selected]
            if is_dcatapes:
                themes_list = datosgobes_themes_list + vocabularies_uris
                data[key] = json.dumps(themes_list)
            else:
                data[key] = json.dumps(datosgobes_themes_list)

            if field.get('required') and not selected:
                errors[key].append(_('Select at least one'))

    return validator


"""
ALLOW_EMPTY_SCHEMING_ISODATETIME
OVERWRITES CKANEXT-SCHEMING 'SCHEMING_ISODATETIME' VALIDATOR IN ORDER TO LET MISSING OR EMPTY FIELDS IF NOT REQUIRED
"""

@scheming_validator
@register_validator
def allow_empty_scheming_isodatetime(field, schema):
    required = field.get('required', False)
    header = '[allow_empty_scheming_isodatetime VALIDATOR]'
    def validator(key, data, errors, context):
        log.debug('{} validating. Key: {} required: {}'.format(header, key, required))
        
        value = data[key]
        date = None

        if value:
            return validate_date(value)
            '''
            if isinstance(value, datetime.datetime):
                return value
            else:
                try:
                    date = h.date_str_to_datetime(value)
                except (TypeError, ValueError) as e:
                    raise Invalid(_('Date format incorrect'))
            '''
        else:
            extras = data.get(('__extras',))
            if not extras or (key[0] + '_date' not in extras and
                              key[0] + '_time' not in extras):
                if field.get('required'):
                    not_empty(key, data, errors, context)
            else:
                date = validate_date_inputs(
                    field, key, data, extras, errors, context)

        data[key] = date
        
        if not required:
            ignore_missing(key, data, errors, context)
            ignore_empty(key, data, errors, context)

    return validator

def validate_date(value):
    if value:
        if isinstance(value, datetime.datetime):
            return value
        else:
            try:
                if is_year(value) or is_year_month(value) or is_date(value):
                    return value
            except TypeError:
                raise Invalid(_("Dates must be provided as strings or datetime objects"))
            try:
                parse_date(value)
            except ValueError:
                raise Invalid(
                    _("Date format incorrect. Supported formats are YYYY, YYYY-MM, YYYY-MM-DD and YYYY-MM-DDTHH:MM:SS")
                )
    

"""
VALIDATOR FOR DCT:SPATIAL IN BOTH NTI AND DCATAPES PROFILES
"""
@scheming_validator
@register_validator
def multiple_select_spatial(field, schema):
    required = field.get('required', False)
    header = '[multiple_select_spatial VALIDATOR]'
    spatial_choice_order = [c['value'] for c in ds_constants.DATOSGOB_DCT_SPATIAL_CHOICES]
    spatial_choice_values = set(spatial_choice_order)
    
    def validator(key, data, errors, context):
        log.debug('{} validating. Key: {}'.format(header, key))
        
        if errors[key]:
            return
        
        # If updating or adding new distributions to an existing dataset
        if data[key] is missing and ('__junk',) in data:
            junk = data.get(('__junk',), {})
            junk_dict_list = {}
            for junk_key, junk_value in junk.items():
                if isinstance(junk_key, tuple) and len(junk_key) == 3:
                    base, index, subfield = junk_key
                    if base == 'spatial':
                        if index not in junk_dict_list:
                            junk_dict_list[index] = {}
                        junk_dict_list[index][subfield] = junk_value
            junk_dict_list = [v for _, v in sorted(junk_dict_list.items())]
            data[key] = json.dumps(junk_dict_list)
            del data[('__junk',)]
            return
        
        if not required:
            ignore_missing(key, data, errors, context)
            ignore_empty(key, data, errors, context)

        value = data[key]
        extras = data.get(key[:-1] + ('__extras',), {})

        if value is not missing:
            if extras:
                # If creating new dataset and before adding distributions
                ckan_phase = extras['_ckan_phase'] if '_ckan_phase' in extras else None
                dataset_state = data[('state',)] if ('state',) in data else None
                if ckan_phase == 'dataset_new_1' or dataset_state == 'draft':
                    if isinstance(value, str) and not value.startswith('['):
                        value = [value]
                    if isinstance(value, list):
                        data[key] = json.dumps(value)
                    return

            if isinstance(value, str) and value.startswith('['):
                try:
                    value = json.loads(value)
                except ValueError:
                    errors[key].append(_('Failed to decode JSON string'))
                    return
                except UnicodeDecodeError:
                    errors[key].append(_('Invalid encoding for JSON string'))
                    return
            elif isinstance(value, str):
                value = [value]
            if not isinstance(value, list):
                errors[key].append(_('Expecting JSON object'))
                return
        else:
            value = []

        application_profile = dh.dge_get_application_profile(data)
        
        if value:
            selected = set()
            spatial_uris = []
            if application_profile and application_profile == ds_constants.NTI:
                spatial_uris = [s['uri'] for s in value]
            elif not application_profile:
                if isinstance(value, list) and all(isinstance(item, dict) for item in value):
                    spatial_uris = [s['uri'] for s in value]
                else:
                    spatial_uris = value
                
            for spatial_uri in spatial_uris:
                if spatial_uri in spatial_choice_values:
                    selected.add(spatial_uri)
                    continue
                errors[key].append(_('unexpected choice "%s"') % spatial_uri)

            if not errors[key] and len(selected) > 0:
                if not application_profile == ds_constants.DCATAPES_100:
                    out = [{'uri': spatial_choice, 'geometry': '', 'bbox': '', 'centroid': ''} for spatial_choice in spatial_choice_order if spatial_choice in selected]
                    data[key] = json.dumps(out)

                    if field.get('required') and not selected:
                        errors[key].append(_('Select at least one'))            
                else:
                    out = value
                    data[key] = json.dumps(out)
                
    return validator


def _unique_identifier(identifier_value, data, key, errors):
    '''
    Validates if dct:identifier is unique in current dataset
    '''
    header = '[unique_identifier VALIDATOR]'
    log.debug('{} validating. Key: {}'.format(header, key))
    if identifier_value:
        if isinstance(identifier_value, str):
            identifier_value = json.loads(identifier_value)
        if not isinstance(identifier_value, list):
            raise Exception()
        key_to_check = ('id',)
        if key_to_check in data:
            package_id = data[('id',)]
            for identifier in identifier_value:
                _check_identifier(errors, key, identifier, package_id)
        else:
            for identifier in identifier_value:
                _check_identifier(errors, key, identifier, None)


def _check_identifier(errors, key, identifier_value, package_id=None):
    '''
    Checks if the dct:identifier already exists in database.
    Adds an error message if true
    '''
    from ckan.model import PackageExtra, Package
    
    query = '''
            select pe.package_id
            from public.package_extra pe
            where pe.key = 'identifier'
            and '{p0}' = any (select json_array_elements_text(pe.value::json));
            '''.format(p0=identifier_value)
    results = model.Session.execute(query).fetchall()

    if results and len(results) > 0:
        packages = [result[0] for result in results]
        active_packages = model.Session.query(Package).filter(
            Package.id.in_(packages)).filter_by(state='active')
        if active_packages.count() > 0:
            if package_id:
                for package in active_packages:
                    if package_id != package.id:
                        errors[key].append(
                            (f'El campo identificador (dct:identifier) debe ser \u00FAnico. Actualmente existe un dataset con el identificador: {identifier_value}'))
                        raise StopOnError
            else:
                if active_packages.count() > 0:
                    errors[key].append(
                        (f'El campo identificador (dct:identifier) debe ser \u00FAnico. Actualmente existe un dataset con el identificador: {identifier_value}'))
                    raise StopOnError

@scheming_validator
@register_validator
def dge_scheming_multiple_text(field, schema):
    """
    Accept repeating text input in the following forms and convert to a json list
    for storage. Also act like scheming_required to check for at least one non-empty
    string when required is true:

    1. a list of strings, eg.

       ["Person One", "Person Two"]

    2. a single string value to allow single text fields to be
       migrated to repeating text

       "Person One"
    """
    required = field.get('required', False)
    unique = field.get('unique', False)
    header = '[dge_scheming_multiple_text VALIDATOR]'
    def _dge_scheming_multiple_text(key, data, errors, context):
        log.debug('{} validating. Key: {}'.format(header, key))
        # just in case there was an error before our validator,
        # bail out here because our errors won't be useful
        if errors[key]:
            return

        value = data[key]
        # 1. list of strings or 2. single string
        if value is not missing:
            if isinstance(value, six.string_types):
                value = [value]
            if not isinstance(value, list):
                errors[key].append(_('expecting list of strings'))
                raise StopOnError

            out = []
            for element in value:
                if not element:
                    continue

                if not isinstance(element, six.string_types):
                    errors[key].append(_('invalid type for repeating text: %r')
                                       % element)
                    continue
                if isinstance(element, six.binary_type):
                    try:
                        element = element.decode('utf-8')
                    except UnicodeDecodeError:
                        errors[key]. append(_('invalid encoding for "%s" value')
                                            % element)
                        continue

                out.append(element)

            if errors[key]:
                raise StopOnError
            
            # Avoiding storing empty lists
            if out and len(out) > 0:
                if unique:
                    _unique_identifier(out, data, key, errors)
                data[key] = json.dumps(out)

        if (data[key] is missing or data[key] == '[]' or not data[key]) and required:
            errors[key].append(_('Missing value'))
            raise StopOnError
        
        # Ignoring missing or empty if not required
        if not required:
            ignore_missing(key, data, errors, context)
            ignore_empty(key, data, errors, context)

    return _dge_scheming_multiple_text