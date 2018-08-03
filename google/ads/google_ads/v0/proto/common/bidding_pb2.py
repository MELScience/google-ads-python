# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/common/bidding.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.enums import page_one_promoted_strategy_goal_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_page__one__promoted__strategy__goal__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/common/bidding.proto',
  package='google.ads.googleads.v0.common',
  syntax='proto3',
  serialized_pb=_b('\n2google/ads/googleads_v0/proto/common/bidding.proto\x12\x1egoogle.ads.googleads.v0.common\x1aIgoogle/ads/googleads_v0/proto/enums/page_one_promoted_strategy_goal.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\r\n\x0b\x45nhancedCpc\"E\n\tManualCpc\x12\x38\n\x14\x65nhanced_cpc_enabled\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x0b\n\tManualCpm\"\x15\n\x13MaximizeConversions\"L\n\x17MaximizeConversionValue\x12\x31\n\x0btarget_roas\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\"\xc6\x03\n\x0fPageOnePromoted\x12q\n\rstrategy_goal\x18\x01 \x01(\x0e\x32Z.google.ads.googleads.v0.enums.PageOnePromotedStrategyGoalEnum.PageOnePromotedStrategyGoal\x12;\n\x16\x63pc_bid_ceiling_micros\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x32\n\x0c\x62id_modifier\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x37\n\x13only_raise_cpc_bids\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12I\n%raise_cpc_bid_when_budget_constrained\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12K\n\'raise_cpc_bid_when_quality_score_is_low\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\xbb\x01\n\tTargetCpa\x12\x36\n\x11target_cpa_micros\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x16\x63pc_bid_ceiling_micros\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x39\n\x14\x63pc_bid_floor_micros\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\xd2\x02\n\x12TargetOutrankShare\x12@\n\x1btarget_outrank_share_micros\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x37\n\x11\x63ompetitor_domain\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x16\x63pc_bid_ceiling_micros\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x37\n\x13only_raise_cpc_bids\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12K\n\'raise_cpc_bid_when_quality_score_is_low\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\xb7\x01\n\nTargetRoas\x12\x31\n\x0btarget_roas\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12;\n\x16\x63pc_bid_ceiling_micros\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x39\n\x14\x63pc_bid_floor_micros\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\x84\x01\n\x0bTargetSpend\x12\x38\n\x13target_spend_micros\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x16\x63pc_bid_ceiling_micros\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\x83\x01\n\nPercentCpc\x12;\n\x16\x63pc_bid_ceiling_micros\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x14\x65nhanced_cpc_enabled\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\xc2\x01\n\"com.google.ads.googleads.v0.commonB\x0c\x42iddingProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Commonb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_page__one__promoted__strategy__goal__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_ENHANCEDCPC = _descriptor.Descriptor(
  name='EnhancedCpc',
  full_name='google.ads.googleads.v0.common.EnhancedCpc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=193,
  serialized_end=206,
)


_MANUALCPC = _descriptor.Descriptor(
  name='ManualCpc',
  full_name='google.ads.googleads.v0.common.ManualCpc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enhanced_cpc_enabled', full_name='google.ads.googleads.v0.common.ManualCpc.enhanced_cpc_enabled', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=208,
  serialized_end=277,
)


_MANUALCPM = _descriptor.Descriptor(
  name='ManualCpm',
  full_name='google.ads.googleads.v0.common.ManualCpm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=279,
  serialized_end=290,
)


_MAXIMIZECONVERSIONS = _descriptor.Descriptor(
  name='MaximizeConversions',
  full_name='google.ads.googleads.v0.common.MaximizeConversions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=292,
  serialized_end=313,
)


_MAXIMIZECONVERSIONVALUE = _descriptor.Descriptor(
  name='MaximizeConversionValue',
  full_name='google.ads.googleads.v0.common.MaximizeConversionValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_roas', full_name='google.ads.googleads.v0.common.MaximizeConversionValue.target_roas', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=315,
  serialized_end=391,
)


