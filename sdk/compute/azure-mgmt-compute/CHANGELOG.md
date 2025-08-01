# Release History

## 35.0.0 (2025-07-21)

### Features Added

  - Model AccessUri has a new parameter security_metadata_access_sas
  - Model AvailabilitySet has a new parameter system_data
  - Model CapacityReservation has a new parameter system_data
  - Model CapacityReservationGroup has a new parameter system_data
  - Model CreationData has a new parameter instant_access_duration_minutes
  - Model CreationData has a new parameter security_metadata_uri
  - Model DedicatedHost has a new parameter system_data
  - Model DedicatedHostGroup has a new parameter system_data
  - Model DedicatedHostSizeListResult has a new parameter next_link
  - Model Disk has a new parameter availability_policy
  - Model Disk has a new parameter system_data
  - Model DiskAccess has a new parameter system_data
  - Model DiskEncryptionSet has a new parameter system_data
  - Model DiskRestorePoint has a new parameter system_data
  - Model DiskUpdate has a new parameter availability_policy
  - Model Image has a new parameter system_data
  - Model PrivateEndpointConnection has a new parameter system_data
  - Model ProximityPlacementGroup has a new parameter system_data
  - Model ProxyResource has a new parameter system_data
  - Model Resource has a new parameter system_data
  - Model RestorePoint has a new parameter system_data
  - Model RestorePointCollection has a new parameter system_data
  - Model RollingUpgradeStatusInfo has a new parameter system_data
  - Model Snapshot has a new parameter snapshot_access_state
  - Model Snapshot has a new parameter system_data
  - Model SnapshotUpdate has a new parameter snapshot_access_state
  - Model SshPublicKeyResource has a new parameter system_data
  - Model SupportedCapabilities has a new parameter supported_security_option
  - Model SystemData has a new parameter created_by
  - Model SystemData has a new parameter created_by_type
  - Model SystemData has a new parameter last_modified_by
  - Model SystemData has a new parameter last_modified_by_type
  - Model VirtualMachine has a new parameter system_data
  - Model VirtualMachineExtension has a new parameter system_data
  - Model VirtualMachineExtensionImage has a new parameter system_data
  - Model VirtualMachineRunCommand has a new parameter system_data
  - Model VirtualMachineScaleSet has a new parameter system_data
  - Model VirtualMachineScaleSetVM has a new parameter system_data
  - Model VirtualMachineSizeListResult has a new parameter next_link

### Breaking Changes

  - Model Resource no longer has parameter location
  - Model Resource no longer has parameter tags
  - Parameter location of model VirtualMachineExtension is now required
  - Parameter value of model PrivateEndpointConnectionListResult is now required
  - Parameter value of model RestorePointCollectionListResult is now required

## 34.1.0 (2025-03-24)

### Features Added

  - Added operation AvailabilitySetsOperations.begin_convert_to_virtual_machine_scale_set
  - Added operation AvailabilitySetsOperations.cancel_migration_to_virtual_machine_scale_set
  - Added operation AvailabilitySetsOperations.start_migration_to_virtual_machine_scale_set
  - Added operation AvailabilitySetsOperations.validate_migration_to_virtual_machine_scale_set
  - Added operation VirtualMachineImagesOperations.list_with_properties
  - Added operation VirtualMachinesOperations.begin_migrate_to_vm_scale_set
  - Model AvailabilitySet has a new parameter virtual_machine_scale_set_migration_info
  - Model AvailabilitySetUpdate has a new parameter virtual_machine_scale_set_migration_info
  - Model ProxyAgentSettings has a new parameter imds
  - Model ProxyAgentSettings has a new parameter wire_server
  - Model ResiliencyPolicy has a new parameter automatic_zone_rebalancing_policy
  - Model ScaleInPolicy has a new parameter prioritize_unhealthy_v_ms
  - Model SkuProfileVMSize has a new parameter rank
  - Model StorageProfile has a new parameter align_regional_disks_to_vm_zone
  - Model VirtualMachine has a new parameter placement
  - Model VirtualMachineScaleSetVM has a new parameter resilient_vm_deletion_status

## 34.0.0 (2025-01-20)

### Features Added

  - Model CloudServiceVaultCertificate has a new parameter is_bootstrap_certificate

### Breaking Changes

  - Removed subfolders of some unused Api-Versions for smaller package size. If your application requires a specific and non-latest Api-Version, it's recommended to pin this package to the previous released version; If your application always only use latest Api-Version, please ignore this change.
  - Model Gallery no longer has parameter identity
  - Model GalleryImage no longer has parameter allow_update_image
  - Model GalleryImageFeature no longer has parameter starts_at_version
  - Model GalleryImageUpdate no longer has parameter allow_update_image
  - Model GalleryImageVersion no longer has parameter restore
  - Model GalleryImageVersion no longer has parameter validations_profile
  - Model GalleryImageVersionSafetyProfile no longer has parameter block_deletion_before_end_of_life
  - Model GalleryImageVersionUpdate no longer has parameter restore
  - Model GalleryImageVersionUpdate no longer has parameter validations_profile
  - Model GalleryList no longer has parameter security_profile
  - Model GalleryUpdate no longer has parameter identity
  - Model TargetRegion no longer has parameter additional_replica_sets
  - Model UserArtifactSettings no longer has parameter script_behavior_after_reboot
  - Removed operation group GalleryInVMAccessControlProfileVersionsOperations
  - Removed operation group GalleryInVMAccessControlProfilesOperations
  - Removed operation group SoftDeletedResourceOperation

## 33.1.0 (2024-12-16)

### Features Added

  - Added operation group GalleryInVMAccessControlProfileVersionsOperations
  - Added operation group GalleryInVMAccessControlProfilesOperations
  - Added operation group SoftDeletedResourceOperations
  - Model Gallery has a new parameter identity
  - Model GalleryImage has a new parameter allow_update_image
  - Model GalleryImageFeature has a new parameter starts_at_version
  - Model GalleryImageUpdate has a new parameter allow_update_image
  - Model GalleryImageVersion has a new parameter restore
  - Model GalleryImageVersion has a new parameter validations_profile
  - Model GalleryImageVersionSafetyProfile has a new parameter block_deletion_before_end_of_life
  - Model GalleryImageVersionUpdate has a new parameter restore
  - Model GalleryImageVersionUpdate has a new parameter validations_profile
  - Model GalleryList has a new parameter security_profile
  - Model GalleryUpdate has a new parameter identity
  - Model TargetRegion has a new parameter additional_replica_sets
  - Model UserArtifactSettings has a new parameter script_behavior_after_reboot

## 33.0.0 (2024-08-20)

### Features Added

  - Model AvailabilitySet has a new parameter scheduled_events_policy
  - Model AvailabilitySetUpdate has a new parameter scheduled_events_policy
  - Model VirtualMachineScaleSet has a new parameter sku_profile
  - Model VirtualMachineScaleSet has a new parameter zonal_platform_fault_domain_align_mode
  - Model VirtualMachineScaleSetUpdate has a new parameter sku_profile
  - Model VirtualMachineScaleSetUpdate has a new parameter zonal_platform_fault_domain_align_mode
  - Model VirtualMachineScaleSetUpdate has a new parameter zones

### Breaking Changes

  - Model PurchasePlan no longer has parameter promotion_code

## 32.0.0 (2024-07-22)

### Features Added

  - Model DiskRestorePoint has a new parameter logical_sector_size
  - Model PurchasePlan has a new parameter promotion_code
  - Model SecurityPostureReference has a new parameter is_overridable
  - Model VirtualMachineScaleSetUpdateVMProfile has a new parameter security_posture_reference

### Breaking Changes

  - Parameter id of model SecurityPostureReference is now required

## 31.0.0 (2024-04-22)

### Features Added

  - Model DataDisk has a new parameter source_resource
  - Model DataDisksToAttach has a new parameter caching
  - Model DataDisksToAttach has a new parameter delete_option
  - Model DataDisksToAttach has a new parameter disk_encryption_set
  - Model DataDisksToAttach has a new parameter write_accelerator_enabled
  - Model VirtualMachine has a new parameter scheduled_events_policy
  - Model VirtualMachineScaleSet has a new parameter scheduled_events_policy
  - Model VirtualMachineScaleSetReimageParameters has a new parameter force_update_os_disk_for_ephemeral
  - Model VirtualMachineScaleSetUpdateOSDisk has a new parameter diff_disk_settings
  - Model VirtualMachineScaleSetVMReimageParameters has a new parameter force_update_os_disk_for_ephemeral
  - Model VirtualMachineUpdate has a new parameter scheduled_events_policy
  - Operation CapacityReservationGroupsOperations.list_by_subscription has a new optional parameter resource_ids_only

### Breaking Changes

  - Model PurchasePlan no longer has parameter promotion_code

## 30.6.0 (2024-03-15)

### Features Added

  - Model GalleryArtifactVersionFullSource has a new parameter virtual_machine_id

### Bugs Fixed

  - Fix api_version in next_link for paging operation

## 30.5.0 (2024-01-22)

