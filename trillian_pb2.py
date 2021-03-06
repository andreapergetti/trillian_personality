# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trillian.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from crypto.keyspb import keyspb_pb2 as crypto_dot_keyspb_dot_keyspb__pb2
from crypto.sigpb import sigpb_pb2 as crypto_dot_sigpb_dot_sigpb__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='trillian.proto',
  package='trillian',
  syntax='proto3',
  serialized_options=b'\n\031com.google.trillian.protoB\rTrillianProtoP\001Z\032github.com/google/trillian',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0etrillian.proto\x12\x08trillian\x1a\x1a\x63rypto/keyspb/keyspb.proto\x1a\x18\x63rypto/sigpb/sigpb.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbb\x05\n\x04Tree\x12\x0f\n\x07tree_id\x18\x01 \x01(\x03\x12\'\n\ntree_state\x18\x02 \x01(\x0e\x32\x13.trillian.TreeState\x12%\n\ttree_type\x18\x03 \x01(\x0e\x32\x12.trillian.TreeType\x12-\n\rhash_strategy\x18\x04 \x01(\x0e\x32\x16.trillian.HashStrategy\x12<\n\x0ehash_algorithm\x18\x05 \x01(\x0e\x32$.sigpb.DigitallySigned.HashAlgorithm\x12\x46\n\x13signature_algorithm\x18\x06 \x01(\x0e\x32).sigpb.DigitallySigned.SignatureAlgorithm\x12\x14\n\x0c\x64isplay_name\x18\x08 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\t \x01(\t\x12)\n\x0bprivate_key\x18\x0c \x01(\x0b\x32\x14.google.protobuf.Any\x12.\n\x10storage_settings\x18\r \x01(\x0b\x32\x14.google.protobuf.Any\x12%\n\npublic_key\x18\x0e \x01(\x0b\x32\x11.keyspb.PublicKey\x12\x34\n\x11max_root_duration\x18\x0f \x01(\x0b\x32\x19.google.protobuf.Duration\x12/\n\x0b\x63reate_time\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07\x64\x65leted\x18\x13 \x01(\x08\x12/\n\x0b\x64\x65lete_time\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.TimestampJ\x04\x08\x12\x10\x13J\x04\x08\x07\x10\x08J\x04\x08\n\x10\x0bJ\x04\x08\x0b\x10\x0c\"s\n\rSignedLogRoot\x12\x10\n\x08key_hint\x18\x07 \x01(\x0c\x12\x10\n\x08log_root\x18\x08 \x01(\x0c\x12\x1a\n\x12log_root_signature\x18\t \x01(\x0cJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07\"^\n\rSignedMapRoot\x12\x10\n\x08map_root\x18\t \x01(\x0c\x12\x11\n\tsignature\x18\x04 \x01(\x0cJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08J\x04\x08\x08\x10\t\"1\n\x05Proof\x12\x12\n\nleaf_index\x18\x01 \x01(\x03\x12\x0e\n\x06hashes\x18\x03 \x03(\x0cJ\x04\x08\x02\x10\x03*D\n\rLogRootFormat\x12\x1b\n\x17LOG_ROOT_FORMAT_UNKNOWN\x10\x00\x12\x16\n\x12LOG_ROOT_FORMAT_V1\x10\x01*\x97\x01\n\x0cHashStrategy\x12\x19\n\x15UNKNOWN_HASH_STRATEGY\x10\x00\x12\x12\n\x0eRFC6962_SHA256\x10\x01\x12\x13\n\x0fTEST_MAP_HASHER\x10\x02\x12\x19\n\x15OBJECT_RFC6962_SHA256\x10\x03\x12\x15\n\x11\x43ONIKS_SHA512_256\x10\x04\x12\x11\n\rCONIKS_SHA256\x10\x05*\x8b\x01\n\tTreeState\x12\x16\n\x12UNKNOWN_TREE_STATE\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\n\n\x06\x46ROZEN\x10\x02\x12\x1f\n\x17\x44\x45PRECATED_SOFT_DELETED\x10\x03\x1a\x02\x08\x01\x12\x1f\n\x17\x44\x45PRECATED_HARD_DELETED\x10\x04\x1a\x02\x08\x01\x12\x0c\n\x08\x44RAINING\x10\x05*G\n\x08TreeType\x12\x15\n\x11UNKNOWN_TREE_TYPE\x10\x00\x12\x07\n\x03LOG\x10\x01\x12\x07\n\x03MAP\x10\x02\x12\x12\n\x0ePREORDERED_LOG\x10\x03\x42H\n\x19\x63om.google.trillian.protoB\rTrillianProtoP\x01Z\x1agithub.com/google/trillianb\x06proto3'
  ,
  dependencies=[crypto_dot_keyspb_dot_keyspb__pb2.DESCRIPTOR,crypto_dot_sigpb_dot_sigpb__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_LOGROOTFORMAT = _descriptor.EnumDescriptor(
  name='LogRootFormat',
  full_name='trillian.LogRootFormat',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LOG_ROOT_FORMAT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOG_ROOT_FORMAT_V1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1140,
  serialized_end=1208,
)
_sym_db.RegisterEnumDescriptor(_LOGROOTFORMAT)

LogRootFormat = enum_type_wrapper.EnumTypeWrapper(_LOGROOTFORMAT)
_HASHSTRATEGY = _descriptor.EnumDescriptor(
  name='HashStrategy',
  full_name='trillian.HashStrategy',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_HASH_STRATEGY', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RFC6962_SHA256', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEST_MAP_HASHER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OBJECT_RFC6962_SHA256', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONIKS_SHA512_256', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONIKS_SHA256', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1211,
  serialized_end=1362,
)
_sym_db.RegisterEnumDescriptor(_HASHSTRATEGY)

HashStrategy = enum_type_wrapper.EnumTypeWrapper(_HASHSTRATEGY)
_TREESTATE = _descriptor.EnumDescriptor(
  name='TreeState',
  full_name='trillian.TreeState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TREE_STATE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FROZEN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_SOFT_DELETED', index=3, number=3,
      serialized_options=b'\010\001',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPRECATED_HARD_DELETED', index=4, number=4,
      serialized_options=b'\010\001',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DRAINING', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1365,
  serialized_end=1504,
)
_sym_db.RegisterEnumDescriptor(_TREESTATE)

TreeState = enum_type_wrapper.EnumTypeWrapper(_TREESTATE)
_TREETYPE = _descriptor.EnumDescriptor(
  name='TreeType',
  full_name='trillian.TreeType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TREE_TYPE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOG', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PREORDERED_LOG', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1506,
  serialized_end=1577,
)
_sym_db.RegisterEnumDescriptor(_TREETYPE)

TreeType = enum_type_wrapper.EnumTypeWrapper(_TREETYPE)
LOG_ROOT_FORMAT_UNKNOWN = 0
LOG_ROOT_FORMAT_V1 = 1
UNKNOWN_HASH_STRATEGY = 0
RFC6962_SHA256 = 1
TEST_MAP_HASHER = 2
OBJECT_RFC6962_SHA256 = 3
CONIKS_SHA512_256 = 4
CONIKS_SHA256 = 5
UNKNOWN_TREE_STATE = 0
ACTIVE = 1
FROZEN = 2
DEPRECATED_SOFT_DELETED = 3
DEPRECATED_HARD_DELETED = 4
DRAINING = 5
UNKNOWN_TREE_TYPE = 0
LOG = 1
MAP = 2
PREORDERED_LOG = 3



_TREE = _descriptor.Descriptor(
  name='Tree',
  full_name='trillian.Tree',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tree_id', full_name='trillian.Tree.tree_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tree_state', full_name='trillian.Tree.tree_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tree_type', full_name='trillian.Tree.tree_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash_strategy', full_name='trillian.Tree.hash_strategy', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash_algorithm', full_name='trillian.Tree.hash_algorithm', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature_algorithm', full_name='trillian.Tree.signature_algorithm', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='trillian.Tree.display_name', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='trillian.Tree.description', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='private_key', full_name='trillian.Tree.private_key', index=8,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='storage_settings', full_name='trillian.Tree.storage_settings', index=9,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='public_key', full_name='trillian.Tree.public_key', index=10,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_root_duration', full_name='trillian.Tree.max_root_duration', index=11,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='trillian.Tree.create_time', index=12,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='trillian.Tree.update_time', index=13,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='trillian.Tree.deleted', index=14,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delete_time', full_name='trillian.Tree.delete_time', index=15,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=874,
)


_SIGNEDLOGROOT = _descriptor.Descriptor(
  name='SignedLogRoot',
  full_name='trillian.SignedLogRoot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_hint', full_name='trillian.SignedLogRoot.key_hint', index=0,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log_root', full_name='trillian.SignedLogRoot.log_root', index=1,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log_root_signature', full_name='trillian.SignedLogRoot.log_root_signature', index=2,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=876,
  serialized_end=991,
)


_SIGNEDMAPROOT = _descriptor.Descriptor(
  name='SignedMapRoot',
  full_name='trillian.SignedMapRoot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='map_root', full_name='trillian.SignedMapRoot.map_root', index=0,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='trillian.SignedMapRoot.signature', index=1,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=993,
  serialized_end=1087,
)


_PROOF = _descriptor.Descriptor(
  name='Proof',
  full_name='trillian.Proof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='leaf_index', full_name='trillian.Proof.leaf_index', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hashes', full_name='trillian.Proof.hashes', index=1,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1089,
  serialized_end=1138,
)

_TREE.fields_by_name['tree_state'].enum_type = _TREESTATE
_TREE.fields_by_name['tree_type'].enum_type = _TREETYPE
_TREE.fields_by_name['hash_strategy'].enum_type = _HASHSTRATEGY
_TREE.fields_by_name['hash_algorithm'].enum_type = crypto_dot_sigpb_dot_sigpb__pb2._DIGITALLYSIGNED_HASHALGORITHM
_TREE.fields_by_name['signature_algorithm'].enum_type = crypto_dot_sigpb_dot_sigpb__pb2._DIGITALLYSIGNED_SIGNATUREALGORITHM
_TREE.fields_by_name['private_key'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_TREE.fields_by_name['storage_settings'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_TREE.fields_by_name['public_key'].message_type = crypto_dot_keyspb_dot_keyspb__pb2._PUBLICKEY
_TREE.fields_by_name['max_root_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TREE.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TREE.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TREE.fields_by_name['delete_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Tree'] = _TREE
DESCRIPTOR.message_types_by_name['SignedLogRoot'] = _SIGNEDLOGROOT
DESCRIPTOR.message_types_by_name['SignedMapRoot'] = _SIGNEDMAPROOT
DESCRIPTOR.message_types_by_name['Proof'] = _PROOF
DESCRIPTOR.enum_types_by_name['LogRootFormat'] = _LOGROOTFORMAT
DESCRIPTOR.enum_types_by_name['HashStrategy'] = _HASHSTRATEGY
DESCRIPTOR.enum_types_by_name['TreeState'] = _TREESTATE
DESCRIPTOR.enum_types_by_name['TreeType'] = _TREETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tree = _reflection.GeneratedProtocolMessageType('Tree', (_message.Message,), {
  'DESCRIPTOR' : _TREE,
  '__module__' : 'trillian_pb2'
  # @@protoc_insertion_point(class_scope:trillian.Tree)
  })
_sym_db.RegisterMessage(Tree)

SignedLogRoot = _reflection.GeneratedProtocolMessageType('SignedLogRoot', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDLOGROOT,
  '__module__' : 'trillian_pb2'
  # @@protoc_insertion_point(class_scope:trillian.SignedLogRoot)
  })
_sym_db.RegisterMessage(SignedLogRoot)

SignedMapRoot = _reflection.GeneratedProtocolMessageType('SignedMapRoot', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDMAPROOT,
  '__module__' : 'trillian_pb2'
  # @@protoc_insertion_point(class_scope:trillian.SignedMapRoot)
  })
_sym_db.RegisterMessage(SignedMapRoot)

Proof = _reflection.GeneratedProtocolMessageType('Proof', (_message.Message,), {
  'DESCRIPTOR' : _PROOF,
  '__module__' : 'trillian_pb2'
  # @@protoc_insertion_point(class_scope:trillian.Proof)
  })
_sym_db.RegisterMessage(Proof)


DESCRIPTOR._options = None
_TREESTATE.values_by_name["DEPRECATED_SOFT_DELETED"]._options = None
_TREESTATE.values_by_name["DEPRECATED_HARD_DELETED"]._options = None
# @@protoc_insertion_point(module_scope)