_PAGEONEPROMOTED = _descriptor.Descriptor(
  name='PageOnePromoted',
  full_name='google.ads.googleads.v0.common.PageOnePromoted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='strategy_goal', full_name='google.ads.googleads.v0.common.PageOnePromoted.strategy_goal', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_ceiling_micros', full_name='google.ads.googleads.v0.common.PageOnePromoted.cpc_bid_ceiling_micros', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bid_modifier', full_name='google.ads.googleads.v0.common.PageOnePromoted.bid_modifier', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='only_raise_cpc_bids', full_name='google.ads.googleads.v0.common.PageOnePromoted.only_raise_cpc_bids', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raise_cpc_bid_when_budget_constrained', full_name='google.ads.googleads.v0.common.PageOnePromoted.raise_cpc_bid_when_budget_constrained', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raise_cpc_bid_when_quality_score_is_low', full_name='google.ads.googleads.v0.common.PageOnePromoted.raise_cpc_bid_when_quality_score_is_low', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=394,
  serialized_end=848,
)


_TARGETCPA = _descriptor.Descriptor(
  name='TargetCpa',
  full_name='google.ads.googleads.v0.common.TargetCpa',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_cpa_micros', full_name='google.ads.googleads.v0.common.TargetCpa.target_cpa_micros', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_ceiling_micros', full_name='google.ads.googleads.v0.common.TargetCpa.cpc_bid_ceiling_micros', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_floor_micros', full_name='google.ads.googleads.v0.common.TargetCpa.cpc_bid_floor_micros', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=851,
  serialized_end=1038,
)


_TARGETOUTRANKSHARE = _descriptor.Descriptor(
  name='TargetOutrankShare',
  full_name='google.ads.googleads.v0.common.TargetOutrankShare',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_outrank_share_micros', full_name='google.ads.googleads.v0.common.TargetOutrankShare.target_outrank_share_micros', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='competitor_domain', full_name='google.ads.googleads.v0.common.TargetOutrankShare.competitor_domain', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_ceiling_micros', full_name='google.ads.googleads.v0.common.TargetOutrankShare.cpc_bid_ceiling_micros', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='only_raise_cpc_bids', full_name='google.ads.googleads.v0.common.TargetOutrankShare.only_raise_cpc_bids', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raise_cpc_bid_when_quality_score_is_low', full_name='google.ads.googleads.v0.common.TargetOutrankShare.raise_cpc_bid_when_quality_score_is_low', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=1041,
  serialized_end=1379,
)


_TARGETROAS = _descriptor.Descriptor(
  name='TargetRoas',
  full_name='google.ads.googleads.v0.common.TargetRoas',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_roas', full_name='google.ads.googleads.v0.common.TargetRoas.target_roas', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_ceiling_micros', full_name='google.ads.googleads.v0.common.TargetRoas.cpc_bid_ceiling_micros', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_floor_micros', full_name='google.ads.googleads.v0.common.TargetRoas.cpc_bid_floor_micros', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=1382,
  serialized_end=1565,
)


_TARGETSPEND = _descriptor.Descriptor(
  name='TargetSpend',
  full_name='google.ads.googleads.v0.common.TargetSpend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_spend_micros', full_name='google.ads.googleads.v0.common.TargetSpend.target_spend_micros', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_ceiling_micros', full_name='google.ads.googleads.v0.common.TargetSpend.cpc_bid_ceiling_micros', index=1,
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
  ],
  serialized_start=1568,
  serialized_end=1700,
)


_PERCENTCPC = _descriptor.Descriptor(
  name='PercentCpc',
  full_name='google.ads.googleads.v0.common.PercentCpc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpc_bid_ceiling_micros', full_name='google.ads.googleads.v0.common.PercentCpc.cpc_bid_ceiling_micros', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enhanced_cpc_enabled', full_name='google.ads.googleads.v0.common.PercentCpc.enhanced_cpc_enabled', index=1,
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
  ],
  serialized_start=1703,
  serialized_end=1834,
)