### Features Added

  - Model CreationData has a new parameter provisioned_bandwidth_copy_speed
  - Model PurchasePlan has a new parameter promotion_code

## 30.4.0 (2023-12-18)

### Features Added

  - Added operation DedicatedHostsOperations.begin_redeploy
  - Added operation VirtualMachineScaleSetVMsOperations.begin_approve_rolling_upgrade
  - Added operation VirtualMachineScaleSetVMsOperations.begin_attach_detach_data_disks
  - Added operation VirtualMachineScaleSetsOperations.begin_approve_rolling_upgrade
  - Added operation VirtualMachinesOperations.begin_attach_detach_data_disks
  - Model AutomaticOSUpgradePolicy has a new parameter os_rolling_upgrade_deferral
  - Model CapacityReservationGroup has a new parameter sharing_profile
  - Model CapacityReservationGroupInstanceView has a new parameter shared_subscription_ids
  - Model CapacityReservationGroupUpdate has a new parameter sharing_profile
  - Model CommunityGallery has a new parameter artifact_tags
  - Model CommunityGallery has a new parameter community_metadata
  - Model CommunityGallery has a new parameter disclaimer
  - Model CommunityGalleryImage has a new parameter artifact_tags
  - Model CommunityGalleryImage has a new parameter disclaimer
  - Model CommunityGalleryImageVersion has a new parameter artifact_tags
  - Model CommunityGalleryImageVersion has a new parameter disclaimer
  - Model GalleryImageVersion has a new parameter security_profile
  - Model GalleryImageVersionUpdate has a new parameter security_profile
  - Model RestorePointSourceVMStorageProfile has a new parameter disk_controller_type
  - Model SecurityProfile has a new parameter encryption_identity
  - Model SecurityProfile has a new parameter proxy_agent_settings
  - Model SharedGallery has a new parameter artifact_tags
  - Model SharedGalleryImage has a new parameter artifact_tags
  - Model SharedGalleryImageVersion has a new parameter artifact_tags
  - Model VirtualMachine has a new parameter etag
  - Model VirtualMachine has a new parameter managed_by
  - Model VirtualMachineInstanceView has a new parameter is_vm_in_standby_pool
  - Model VirtualMachineScaleSet has a new parameter etag
  - Model VirtualMachineScaleSet has a new parameter resiliency_policy
  - Model VirtualMachineScaleSetUpdate has a new parameter resiliency_policy
  - Model VirtualMachineScaleSetVM has a new parameter etag
  - Model VirtualMachineScaleSetVMProfile has a new parameter time_created
  - Operation SshPublicKeysOperations.generate_key_pair has a new optional parameter parameters
  - Operation VirtualMachineScaleSetVMsOperations.begin_update has a new optional parameter if_match
  - Operation VirtualMachineScaleSetVMsOperations.begin_update has a new optional parameter if_none_match
  - Operation VirtualMachineScaleSetsOperations.begin_create_or_update has a new optional parameter if_match
  - Operation VirtualMachineScaleSetsOperations.begin_create_or_update has a new optional parameter if_none_match
  - Operation VirtualMachineScaleSetsOperations.begin_update has a new optional parameter if_match
  - Operation VirtualMachineScaleSetsOperations.begin_update has a new optional parameter if_none_match
  - Operation VirtualMachinesOperations.begin_create_or_update has a new optional parameter if_match
  - Operation VirtualMachinesOperations.begin_create_or_update has a new optional parameter if_none_match
  - Operation VirtualMachinesOperations.begin_update has a new optional parameter if_match
  - Operation VirtualMachinesOperations.begin_update has a new optional parameter if_none_match

## 30.3.0 (2023-10-23)

### Features Added

  - Model CreationData has a new parameter elastic_san_resource_id
  - Model Disk has a new parameter last_ownership_update_time

## 30.2.0 (2023-09-15)

### Features Added

  - Model VirtualMachineNetworkInterfaceConfiguration has a new parameter auxiliary_mode
  - Model VirtualMachineNetworkInterfaceConfiguration has a new parameter auxiliary_sku
  - Model VirtualMachinePublicIPAddressDnsSettingsConfiguration has a new parameter domain_name_label_scope
  - Model VirtualMachineScaleSetNetworkConfiguration has a new parameter auxiliary_mode
  - Model VirtualMachineScaleSetNetworkConfiguration has a new parameter auxiliary_sku
  - Model VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings has a new parameter domain_name_label_scope
  - Model VirtualMachineScaleSetUpdateNetworkConfiguration has a new parameter auxiliary_mode
  - Model VirtualMachineScaleSetUpdateNetworkConfiguration has a new parameter auxiliary_sku
  - Model VirtualMachineScaleSetVM has a new parameter time_created

## 30.1.0 (2023-07-21)

### Features Added

  - Model GrantAccessData has a new parameter file_format

## 30.0.0 (2023-05-25)

### Features Added

  - Added operation DedicatedHostsOperations.list_available_sizes
  - Added operation VirtualMachineScaleSetsOperations.begin_reapply
  - Model DedicatedHostUpdate has a new parameter sku
  - Model LinuxVMGuestPatchAutomaticByPlatformSettings has a new parameter bypass_platform_safety_checks_on_user_schedule
  - Model RestorePointSourceMetadata has a new parameter hyper_v_generation
  - Model RestorePointSourceVMDataDisk has a new parameter write_accelerator_enabled
  - Model RestorePointSourceVMOSDisk has a new parameter write_accelerator_enabled
  - Model VirtualMachineExtension has a new parameter provision_after_extensions
  - Model VirtualMachineRunCommand has a new parameter error_blob_managed_identity
  - Model VirtualMachineRunCommand has a new parameter output_blob_managed_identity
  - Model VirtualMachineRunCommand has a new parameter treat_failure_as_deployment_failure
  - Model VirtualMachineRunCommandScriptSource has a new parameter script_uri_managed_identity
  - Model VirtualMachineRunCommandUpdate has a new parameter error_blob_managed_identity
  - Model VirtualMachineRunCommandUpdate has a new parameter output_blob_managed_identity
  - Model VirtualMachineRunCommandUpdate has a new parameter treat_failure_as_deployment_failure
  - Model VirtualMachineScaleSetUpdate has a new parameter priority_mix_policy
  - Model VirtualMachineScaleSetUpdate has a new parameter spot_restore_policy
  - Model VirtualMachineScaleSetVMExtension has a new parameter location
  - Model VirtualMachineScaleSetVMExtension has a new parameter provision_after_extensions
  - Model VirtualMachineScaleSetVMInstanceView has a new parameter computer_name
  - Model VirtualMachineScaleSetVMInstanceView has a new parameter hyper_v_generation
  - Model VirtualMachineScaleSetVMInstanceView has a new parameter os_name
  - Model VirtualMachineScaleSetVMInstanceView has a new parameter os_version
  - Model VirtualMachineScaleSetVMProfile has a new parameter security_posture_reference
  - Model WindowsVMGuestPatchAutomaticByPlatformSettings has a new parameter bypass_platform_safety_checks_on_user_schedule
  - Operation VirtualMachineScaleSetsOperations.begin_deallocate has a new optional parameter hibernate
  - Operation VirtualMachinesOperations.list has a new optional parameter expand
  - Operation VirtualMachinesOperations.list_all has a new optional parameter expand

### Breaking Changes

  - Model VirtualMachineScaleSetIPConfiguration no longer has parameter id
  - Model VirtualMachineScaleSetNetworkConfiguration no longer has parameter id
  - Model VirtualMachineScaleSetUpdateIPConfiguration no longer has parameter id
  - Model VirtualMachineScaleSetUpdateNetworkConfiguration no longer has parameter id

## 29.2.0b2 (2023-04-12)

### Features Added

  - Model VirtualMachineScaleSetVMInstanceView has a new parameter computer_name
  - Model VirtualMachineScaleSetVMInstanceView has a new parameter hyper_v_generation
  - Model VirtualMachineScaleSetVMInstanceView has a new parameter os_name
  - Model VirtualMachineScaleSetVMInstanceView has a new parameter os_version

### Breaking Changes

  - All query and header parameters are now keyword-only
  - Removed api version subfolders. This means you can no longer access any `azure.mgmt.compute.v20xx_xx_xx` modules.
  - Removed `.models` method from `ComputeManagementClient`. Instead, import models from `azure.mgmt.compute.models`.
  - Model VirtualMachineScaleSetIPConfiguration no longer has parameter id
  - Model VirtualMachineScaleSetNetworkConfiguration no longer has parameter id

### Other Changes

  - Initial stable release with our new combined multiapi package. Package size is now 5% of what it used to be.


## 29.2.0b1 (2023-02-20)

### Features Added

  - Model VirtualMachineScaleSetVMInstanceView has a new parameter computer_name
  - Model VirtualMachineScaleSetVMInstanceView has a new parameter hyper_v_generation
  - Model VirtualMachineScaleSetVMInstanceView has a new parameter os_name
  - Model VirtualMachineScaleSetVMInstanceView has a new parameter os_version

## 29.1.0 (2023-01-17)

