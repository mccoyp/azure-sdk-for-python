# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessRight(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Access rights of the access policy."""

    READ = "Read"
    WRITE = "Write"
    DELETE = "Delete"


class CopyStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CopyStatusType."""

    PENDING = "pending"
    SUCCESS = "success"
    ABORTED = "aborted"
    FAILED = "failed"


class DeleteSnapshotsOptionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DeleteSnapshotsOptionType."""

    INCLUDE = "include"
    INCLUDE_LEASED = "include-leased"


class FileLastWrittenMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """FileLastWrittenMode."""

    NOW = "Now"
    PRESERVE = "Preserve"


class FilePermissionFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """FilePermissionFormat."""

    SDDL = "Sddl"
    BINARY = "Binary"


class FileRangeWriteType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """FileRangeWriteType."""

    UPDATE = "update"
    CLEAR = "clear"


class LeaseDurationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """When a share is leased, specifies whether the lease is of infinite or fixed duration."""

    INFINITE = "infinite"
    FIXED = "fixed"


class LeaseStateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Lease state of the share."""

    AVAILABLE = "available"
    LEASED = "leased"
    EXPIRED = "expired"
    BREAKING = "breaking"
    BROKEN = "broken"


class LeaseStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current lease status of the share."""

    LOCKED = "locked"
    UNLOCKED = "unlocked"


class ListFilesIncludeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ListFilesIncludeType."""

    TIMESTAMPS = "Timestamps"
    ETAG = "Etag"
    ATTRIBUTES = "Attributes"
    PERMISSION_KEY = "PermissionKey"


class ListSharesIncludeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ListSharesIncludeType."""

    SNAPSHOTS = "snapshots"
    METADATA = "metadata"
    DELETED = "deleted"


class ModeCopyMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ModeCopyMode."""

    SOURCE = "source"
    OVERRIDE = "override"


class NfsFileType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """NfsFileType."""

    REGULAR = "Regular"
    DIRECTORY = "Directory"
    SYM_LINK = "SymLink"


class OwnerCopyMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """OwnerCopyMode."""

    SOURCE = "source"
    OVERRIDE = "override"


class PermissionCopyModeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PermissionCopyModeType."""

    SOURCE = "source"
    OVERRIDE = "override"


class ShareAccessTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ShareAccessTier."""

    TRANSACTION_OPTIMIZED = "TransactionOptimized"
    HOT = "Hot"
    COOL = "Cool"
    PREMIUM = "Premium"


class ShareRootSquash(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ShareRootSquash."""

    NO_ROOT_SQUASH = "NoRootSquash"
    ROOT_SQUASH = "RootSquash"
    ALL_SQUASH = "AllSquash"