_MANUALCPC.fields_by_name['enhanced_cpc_enabled'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_MAXIMIZECONVERSIONVALUE.fields_by_name['target_roas'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_PAGEONEPROMOTED.fields_by_name['strategy_goal'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_page__one__promoted__strategy__goal__pb2._PAGEONEPROMOTEDSTRATEGYGOALENUM_PAGEONEPROMOTEDSTRATEGYGOAL
_PAGEONEPROMOTED.fields_by_name['cpc_bid_ceiling_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_PAGEONEPROMOTED.fields_by_name['bid_modifier'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_PAGEONEPROMOTED.fields_by_name['only_raise_cpc_bids'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_PAGEONEPROMOTED.fields_by_name['raise_cpc_bid_when_budget_constrained'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_PAGEONEPROMOTED.fields_by_name['raise_cpc_bid_when_quality_score_is_low'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_TARGETCPA.fields_by_name['target_cpa_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETCPA.fields_by_name['cpc_bid_ceiling_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETCPA.fields_by_name['cpc_bid_floor_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETOUTRANKSHARE.fields_by_name['target_outrank_share_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_TARGETOUTRANKSHARE.fields_by_name['competitor_domain'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_TARGETOUTRANKSHARE.fields_by_name['cpc_bid_ceiling_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETOUTRANKSHARE.fields_by_name['only_raise_cpc_bids'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_TARGETOUTRANKSHARE.fields_by_name['raise_cpc_bid_when_quality_score_is_low'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_TARGETROAS.fields_by_name['target_roas'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_TARGETROAS.fields_by_name['cpc_bid_ceiling_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETROAS.fields_by_name['cpc_bid_floor_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETSPEND.fields_by_name['target_spend_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TARGETSPEND.fields_by_name['cpc_bid_ceiling_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_PERCENTCPC.fields_by_name['cpc_bid_ceiling_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_PERCENTCPC.fields_by_name['enhanced_cpc_enabled'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
DESCRIPTOR.message_types_by_name['EnhancedCpc'] = _ENHANCEDCPC
DESCRIPTOR.message_types_by_name['ManualCpc'] = _MANUALCPC
DESCRIPTOR.message_types_by_name['ManualCpm'] = _MANUALCPM
DESCRIPTOR.message_types_by_name['MaximizeConversions'] = _MAXIMIZECONVERSIONS
DESCRIPTOR.message_types_by_name['MaximizeConversionValue'] = _MAXIMIZECONVERSIONVALUE
DESCRIPTOR.message_types_by_name['PageOnePromoted'] = _PAGEONEPROMOTED
DESCRIPTOR.message_types_by_name['TargetCpa'] = _TARGETCPA
DESCRIPTOR.message_types_by_name['TargetOutrankShare'] = _TARGETOUTRANKSHARE
DESCRIPTOR.message_types_by_name['TargetRoas'] = _TARGETROAS
DESCRIPTOR.message_types_by_name['TargetSpend'] = _TARGETSPEND
DESCRIPTOR.message_types_by_name['PercentCpc'] = _PERCENTCPC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EnhancedCpc = _reflection.GeneratedProtocolMessageType('EnhancedCpc', (_message.Message,), dict(
  DESCRIPTOR = _ENHANCEDCPC,
  __module__ = 'google.ads.googleads_v0.proto.common.bidding_pb2'
  ,
  __doc__ = """An automated bidding strategy that raises bids for clicks that seem more
  likely to lead to a conversion and lowers them for clicks where they
  seem less likely.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.EnhancedCpc)
  ))
_sym_db.RegisterMessage(EnhancedCpc)

ManualCpc = _reflection.GeneratedProtocolMessageType('ManualCpc', (_message.Message,), dict(
  DESCRIPTOR = _MANUALCPC,
  __module__ = 'google.ads.googleads_v0.proto.common.bidding_pb2'
  ,
  __doc__ = """Manual click-based bidding where user pays per click.
  
  
  Attributes:
      enhanced_cpc_enabled:
          Whether bids are to be enhanced based on conversion optimizer
          data.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.ManualCpc)
  ))
_sym_db.RegisterMessage(ManualCpc)

ManualCpm = _reflection.GeneratedProtocolMessageType('ManualCpm', (_message.Message,), dict(
  DESCRIPTOR = _MANUALCPM,
  __module__ = 'google.ads.googleads_v0.proto.common.bidding_pb2'
  ,
  __doc__ = """Manual impression-based bidding where user pays per thousand
  impressions.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.ManualCpm)
  ))
_sym_db.RegisterMessage(ManualCpm)

MaximizeConversions = _reflection.GeneratedProtocolMessageType('MaximizeConversions', (_message.Message,), dict(
  DESCRIPTOR = _MAXIMIZECONVERSIONS,
  __module__ = 'google.ads.googleads_v0.proto.common.bidding_pb2'
  ,
  __doc__ = """An automated bidding strategy that sets bids to help get the most
  conversions for your campaign while spending your budget.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.MaximizeConversions)
  ))
_sym_db.RegisterMessage(MaximizeConversions)

MaximizeConversionValue = _reflection.GeneratedProtocolMessageType('MaximizeConversionValue', (_message.Message,), dict(
  DESCRIPTOR = _MAXIMIZECONVERSIONVALUE,
  __module__ = 'google.ads.googleads_v0.proto.common.bidding_pb2'
  ,
  __doc__ = """An automated bidding strategy which tries to maximize conversion value
  given a daily budget.
  
  
  Attributes:
      target_roas:
          The target return on ad spend (ROAS) option. If set, the bid
          strategy will maximize revenue while averaging the target
          return on ad spend. If the target ROAS is high, the bid
          strategy may not be able to spend the full budget. If the
          target ROAS is not set, the bid strategy will aim to achieve
          the highest possible ROAS for the budget.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.MaximizeConversionValue)
  ))
_sym_db.RegisterMessage(MaximizeConversionValue)

PageOnePromoted = _reflection.GeneratedProtocolMessageType('PageOnePromoted', (_message.Message,), dict(
  DESCRIPTOR = _PAGEONEPROMOTED,
  __module__ = 'google.ads.googleads_v0.proto.common.bidding_pb2'
  ,
  __doc__ = """An automated bidding strategy which sets CPC bids to target impressions
  on page one, or page one promoted slots on google.com.
  
  
  Attributes:
      strategy_goal:
          The strategy goal of where impressions are desired to be shown
          on search result pages.
      cpc_bid_ceiling_micros:
          Maximum bid limit that can be set by the bid strategy. The
          limit applies to all keywords managed by the strategy.
      bid_modifier:
          Bid multiplier to be applied to the relevant bid estimate
          (depending on the ``strategy_goal``) in determining a
          keyword's new CPC bid.
      only_raise_cpc_bids:
          Whether the strategy should always follow bid estimate
          changes, or only increase. If false, always sets a keyword's
          new bid to the current bid estimate. If true, only updates a
          keyword's bid if the current bid estimate is greater than the
          current bid.
      raise_cpc_bid_when_budget_constrained:
          Whether the strategy is allowed to raise bids when the
          throttling rate of the budget it is serving out of rises above
          a threshold.
      raise_cpc_bid_when_quality_score_is_low:
          Whether the strategy is allowed to raise bids on keywords with
          lower-range quality scores.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.PageOnePromoted)
  ))
_sym_db.RegisterMessage(PageOnePromoted)

TargetCpa = _reflection.GeneratedProtocolMessageType('TargetCpa', (_message.Message,), dict(
  DESCRIPTOR = _TARGETCPA,
  __module__ = 'google.ads.googleads_v0.proto.common.bidding_pb2'
  ,
  __doc__ = """An automated bid strategy that sets bids to help get as many conversions
  as possible at the target cost-per-acquisition (CPA) you set.
  
  
  Attributes:
      target_cpa_micros:
          Average CPA target. This target should be greater than or
          equal to minimum billable unit based on the currency for the
          account.
      cpc_bid_ceiling_micros:
          Maximum bid limit that can be set by the bid strategy. The
          limit applies to all keywords managed by the strategy.
      cpc_bid_floor_micros:
          Minimum bid limit that can be set by the bid strategy. The
          limit applies to all keywords managed by the strategy.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.TargetCpa)
  ))
_sym_db.RegisterMessage(TargetCpa)

TargetOutrankShare = _reflection.GeneratedProtocolMessageType('TargetOutrankShare', (_message.Message,), dict(
  DESCRIPTOR = _TARGETOUTRANKSHARE,
  __module__ = 'google.ads.googleads_v0.proto.common.bidding_pb2'
  ,
  __doc__ = """An automated bidding strategy that sets bids based on the target
  fraction of auctions where the advertiser should outrank a specific
  competitor.
  
  
  Attributes:
      target_outrank_share_micros:
          The target fraction of auctions where the advertiser should
          outrank the competitor. The advertiser outranks the competitor
          in an auction if either the advertiser appears above the
          competitor in the search results, or appears in the search
          results when the competitor does not. Value must be between 1
          and 1000000, inclusive.
      competitor_domain:
          Competitor's visible domain URL.
      cpc_bid_ceiling_micros:
          Maximum bid limit that can be set by the bid strategy. The
          limit applies to all keywords managed by the strategy.
      only_raise_cpc_bids:
          Whether the strategy should always follow bid estimate
          changes, or only increase. If false, always set a keyword's
          new bid to the current bid estimate. If true, only updates a
          keyword's bid if the current bid estimate is greater than the
          current bid.
      raise_cpc_bid_when_quality_score_is_low:
          Whether the strategy is allowed to raise bids on keywords with
          lower-range quality scores.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.TargetOutrankShare)
  ))
_sym_db.RegisterMessage(TargetOutrankShare)

TargetRoas = _reflection.GeneratedProtocolMessageType('TargetRoas', (_message.Message,), dict(
  DESCRIPTOR = _TARGETROAS,
  __module__ = 'google.ads.googleads_v0.proto.common.bidding_pb2'
  ,
  __doc__ = """An automated bidding strategy that helps you maximize revenue while
  averaging a specific target return on ad spend (ROAS).
  
  
  Attributes:
      target_roas:
          Required. The desired revenue (based on conversion data) per
          unit of spend. Value must be between 0.01 and 1000.0,
          inclusive.
      cpc_bid_ceiling_micros:
          Maximum bid limit that can be set by the bid strategy. The
          limit applies to all keywords managed by the strategy.
      cpc_bid_floor_micros:
          Minimum bid limit that can be set by the bid strategy. The
          limit applies to all keywords managed by the strategy.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.TargetRoas)
  ))
_sym_db.RegisterMessage(TargetRoas)

TargetSpend = _reflection.GeneratedProtocolMessageType('TargetSpend', (_message.Message,), dict(
  DESCRIPTOR = _TARGETSPEND,
  __module__ = 'google.ads.googleads_v0.proto.common.bidding_pb2'
  ,
  __doc__ = """An automated bid strategy that sets your bids to help get as many clicks
  as possible within your budget.
  
  
  Attributes:
      target_spend_micros:
          The spend target under which to maximize clicks. A TargetSpend
          bidder will attempt to spend the smaller of this value or the
          natural throttling spend amount. If not specified, the budget
          is used as the spend target.
      cpc_bid_ceiling_micros:
          Maximum bid limit that can be set by the bid strategy. The
          limit applies to all keywords managed by the strategy.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.TargetSpend)
  ))
_sym_db.RegisterMessage(TargetSpend)

PercentCpc = _reflection.GeneratedProtocolMessageType('PercentCpc', (_message.Message,), dict(
  DESCRIPTOR = _PERCENTCPC,
  __module__ = 'google.ads.googleads_v0.proto.common.bidding_pb2'
  ,
  __doc__ = """A bidding strategy where bids are a fraction of the advertised price for
  some good or service.
  
  
  Attributes:
      cpc_bid_ceiling_micros:
          Maximum bid limit that can be set by the bid strategy. This is
          an optional field entered by the advertiser and specified in
          local micros. Note: A zero value is interpreted in the same
          way as having bid\_ceiling undefined.
      enhanced_cpc_enabled:
          Adjusts the bid for each auction upward or downward, depending
          on the likelihood of a conversion. Individual bids may exceed
          cpc\_bid\_ceiling\_micros, but the average bid amount for a
          campaign should not.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.PercentCpc)
  ))
_sym_db.RegisterMessage(PercentCpc)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.commonB\014BiddingProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Common\312\002\036Google\\Ads\\GoogleAds\\V0\\Common'))
# @@protoc_insertion_point(module_scope)