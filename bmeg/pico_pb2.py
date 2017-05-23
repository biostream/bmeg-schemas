# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pico.proto

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
  name='pico.proto',
  package='bmeg',
  syntax='proto3',
  serialized_pb=_b('\n\npico.proto\x12\x04\x62meg\"\'\n\x04List\x12\x1f\n\x05items\x18\x03 \x03(\x0b\x32\x10.bmeg.Expression\"v\n\tCondition\x12#\n\tpredicate\x18\x01 \x01(\x0b\x32\x10.bmeg.Expression\x12\x1f\n\x05truth\x18\x02 \x01(\x0b\x32\x10.bmeg.Expression\x12#\n\tfalsehood\x18\x03 \x01(\x0b\x32\x10.bmeg.Expression\"7\n\x02\x46n\x12\x11\n\targuments\x18\x01 \x03(\t\x12\x1e\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x10.bmeg.Expression\"?\n\x07\x42inding\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12$\n\nexpression\x18\x02 \x01(\x0b\x32\x10.bmeg.Expression\"F\n\x03Let\x12\x1f\n\x08\x62indings\x18\x01 \x03(\x0b\x32\r.bmeg.Binding\x12\x1e\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x10.bmeg.Expression\"P\n\x05\x41pply\x12\"\n\x08\x66unction\x18\x01 \x01(\x0b\x32\x10.bmeg.Expression\x12#\n\targuments\x18\x02 \x03(\x0b\x32\x10.bmeg.Expression\"\xec\x01\n\nExpression\x12\r\n\x03nil\x18\x01 \x01(\x08H\x00\x12\x10\n\x06symbol\x18\x02 \x01(\tH\x00\x12\x10\n\x06string\x18\x03 \x01(\tH\x00\x12\x10\n\x06number\x18\x04 \x01(\x01H\x00\x12\x1a\n\x04list\x18\x05 \x01(\x0b\x32\n.bmeg.ListH\x00\x12$\n\tcondition\x18\x07 \x01(\x0b\x32\x0f.bmeg.ConditionH\x00\x12\x16\n\x02\x66n\x18\x06 \x01(\x0b\x32\x08.bmeg.FnH\x00\x12\x18\n\x03let\x18\x08 \x01(\x0b\x32\t.bmeg.LetH\x00\x12\x1c\n\x05\x61pply\x18\t \x01(\x0b\x32\x0b.bmeg.ApplyH\x00\x42\x07\n\x05valueb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LIST = _descriptor.Descriptor(
  name='List',
  full_name='bmeg.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='bmeg.List.items', index=0,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=20,
  serialized_end=59,
)


_CONDITION = _descriptor.Descriptor(
  name='Condition',
  full_name='bmeg.Condition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='predicate', full_name='bmeg.Condition.predicate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='truth', full_name='bmeg.Condition.truth', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='falsehood', full_name='bmeg.Condition.falsehood', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=61,
  serialized_end=179,
)


_FN = _descriptor.Descriptor(
  name='Fn',
  full_name='bmeg.Fn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arguments', full_name='bmeg.Fn.arguments', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='bmeg.Fn.body', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=181,
  serialized_end=236,
)


_BINDING = _descriptor.Descriptor(
  name='Binding',
  full_name='bmeg.Binding',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='bmeg.Binding.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expression', full_name='bmeg.Binding.expression', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=238,
  serialized_end=301,
)


_LET = _descriptor.Descriptor(
  name='Let',
  full_name='bmeg.Let',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bindings', full_name='bmeg.Let.bindings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='bmeg.Let.body', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=303,
  serialized_end=373,
)


_APPLY = _descriptor.Descriptor(
  name='Apply',
  full_name='bmeg.Apply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='function', full_name='bmeg.Apply.function', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arguments', full_name='bmeg.Apply.arguments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=375,
  serialized_end=455,
)


_EXPRESSION = _descriptor.Descriptor(
  name='Expression',
  full_name='bmeg.Expression',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nil', full_name='bmeg.Expression.nil', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='bmeg.Expression.symbol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string', full_name='bmeg.Expression.string', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number', full_name='bmeg.Expression.number', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='list', full_name='bmeg.Expression.list', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition', full_name='bmeg.Expression.condition', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fn', full_name='bmeg.Expression.fn', index=6,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='let', full_name='bmeg.Expression.let', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apply', full_name='bmeg.Expression.apply', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='value', full_name='bmeg.Expression.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=458,
  serialized_end=694,
)

