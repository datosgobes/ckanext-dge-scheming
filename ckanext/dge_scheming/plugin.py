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

import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.lib.helpers as h
import ckanext.scheming.helpers as sh

from ckanext.dge_scheming import validators, helpers
from ckantoolkit import (
    check_ckan_version,
)

log = logging.getLogger(__name__)

class DgeSchemingPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IValidators, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IResourceController, inherit=True)

    # #########################################################################
    # #########################################################################
    # IConfigurer
    # #########################################################################
    # #########################################################################
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')

    # #########################################################################
    # #########################################################################
    # IValidators
    # #########################################################################
    # #########################################################################
    def get_validators(self):
        return {
            'uri_text': validators.uri_text,
            'uri_text_output': validators.uri_text_output,
            'date_frequency': validators.date_frequency,
            'date_frequency_output': validators.date_frequency_output,
            'date_period': validators.date_period,
            'date_period_output': validators.date_period_output,
            'multilanguage_url': validators.multilanguage_url,
            'multiple_uri_text': validators.multiple_uri_text,
            'multiple_uri_text_output': validators.multiple_uri_text_output,
            'multiple_required_language': validators.multiple_required_language,
            'multiple_one_value': validators.multiple_one_value,
            'select_organization': validators.select_organization,
            'tags_html_detected': validators.tags_html_detected,
            'url_encode': validators.url_encode,
            'multiple_url_encode': validators.multiple_url_encode,
            'at_least_one_required': validators.at_least_one_required,
            'format_to_media_type': validators.format_to_media_type,
            'multilanguage_tags': validators.multilanguage_tags,
            'multiple_theme_choice': validators.multiple_theme_choice,
            'allow_empty_scheming_isodatetime': validators.allow_empty_scheming_isodatetime,
            'multiple_select_spatial': validators.multiple_select_spatial,
            'dge_scheming_multiple_text': validators.dge_scheming_multiple_text
            #'multiple_select_dataservice': validators.multiple_select_dataservice
            }

    # #########################################################################
    # #########################################################################
    # ITemplateHelpers
    # #########################################################################
    # #########################################################################
    def get_helpers(self):
        return {
            'dge_dataset_form_value': helpers.dge_dataset_form_value,
            'dge_dataset_form_lang_and_value': helpers.dge_dataset_form_lang_and_value,
            'dge_dataset_form_organization_list': helpers.dge_dataset_form_organization_list,
            'dge_multiple_field_required': helpers.dge_multiple_field_required,
            'dge_multiple_uri_field_one_required': helpers.dge_multiple_uri_field_one_required,
            'dge_dataset_license_to_distributions_license': helpers.dge_dataset_license_to_distributions_license,
            'dge_get_nti_field_choices': helpers.dge_get_nti_field_choices,
            'dge_get_application_profile': helpers.dge_get_application_profile,
            'dge_is_nti_application_profile': helpers.dge_is_nti_application_profile,
            'dge_is_dcatapes_application_profile': helpers.dge_is_dcatapes_application_profile,
            'dge_is_datosgobes_theme_uri': helpers.dge_is_datosgobes_theme_uri,
            'dge_parse_frequency_identifier': helpers.dge_parse_frequency_identifier,
            'dge_scheming_field_nti_required': helpers.dge_scheming_field_nti_required,
            'dge_get_value_from_nti_identifier': helpers.dge_get_value_from_nti_identifier,
            'dge_is_list_of_items_field_value': helpers.dge_is_list_of_items_field_value
            }


    # #########################################################################
    # #########################################################################
    # IPackageController
    # #########################################################################
    # #########################################################################
    # CKAN < 2.10 hooks
    def after_update(self, context, data_dict):
        helpers.dge_dataset_license_to_distributions_license(context, data_dict)
        
    # #########################################################################
    # #########################################################################
    # IResourceController
    # #########################################################################
    # #########################################################################
    def before_create(self, context, resource):
        return
        
    def after_create(self, context, resource):
        return
    
    
