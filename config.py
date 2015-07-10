config = {

"PUBLISHSETTINGS_FILE" : "CollaberaInteropTest-5-28-2015-credentials.publishsettings",

#************** ACCOUNT VARIABLES *****************

"LOG_FILE" : "LOG_FILE.txt",
"LOG_FILERR" : "LOG_FILERR.txt",
"FILE_PATH" : "FILE_PATH.json",
"CERT_FILE" : "CERT_FILE.pem",
"CUSTOM_DATA_FILE" : "CustomDataFile",

#************** ACCOUNT VARIABLES *****************

"SUBSCRIPTION_ID" : "bfb5e0bf-124b-4d0c-9352-7c0a9f4d9948",
"CONFIG_KEY" : "Key",
"CONFIG_VALUE" : "Value",

#************** StaticIP VARIABLES *****************
"STATICIP_VM_NAME" : "XplatVMStatic",
"DOCKER_STATIC_VM_NAME" : "XplatDockVMStat",
"STATIC_IP_TO_CREATE" : "10.0.0.7",
"STATIC_IP_TO_SET" : "10.0.0.8",
#************** VM VARIABLES *****************
"VM_NAME" : "TempXplatTestVM1",
#"VM_NAME" : "OffshoreTest",
"VM_WIN_NAME" : "TestXplatWin",
"VM_VNET_NAME" : "XplatTestVNet",
"VM_VNET_LABEL" : "Xplat_vnet_img_vm",
"VM_SIZE_NAME" : "XplatTestVMSize",
"VM_COMM_NAME" : "XplatTestComm",
"VM_SSH_NAME" : "XplatTestSsh",
"VM_DOCKER_NAME" : "XplatDockerVM",
"VM_RIP_NAME" : "XplatRIPVM",
"VM_DOCKER_PORT" : "4113",
"VM_CUSTOMDATA_NAME" : "XplatCustomdata",
"LOGINUSER" : "v-sreban@microsoft.com",
"LOGINPASSWORD" : "T5Sv~8?n",

"IMAGE_NAME" :"TEstImage",
"WIN_IMAGE_NAME" :"VMImage", #diskname is obtained from vm image list and choose the one with windows
"VM_VNET_IMAGE_NAME" :"XplatTestImage",
"VM_COMM_IMAGE_NAME" :"vmdepot-36259-1-1", #browse http://vmdepot.msopentech.com/ select a vm anc click on deployment button
"VM_DOCKER_IMG_NAME" : "TEstImage",   # Existing Linux Image

"USER_NAME" :"XplatTestUser",
"PASSWORD" :"Pa$$word@123" ,
"LOCATION" : '"West US"',

#************** VM IMAGE VARIABLES *****************
"AFFINITY_GRP_NAME":"NewAffinityGroup02",
"AFFINITY_GRP_LABEL":"XplatTestGrp2",
"AFFINITY_GRP_DESC":'"Test Affinity Group2"',

#************** VM Extension VARIABLES *****************
"EXTN_PUB_NAME":"Microsoft.Compute",
"EXTN_NAME":"BGInfo",
"EXTN_VERSION":"1.1 ",
"EXTN_FILE":"foo.json",
#************** VM NETWORK VARIABLES *****************
"NETWORK_NAME":"clintwrkpyvnet",

#************** VM IMAGE VARIABLES *****************
"VM_IMAGE_NAME" : "XplatTestImage",
"VM_IMAGE_LABEL" : "XplatTestImageLabel",
"VM_IMAGE_DESC" : '"Test Offshore Image"',
"VM_DISK_SOURCE_PATH" :"https://acsforsdk2.blob.core.windows.net/disks/OffshoreXplatTest", #mediauri obtained from vm disk show diskname(diskname is obtained from vm disk list and choose the one with linux as os)
"IMAGE_BLOB_URL" : "http://acsforsdk2.blob.core.windows.net/vm-images/ToDelete151",		#http://StoragecontainerUrl/vm-images/OffshoreXplatTestImage002"
"TARGET_IMG_NAME" : "XplatTestTargetImg",

#************** VM DISK IMAGE VARIABLES *****************
"VM_DISK_IMAGE_NAME" :"ToDelete151",
"VM_DISK_NEW_IMAGE_NAME" :"XplatTestDiskNewImage",
"VM_DISK_LABEL" : "XplatTestDisklb151",
"VM_DISK_NEW_LABEL" : "XplatTestDiskNewlbl",
"VM_DISK_DESC" : '"Test Offshore Disk"',
"DISK_IMAGE_BLOB_URL": "https://acsforsdk2.blob.core.windows.net/disks/ToDelete151", 			#http://StoragecontainerUrl/disks/OffshoreXplatTestDisk"
"VM_DISK_ATTACH_BLOB_URL": "https://acsforsdk2.blob.core.windows.net/disks/VM_DISK_ATTACH_BLOB_URL", 	#http://StoragecontainerUrl/disks/disknewupload.vhd"

#************** PIP COMMANDS ****************************
"VM_WIN_PIP" : "VMeToDelPIP",
"PUBLICIPNAME" : "TestIP2",
"PUBLICIPSET" : "VMPUBLICIPSET",


#************** ACL COMMANDS ****************************
"VM_WIN_ACL" : "VMeToDelACL",
"ENDPOINT" : "tcp-21-23",
"REMOTESUBNET" : "23.99.18.228/31",
"ORDER" : "3",
"ACL_ACTION" : "permit",

#************** VM DISK UPLOAD VARIABLES *****************
"DISK_UPLOAD_BLOB_URL": "DISK_UPLOAD_BLOB_URL",			#http://StoragecontainerUrl/disks/OffshoreTestDiskImage002.vhd",
"DISK_UPLOAD_SOURCE_PATH" : "DISK_UPLOAD_SOURCE_PATH", 	#http://StoragecontainerUrl/vm-images/OffshoreTestImage002.vhd",
"STORAGE_ACCOUNT_KEY": "STORAGE_ACCOUNT_KEY", 			#YW55IGNhcm5hbCBwbGVhc3VyZQ==

#************** MULTIPLE ENDPOINT VALUES **************************
"ONLYPP_PUBLICPORT":"3333",

"PPANDLP_PUBLICPORT":"4444",
"PPANDLP_LOCALPORT":"4454",

"PP_LPANDLBSET_PUBLICPORT":"5555",
"PP_LPANDLBSET_LOCALPORT":"5565",
"PP_LPANDLBSET_PROTOCOL":"tcp",
"PP_LPANDLBSET_ENABLEDIRECTSERVERRETURN":"false",
"PP_LPANDLBSET_LOADBALANCERSETNAME":"LbSet1",

"PP_LP_LBSETANDPROB_PUBLICPORT":"6666",
"PP_LP_LBSETANDPROB_LOCALPORT":"6676",
"PP_LP_LBSETANDPROB_PROTOCOL":"tcp",
"PP_LP_LBSETANDPROB_ENABLEDIRECTSERVERRETURN":"false",
"PP_LP_LBSETANDPROB_LOADBALANCERSETNAME":"LbSet2",
"PP_LP_LBSETANDPROB_PROBPROTOCOL":"http",
"PP_LP_LBSETANDPROB_PROBPORT":"7777",
"PP_LP_LBSETANDPROB_PROBPATH":"/prob/listner1",

#RESERVED-IP
"RIPNAME" : "XplatTestRIP5",

#LOADBALANCER
"SUBNET" : "Subnet-1" ,
"INTERNAL_LB_NAME" : "internalLBName" ,
"SUBNETIP" : "subnetip" ,
"INTERNAL_LB_NAME_UPDATE" : "internalLBName" ,

#************** NETWORK VARIABLES *****************

"GRPNAME" : "ArmResGrpPython",
"NETWORK_VNET_NAME" : "NetworkVnet",
"NETWORK_SUBNET_NAME" : "clipysubnet",   # NetworkVnetSubnet
"ADDRESS_PREFIXES" : "10.32.0.0/11",
"ADDRESS_PREFIXES_SET" : "10.64.0.0/10",
"TAGS" : "tag1=value1",
"NETWORK_NSG_NAME" : "NetworkNsg",
"TAGS_SET" : "tag1=value1;tag2=value2",
"NETWORK_NSG_RULE_NAME" : "NetworkNsgRule",
"DESCRIPTION" : "NsgRule",
"DESCRIPTION_SET" : "NsgRuleSet",
"PROTOCOL" : "tcp",
"PROTOCOL_SET" : "udp",
"SOURCE_ADDRESS_PREFIX" : "10.0.0.0/24",
"SOURCE_ADDRESS_PREFIX_SET" : "10.0.0.0/8",
"SOURCE_PORT_RANGE" : "200",
"SOURCE_PORT_RANGE_SET" : "250",
"DESTINATION_ADDRESS_PREFIX" : "10.0.0.0/12",
"DESTINATION_ADDRESS_PREFIX_SET" : "10.0.0.0/16",
"DESTINATION_PORT_RANGE" : "250",
"DESTINATION_PORT_RANGE_SET" : "300",
"ACCESS" : "Allow",
"ACCESS_SET" : "Deny",
"PRIORITY" : "250",
"PRIORITY_SET" : "300",
"DIRECTION" : "Inbound",
"DIRECTION_SET" : "Outbound",
"NETWORK_PUBLICIP" : "NetworkPublicIp",
"DOMAIN_NAME" : "dnsname",
"DOMAIN_NAME_SET" : "dnsnameset",
"ALLOCATION_METHOD" : "Static",
"ALLOCATION_METHOD_SET" : "Dynamic",
"IDLE_TIMEOUT" : "4",
"IDLE_TIMEOUT_SET" : "5",
"NETWORK_NIC_NAME" : "NetworkNic",
"PRIVATEIP_ADDRESS" : "10.31.255.250",
"ACTION" : "Allow",
"ACTION_SET" : "Deny",
"TYPE" : "Inbound",
"TYPE_SET" : "Outbound",
"NSG_LABEL" : "Nsg Testing",
"ROUTE_LABEL" : "Route Testing",
"ROUTE_ADDRESS_PREFIXES" : "0.0.0.0/0",
"NEXT_HOP_TYPE" : "VPNGateway",
"NETWORK_ROUTE_TABLE" : "CliRouteTable",
"NETWORK_ROUTE" : "CliRoute",
"NETWORK_TRAFFICMANAGER_PROFILE_NAME" : "TestTMProfile",
"DOMAIN_NAME" : "TestDomainName.trafficmanager.net",
"lOADBALANCING_METHOD" : "performance",
"MONITOR_PORT" : "2",
"MONITOR_PROTOCOL" : "http",
"MONITOR_RELATIVE_PATH" : "/health.aspx",
"TTL" : "40",
"lOADBALANCING_METHOD_SET" : "failover",
"MONITOR_PORT_SET" : "4",
"MONITOR_PROTOCOL_SET" : "https",
"MONITOR_RELATIVE_PATH_SET" : "/healthy.aspx",
"TTL_SET" : "45",
"NETWORK_APPLICATION_GATEWAY_NAME" : "TestAppGateway1",
"INSTANCE_COUNT" : "2",
"GATEWAY_SIZE" : "Small",
"APPGATEWAY_DESCRIPTION" : "Testing App Gateway",
"INSTANCE_COUNT_SET" : "4",
"GATEWAY_SIZE_SET" : "Medium",
"APPGATEWAY_DESCRIPTION_SET" : "Testing Application Gateway",
"APPGATE_ADDRESSPOOL_NAME" : "AppGateAddPool1",
"ADDRESSPOOL_IP" : "10.0.0.10",
"APPGATE_HTTPSETTINGS_NAME" : " AppGateHttpSetting1",
"HTTPSETTINGS_PROTOCOL" : "Http",
"HTTPSETTINGS_PORT" : "10",
"HTTPSETTINGS_CBAFFINITY" : "Enabled",
"APPGATE_FRONTENDIP_NAME" : "fip1",
"FRONTENDIP_TYPE" : "Private",
"FRONTENDIP_STATICIP" : "10.0.1.10",
"APPGATE_FRONTENDPORT_NAME" : "AppGateFrontendPort1",
"FRNTENDPORT_PORT" : "20",
"APPGATE_HTTPLISTENER_NAME" : "AppGateHttplistName1",
"HTTPLISTENER_PROTOCOL" : "Http",
"APPGATE_LBRULE_NAME" : "AppGateLbRule1",
"LBRULE_TYPE" : "Basic",
"APPGATE_EXPORT_FILE" : "AppGateExport.txt", #E:\4486\25-June-2015\azure-xplat-cli-dev-asm-network\
# Vpn-Gateway & Local-Network Variables
"NETWORK_VPN_VNET_NAME" : "CliGtWyTestVnet",
"VPN_VNET_ADDRESS" : "10.1.0.0",
"VPN_VNETCIDR" : "16",
"VPN_VNET_SUBNET_START_IP" : "10.1.0.0",
"VPN_VNET_SUBNET_CIDR" : "19",
"VPN_LOCATION" : '"West US"',
"NETWORK_VPN_SUBNET_NAME" : "GatewaySubnet",
"VPN_SUBNET_ADDRESS" : "10.1.32.0/29",
"NETWORK_LOCALNETWORK_NAME" : "CliGtWyTestLocNetwork",
"VPN_GATEWAY_ADDRESS" : "200.200.200.200",
"LOCAL_NETWORK_ADDRESS" : "10.2.0.0/16",
"LOCAL_NETWORK_ADDRESS_SET" : "10.0.0.0/19",
"VPN_GATEWAY_ADDRESS_SET" : "20.20.20.20",
"VPN_GAETWAY_TYPE" :"DynamicRouting",
"VPN_SKU" : "Default",
"VPN_KEYVALUE" : "abcd",
"VPN_KEYLENGHT" : "123",
"VPN_DURATION" : "300",
"VPN_STORAGE" : "acsforsdk2",
"VPN_STORAGE_KEY" : "dB/thYTVa0biqAzEciJBjSqUBJG/6+ayHe2+yQGkBTijnU3eVookQReEVmdsqCSWevoLwXT+UE9Aid9wLO3dBQ==",
"VPN_CONTAINER" : "gatewycont",

#************** FLAG VALUES **************************

"GLOBAL_FLAG" : "1",
"AD_Login" : "0",

# NPM FLAGS

"NPM_CLEAR_FLAG" : "0" ,
"NPM_INSTALL_FLAG" : "0" ,

# ACCOUNT FLAGS 
"AZURE_HELP_FLAG" : "0" ,
"ACCOUNT_DWNLD_FLAG" : "0" ,
"ACCOUNT_IMPRT_FLAG" : "0" ,
"ACCOUNT_LIST_FLAG" : "0" ,
"ACCOUNT_SET_FLAG" : "0" ,
"ACCOUNT_AFF_GRP_FLAG" : "0" ,
"ACCOUNT_AFF_GRP_CREATE_FLAG" : "0" ,
"ACCOUNT_AFF_GRP_SHOW_FLAG" : "0" ,
"ACCOUNT_STORAGE_LIST_FLAG" : "0" ,
"ACCOUNT_CONFIG_LIST_FLAG" : "0" ,
"ACCOUNT_CONFIG_SET_FLAG" : "0" ,
"AZURE_SERV_LIST_FLAG" : "0" ,
"AZURE_LOC_LIST_FLAG" : "0" ,
"AZURE_SERVICE_DEL_FLAG" : "0" ,
"ACCOUNT_CLEAR_FLAG" : "0" ,
"AZURE_LOGIN_FLAG" : "0",

#STATICIP FLAGS
"VM_STATICIP_CREATE_FLAG":"0",
# VM FLAGS

"VM_CREATE_FLAG" : "0" ,
"VM_VNET_CREATE_FLAG" : "0" ,
"VM_SIZE_CREATE_FLAG" : "0" ,
"VM_CUSTOMDATA_CREATE_FLAG" : "0" ,
"VM_COMM_IMG_CREATE_FLAG" : "0" ,
"VM_SSH_FLAG" : "0" ,
"VM_EXPORT_FLAG" : "0" ,
"VM_CAPTURE_FLAG" : "0" ,
"VM_CREATE_FROM_FLAG" : "0" ,
"VM_LIST_FLAG" : "0" ,
"VM__SHOW_FLAG" : "0" ,
"VM_SHUTDWN_FLAG" : "0" ,
"VM_START_FLAG" : "0" ,
"VM_RESTART_FLAG" : "0" ,
"VM_ENDPNT_CREATE_FLAG" : "0" ,
"VM_ENDPNT_CREATE_MUL_FLAG" : "0" ,
"VM_ENDPNT_SHOW_FLAG" : "0" ,
"VM_ENDPNT_LIST_FLAG" : "0" ,
"VM_ENDPNT_UPD_FLAG" : "0" ,
"VM_ENDPNT_DEL_FLAG" : "0" ,
"VM_DEL_FLAG" : "0" ,
"VM_AFFINITY_DEL_FLAG" : "0" ,
"VM_VNET_DEL_FLAG" : "0" ,
"VM_SIZE_DEL_FLAG" : "0" ,
"VM_CUSTOMDATA_DEL_FLAG" : "0" ,
"VM_COMM_DEL_FLAG" : "0" ,
"VM_SSH_DEL_FLAG" : "0" ,
"VM_RIP_CREATE_FLAG" : "0" ,
"VM_RIP_DEL_FLAG" : "0" ,

#PIP FLAGS
"PIP_VM_CREATE_FLAG" : "0",
"PIP_VM_LIST_FLAG" : "0",
"PIP_VM_REMOVE_FLAG" : "0",
"PIP_VM_SET_FLAG" : "0",
"PIP_VM_DELETE_FLAG" : "0",

#ACL FLAGS
"ACL_VM_CREATE_FLAG" : "0",
"ACL_RULE_CREATE_FLAG" : "0",
"ACL_RULE_LIST_FLAG" : "0",
"ACL_RULE_DELETE_FLAG" : "0",

# IMAGE FLAGS

"IMAGE_CREATE_FLAG" : "0" ,
"IMAGE_LIST_FLAG" : "0" ,
"IMAGE_SHOW_FLAG" : "0" ,
"IMAGE_DEL_FLAG" : "0" ,

# DISK FLAGS

"DISK_LIST_FLAG" : "0" ,
"DISK_LIST_VM_NAME_FLAG" : "0",
"DISK_CREATE_FLAG" : "0" ,
"DISK_ATTCH_FLAG" : "0" ,
"DISK_ATTCH_NEW_FLAG" : "0" ,
"DISK_DETACH_FLAG" : "0" ,
"DISK_SHOW_FLAG" : "0" ,
"DISK_UPLOAD_FLAG" : "0" ,
"NETWORK_CREATE_FLAG" : "0" ,
"NETWORK_DELETE_FLAG" : "0" ,
"DISK_DEL_FLAG" : "0" ,

#DOCKER FLAGS
"VM_DOCKER_CREATE_FLAG" : "0" ,
"VM_DOCKER_DELETE_FLAG" : "0",

#EXTENSION_FLAGS
"VM_EXTENSION_LIST_FLAG" : "0" ,
"VM_EXTENSION_GET_FLAG" : "0" ,
"VM_EXTENSION_SET_FLAG" : "0" ,

#RESERVED-IP
"RESERVED_IP_SHOW_FLAG" : "0" ,
"RESERVED_IP_CREATE_FLAG" : "0" ,
"RESERVED_IP_LIST_FLAG" : "0" ,
"RESERVED_IP_DELETE_FLAG" : "0" ,

#LOADBALANCER
"LOADBALANCER_CREATE_FLAG" : "0" ,
"LOADBALANCER_ADD_FLAG" : "0" ,
"LOADBALANCER_LIST_FLAG" : "0" ,
"LOADBALANCER_SET_FLAG" : "0" ,
"LOADBALANCER_DELETE_FLAG" : "0" ,
"VM_LOADBALANCER_DEL_FLAG" : "0",


# NETWORK FLAGS 
"NETWORKVNET_CREATE_FLAG" : "0",
"NETWORKVNET_SET_FLAG" : "0",
"NETWORKVNET_LIST_FLAG" : "0",
"NETWORKVNET_SHOW_FLAG" : "0",
"NETWORKNSG_CREATE_FLAG" : "0",
"NETWORKNSG_LIST_FLAG" : "0",
"NETWORKNSG_SHOW_FLAG" : "0",
"NETWORKVNETSUBNET_CREATE_FLAG" : "0",
"NETWORKVNETSUBNET_SET_FLAG" : "0",
"NETWORKVNETSUBNET_LIST_FLAG" : "0",
"NETWORKVNETSUBNET_SHOW_FLAG" : "0",
"NETWORKNSGRULE_CREATE_FLAG" : "0",
"NETWORKNSGRULE_SET_FLAG" : "0",
"NETWORKNSGRULE_LIST_FLAG" : "0",
"NETWORKNSGRULE_SHOW_FLAG" : "0",
"NETWORKNSGRULE_DELETE_FLAG" : "0",
"NETWORKPUBLICIP_CREATE_FLAG" : "0",
"NETWORKPUBLICIP_SET_FLAG" : "0",
"NETWORKPUBLICIP_LIST_FLAG" : "0",
"NETWORKPUBLICIP_SHOW_FLAG" : "0",
"NETWORKNIC_CREATE_FLAG" : "0",
"NETWORKNIC_SET_FLAG" : "0",
"NETWORKNIC_LIST_FLAG" : "0",
"NETWORKNIC_SHOW_FLAG" : "0",
"NETWORKLB_CREATE_FLAG" : "0",
"NETWORKLB_LIST_FLAG" : "0",
"NETWORKLB_SHOW_FLAG" : "0",
"NETWORKLB_FRONTENDIP_CREATE_FLAG" : "0",
"NETWORKLB_FRONTENDIP_SET_FLAG" : "0",
"NETWORKLB_FRONTENDIP_LIST_FLAG" : "0",
"NETWORKLB_PROBE_CREATE_FLAG" : "0",
"NETWORKLB_PROBE_SET_FLAG" : "0",
"NETWORKLB_PROBE_LIST_FLAG" : "0",
"NETWORKLB_INBOUNDNATRULE_CREATE_FLAG" : "0",
"NETWORKLB_INBOUNDNATRULE_SET_FLAG" : "0",
"NETWORKLB_INBOUNDNATRULE_LIST_FLAG" : "0",
"NETWORKLB_INBOUNDNATRULE_DELETE_FLAG" : "0",
"NETWORKLB_ADDRESSPOOL_CREATE_FLAG" : "0",
"NETWORKLB_ADDRESSPOOL_ADD_FLAG" : "0",
"NETWORKLB_ADDRESSPOOL_REMOVE_FLAG" : "0",
"NETWORKLB_ADDRESSPOOL_LIST_FLAG" : "0",
"NETWORKLB_RULE_CREATE_FLAG" : "0",
"NETWORKLB_RULE_SET_FLAG" : "0",
"NETWORKLB_RULE_LIST_FLAG" : "0",
"NETWORKLB_RULE_DELETE_FLAG" : "0",
"NETWORKLB_ADDRESSPOOL_DELETE_FLAG" : "0",
"NETWORKLB_FRONTENDIP_DELETE_FLAG" : "0",
"NETWORKLB_PROBE_DELETE_FLAG" : "0",
"NETWORKLB_DELETE_FLAG" : "0",
"NETWORKVNETSUBNET_DELETE_FLAG" : "0",
"NETWORKVNET_DELETE_FLAG" : "0",
"NETWORKNSG_DELETE_FLAG" : "0",
"NETWORKNIC_DELETE_FLAG" : "0",
"NETWORKPUBLICIP_DELETE_FLAG" : "0",
"RESOURCEGROUP_DELETE_FLAG" : "0",
"NETWORKNSGSUBNET_ADD_FLAG" : "0",
"NETWORKNSGSUBNET_REMOVE_FLAG" : "0",
"NETWORKROUTETABLE_CREATE_FLAG" : "0",
"NETWORKROUTETABLE_LIST_FLAG" : "0",
"NETWORKROUTETABLE_SHOW_FLAG" : "0",
"NETWORKROUTETABLE_ROUTE_SET_FLAG" : "0",
"NETWORKROUTETABLE_ROUTE_DELETE_FLAG" : "0",
"NETWORKSUBNET_ROUTETABLE_ADD_FLAG" : "0",
"NETWORKSUBNET_ROUTETABLE_SHOW_FLAG" : "0",
"NETWORKSUBNET_ROUTETABLE_DELETE_FLAG" : "0",
"NETWORKROUTETABLE_DELETE_FLAG" : "0",
"TRAFFICMANAGER_PROFILE_CREATE_FLAG" : "0",
"TRAFFICMANAGER_PROFILE_SET_FLAG" : "0",
"TRAFFICMANAGER_PROFILE_LIST_FLAG" : "0",
"TRAFFICMANAGER_PROFILE_SHOW_FLAG" : "0",
"TRAFFICMANAGER_PROFILE_ENABLE_FLAG" : "0",
"TRAFFICMANAGER_PROFILE_DISABLE_FLAG" : "0",
"TRAFFICMANAGER_PROFILE_DELETE_FLAG" : "0",
"APPLICATIONGATEWAY_CREATE_FLAG" : "1",
"APPLICATIONGATEWAY_SET_FLAG" : "",
"APPLICATIONGATEWAY_LIST_FLAG" : "0",
"APPLICATIONGATEWAY_SHOW_FLAG" : "0",
"APPLICATIONGATEWAY_START_FLAG" : "0",
"APPLICATIONGATEWAY_STOP_FLAG" : "0",
"APPLICATIONGATEWAY_DELETE_FLAG" : "0",
"APPGATE_ADDPOOL_ADD_FLAG" : "0",
"APPGATE_HTTPSETTINGS_ADD_FLAG" : "0",
"APPGATE_FRONTENDIP_ADD_FLAG" : "0",
"APPGATE_FRONTENDPORT_ADD_FLAG" : "0",
"APPGATE_HTTPLISTENER_ADD_FLAG" : "0",
"APPGATE_LBRULE_ADD_FLAG" : "0",
"APPGATE_CONFIG_EXPORT_FLAG" : "0",
"APPGATE_CONFIG_SHOW_FLAG" : "0",
"APPGATE_CONFIG_IMPORT_FLAG" : "0",
"APPGATE_LBRULE_REMOVE_FLAG" : "0",
"APPGATE_ADDPOOL_REMOVE_FLAG" : "0",
"APPGATE_HTTPLISTENER_REMOVE_FLAG" : "0",
"APPGATE_HTTPSETTINGS_REMOVE_FLAG" : "0",
"APPGATE_FRONTEND_REMOVE_FLAG" : "0",
"APPGATE_FRONTENDPORT_REMOVE_FLAG" : "0",
"VNET_FORGATEWAY_CREATE_FLAG" : "0",
"SUBNET_FORGATEWAY_CREATE_FLAG" : "0",
"LOCAL_NETWORK_CREATE_FLAG" : "0",
"LOCAL_NETWORK_SHOW_FLAG" : "0",
"LOCAL_NETWORK_LIST_FLAG" : "0",
"VNET_LOCAL_NETWORK_ADD_FLAG" : "0",
"VPN_GATEWAY_CREATE_FLAG" : "0",
"VPN_GATEWAY_SHOW_FLAG" : "0",
"VPN_GATEWAY_SHAREDKEY_SET_FLAG" : "0",
"VPN_GATEWAY_SHAREDKEY_RESET_FLAG" : "0",
"VPN_GATEWAY_CONNECTION_LIST_FLAG" : "0",
"VPN_GATEWAY_DEVICE_LIST_FLAG" : "0",
"VPN_GATEWAY_DIAGNOSTIC_START_FLAG" : "0",
"VPN_GATEWAY_DIAGNOSTIC_STOP_FLAG" : "0",
"VPN_GATEWAY_DIAGNOSTIC_GET_FLAG" : "0",
"VPN_GATEWAY_DELETE_FLAG" : "0",
"LOCAL_NETWORK_REMOVE_FLAG" : "0",
"VNET_FORGATEWAY_DELETE_FLAG" : "0",
"LOCAL_NETWORK_SET_FLAG" : "0",
"LOCAL_NETWORK_DELETE_FLAG" : "0",

}