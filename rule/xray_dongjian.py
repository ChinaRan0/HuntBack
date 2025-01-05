import requests
import json


def check(ip,port):
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
    url = f"https://{ip}:{port}/api/locales/resources.json?lng=zh-CN+zh&ns=oem+oemFiles+SkyeyeSetTypeEnum+TaskTypeEnum+CategoryEnum+SeverityEnum+CPEOperatorEnum+VulnKindEnum+PartEnum+CPETypeEnum+ImageRegistryTypeEnum+PlanTypeEnum+WeekdayEnum+ImageTaskTypeEnum+PermissionOptionEnum+TaskStatusEnum+TaskSeverityEnum+SortOrderEnum+XProcessSortingKeyEnum+PlanExecutionSettiongRuleEnum+ExecutionWindowTypeEnum+ExecutionCronTypeEnum+TaskSpeedEnum+TargetTypeEnum+SSHTypeEnum+LoginProtoEnum+TaskPriorityEnum+TaskRiskEnum+CheckListStateEnum+BaselineSetSortingKeyEnum+BaselineHostStatusEnum+BaselineChecklistSortingKeyEnum+BaselineHostTargetSortingKeyEnum+ItemListSortingKeyEnum+ResultStatusEnum+ProductTypeEnum+DeploymentTypeEnum+EngineStatusEnum+DataBackupFrequencyEnum+ServerBackupStatusEnum+ToolStatusEnum+NetInterfaceStateEnum+SpeedEnum+VulnIdTypeEnum+PluginRiskTypeEnum+TagTypeEnum+InstanceOrigionEnum+PluginTargetTypeEnum+AuditLogActionEnum+ResultTypeEnum+StrategyNameEnum+TemplateTypeEnum+StateEnum+AssetSeverityEnum+ProtocolEnum+ParameterPositionEnum+VulnStatusEnum+DefinitenessEnum+LocationCoordinateKindEnum+HostAliveStatusEnum+OriginEnum+XProcessStatusEnum+AggregatedVulnSortingKeyEnum+VulnSortingKeyEnum+ApiModEnum+SensitiveInfoTypeEnum+SensitiveLevelEnum+XProcessLogTypeEnum+TaskResultSortingKeyEnum+RetestStatusEnum+PriorityLevelEnum+AliveStatusTimeChoiceEnum+VulnStatusRecordCreatorEnum+LoginLockModeEnum+LoginModeEnum+PasswordComplexityEnum+VulnUnFixedAlertSendToEnum+CustomerEnvironEnum+ActionTypeEnum+ActionStatusEnum+ExecutionStatusEnum+UpgradeModuleTypeEnum+ReportTemplateEnum+LanguageEnum+AssetTypeEnum+BaselineReportTemplateOptionsEnum+ScanReportTemplateOptionsEnum+VulnReportTemplateOptionsEnum+AssetReportTemplateOptionsEnum+TaskCompareReportTemplateOptionsEnum+AssetCompareReportTemplateOptionsEnum+ReportPolymerEnum+ReportOutputFormEnum+ReportStatusEnum+ReportFileTypeEnum+UserStateEnum+VulnStatusActionEnum+VulnDistributeStatisticSortingKeyEnum+VulnerabilityPositionEnum+SSHAuthTypeEnum+DebugFileGenerateProcessEnum+ScannerDictTypeEnum+WeakPasswordServiceEnum+DictUsageEnum+GroupTypeEnum+StrategyTargetTypeEnum+NormalTaskPriorityEnum+StorageTypeEnum+AuditLogLimitEnum+LogStorageTimeEnum+SyslogRFCEnum+AccessIpRestrictionsEnum+FTPWorkModeEnum+SystemStatusEnum+ContainerNameEnum+ContainerStatusEnum+SmtpEncryptionMethodEnum+MatchOperatorEnum+EditionEnum+ModulePermissionEnum+ExtensiveModulePermissionEnum+AssetCreationInputTypeEnum+AssetGroupModeEnum+LocationLevelEnum+AssetSortingKeyEnum+AliveStatusSetChoiceEnum+M2MUpdateEnum+ToolEnum+IpConfigTypeEnum+RouteTypeEnum+PamPlatformEnum+ExportFileModuleEnum+LogoutChannelEnum+base+ErrorNameEnum+TimeUnitEnum+AssetAddingMethodEnum+AssetLocationDistributionAmountEnum+AssetReportTargetTypeEnum+AuthTypeEnum+BooleanEnum+CrawlerTypeEnum+CronTypeEnum+DetectionLevelEnum+ExecutionTimeRuleEnum+IgnoreTypeEnum+RolePermissionSelectTitleEnum+SimpleBackupStatusEnum+StatisticAssetSeverityEnum+SwaggerTargetTypeEnum+SystemLanguageEnum+SystemSettingTabKeysEnum+TimeTypeEnum+allReportTemplate+asset+auxiliaryTool+fingerprint+login+menu+openApi+poc+profile+remoteAssistant+reportTemplate+sas+scalar+scanningConfig+service+setting+statistic+sysinfo+task+user+vulnerability+website+xnode"
    try:
        res = requests.get(url=url, headers=headers, verify=False,timeout=3)
    # print(res.text)
        if "X-Ray" in res.text:
            print(f"https://{ip}:{port}----长亭洞鉴（X-Ray）安全评估系统")
    except:
        pass