### Features Added

  - Model CloudService has a new parameter zones
  - Model RestorePointSourceMetadata has a new parameter user_data
  - Model RollingUpgradePolicy has a new parameter max_surge
  - Model RollingUpgradePolicy has a new parameter rollback_failed_instances_on_policy_breach
  - Model ScheduledEventsProfile has a new parameter os_image_notification_profile
  - Model VirtualMachineImage has a new parameter image_deprecation_status
  - Model VirtualMachineReimageParameters has a new parameter exact_version
  - Model VirtualMachineReimageParameters has a new parameter os_profile
  - Model VirtualMachineScaleSet has a new parameter constrained_maximum_capacity
  - Model VirtualMachineScaleSetOSProfile has a new parameter require_guest_provision_signal
  - Model VirtualMachineScaleSetReimageParameters has a new parameter exact_version
  - Model VirtualMachineScaleSetReimageParameters has a new parameter os_profile
  - Model VirtualMachineScaleSetVMProfile has a new parameter service_artifact_reference
  - Model VirtualMachineScaleSetVMReimageParameters has a new parameter exact_version
  - Model VirtualMachineScaleSetVMReimageParameters has a new parameter os_profile

## 29.0.0 (2022-10-13)

### Features Added

  - Model CreationData has a new parameter performance_plus
  - Model Disk has a new parameter bursting_enabled_time
  - Model Disk has a new parameter optimized_for_frequent_attach
  - Model DiskUpdate has a new parameter optimized_for_frequent_attach
  - Model GalleryApplication has a new parameter custom_actions
  - Model GalleryApplicationUpdate has a new parameter custom_actions
  - Model GalleryApplicationVersion has a new parameter safety_profile
  - Model GalleryApplicationVersionPublishingProfile has a new parameter custom_actions
  - Model GalleryApplicationVersionUpdate has a new parameter safety_profile
  - Model GalleryImageVersion has a new parameter safety_profile
  - Model GalleryImageVersionUpdate has a new parameter safety_profile
  - Model SharedGalleryImage has a new parameter eula
  - Model SharedGalleryImage has a new parameter privacy_statement_uri
  - Model Snapshot has a new parameter incremental_snapshot_family_id
  - Model SupportedCapabilities has a new parameter disk_controller_types
  - Model TargetRegion has a new parameter exclude_from_latest

### Breaking Changes

  - Model GalleryArtifactVersionSource no longer has parameter uri

## 28.0.1 (2022-09-30)

### Bugs Fixed

  - Fix paging problem about `api_version`

## 28.0.0 (2022-09-20)

### Features Added

  - Model CapacityReservation has a new parameter platform_fault_domain_count
  - Model CapacityReservationUpdate has a new parameter platform_fault_domain_count
  - Model CapacityReservationUtilization has a new parameter current_capacity
  - Model LinuxConfiguration has a new parameter enable_vm_agent_platform_updates
  - Model StorageProfile has a new parameter disk_controller_type
  - Model VirtualMachineNetworkInterfaceConfiguration has a new parameter disable_tcp_state_tracking
  - Model VirtualMachineScaleSet has a new parameter priority_mix_policy
  - Model VirtualMachineScaleSetNetworkConfiguration has a new parameter disable_tcp_state_tracking
  - Model VirtualMachineScaleSetStorageProfile has a new parameter disk_controller_type
  - Model VirtualMachineScaleSetUpdateNetworkConfiguration has a new parameter disable_tcp_state_tracking
  - Model VirtualMachineScaleSetUpdateStorageProfile has a new parameter disk_controller_type
  - Model VirtualMachineScaleSetUpdateVMProfile has a new parameter hardware_profile
  - Model WindowsConfiguration has a new parameter enable_vm_agent_platform_updates

### Breaking Changes

  - Model PurchasePlan no longer has parameter promotion_code
  - Operation VirtualMachineRunCommandsOperations.begin_create_or_update no longer has parameter content_type
  - Operation VirtualMachineRunCommandsOperations.begin_update no longer has parameter content_type
  - Operation VirtualMachineScaleSetVMRunCommandsOperations.begin_create_or_update no longer has parameter content_type
  - Operation VirtualMachineScaleSetVMRunCommandsOperations.begin_update no longer has parameter content_type
  - Operation VirtualMachineScaleSetVMsOperations.begin_run_command no longer has parameter content_type
  - Operation VirtualMachinesOperations.begin_run_command no longer has parameter content_type

## 27.2.0 (2022-06-29)

**Features**

  - Model CloudService has a new parameter system_data
  - Model CloudServiceNetworkProfile has a new parameter slot_type

## 27.1.0 (2022-06-09)

**Features**

  - Added operation CommunityGalleryImageVersionsOperations.list
  - Added operation CommunityGalleryImagesOperations.list
  - Added operation VirtualMachineImagesOperations.list_by_edge_zone
  - Model CommunityGalleryImage has a new parameter architecture
  - Model CommunityGalleryImage has a new parameter eula
  - Model CommunityGalleryImage has a new parameter privacy_statement_uri
  - Model CommunityGalleryImageVersion has a new parameter exclude_from_latest
  - Model CommunityGalleryImageVersion has a new parameter storage_profile
  - Model DiskEncryptionSet has a new parameter federated_client_id
  - Model DiskEncryptionSetUpdate has a new parameter federated_client_id
  - Model DiskRestorePoint has a new parameter security_profile
  - Model EncryptionSetIdentity has a new parameter user_assigned_identities
  - Model GalleryApplicationVersionPublishingProfile has a new parameter advanced_settings
  - Model GalleryApplicationVersionPublishingProfile has a new parameter settings
  - Model ImageDiskReference has a new parameter community_gallery_image_id
  - Model ImageDiskReference has a new parameter shared_gallery_image_id
  - Model PurchasePlan has a new parameter promotion_code
  - Model SharedGalleryImage has a new parameter architecture
  - Model SharedGalleryImageVersion has a new parameter exclude_from_latest
  - Model SharedGalleryImageVersion has a new parameter storage_profile
  - Model Snapshot has a new parameter copy_completion_error

## 27.0.0 (2022-05-17)

**Features**

  - Model AutomaticOSUpgradePolicy has a new parameter use_rolling_upgrade_policy
  - Model DedicatedHostGroup has a new parameter additional_capabilities
  - Model DedicatedHostGroupUpdate has a new parameter additional_capabilities
  - Model DiskRestorePointReplicationStatus has a new parameter completion_percent
  - Model LinuxPatchSettings has a new parameter automatic_by_platform_settings
  - Model PatchSettings has a new parameter automatic_by_platform_settings
  - Model ProximityPlacementGroup has a new parameter intent
  - Model ProximityPlacementGroup has a new parameter zones
  - Model VMGalleryApplication has a new parameter enable_automatic_upgrade
  - Model VMGalleryApplication has a new parameter treat_failure_as_deployment_failure
  - Model VirtualMachineScaleSetDataDisk has a new parameter delete_option
  - Model VirtualMachineScaleSetOSDisk has a new parameter delete_option
  - Model VirtualMachineScaleSetUpdateOSDisk has a new parameter delete_option
  - Model VirtualMachineScaleSetVM has a new parameter identity
  - Operation VirtualMachineRunCommandsOperations.begin_create_or_update has a new optional and keyword-only parameter content_type
  - Operation VirtualMachineRunCommandsOperations.begin_update has a new optional and keyword-only parameter content_type
  - Operation VirtualMachineScaleSetVMRunCommandsOperations.begin_create_or_update has a new optional and keyword-only parameter content_type
  - Operation VirtualMachineScaleSetVMRunCommandsOperations.begin_update has a new optional and keyword-only parameter content_type
  - Operation VirtualMachineScaleSetVMsOperations.begin_run_command has a new optional and keyword-only parameter content_type
  - Operation VirtualMachinesOperations.begin_run_command has a new optional and keyword-only parameter content_type

**Breaking changes**

  - Model PurchasePlan no longer has parameter promotion_code

## 26.1.0 (2022-02-28)

**Features**

  - Model Disk has a new parameter data_access_auth_mode
  - Model DiskUpdate has a new parameter data_access_auth_mode
  - Model GalleryImage has a new parameter architecture
  - Model GalleryImageUpdate has a new parameter architecture
  - Model PurchasePlan has a new parameter promotion_code
  - Model Snapshot has a new parameter data_access_auth_mode
  - Model SnapshotUpdate has a new parameter data_access_auth_mode
  - Model SupportedCapabilities has a new parameter architecture
  - Model VirtualMachineImage has a new parameter architecture

## 26.0.0 (2022-02-14)

**Features**

  - Model Gallery has a new parameter sharing_status
  - Model GalleryApplicationVersionPublishingProfile has a new parameter target_extended_locations
  - Model GalleryArtifactPublishingProfileBase has a new parameter target_extended_locations
  - Model GalleryImageVersionPublishingProfile has a new parameter target_extended_locations
  - Model GalleryUpdate has a new parameter sharing_status
  - Model OSDiskImageEncryption has a new parameter security_profile
  - Model SharingProfile has a new parameter community_gallery_info

