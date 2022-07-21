# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: earth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x65\x61rth.proto\"\x14\n\x04Mode\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\"5\n\x07SatInfo\x12\t\n\x01t\x18\x01 \x01(\x02\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\x12\t\n\x01z\x18\x04 \x01(\x02\"6\n\x07TLEInfo\x12\r\n\x05line1\x18\x01 \x01(\t\x12\r\n\x05line2\x18\x02 \x01(\t\x12\r\n\x05line3\x18\x03 \x01(\t\"\x15\n\x04Test\x12\r\n\x05\x61ngle\x18\x01 \x01(\x02\" \n\rResponse_code\x12\x0f\n\x07message\x18\x01 \x01(\t2\xbc\x01\n\x06Satrac\x12)\n\x0eSetProgramMode\x12\x05.Mode\x1a\x0e.Response_code\"\x00\x12\x30\n\x12SendSatInformation\x12\x08.SatInfo\x1a\x0e.Response_code\"\x00\x12\x30\n\x12SendTLEInformation\x12\x08.TLEInfo\x1a\x0e.Response_code\"\x00\x12#\n\x08SendTest\x12\x05.Test\x1a\x0e.Response_code\"\x00\x62\x06proto3')



_MODE = DESCRIPTOR.message_types_by_name['Mode']
_SATINFO = DESCRIPTOR.message_types_by_name['SatInfo']
_TLEINFO = DESCRIPTOR.message_types_by_name['TLEInfo']
_TEST = DESCRIPTOR.message_types_by_name['Test']
_RESPONSE_CODE = DESCRIPTOR.message_types_by_name['Response_code']
Mode = _reflection.GeneratedProtocolMessageType('Mode', (_message.Message,), {
  'DESCRIPTOR' : _MODE,
  '__module__' : 'earth_pb2'
  # @@protoc_insertion_point(class_scope:Mode)
  })
_sym_db.RegisterMessage(Mode)

SatInfo = _reflection.GeneratedProtocolMessageType('SatInfo', (_message.Message,), {
  'DESCRIPTOR' : _SATINFO,
  '__module__' : 'earth_pb2'
  # @@protoc_insertion_point(class_scope:SatInfo)
  })
_sym_db.RegisterMessage(SatInfo)

TLEInfo = _reflection.GeneratedProtocolMessageType('TLEInfo', (_message.Message,), {
  'DESCRIPTOR' : _TLEINFO,
  '__module__' : 'earth_pb2'
  # @@protoc_insertion_point(class_scope:TLEInfo)
  })
_sym_db.RegisterMessage(TLEInfo)

Test = _reflection.GeneratedProtocolMessageType('Test', (_message.Message,), {
  'DESCRIPTOR' : _TEST,
  '__module__' : 'earth_pb2'
  # @@protoc_insertion_point(class_scope:Test)
  })
_sym_db.RegisterMessage(Test)

Response_code = _reflection.GeneratedProtocolMessageType('Response_code', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE_CODE,
  '__module__' : 'earth_pb2'
  # @@protoc_insertion_point(class_scope:Response_code)
  })
_sym_db.RegisterMessage(Response_code)

_SATRAC = DESCRIPTOR.services_by_name['Satrac']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MODE._serialized_start=15
  _MODE._serialized_end=35
  _SATINFO._serialized_start=37
  _SATINFO._serialized_end=90
  _TLEINFO._serialized_start=92
  _TLEINFO._serialized_end=146
  _TEST._serialized_start=148
  _TEST._serialized_end=169
  _RESPONSE_CODE._serialized_start=171
  _RESPONSE_CODE._serialized_end=203
  _SATRAC._serialized_start=206
  _SATRAC._serialized_end=394
# @@protoc_insertion_point(module_scope)