_LIST.fields_by_name['items'].message_type = _EXPRESSION
_CONDITION.fields_by_name['predicate'].message_type = _EXPRESSION
_CONDITION.fields_by_name['truth'].message_type = _EXPRESSION
_CONDITION.fields_by_name['falsehood'].message_type = _EXPRESSION
_FN.fields_by_name['body'].message_type = _EXPRESSION
_BINDING.fields_by_name['expression'].message_type = _EXPRESSION
_LET.fields_by_name['bindings'].message_type = _BINDING
_LET.fields_by_name['body'].message_type = _EXPRESSION
_APPLY.fields_by_name['function'].message_type = _EXPRESSION
_APPLY.fields_by_name['arguments'].message_type = _EXPRESSION
_EXPRESSION.fields_by_name['list'].message_type = _LIST
_EXPRESSION.fields_by_name['condition'].message_type = _CONDITION
_EXPRESSION.fields_by_name['fn'].message_type = _FN
_EXPRESSION.fields_by_name['let'].message_type = _LET
_EXPRESSION.fields_by_name['apply'].message_type = _APPLY
_EXPRESSION.oneofs_by_name['value'].fields.append(
  _EXPRESSION.fields_by_name['nil'])
_EXPRESSION.fields_by_name['nil'].containing_oneof = _EXPRESSION.oneofs_by_name['value']
_EXPRESSION.oneofs_by_name['value'].fields.append(
  _EXPRESSION.fields_by_name['symbol'])
_EXPRESSION.fields_by_name['symbol'].containing_oneof = _EXPRESSION.oneofs_by_name['value']
_EXPRESSION.oneofs_by_name['value'].fields.append(
  _EXPRESSION.fields_by_name['string'])
_EXPRESSION.fields_by_name['string'].containing_oneof = _EXPRESSION.oneofs_by_name['value']
_EXPRESSION.oneofs_by_name['value'].fields.append(
  _EXPRESSION.fields_by_name['number'])
_EXPRESSION.fields_by_name['number'].containing_oneof = _EXPRESSION.oneofs_by_name['value']
_EXPRESSION.oneofs_by_name['value'].fields.append(
  _EXPRESSION.fields_by_name['list'])
_EXPRESSION.fields_by_name['list'].containing_oneof = _EXPRESSION.oneofs_by_name['value']
_EXPRESSION.oneofs_by_name['value'].fields.append(
  _EXPRESSION.fields_by_name['condition'])
_EXPRESSION.fields_by_name['condition'].containing_oneof = _EXPRESSION.oneofs_by_name['value']
_EXPRESSION.oneofs_by_name['value'].fields.append(
  _EXPRESSION.fields_by_name['fn'])
_EXPRESSION.fields_by_name['fn'].containing_oneof = _EXPRESSION.oneofs_by_name['value']
_EXPRESSION.oneofs_by_name['value'].fields.append(
  _EXPRESSION.fields_by_name['let'])
_EXPRESSION.fields_by_name['let'].containing_oneof = _EXPRESSION.oneofs_by_name['value']
_EXPRESSION.oneofs_by_name['value'].fields.append(
  _EXPRESSION.fields_by_name['apply'])
_EXPRESSION.fields_by_name['apply'].containing_oneof = _EXPRESSION.oneofs_by_name['value']
DESCRIPTOR.message_types_by_name['List'] = _LIST
DESCRIPTOR.message_types_by_name['Condition'] = _CONDITION
DESCRIPTOR.message_types_by_name['Fn'] = _FN
DESCRIPTOR.message_types_by_name['Binding'] = _BINDING
DESCRIPTOR.message_types_by_name['Let'] = _LET
DESCRIPTOR.message_types_by_name['Apply'] = _APPLY
DESCRIPTOR.message_types_by_name['Expression'] = _EXPRESSION

List = _reflection.GeneratedProtocolMessageType('List', (_message.Message,), dict(
  DESCRIPTOR = _LIST,
  __module__ = 'pico_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.List)
  ))
_sym_db.RegisterMessage(List)

Condition = _reflection.GeneratedProtocolMessageType('Condition', (_message.Message,), dict(
  DESCRIPTOR = _CONDITION,
  __module__ = 'pico_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Condition)
  ))
_sym_db.RegisterMessage(Condition)

Fn = _reflection.GeneratedProtocolMessageType('Fn', (_message.Message,), dict(
  DESCRIPTOR = _FN,
  __module__ = 'pico_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Fn)
  ))
_sym_db.RegisterMessage(Fn)

Binding = _reflection.GeneratedProtocolMessageType('Binding', (_message.Message,), dict(
  DESCRIPTOR = _BINDING,
  __module__ = 'pico_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Binding)
  ))
_sym_db.RegisterMessage(Binding)

Let = _reflection.GeneratedProtocolMessageType('Let', (_message.Message,), dict(
  DESCRIPTOR = _LET,
  __module__ = 'pico_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Let)
  ))
_sym_db.RegisterMessage(Let)

Apply = _reflection.GeneratedProtocolMessageType('Apply', (_message.Message,), dict(
  DESCRIPTOR = _APPLY,
  __module__ = 'pico_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Apply)
  ))
_sym_db.RegisterMessage(Apply)

Expression = _reflection.GeneratedProtocolMessageType('Expression', (_message.Message,), dict(
  DESCRIPTOR = _EXPRESSION,
  __module__ = 'pico_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Expression)
  ))
_sym_db.RegisterMessage(Expression)


# @@protoc_insertion_point(module_scope)