**Breaking changes**

  - Operation GalleriesOperations.get has a new signature

## 25.0.0 (2022-01-28)

**Features**

  - Added operation DedicatedHostsOperations.begin_restart
  - Model AutomaticRepairsPolicy has a new parameter repair_action
  - Model CapacityReservation has a new parameter time_created
  - Model CapacityReservationUpdate has a new parameter time_created
  - Model DedicatedHost has a new parameter time_created
  - Model DedicatedHostUpdate has a new parameter time_created
  - Model ImageReference has a new parameter community_gallery_image_id
  - Model ManagedDiskParameters has a new parameter security_profile
  - Model RestorePoint has a new parameter instance_view
  - Model RestorePoint has a new parameter source_restore_point
  - Model VirtualMachine has a new parameter time_created
  - Model VirtualMachineExtension has a new parameter protected_settings_from_key_vault
  - Model VirtualMachineExtensionUpdate has a new parameter protected_settings_from_key_vault
  - Model VirtualMachineScaleSet has a new parameter time_created
  - Model VirtualMachineScaleSetExtension has a new parameter protected_settings_from_key_vault
  - Model VirtualMachineScaleSetExtensionUpdate has a new parameter protected_settings_from_key_vault
  - Model VirtualMachineScaleSetManagedDiskParameters has a new parameter security_profile
  - Model VirtualMachineScaleSetOSProfile has a new parameter allow_extension_operations
  - Model VirtualMachineScaleSetUpdatePublicIPAddressConfiguration has a new parameter public_ip_prefix
  - Model VirtualMachineScaleSetVMExtension has a new parameter protected_settings_from_key_vault
  - Model VirtualMachineScaleSetVMExtensionUpdate has a new parameter protected_settings_from_key_vault
  - Model VirtualMachineScaleSetVMProfile has a new parameter hardware_profile
  - Model VirtualMachineUpdate has a new parameter time_created

**Breaking changes**

  - Model PurchasePlan no longer has parameter promotion_code
  - Operation RestorePointsOperations.get has a new signature
  - Operation VirtualMachineScaleSetsOperations.force_recovery_service_fabric_platform_update_domain_walk has a new signature
  - Operation VirtualMachineScaleSetsOperations.force_recovery_service_fabric_platform_update_domain_walk has a new signature
  - Operation VirtualMachinesOperations.list has a new signature
  - Operation VirtualMachinesOperations.list_all has a new signature

## 24.0.1 (2022-01-17)

**Bugfixes**

  - Added support for Python3.6 back

## 24.0.0 (2022-01-06)

**Features**

  - Model AccessUri has a new parameter security_data_access_sas
  - Model CreationData has a new parameter security_data_uri
  - Model DiskRestorePoint has a new parameter replication_state
  - Model DiskRestorePoint has a new parameter source_resource_location
  - Model DiskSecurityProfile has a new parameter secure_vm_disk_encryption_set_id
  - Model GrantAccessData has a new parameter get_secure_vm_guest_state_sas
  - Model PurchasePlan has a new parameter promotion_code
  - Model RestorePoint has a new parameter time_created
  - Model Snapshot has a new parameter security_profile
  - Model SnapshotUpdate has a new parameter supported_capabilities

**Breaking changes**

  - Model RestorePoint no longer has parameter provisioning_details

## 23.1.0 (2021-10-12)

**Features**

  - Model PurchasePlanAutoGenerated has a new parameter promotion_code
  - Model Disk has a new parameter public_network_access
  - Model Disk has a new parameter completion_percent
  - Model Disk has a new parameter supported_capabilities
  - Model SnapshotUpdate has a new parameter public_network_access
  - Model Snapshot has a new parameter public_network_access
  - Model Snapshot has a new parameter completion_percent
  - Model Snapshot has a new parameter supported_capabilities
  - Model DiskRestorePoint has a new parameter network_access_policy
  - Model DiskRestorePoint has a new parameter disk_access_id
  - Model DiskRestorePoint has a new parameter public_network_access
  - Model DiskRestorePoint has a new parameter supported_capabilities
  - Model DiskRestorePoint has a new parameter completion_percent
  - Model DiskAccess has a new parameter extended_location
  - Model DiskEncryptionSet has a new parameter auto_key_rotation_error
  - Model DiskUpdate has a new parameter public_network_access
  - Model DiskUpdate has a new parameter supported_capabilities
  - Added operation group CommunityGalleryImageVersionsOperations
  - Added operation group CommunityGalleriesOperations
  - Added operation group CommunityGalleryImagesOperations

## 23.0.0 (2021-09-02)

**Features**

  - Model HardwareProfile has a new parameter vm_size_properties
  - Model VirtualMachineScaleSetVMProfile has a new parameter application_profile
  - Model AdditionalCapabilities has a new parameter hibernation_enabled
  - Model VirtualMachine has a new parameter application_profile
  - Model VirtualMachineScaleSetVMExtensionUpdate has a new parameter suppress_failures
  - Model Gallery has a new parameter soft_delete_policy
  - Model ScaleInPolicy has a new parameter force_deletion
  - Model VirtualMachineScaleSetExtensionUpdate has a new parameter suppress_failures
  - Model GalleryArtifactPublishingProfileBase has a new parameter replication_mode
  - Model GalleryImageVersionPublishingProfile has a new parameter replication_mode
  - Model GalleryApplicationVersionPublishingProfile has a new parameter replication_mode
  - Model ImageReference has a new parameter shared_gallery_image_id
  - Model VirtualMachineUpdate has a new parameter application_profile
  - Model VirtualMachineScaleSetVMExtension has a new parameter suppress_failures
  - Model ResourceSkuLocationInfo has a new parameter type
  - Model ResourceSkuLocationInfo has a new parameter extended_locations
  - Model VirtualMachineScaleSetExtension has a new parameter suppress_failures
  - Model VirtualMachineExtension has a new parameter suppress_failures
  - Model VirtualMachineExtensionUpdate has a new parameter suppress_failures
  - Model GalleryUpdate has a new parameter soft_delete_policy

**Breaking changes**

  - Operation ResourceSkusOperations.list has a new signature
  - Operation VirtualMachinesOperations.begin_deallocate has a new signature

## 22.1.0 (2021-07-22)

**Features**

  - Model VirtualMachineUpdate has a new parameter capacity_reservation
  - Model VirtualMachine has a new parameter capacity_reservation
  - Model VirtualMachineScaleSet has a new parameter spot_restore_policy
  - Model VirtualMachineScaleSetVMProfile has a new parameter capacity_reservation
  - Added operation group CapacityReservationsOperations
  - Added operation group CapacityReservationGroupsOperations

## 22.0.0 (2021-07-08)

**Features**

  - Model RestorePointSourceMetadata has a new parameter location
  - Added operation DiskRestorePointOperations.begin_revoke_access
  - Added operation DiskRestorePointOperations.begin_grant_access

**Breaking changes**

  - Model PublicIPAddressSku has a new signature

## 21.0.0 (2021-05-25)

**Features**

  - Model NetworkInterfaceReference has a new parameter delete_option
  - Model DataDisk has a new parameter delete_option
  - Model VirtualMachineScaleSetPublicIPAddressConfiguration has a new parameter sku
  - Model VirtualMachineScaleSetPublicIPAddressConfiguration has a new parameter delete_option
  - Model VirtualMachineScaleSetNetworkConfiguration has a new parameter delete_option
  - Model OSDisk has a new parameter delete_option
  - Model VirtualMachineScaleSetVM has a new parameter user_data
  - Model VirtualMachineScaleSetUpdateNetworkProfile has a new parameter network_api_version
  - Model VirtualMachineScaleSetUpdateVMProfile has a new parameter user_data
  - Model VirtualMachineScaleSetVMProfile has a new parameter user_data
  - Model LinuxPatchSettings has a new parameter assessment_mode
  - Model VirtualMachineScaleSetUpdatePublicIPAddressConfiguration has a new parameter delete_option
  - Model VirtualMachineUpdate has a new parameter user_data
  - Model VirtualMachineUpdate has a new parameter scheduled_events_profile
  - Model NetworkProfile has a new parameter network_api_version
  - Model NetworkProfile has a new parameter network_interface_configurations
  - Model VirtualMachine has a new parameter user_data
  - Model VirtualMachine has a new parameter scheduled_events_profile
  - Model PatchSettings has a new parameter assessment_mode
  - Model VirtualMachineScaleSetUpdateNetworkConfiguration has a new parameter delete_option
  - Model VirtualMachineScaleSetNetworkProfile has a new parameter network_api_version
  - Added operation group RestorePointCollectionsOperations
  - Added operation group RestorePointsOperations

**Breaking changes**

  - Operation VirtualMachineScaleSetsOperations.get has a new signature
  - Model PurchasePlan no longer has parameter promotion_code

## 20.0.0 (2021-04-06)