class ShareTokenIntent(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ShareTokenIntent."""

    BACKUP = "backup"


class StorageErrorCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Error codes returned by the service."""

    ACCOUNT_ALREADY_EXISTS = "AccountAlreadyExists"
    ACCOUNT_BEING_CREATED = "AccountBeingCreated"
    ACCOUNT_IS_DISABLED = "AccountIsDisabled"
    AUTHENTICATION_FAILED = "AuthenticationFailed"
    AUTHORIZATION_FAILURE = "AuthorizationFailure"
    CONDITION_HEADERS_NOT_SUPPORTED = "ConditionHeadersNotSupported"
    CONDITION_NOT_MET = "ConditionNotMet"
    EMPTY_METADATA_KEY = "EmptyMetadataKey"
    FILE_SHARE_PROVISIONED_BANDWIDTH_DOWNGRADE_NOT_ALLOWED = "FileShareProvisionedBandwidthDowngradeNotAllowed"
    FILE_SHARE_PROVISIONED_IOPS_DOWNGRADE_NOT_ALLOWED = "FileShareProvisionedIopsDowngradeNotAllowed"
    INSUFFICIENT_ACCOUNT_PERMISSIONS = "InsufficientAccountPermissions"
    INTERNAL_ERROR = "InternalError"
    INVALID_AUTHENTICATION_INFO = "InvalidAuthenticationInfo"
    INVALID_HEADER_VALUE = "InvalidHeaderValue"
    INVALID_HTTP_VERB = "InvalidHttpVerb"
    INVALID_INPUT = "InvalidInput"
    INVALID_MD5 = "InvalidMd5"
    INVALID_METADATA = "InvalidMetadata"
    INVALID_QUERY_PARAMETER_VALUE = "InvalidQueryParameterValue"
    INVALID_RANGE = "InvalidRange"
    INVALID_RESOURCE_NAME = "InvalidResourceName"
    INVALID_URI = "InvalidUri"
    INVALID_XML_DOCUMENT = "InvalidXmlDocument"
    INVALID_XML_NODE_VALUE = "InvalidXmlNodeValue"
    MD5_MISMATCH = "Md5Mismatch"
    METADATA_TOO_LARGE = "MetadataTooLarge"
    MISSING_CONTENT_LENGTH_HEADER = "MissingContentLengthHeader"
    MISSING_REQUIRED_QUERY_PARAMETER = "MissingRequiredQueryParameter"
    MISSING_REQUIRED_HEADER = "MissingRequiredHeader"
    MISSING_REQUIRED_XML_NODE = "MissingRequiredXmlNode"
    MULTIPLE_CONDITION_HEADERS_NOT_SUPPORTED = "MultipleConditionHeadersNotSupported"
    OPERATION_TIMED_OUT = "OperationTimedOut"
    OUT_OF_RANGE_INPUT = "OutOfRangeInput"
    OUT_OF_RANGE_QUERY_PARAMETER_VALUE = "OutOfRangeQueryParameterValue"
    REQUEST_BODY_TOO_LARGE = "RequestBodyTooLarge"
    RESOURCE_TYPE_MISMATCH = "ResourceTypeMismatch"
    REQUEST_URL_FAILED_TO_PARSE = "RequestUrlFailedToParse"
    RESOURCE_ALREADY_EXISTS = "ResourceAlreadyExists"
    RESOURCE_NOT_FOUND = "ResourceNotFound"
    SERVER_BUSY = "ServerBusy"
    UNSUPPORTED_HEADER = "UnsupportedHeader"
    UNSUPPORTED_XML_NODE = "UnsupportedXmlNode"
    UNSUPPORTED_QUERY_PARAMETER = "UnsupportedQueryParameter"
    UNSUPPORTED_HTTP_VERB = "UnsupportedHttpVerb"
    CANNOT_DELETE_FILE_OR_DIRECTORY = "CannotDeleteFileOrDirectory"
    CLIENT_CACHE_FLUSH_DELAY = "ClientCacheFlushDelay"
    DELETE_PENDING = "DeletePending"
    DIRECTORY_NOT_EMPTY = "DirectoryNotEmpty"
    FILE_LOCK_CONFLICT = "FileLockConflict"
    INVALID_FILE_OR_DIRECTORY_PATH_NAME = "InvalidFileOrDirectoryPathName"
    PARENT_NOT_FOUND = "ParentNotFound"
    READ_ONLY_ATTRIBUTE = "ReadOnlyAttribute"
    SHARE_ALREADY_EXISTS = "ShareAlreadyExists"
    SHARE_BEING_DELETED = "ShareBeingDeleted"
    SHARE_DISABLED = "ShareDisabled"
    SHARE_NOT_FOUND = "ShareNotFound"
    SHARING_VIOLATION = "SharingViolation"
    SHARE_SNAPSHOT_IN_PROGRESS = "ShareSnapshotInProgress"
    SHARE_SNAPSHOT_COUNT_EXCEEDED = "ShareSnapshotCountExceeded"
    SHARE_SNAPSHOT_OPERATION_NOT_SUPPORTED = "ShareSnapshotOperationNotSupported"
    SHARE_HAS_SNAPSHOTS = "ShareHasSnapshots"
    PREVIOUS_SNAPSHOT_NOT_FOUND = "PreviousSnapshotNotFound"
    CONTAINER_QUOTA_DOWNGRADE_NOT_ALLOWED = "ContainerQuotaDowngradeNotAllowed"
    AUTHORIZATION_SOURCE_IP_MISMATCH = "AuthorizationSourceIPMismatch"
    AUTHORIZATION_PROTOCOL_MISMATCH = "AuthorizationProtocolMismatch"
    AUTHORIZATION_PERMISSION_MISMATCH = "AuthorizationPermissionMismatch"
    AUTHORIZATION_SERVICE_MISMATCH = "AuthorizationServiceMismatch"
    AUTHORIZATION_RESOURCE_TYPE_MISMATCH = "AuthorizationResourceTypeMismatch"
    FEATURE_VERSION_MISMATCH = "FeatureVersionMismatch"
    SHARE_SNAPSHOT_NOT_FOUND = "ShareSnapshotNotFound"
