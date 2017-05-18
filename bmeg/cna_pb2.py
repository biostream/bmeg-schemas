# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cna.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cna.proto',
  package='bmeg',
  syntax='proto3',
  serialized_pb=_b('\n\tcna.proto\x12\x04\x62meg\"/\n\nCNACallSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rbio_sample_id\x18\x02 \x01(\t\"s\n\nCNASegment\x12\x16\n\x0ereference_name\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x03\x12\r\n\x05value\x18\x04 \x01(\x02\x12\r\n\x05genes\x18\x05 \x03(\t\x12\x13\n\x0b\x63\x61ll_set_id\x18\x06 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CNACALLSET = _descriptor.Descriptor(
  name='CNACallSet',
  full_name='bmeg.CNACallSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.CNACallSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bio_sample_id', full_name='bmeg.CNACallSet.bio_sample_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=66,
)


_CNASEGMENT = _descriptor.Descriptor(
  name='CNASegment',
  full_name='bmeg.CNASegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='bmeg.CNASegment.reference_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='bmeg.CNASegment.start', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='bmeg.CNASegment.end', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='bmeg.CNASegment.value', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genes', full_name='bmeg.CNASegment.genes', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='call_set_id', full_name='bmeg.CNASegment.call_set_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=183,
)

DESCRIPTOR.message_types_by_name['CNACallSet'] = _CNACALLSET
DESCRIPTOR.message_types_by_name['CNASegment'] = _CNASEGMENT

CNACallSet = _reflection.GeneratedProtocolMessageType('CNACallSet', (_message.Message,), dict(
  DESCRIPTOR = _CNACALLSET,
  __module__ = 'cna_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.CNACallSet)
  ))
_sym_db.RegisterMessage(CNACallSet)

CNASegment = _reflection.GeneratedProtocolMessageType('CNASegment', (_message.Message,), dict(
  DESCRIPTOR = _CNASEGMENT,
  __module__ = 'cna_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.CNASegment)
  ))
_sym_db.RegisterMessage(CNASegment)


# @@protoc_insertion_point(module_scope)