**Features**

  - Model PurchasePlan has a new parameter promotion_code
  - Model DiskUpdate has a new parameter supports_hibernation
  - Model DiskUpdate has a new parameter property_updates_in_progress
  - Model SnapshotUpdate has a new parameter supports_hibernation
  - Model DiskRestorePoint has a new parameter supports_hibernation
  - Model DiskEncryptionSetUpdate has a new parameter identity
  - Model DiskEncryptionSetUpdate has a new parameter rotation_to_latest_key_version_enabled
  - Model CloudServiceProperties has a new parameter allow_model_override
  - Model LoadBalancerConfiguration has a new parameter id
  - Model CloudServiceInstanceView has a new parameter private_ids
  - Model Snapshot has a new parameter supports_hibernation
  - Model DiskEncryptionSet has a new parameter last_key_rotation_timestamp
  - Model DiskEncryptionSet has a new parameter rotation_to_latest_key_version_enabled
  - Model Disk has a new parameter security_profile
  - Model Disk has a new parameter supports_hibernation
  - Model Disk has a new parameter property_updates_in_progress
  - Added operation group CloudServiceOperatingSystemsOperations

**Breaking changes**

  - Parameter name of model LoadBalancerConfiguration is now required
  - Parameter properties of model LoadBalancerConfiguration is now required
  - Parameter frontend_ip_configurations of model LoadBalancerConfigurationProperties is now required
  - Parameter name of model LoadBalancerFrontendIPConfiguration is now required
  - Parameter properties of model LoadBalancerFrontendIPConfiguration is now required


## 19.0.0 (2021-02-20)

**Features**

  - Model VirtualMachineUpdate has a new parameter platform_fault_domain
  - Model VirtualMachineImage has a new parameter extended_location
  - Model VirtualMachineImage has a new parameter features
  - Model VirtualMachineSoftwarePatchProperties has a new parameter kb_id
  - Model LinuxConfiguration has a new parameter patch_settings
  - Model PatchSettings has a new parameter enable_hotpatching
  - Model VirtualMachineAssessPatchesResult has a new parameter available_patches
  - Model VirtualMachineImageResource has a new parameter extended_location
  - Model VirtualMachinePatchStatus has a new parameter configuration_statuses
  - Model RollingUpgradePolicy has a new parameter enable_cross_zone_upgrade
  - Model RollingUpgradePolicy has a new parameter prioritize_unhealthy_instances
  - Model DataDisk has a new parameter detach_option
  - Model Image has a new parameter extended_location
  - Model VirtualMachine has a new parameter extended_location
  - Model VirtualMachine has a new parameter platform_fault_domain
  - Model SecurityProfile has a new parameter uefi_settings
  - Model SecurityProfile has a new parameter security_type
  - Model VirtualMachineScaleSet has a new parameter extended_location
  - Model VirtualMachineScaleSet has a new parameter orchestration_mode
  - Added operation VirtualMachinesOperations.begin_install_patches
  - Added operation VirtualMachineScaleSetsOperations.list_by_location
  - Added operation group VirtualMachineImagesEdgeZoneOperations

**Breaking changes**

  - Operation VirtualMachineScaleSetVMsOperations.begin_delete has a new signature
  - Operation VirtualMachineScaleSetsOperations.begin_delete has a new signature
  - Operation VirtualMachineScaleSetsOperations.begin_delete_instances has a new signature
  - Model VirtualMachineSoftwarePatchProperties no longer has parameter kbid
  - Model LastPatchInstallationSummary no longer has parameter started_by
  - Model LastPatchInstallationSummary no longer has parameter reboot_status
  - Model VirtualMachineAssessPatchesResult no longer has parameter patches
  - Model PurchasePlan no longer has parameter promotion_code

## 18.2.0 (2021-02-02)

**Features**

  - Added operation group CloudServicesUpdateDomainOperations
  - Added operation group CloudServiceRolesOperations
  - Added operation group CloudServiceRoleInstancesOperations
  - Added operation group CloudServicesOperations

## 18.1.0 (2021-01-19)

**Features**
  - Model Disk has a new parameter purchase_plan
  - Model Disk has a new parameter extended_location
  - Model Disk has a new parameter bursting_enabled
  - Model ThrottledRequestsInput has a new parameter group_by_client_application_id
  - Model ThrottledRequestsInput has a new parameter group_by_user_agent
  - Model Snapshot has a new parameter purchase_plan
  - Model Snapshot has a new parameter extended_location
  - Model DiskUpdate has a new parameter purchase_plan
  - Model DiskUpdate has a new parameter bursting_enabled
  - Model LogAnalyticsInputBase has a new parameter group_by_client_application_id
  - Model LogAnalyticsInputBase has a new parameter group_by_user_agent
  - Model PurchasePlan has a new parameter promotion_code
  - Model VirtualMachineScaleSetNetworkConfiguration has a new parameter enable_fpga
  - Model RequestRateByIntervalInput has a new parameter group_by_client_application_id
  - Model RequestRateByIntervalInput has a new parameter group_by_user_agent
  - Model VirtualMachineScaleSetUpdateNetworkConfiguration has a new parameter enable_fpga
  - Added operation DiskAccessesOperations.list_private_endpoint_connections
  - Added operation DiskAccessesOperations.begin_delete_a_private_endpoint_connection
  - Added operation DiskAccessesOperations.begin_update_a_private_endpoint_connection
  - Added operation DiskAccessesOperations.get_a_private_endpoint_connection
  - Added operation group DiskRestorePointOperations

## 18.0.0 (2020-11-17)

**Features**

  - Model GalleryImageUpdate has a new parameter features
  - Model GalleryApplicationVersionPublishingProfile has a new parameter manage_actions
  - Model GalleryImage has a new parameter features
  - Model Gallery has a new parameter sharing_profile
  - Model GalleryArtifactVersionSource has a new parameter uri
  - Model GalleryUpdate has a new parameter sharing_profile
  - Model UserArtifactSource has a new parameter default_configuration_link
  - Added operation VirtualMachineRunCommandsOperations.begin_update
  - Added operation VirtualMachineRunCommandsOperations.begin_create_or_update
  - Added operation VirtualMachineRunCommandsOperations.begin_delete
  - Added operation VirtualMachineRunCommandsOperations.get_by_virtual_machine
  - Added operation VirtualMachineRunCommandsOperations.list_by_virtual_machine
  - Added operation group SharedGalleriesOperations
  - Added operation group VirtualMachineScaleSetVMRunCommandsOperations
  - Added operation group GallerySharingProfileOperations
  - Added operation group SharedGalleryImageVersionsOperations
  - Added operation group SharedGalleryImagesOperations

**Breaking changes**

  - Operation GalleriesOperations.get has a new signature
  - Operation VirtualMachinesOperations.begin_delete has a new signature
  - Model GalleryApplicationVersionPublishingProfile no longer has parameter content_type
  - Model UserArtifactSource no longer has parameter file_name

## 17.0.0 (2020-09-16)

**Features**

  - Model VirtualMachineExtensionUpdate has a new parameter enable_automatic_upgrade
  - Model VirtualMachineScaleSetExtensionUpdate has a new parameter enable_automatic_upgrade
  - Model DedicatedHostGroup has a new parameter instance_view
  - Model DedicatedHostGroup has a new parameter support_automatic_placement
  - Model VirtualMachineScaleSetExtension has a new parameter enable_automatic_upgrade
  - Model VirtualMachineScaleSetVM has a new parameter security_profile
  - Model VirtualMachineImage has a new parameter disallowed
  - Model VirtualMachine has a new parameter security_profile
  - Model VirtualMachine has a new parameter extensions_time_budget
  - Model VirtualMachine has a new parameter host_group
  - Model VirtualMachineInstanceView has a new parameter vm_health
  - Model VirtualMachineInstanceView has a new parameter patch_status
  - Model VirtualMachineInstanceView has a new parameter assigned_host
  - Model DiskEncryptionSet has a new parameter encryption_type
  - Model Snapshot has a new parameter disk_state
  - Model Snapshot has a new parameter disk_access_id
  - Model Snapshot has a new parameter network_access_policy
  - Model CreationData has a new parameter logical_sector_size
  - Model DiskEncryptionSetUpdate has a new parameter encryption_type
  - Model VirtualMachineScaleSetVMInstanceView has a new parameter assigned_host
  - Model WindowsConfiguration has a new parameter patch_settings
  - Model DiskUpdate has a new parameter disk_access_id
  - Model DiskUpdate has a new parameter network_access_policy
  - Model DiskUpdate has a new parameter tier
  - Model VirtualMachineScaleSetUpdateVMProfile has a new parameter security_profile
  - Model VirtualMachineScaleSetVMProfile has a new parameter security_profile
  - Model VirtualMachineUpdate has a new parameter security_profile
  - Model VirtualMachineUpdate has a new parameter extensions_time_budget
  - Model VirtualMachineUpdate has a new parameter host_group
  - Model Disk has a new parameter disk_access_id
  - Model Disk has a new parameter network_access_policy
  - Model Disk has a new parameter tier
  - Model VirtualMachineExtension has a new parameter enable_automatic_upgrade
  - Model VirtualMachineScaleSet has a new parameter host_group
  - Model DedicatedHostGroupUpdate has a new parameter instance_view
  - Model DedicatedHostGroupUpdate has a new parameter support_automatic_placement
  - Model SnapshotUpdate has a new parameter disk_access_id
  - Model SnapshotUpdate has a new parameter network_access_policy
  - Model VirtualMachineScaleSetExtensionProfile has a new parameter extensions_time_budget
  - Added operation VirtualMachineScaleSetVMsOperations.retrieve_boot_diagnostics_data
  - Added operation VirtualMachinesOperations.retrieve_boot_diagnostics_data
  - Added operation VirtualMachinesOperations.begin_assess_patches
  - Added operation DiskEncryptionSetsOperations.list_associated_resources
  - Added operation group DiskAccessesOperations

