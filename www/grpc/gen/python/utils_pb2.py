# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: utils.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0butils.proto\x12\x06pactus\"]\n SignMessageWithPrivateKeyRequest\x12\x1f\n\x0bprivate_key\x18\x01 \x01(\tR\nprivateKey\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\"A\n!SignMessageWithPrivateKeyResponse\x12\x1c\n\tsignature\x18\x01 \x01(\tR\tsignature\"m\n\x14VerifyMessageRequest\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message\x12\x1c\n\tsignature\x18\x02 \x01(\tR\tsignature\x12\x1d\n\npublic_key\x18\x03 \x01(\tR\tpublicKey\"2\n\x15VerifyMessageResponse\x12\x19\n\x08is_valid\x18\x01 \x01(\x08R\x07isValid2\xc7\x01\n\x05Utils\x12p\n\x19SignMessageWithPrivateKey\x12(.pactus.SignMessageWithPrivateKeyRequest\x1a).pactus.SignMessageWithPrivateKeyResponse\x12L\n\rVerifyMessage\x12\x1c.pactus.VerifyMessageRequest\x1a\x1d.pactus.VerifyMessageResponseB@\n\x0cpactus.utilsZ0github.com/pactus-project/pactus/www/grpc/pactusb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'utils_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\014pactus.utilsZ0github.com/pactus-project/pactus/www/grpc/pactus'
  _SIGNMESSAGEWITHPRIVATEKEYREQUEST._serialized_start=23
  _SIGNMESSAGEWITHPRIVATEKEYREQUEST._serialized_end=116
  _SIGNMESSAGEWITHPRIVATEKEYRESPONSE._serialized_start=118
  _SIGNMESSAGEWITHPRIVATEKEYRESPONSE._serialized_end=183
  _VERIFYMESSAGEREQUEST._serialized_start=185
  _VERIFYMESSAGEREQUEST._serialized_end=294
  _VERIFYMESSAGERESPONSE._serialized_start=296
  _VERIFYMESSAGERESPONSE._serialized_end=346
  _UTILS._serialized_start=349
  _UTILS._serialized_end=548
# @@protoc_insertion_point(module_scope)