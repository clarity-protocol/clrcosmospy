# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: score_send.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import clrcosmospy.interfaces.gogo_pb2 as gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10score_send.proto\x12!clarityprotocol.protocol.protocol\x1a\ngogo.proto\"\xa5\x01\n\tScoreSend\x12#\n\x07\x63reator\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"network\"\x12#\n\x07network\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"network\"\x12#\n\x07\x61\x64\x64ress\x18\x03 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"address\"\x12\x1f\n\x05value\x18\x04 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"value\":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x42\x37Z5github.com/clarity-protocol/protocol/x/protocol/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'score_send_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z5github.com/clarity-protocol/protocol/x/protocol/types'
  _SCORESEND.fields_by_name['creator']._options = None
  _SCORESEND.fields_by_name['creator']._serialized_options = b'\362\336\037\016yaml:\"network\"'
  _SCORESEND.fields_by_name['network']._options = None
  _SCORESEND.fields_by_name['network']._serialized_options = b'\362\336\037\016yaml:\"network\"'
  _SCORESEND.fields_by_name['address']._options = None
  _SCORESEND.fields_by_name['address']._serialized_options = b'\362\336\037\016yaml:\"address\"'
  _SCORESEND.fields_by_name['value']._options = None
  _SCORESEND.fields_by_name['value']._serialized_options = b'\362\336\037\014yaml:\"value\"'
  _SCORESEND._options = None
  _SCORESEND._serialized_options = b'\350\240\037\000\210\240\037\000'
  _SCORESEND._serialized_start=68
  _SCORESEND._serialized_end=233
# @@protoc_insertion_point(module_scope)