**Breaking changes**

  - Operation DedicatedHostGroupsOperations.get has a new signature

## 17.0.0b1 (2020-06-17)

This is beta preview version.

This version uses a next-generation code generator that introduces important breaking changes, but also important new features (like unified authentication and async programming).

**General breaking changes**

- Credential system has been completly revamped:

  - `azure.common.credentials` or `msrestazure.azure_active_directory` instances are no longer supported, use the `azure-identity` classes instead: https://pypi.org/project/azure-identity/
  - `credentials` parameter has been renamed `credential`

- The `config` attribute no longer exists on a client, configuration should be passed as kwarg. Example: `MyClient(credential, subscription_id, enable_logging=True)`. For a complete set of
  supported options, see the [parameters accept in init documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)
- You can't import a `version` module anymore, use `__version__` instead
- Operations that used to return a `msrest.polling.LROPoller` now returns a `azure.core.polling.LROPoller` and are prefixed with `begin_`.
- Exceptions tree have been simplified and most exceptions are now `azure.core.exceptions.HttpResponseError` (`CloudError` has been removed).
- Most of the operation kwarg have changed. Some of the most noticeable:

  - `raw` has been removed. Equivalent feature can be found using `cls`, a callback that will give access to internal HTTP response for advanced user
  - For a complete set of
  supported options, see the [parameters accept in Request documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)

**General new features**

- Type annotations support using `typing`. SDKs are mypy ready.
- This client has now stable and official support for async. Check the `aio` namespace of your package to find the async client.
- This client now support natively tracing library like OpenCensus or OpenTelemetry. See this [tracing quickstart](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core-tracing-opentelemetry) for an overview.

## 12.0.0 (2020-03-23)

**Features**

- Model VirtualMachineScaleSetInstanceView has a new parameter orchestration_services
- Added operation VirtualMachineScaleSetsOperations.set_orchestration_service_state
- Added operation group SshPublicKeysOperations

**Breaking changes**

- Model AvailabilitySetUpdate no longer has parameter id
- Model AvailabilitySetUpdate no longer has parameter name
- Model AvailabilitySetUpdate no longer has parameter type
- Model VirtualMachineScaleSetUpdate no longer has parameter id
- Model VirtualMachineScaleSetUpdate no longer has parameter name
- Model VirtualMachineScaleSetUpdate no longer has parameter type
- Model DedicatedHostGroupUpdate no longer has parameter id
- Model DedicatedHostGroupUpdate no longer has parameter name
- Model DedicatedHostGroupUpdate no longer has parameter type
- Model VirtualMachineUpdate no longer has parameter id
- Model VirtualMachineUpdate no longer has parameter name
- Model VirtualMachineUpdate no longer has parameter type
- Model DedicatedHostUpdate no longer has parameter id
- Model DedicatedHostUpdate no longer has parameter name
- Model DedicatedHostUpdate no longer has parameter type
- Model ImageUpdate no longer has parameter id
- Model ImageUpdate no longer has parameter name
- Model ImageUpdate no longer has parameter type
- Model VirtualMachineExtensionUpdate no longer has parameter virtual_machine_extension_update_type
- Model VirtualMachineExtensionUpdate no longer has parameter id
- Model VirtualMachineExtensionUpdate no longer has parameter name
- Model ProximityPlacementGroupUpdate has a new signature
- Model UpdateResource has a new signature

## 11.1.0 (2020-03-09)

**Features**

- Operation VirtualMachineImagesOperations.list has a new parameter $expand

**Bugfixes**

- remove not-working $filter in Operation VirtualMachineImagesOperations.list

## 11.0.0 (2020-02-27)

**Features**

  - Model AvailabilitySetUpdate has a new parameter name
  - Model AvailabilitySetUpdate has a new parameter id
  - Model AvailabilitySetUpdate has a new parameter type
  - Model DedicatedHostGroupUpdate has a new parameter name
  - Model DedicatedHostGroupUpdate has a new parameter id
  - Model DedicatedHostGroupUpdate has a new parameter type
  - Model ImageReference has a new parameter exact_version
  - Model SnapshotUpdate has a new parameter encryption
  - Model ProximityPlacementGroup has a new parameter colocation_status
  - Model ImageUpdate has a new parameter name
  - Model ImageUpdate has a new parameter id
  - Model ImageUpdate has a new parameter type
  - Model VirtualMachineExtensionUpdate has a new parameter name
  - Model VirtualMachineExtensionUpdate has a new parameter id
  - Model VirtualMachineExtensionUpdate has a new parameter virtual_machine_extension_update_type
  - Model Disk has a new parameter share_info
  - Model Disk has a new parameter disk_mbps_read_only
  - Model Disk has a new parameter managed_by_extended
  - Model Disk has a new parameter max_shares
  - Model Disk has a new parameter disk_iops_read_only
  - Model CreationData has a new parameter gallery_image_reference
  - Model DiskUpdate has a new parameter max_shares
  - Model DiskUpdate has a new parameter encryption
  - Model DiskUpdate has a new parameter disk_mbps_read_only
  - Model DiskUpdate has a new parameter disk_iops_read_only
  - Model VirtualMachineScaleSetUpdate has a new parameter name
  - Model VirtualMachineScaleSetUpdate has a new parameter id
  - Model VirtualMachineScaleSetUpdate has a new parameter type
  - Model DedicatedHostUpdate has a new parameter name
  - Model DedicatedHostUpdate has a new parameter id
  - Model DedicatedHostUpdate has a new parameter type
  - Model TargetRegion has a new parameter encryption
  - Model VirtualMachineUpdate has a new parameter name
  - Model VirtualMachineUpdate has a new parameter id
  - Model VirtualMachineUpdate has a new parameter type
  - Model VirtualMachineScaleSetExtension has a new parameter type1
  - Added operation GalleriesOperations.update
  - Added operation GalleryImagesOperations.update
  - Added operation GalleryImageVersionsOperations.update
  - Added operation VirtualMachineScaleSetExtensionsOperations.update
  - Added operation GalleryApplicationVersionsOperations.update
  - Added operation GalleryApplicationsOperations.update

**Breaking changes**

  - Model AutomaticRepairsPolicy no longer has parameter max_instance_repairs_percent
  - Model ProximityPlacementGroupUpdate has a new signature
  - Model UpdateResource has a new signature

## 10.0.0 (2019-11-18)

**Features**

  - Model VirtualMachineScaleSetUpdate has a new parameter
    proximity_placement_group
  - Enum VirtualMachinePriorityTypes has new value Spot

**Breaking changes**

  - Operation ProximityPlacementGroupsOperations.get has a new signature

## 9.0.0 (2019-10-22)

**Features**

  - Model VirtualMachineScaleSetUpdateNetworkProfile has a new parameter
    health_probe
  - Model VirtualMachineScaleSetUpdate has a new parameter
    do_not_run_extensions_on_overprovisioned_vms
  - Model VirtualMachineScaleSetUpdate has a new parameter
    automatic_repairs_policy
  - Model VirtualMachineScaleSetManagedDiskParameters has a new
    parameter disk_encryption_set
  - Model ImageDataDisk has a new parameter disk_encryption_set
  - Model VirtualMachineScaleSet has a new parameter
    automatic_repairs_policy
  - Model ImageOSDisk has a new parameter disk_encryption_set
  - Model ManagedDiskParameters has a new parameter
    disk_encryption_set
  - Model Snapshot has a new parameter encryption
  - Model VirtualMachineScaleSetDataDisk has a new parameter
    disk_mbps_read_write
  - Model VirtualMachineScaleSetDataDisk has a new parameter
    disk_iops_read_write
  - Model Disk has a new parameter encryption
  - Model VirtualMachineScaleSetPublicIPAddressConfiguration has a new
    parameter public_ip_address_version
  - Model DataDisk has a new parameter disk_mbps_read_write
  - Model DataDisk has a new parameter disk_iops_read_write
  - Model OSProfile has a new parameter
    require_guest_provision_signal
  - Added operation VirtualMachinesOperations.reapply
  - Added operation group DiskEncryptionSetsOperations
  - Added operation group VirtualMachineScaleSetVMExtensionsOperations

**Breaking changes**

  - Operation VirtualMachinesOperations.list_all has a new signature
  - Operation ResourceSkusOperations.list has a new signature

## 8.0.0 (2019-09-12)

**Note**

  - Compute API version default is now 2019-07-01
  - New disks version 2019-03-01
  - New galleries version 2019-07-01

