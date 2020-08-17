# -*- coding: utf-8 -*-
# Copyright (c) 2020, Leam Technology Systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import json

import frappe
from frappe import _
from frappe.model.document import Document
from six import string_types
import numbers


class EditorjsTemplate(Document):

  def validate_block(self, data: str):
    """
    Validates the data used against a template. This method returns nothing, and will only raise exceptions if there
    are errors
    :param data: The data used against the template. Expected a strigified JSON object
    :return: None
    """
    template_doc = frappe.get_doc('Editorjs Template', self.name)

    # Parse the data field in the block
    _data: dict = json.loads(data)

    # Check if the data is not None
    if not _data:
      frappe.throw(_("Invalid Data"))
    else:
      # Get all the keys in the template
      template_keys = list(map(lambda x: x.key, template_doc.data))
      # Check if all keys in data exist as required by the template
      keys_exist = all([x in template_keys for x in _data])
      if not keys_exist:
        frappe.throw(
            _("Some keys are missing. Keys required are: {template_keys}\n Provided keys are {data_keys}".format(
                template_keys=', '.join(template_keys), data_keys=_data.keys())))

      # Validate the types of each value in the dict
      for k, v in _data.items():
        self._check_type(k, v)

  def _check_type(self, k: str, v: str):
    """
    Throws an error if the types don't match. If there are no errors, nothing is returned
    :param k: The key within the data
    :param v: The value of the key
    :return: None
    """
    types = list(filter(lambda x: x.key == k, self.data))
    is_correct_type = False
    _type = types[0].get('type')
    if _type == 'String':
      is_correct_type = isinstance(v, string_types)
    elif _type == 'Number':
      is_correct_type = isinstance(v, numbers.Number)
    # TODO: Check the object deeply
    elif _type == 'Object':
      is_correct_type = isinstance(v, dict)
    elif _type == 'List':
      is_correct_type = isinstance(v, list)
    elif _type == 'Boolean':
      is_correct_type = isinstance(v, bool)

    if not is_correct_type:
      frappe.throw(_(
          "Wrong type for key: {k}. Should be {correct_type} instead of {given_type}".format(k=k, correct_type=_type,
                                                                                             given_type=type(v))))
