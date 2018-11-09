# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol.proto

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
  name='protocol.proto',
  package='dlvr',
  syntax='proto3',
  serialized_pb=_b('\n\x0eprotocol.proto\x12\x04\x64lvr\".\n\x0f\x45valuateRequest\x12\x1b\n\x06layers\x18\x01 \x03(\x0b\x32\x0b.dlvr.Layer\"]\n\x05Layer\x12\x1f\n\x04\x63onv\x18\x01 \x01(\x0b\x32\x0f.dlvr.ConvLayerH\x00\x12%\n\x07\x64ropout\x18\x02 \x01(\x0b\x32\x12.dlvr.DropoutLayerH\x00\x42\x0c\n\ndefinition\"\x1c\n\tConvLayer\x12\x0f\n\x07\x66ilters\x18\x01 \x01(\x03\"!\n\x0c\x44ropoutLayer\x12\x11\n\tdimension\x18\x01 \x01(\x02\"\"\n\x0eProgressUpdate\x12\x10\n\x08\x61\x63\x63uracy\x18\x01 \x01(\x02\x32H\n\tEvaluator\x12;\n\x08\x45valuate\x12\x15.dlvr.EvaluateRequest\x1a\x14.dlvr.ProgressUpdate\"\x00\x30\x01\x62\x06proto3')
)




_EVALUATEREQUEST = _descriptor.Descriptor(
  name='EvaluateRequest',
  full_name='dlvr.EvaluateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='layers', full_name='dlvr.EvaluateRequest.layers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=24,
  serialized_end=70,
)


_LAYER = _descriptor.Descriptor(
  name='Layer',
  full_name='dlvr.Layer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conv', full_name='dlvr.Layer.conv', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dropout', full_name='dlvr.Layer.dropout', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
      name='definition', full_name='dlvr.Layer.definition',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=72,
  serialized_end=165,
)


_CONVLAYER = _descriptor.Descriptor(
  name='ConvLayer',
  full_name='dlvr.ConvLayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filters', full_name='dlvr.ConvLayer.filters', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=167,
  serialized_end=195,
)


_DROPOUTLAYER = _descriptor.Descriptor(
  name='DropoutLayer',
  full_name='dlvr.DropoutLayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dimension', full_name='dlvr.DropoutLayer.dimension', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=197,
  serialized_end=230,
)


_PROGRESSUPDATE = _descriptor.Descriptor(
  name='ProgressUpdate',
  full_name='dlvr.ProgressUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accuracy', full_name='dlvr.ProgressUpdate.accuracy', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=232,
  serialized_end=266,
)

_EVALUATEREQUEST.fields_by_name['layers'].message_type = _LAYER
_LAYER.fields_by_name['conv'].message_type = _CONVLAYER
_LAYER.fields_by_name['dropout'].message_type = _DROPOUTLAYER
_LAYER.oneofs_by_name['definition'].fields.append(
  _LAYER.fields_by_name['conv'])
_LAYER.fields_by_name['conv'].containing_oneof = _LAYER.oneofs_by_name['definition']
_LAYER.oneofs_by_name['definition'].fields.append(
  _LAYER.fields_by_name['dropout'])
_LAYER.fields_by_name['dropout'].containing_oneof = _LAYER.oneofs_by_name['definition']
DESCRIPTOR.message_types_by_name['EvaluateRequest'] = _EVALUATEREQUEST
DESCRIPTOR.message_types_by_name['Layer'] = _LAYER
DESCRIPTOR.message_types_by_name['ConvLayer'] = _CONVLAYER
DESCRIPTOR.message_types_by_name['DropoutLayer'] = _DROPOUTLAYER
DESCRIPTOR.message_types_by_name['ProgressUpdate'] = _PROGRESSUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EvaluateRequest = _reflection.GeneratedProtocolMessageType('EvaluateRequest', (_message.Message,), dict(
  DESCRIPTOR = _EVALUATEREQUEST,
  __module__ = 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:dlvr.EvaluateRequest)
  ))
_sym_db.RegisterMessage(EvaluateRequest)

Layer = _reflection.GeneratedProtocolMessageType('Layer', (_message.Message,), dict(
  DESCRIPTOR = _LAYER,
  __module__ = 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:dlvr.Layer)
  ))
_sym_db.RegisterMessage(Layer)

ConvLayer = _reflection.GeneratedProtocolMessageType('ConvLayer', (_message.Message,), dict(
  DESCRIPTOR = _CONVLAYER,
  __module__ = 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:dlvr.ConvLayer)
  ))
_sym_db.RegisterMessage(ConvLayer)

DropoutLayer = _reflection.GeneratedProtocolMessageType('DropoutLayer', (_message.Message,), dict(
  DESCRIPTOR = _DROPOUTLAYER,
  __module__ = 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:dlvr.DropoutLayer)
  ))
_sym_db.RegisterMessage(DropoutLayer)

ProgressUpdate = _reflection.GeneratedProtocolMessageType('ProgressUpdate', (_message.Message,), dict(
  DESCRIPTOR = _PROGRESSUPDATE,
  __module__ = 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:dlvr.ProgressUpdate)
  ))
_sym_db.RegisterMessage(ProgressUpdate)



_EVALUATOR = _descriptor.ServiceDescriptor(
  name='Evaluator',
  full_name='dlvr.Evaluator',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=268,
  serialized_end=340,
  methods=[
  _descriptor.MethodDescriptor(
    name='Evaluate',
    full_name='dlvr.Evaluator.Evaluate',
    index=0,
    containing_service=None,
    input_type=_EVALUATEREQUEST,
    output_type=_PROGRESSUPDATE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVALUATOR)

DESCRIPTOR.services_by_name['Evaluator'] = _EVALUATOR

# @@protoc_insertion_point(module_scope)