**Features**

  - Model GalleryImageVersionStorageProfile has a new parameter source
  - Model GalleryDiskImage has a new parameter source
  - Model Snapshot has new parameters: disk_size_bytes, unique_id,
    incremental
  - Model EncryptionSettingsCollection has a new parameter
    encryption_settings_version
  - Model CreationData has new parameters: source_unique_id,
    upload_size_bytes

**Breaking Changes**

  - Model GalleryImageVersionPublishingProfile no longer has parameter
    source

## 7.0.0 (2019-08-27)

**Features**

  - Model VirtualMachineScaleSetUpdateVMProfile has a new parameter
    scheduled_events_profile
  - Model VirtualMachineScaleSetUpdateVMProfile has a new parameter
    billing_profile
  - Model VirtualMachine has a new parameter
    virtual_machine_scale_set
  - Model VirtualMachine has a new parameter priority
  - Model VirtualMachine has a new parameter billing_profile
  - Model VirtualMachine has a new parameter eviction_policy
  - Model VirtualMachineScaleSetVMProfile has a new parameter
    scheduled_events_profile
  - Model VirtualMachineScaleSetVMProfile has a new parameter
    billing_profile
  - Model VirtualMachineImage has a new parameter hyper_vgeneration
  - Model VirtualMachineUpdate has a new parameter
    virtual_machine_scale_set
  - Model VirtualMachineUpdate has a new parameter priority
  - Model VirtualMachineUpdate has a new parameter billing_profile
  - Model VirtualMachineUpdate has a new parameter eviction_policy

**Breaking changes**

  - Operation VirtualMachineScaleSetVMsOperations.get has a new
    signature

## 6.0.0 (2019-07-20)

**Features**

  - Model VirtualMachine has a new parameter host
  - Model VirtualMachineUpdate has a new parameter host
  - Model VirtualMachineInstanceView has a new parameter
    hyper_vgeneration
  - Added operation group GalleryApplicationVersionsOperations
  - Added operation group GalleryApplicationsOperations
  - Added operation group DedicatedHostsOperations
  - Added operation group DedicatedHostGroupsOperations

**Breaking changes**

  - Model GalleryArtifactPublishingProfileBase has a new signature

**General Breaking changes**

This version uses a next-generation code generator that *might*
introduce breaking changes if you were importing from the v20xx_yy_zz
API folders. In summary, some modules were incorrectly
visible/importable and have been renamed. This fixed several issues
caused by usage of classes that were not supposed to be used in the
first place.

  - ComputeManagementClient cannot be imported from
    `azure.mgmt.compute.v20xx_yy_zz.compute_management_client`
    anymore (import from `azure.mgmt.compute.v20xx_yy_zz` works like
    before)
  - ComputeManagementClientConfiguration import has been moved from
    `azure.mgmt.compute.v20xx_yy_zz.compute_management_client` to
    `azure.mgmt.compute.v20xx_yy_zz`
  - A model `MyClass` from a "models" sub-module cannot be imported
    anymore using `azure.mgmt.compute.v20xx_yy_zz.models.my_class`
    (import from `azure.mgmt.compute.v20xx_yy_zz.models` works like
    before)
  - An operation class `MyClassOperations` from an `operations`
    sub-module cannot be imported anymore using
    `azure.mgmt.compute.v20xx_yy_zz.operations.my_class_operations`
    (import from `azure.mgmt.compute.v20xx_yy_zz.operations` works
    like before)

Last but not least, HTTP connection pooling is now enabled by default.
You should always use a client as a context manager, or call close(), or
use no more than one client per process.

## 5.0.0 (2019-04-26)

**Features**

  - Model ImageUpdate has a new parameter hyper_vgeneration
  - Model Image has a new parameter hyper_vgeneration
  - Model AvailabilitySet has a new parameter
    proximity_placement_group
  - Model VirtualMachine has a new parameter proximity_placement_group
  - Model VirtualMachineUpdate has a new parameter
    proximity_placement_group
  - Model VirtualMachineScaleSet has a new parameter
    proximity_placement_group
  - Model VirtualMachineScaleSet has a new parameter
    additional_capabilities
  - Model VirtualMachineScaleSetUpdate has a new parameter
    additional_capabilities
  - Model AvailabilitySetUpdate has a new parameter
    proximity_placement_group
  - Added operation group ProximityPlacementGroupsOperations
  - Model DataDisk has a new parameter to_be_detached
  - Model ResourceSkuLocationInfo has a new output zone_details

**Breaking changes**

  - Model VirtualMachineScaleSetVMProfile no longer has parameter
    additional_capabilities
  - Latest version of disks/snapshot renamed the enum
    StorageAccountTypes to DiskStorageAccountTypes
  - images.create_or_update requires hyper_vgeneration parameter if
    disk is OS type

## 4.6.2 (2019-04-22)

**Bugfix**

  - Revert "images" API version introduced in 4.6.0 from 2019-03-01 to
    2018-10-01 for backward compatiblity #4891

## 4.6.1 (2019-04-18)

**Bugfixes**

  - Make enum declarations in Compute package consistent, for the sake
    of code inspection.

## 4.6.0 (2019-04-12)

**Features**

  - Model VirtualMachineScaleSet has a new parameter
    do_not_run_extensions_on_overprovisioned_vms
  - Model VirtualMachineScaleSetVM has a new parameter
    network_profile_configuration
  - Model VirtualMachineScaleSetVM has a new parameter
    protection_policy
  - Model VirtualMachineScaleSetVM has a new parameter
    model_definition_applied
  - Added operation
    VirtualMachineScaleSetsOperations.convert_to_single_placement_group
  - Operation VirtualMachineScaleSetVMsOperations.power_off has a new
    signature and can now skip_shutdown
  - Operation VirtualMachinesOperations.power_off has a new signature
    and can now skip_shutdown
  - Operation VirtualMachineScaleSetsOperations.power_off has a new
    signature and can now skip_shutdown

## 4.5.1 (2019-03-29)

**Bugfixes**

  - Fix regression in direct import from models

## 4.5.0 (2019-03-28)

**New version of Managed Disks**

  - Disks/Snapshots have a new optional property HyperVGeneration which
    may be set to V1 or V2.
  - EncryptionSettings on a disk are now a collection instead of a
    single value. This allows multiple volumes on an encrypted disk.
  - There is a new CreateOption (Upload) for disks. To upload disks
    customers

>   - PUT a disk with CreateOption.Upload.
>   - Use GrantAccess API with AccessLevel.Write to a get a write SAS to
>     the disk. This is a new access level and it can only be used when
>     uploading to a new disk. Customers can then use storage API to
>     upload the bits for the disk.
>   - There are new DiskStates (DiskState.ReadyToUpload and
>     DiskState.ActiveUpload) that are associated with the upload
>     process.

## 4.4.0 (2018-01-04)

**Features**

  - Model VirtualMachineScaleSetExtension has a new parameter
    provision_after_extensions
  - Operation VirtualMachineScaleSetVMsOperations.reimage has a new
    parameter temp_disk
  - Operation VirtualMachineScaleSetsOperations.reimage has a new
    parameter temp_disk
  - Added operation VirtualMachinesOperations.reimage

## 4.3.1 (2018-10-15)

**Bugfix**

  - Fix sdist broken in 4.3.0. No code change.

## 4.3.0 (2018-10-02)

**Note**

  - Compute API version default is now 2018-10-01

**Features/BreakingChanges**

  - This version updates the access to properties realted to automatic
    OS upgrade introduced in 4.0.0

## 4.2.0 (2018-09-25)

**Features**

  - Model OSDisk has a new parameter diff_disk_settings
  - Model BootDiagnosticsInstanceView has a new parameter status
  - Model VirtualMachineScaleSetOSDisk has a new parameter
    diff_disk_settings
  - Added operation VirtualMachinesOperations.list_by_location

**Note**

  - azure-mgmt-nspkg is not installed anymore on Python 3 (PEP420-based
    namespace package)

## 4.1.0 (2018-09-12)

2018-06-01 for 'disks' and 'snapshots' (new default)

**Features**

  - Model DiskUpdate has a new parameter disk_iops_read_write
  - Model DiskUpdate has a new parameter disk_mbps_read_write
  - Model VirtualMachineUpdate has a new parameter
    additional_capabilities (ultraSSDEnabled attribute)
  - Model VirtualMachineScaleSetVM has a new parameter
    additional_capabilities (ultraSSDEnabled attribute)
  - Model VirtualMachineScaleSetPublicIPAddressConfiguration has a new
    parameter public_ip_prefix
  - Model Disk has a new parameter disk_iops_read_write
  - Model Disk has a new parameter disk_mbps_read_write
  - Model VirtualMachineScaleSetVMProfile has a new parameter
    additional_capabilities (ultraSSDEnabled attribute)
  - Model VirtualMachine has a new parameter additional_capabilities
    (ultraSSDEnabled attribute)
  - Added operation
    VirtualMachineScaleSetRollingUpgradesOperations.start_extension_upgrade
  - New enum value UltraSSD_LRS for StorageAccountTypes

