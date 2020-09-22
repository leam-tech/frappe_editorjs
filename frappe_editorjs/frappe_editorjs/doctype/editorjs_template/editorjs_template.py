# -*- coding: utf-8 -*-
# Copyright (c) 2020, Leam Technology Systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import json
from json import JSONDecodeError

import frappe
from frappe import _
from frappe.model.document import Document
from six import string_types
import numbers


class EditorjsTemplate(Document):
  type_dict = {
      'String': string_types,
      'Number': numbers.Number,
      'Boolean': bool,
      'Object': dict,
      'List': list,
  }

  def validate_block(self, data: str):
    """
    Validates the data used against a template. This method returns nothing, and will only raise exceptions if there
    are errors
    :param data: The data used against the template. Expected a strigified JSON object
    :return: None
    """
    template_doc = frappe.get_doc('Editorjs Template', self.name)
    _data = None
    try:
      # Parse the data field in the block
      _data: dict = frappe.parse_json(frappe.parse_json(data))
    except JSONDecodeError:
      frappe.throw(_("Invalid Data while decoding"))

    # Check if the data is not None
    if _data is None or not isinstance(_data, dict):
      frappe.throw(_("Invalid Data"))
    else:
      _data_keys = _data.keys()
      # Get all the non nullable keys in the template
      non_nullable_template_keys = list(map(lambda x: x.key, list(filter(lambda x: not x.nullable, template_doc.data))))

      # Check if all keys in data exist as required by the template
      keys_exist = all([x in _data_keys for x in non_nullable_template_keys])
      if not keys_exist:
        frappe.throw(
            _("Some keys are missing. Keys required are: {template_keys}\n Provided keys are {data_keys}".format(
                template_keys=', '.join(non_nullable_template_keys), data_keys=_data.keys())))

      # Get only fields that are part of the template
      all_template_keys = list(map(lambda x: x.key, template_doc.data))

      # Validate the types of each value in the dict
      for k, v in _data.items():
        if k in all_template_keys:
          self._check_type(k, v)

  def _check_type(self, k: str, v: str):
    """
    Throws an error if the types don't match. If there are no errors, nothing is returned
    :param k: The key within the data
    :param v: The value of the key
    :return: None
    """
    types = list(filter(lambda x: x.key == k, self.data))
    _type = types[0].get('type')
    _nullable = True if types[0].get('nullable') else False

    is_correct_type = (_nullable and v is None) or isinstance(v, self.type_dict.get(_type))

    if not is_correct_type:
      frappe.throw(_(
          "Wrong type for key: {k}. Should be {correct_type} instead of {given_type}".format(k=k, correct_type=_type,
                                                                                             given_type=type(v))))