## 4.0.1 (2018-07-23)

**Bugfix**

  - Fix incorrect import from azure.mgmt.compute.models

## 4.0.0 (2018-07-20)

**Features**

  - Model VirtualMachineScaleSetIdentity has a new parameter
    user_assigned_identities
  - Model VirtualMachineScaleSetIPConfiguration has a new parameter
    application_security_groups
  - Model VirtualMachineScaleSetUpdateIPConfiguration has a new
    parameter application_security_groups
  - Model VirtualMachineIdentity has a new parameter
    user_assigned_identities
  - Model LinuxConfiguration has a new parameter provision_vm_agent
  - Model OSProfile has a new parameter allow_extension_operations
  - Added operation group GalleryImagesOperations
  - Added operation group GalleryImageVersionsOperations
  - Added operation group GalleriesOperations
  - Model UpgradeOperationHistoricalStatusInfoProperties has a new
    parameter rollback_info
  - Model UpgradePolicy has a new parameter auto_os_upgrade_policy
  - Added operation AvailabilitySetsOperations.list_by_subscription

**Breaking changes**

  - Model VirtualMachineScaleSetIdentity no longer has parameter
    identity_ids
  - Model VirtualMachineScaleSetOSDisk no longer has parameter
    disk_size_gb
  - Model VirtualMachineScaleSetVM no longer has parameter zones
  - Model VirtualMachineScaleSetUpdateOSDisk no longer has parameter
    disk_size_gb
  - Model VirtualMachineIdentity no longer has parameter identity_ids

New default API Version is now 2018-06-01

## 4.0.0rc2 (2018-04-17)

**Features**

  - All clients now support Azure profiles.
  - Add update operation to VirtualMachineExtension operations (all
    ApiVersions)
  - Add get_extensions operation to VirtualMachine operations (all
    ApiVersions)
  - Support eviction policy for virtual machines inside a low priority
    scale set (2017-12-01)
  - Add get_os_upgrade_history to VMSS operations (2017-12-01)

**Bugfixes**

  - Compatibility of the sdist with wheel 0.31.0
  - Fix some invalid models in Python 3 (introduced in 4.0.0rc1)

## 4.0.0rc1 (2018-03-21)

**General Breaking changes**

This version uses a next-generation code generator that *might*
introduce breaking changes.

  - Model signatures now use only keyword-argument syntax. All
    positional arguments must be re-written as keyword-arguments. To
    keep auto-completion in most cases, models are now generated for
    Python 2 and Python 3. Python 3 uses the "*" syntax for
    keyword-only arguments.
  - Enum types now use the "str" mixin (class AzureEnum(str, Enum)) to
    improve the behavior when unrecognized enum values are encountered.
    While this is not a breaking change, the distinctions are important,
    and are documented here:
    <https://docs.python.org/3/library/enum.html#others> At a glance:
      - "is" should not be used at all.
      - "format" will return the string value, where "%s" string
        formatting will return `NameOfEnum.stringvalue`. Format syntax
        should be prefered.
  - New Long Running Operation:
      - Return type changes from
        `msrestazure.azure_operation.AzureOperationPoller` to
        `msrest.polling.LROPoller`. External API is the same.
      - Return type is now **always** a `msrest.polling.LROPoller`,
        regardless of the optional parameters used.
      - The behavior has changed when using `raw=True`. Instead of
        returning the initial call result as `ClientRawResponse`,
        without polling, now this returns an LROPoller. After polling,
        the final resource will be returned as a `ClientRawResponse`.
      - New `polling` parameter. The default behavior is
        `Polling=True` which will poll using ARM algorithm. When
        `Polling=False`, the response of the initial call will be
        returned without polling.
      - `polling` parameter accepts instances of subclasses of
        `msrest.polling.PollingMethod`.
      - `add_done_callback` will no longer raise if called after
        polling is finished, but will instead execute the callback right
        away.

**Compute features**

  - Support zone resilient for image/snapshots (new ApiVersion
    2018-04-01)
  - Add "operations" operation group
  - Add availability_set.update
  - Add images.update
  - Add virtual_machine.update

## 3.1.0rc3 (2018-11-01)

**Features**

  - Add VirtualMachineScaleSetNetworkConfiguration ->
    enable_ip_forwarding
  - Add VirtualMachineScaleSetUpdateNetworkConfiguration ->
    enable_ip_forwarding
  - Add VirtualMachineScaleSetVMProfile -> priority
  - Add ApiVersion 2017-12-01 of virtual_machine_run_commands (new
    default)

## 3.1.0rc2 (2017-12-14)

**Features**

  - Add User Assigned Identity parameters to VM/VMSS creation

**Bugfixes**

  - Add RestrictionInfo to SKUs list (2017-09-01)
  - Restore virtual_machines.run_commands (broken in rc1)

## 3.1.0rc1 (2017-11-27)

**Disclaimer**

This version supports Azure Profile. Meaning, you can specify specific
API versions to support for each operation groups.

The default API versions of this package are now: - 2017-03-30 for
'disks', 'virtual_machine_run_commands' and 'snapshots' - 2017-09-01
for 'resource_skus' - 2017-12-01 for everything else

**Python features**

  - ComputeManagementClient has now a "profile" parameter, which is a
    dict from operation groups name to API version
  - Operation groups now have access to their own models. For instance,
    assuming you have variable called "client", you can access the
    models for this opeations groups (according to your loaded profiles)
    using `client.virtual_machines.models`
  - azure.mgmt.compute.models is deprecated. See
    <https://aka.ms/pysdkmodels> for details.

**Azure features**

  - 'resource_skus' has improved 'location_info' field

## 3.0.1 (2017-09-26)

**Bugfix**

  - Add missing virtual_machine_scale_set_rolling_upgrades
    operation group alias

## 3.0.0 (2017-09-26)

**Features**

  - Availability Zones
  - VMSS Rolling upgrade / patch / health status
  - VM instance view APIs

**Breaking changes**

  - "azure.mgmt.compute.compute" namespace is now simply
    "azure.mgmt.compute". If you were already using "azure.mgmt.compute"
    before, you code should still work exactly the same.
  - ContainerService has now be removed and exported in
    azure-mgmt-containerservice

## 2.1.0 (2017-07-19)

**Features in 2017-03-30**

  - Expose 'enableAcceleratedNetworking' for virtual machine and virtual
    machine SS. Windows GA, Linux in preview.
  - Expose 'forceUpdateTag' to ensure extension gets reinstalled even
    there are no configuration change.

## 2.0.0 (2017-06-29)

**Features**

Compute default Api Version is now 2017-03-30.

New operation groups:

  - resources_skus
  - virtual_machine_scale_set_extensions
  - virtual_machine_run_commands

New methods in VM:

  - perform_maintenance
  - run_command

Several improvements and modifications in Managed Disks.

**Breaking changes**

  - ContainerService: fixed typo in class name
    (ContainerServiceOchestratorTypes is now
    ContainerServiceOrchestratorTypes)
  - Compute: breaking changes in Managed Disk API:
      - Managed field removed from Create AV Set API
      - Account Type replaced with SKU in PUT and GET Managed Disk
        Create API
      - OwnerId replaced by ManagedBy in GET Managed Disk API

Note that you can get the behavior of v1.0.0 by forcing the Api Version
to "2016-04-30-preview" to update your package but not the code:

> ComputeManagementClient(credentials, subscription_id,
> api_version="2016-04-30-preview")

## 1.0.0 (2017-05-15)

  - Tag 1.0.0rc2 as stable (same content)

## 1.0.0rc2 (2017-05-12)

**Features**

  - Add Compute ApiVersion 2016-03-30 (AzureStack default)

## 1.0.0rc1 (2017-04-11)

**Breaking Changes**

  - Container service is now in it's own client ContainerServiceClient

**Features**

To help customers with sovereign clouds (not general Azure), this
version has official multi ApiVersion support for the following resource
type:

  - Compute: 2015-06-15 and 2016-04-30-preview

The following resource types support one ApiVersion:

  - ContainerService: 2017-01-31

## 0.33.0 (2017-02-03)

**Features**

This release adds Managed Disk to compute. This changes the default disk
creation behavior to use the new Managed Disk feature instead of
Storage.

## 0.32.1 (2016-11-14)

  - Add "Kubernetes" on Containers
  - Improve technical documentation

## 0.32.0 (2016-11-02)

**Breaking change**

New APIVersion for "container" 2016-09-30.

  - several parameters (e.g. "username") now dynamically check before
    REST calls validity against a regexp. Exception will be TypeError
    and not CloudError anymore.

## 0.31.0 (2016-11-01)

**Breaking change**

We renamed some "container" methods to follow Azure SDK conventions

  - "container" attribute on the client is now "containers"
  - "list" changed behavior, now listing containers in subscription and
    lost its parameter
  - "list_by_resource_group" new method with the old "list" behavior

## 0.30.0 (2016-10-17)

  - Initial preview release. Based on API version 2016-03-30.

## 0.20.0 (2015-08-31)

  - Initial preview release. Based on API version 2015-05-01-preview.
