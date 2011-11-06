# PySNMP SMI module. Autogenerated from smidump -f python SNMP-TARGET-MIB
# by libsmi2pysnmp-0.1.1 at Sun Nov  6 01:33:45 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( SnmpAdminString, SnmpMessageProcessingModel, SnmpSecurityLevel, SnmpSecurityModel, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString", "SnmpMessageProcessingModel", "SnmpSecurityLevel", "SnmpSecurityModel")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "snmpModules")
( RowStatus, StorageType, TAddress, TDomain, TextualConvention, TestAndIncr, TimeInterval, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TAddress", "TDomain", "TextualConvention", "TestAndIncr", "TimeInterval")

# Types

class SnmpTagList(TextualConvention, OctetString):
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,255)
    
class SnmpTagValue(TextualConvention, OctetString):
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,255)
    

# Objects

snmpTargetMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 12)).setRevisions(("2002-10-14 00:00","1998-08-04 00:00","1997-07-14 00:00",))
if mibBuilder.loadTexts: snmpTargetMIB.setOrganization("IETF SNMPv3 Working Group")
if mibBuilder.loadTexts: snmpTargetMIB.setContactInfo("WG-email:   snmpv3@lists.tislabs.com\nSubscribe:  majordomo@lists.tislabs.com\n            In message body:  subscribe snmpv3\n\nCo-Chair:   Russ Mundy\n            Network Associates Laboratories\nPostal:     15204 Omega Drive, Suite 300\n            Rockville, MD 20850-4601\n            USA\nEMail:      mundy@tislabs.com\nPhone:      +1 301-947-7107\n\nCo-Chair:   David Harrington\n            Enterasys Networks\nPostal:     35 Industrial Way\n            P. O. Box 5004\n            Rochester, New Hampshire 03866-5005\n            USA\nEMail:      dbh@enterasys.com\nPhone:      +1 603-337-2614\n\nCo-editor:  David B. Levi\n            Nortel Networks\nPostal:     3505 Kesterwood Drive\n            Knoxville, Tennessee 37918\nEMail:      dlevi@nortelnetworks.com\nPhone:      +1 865 686 0432\n\nCo-editor:  Paul Meyer\n            Secure Computing Corporation\nPostal:     2675 Long Lake Road\n\n\n\n            Roseville, Minnesota 55113\nEMail:      paul_meyer@securecomputing.com\nPhone:      +1 651 628 1592\n\nCo-editor:  Bob Stewart\n            Retired")
if mibBuilder.loadTexts: snmpTargetMIB.setDescription("This MIB module defines MIB objects which provide\nmechanisms to remotely configure the parameters used\nby an SNMP entity for the generation of SNMP messages.\n\nCopyright (C) The Internet Society (2002). This\nversion of this MIB module is part of RFC 3413;\nsee the RFC itself for full legal notices.")
snmpTargetObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 12, 1))
snmpTargetSpinLock = MibScalar((1, 3, 6, 1, 6, 3, 12, 1, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTargetSpinLock.setDescription("This object is used to facilitate modification of table\nentries in the SNMP-TARGET-MIB module by multiple\nmanagers.  In particular, it is useful when modifying\nthe value of the snmpTargetAddrTagList object.\n\nThe procedure for modifying the snmpTargetAddrTagList\nobject is as follows:\n\n\n\n    1.  Retrieve the value of snmpTargetSpinLock and\n        of snmpTargetAddrTagList.\n\n    2.  Generate a new value for snmpTargetAddrTagList.\n\n    3.  Set the value of snmpTargetSpinLock to the\n        retrieved value, and the value of\n        snmpTargetAddrTagList to the new value.  If\n        the set fails for the snmpTargetSpinLock\n        object, go back to step 1.")
snmpTargetAddrTable = MibTable((1, 3, 6, 1, 6, 3, 12, 1, 2))
if mibBuilder.loadTexts: snmpTargetAddrTable.setDescription("A table of transport addresses to be used in the generation\nof SNMP messages.")
snmpTargetAddrEntry = MibTableRow((1, 3, 6, 1, 6, 3, 12, 1, 2, 1)).setIndexNames((1, "SNMP-TARGET-MIB", "snmpTargetAddrName"))
if mibBuilder.loadTexts: snmpTargetAddrEntry.setDescription("A transport address to be used in the generation\nof SNMP operations.\n\nEntries in the snmpTargetAddrTable are created and\ndeleted using the snmpTargetAddrRowStatus object.")
snmpTargetAddrName = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: snmpTargetAddrName.setDescription("The locally arbitrary, but unique identifier associated\nwith this snmpTargetAddrEntry.")
snmpTargetAddrTDomain = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 2), TDomain()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpTargetAddrTDomain.setDescription("This object indicates the transport type of the address\ncontained in the snmpTargetAddrTAddress object.")
snmpTargetAddrTAddress = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 3), TAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpTargetAddrTAddress.setDescription("This object contains a transport address.  The format of\nthis address depends on the value of the\nsnmpTargetAddrTDomain object.")
snmpTargetAddrTimeout = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 4), TimeInterval().clone('1500')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpTargetAddrTimeout.setDescription("This object should reflect the expected maximum round\ntrip time for communicating with the transport address\ndefined by this row.  When a message is sent to this\naddress, and a response (if one is expected) is not\nreceived within this time period, an implementation\nmay assume that the response will not be delivered.\n\nNote that the time interval that an application waits\nfor a response may actually be derived from the value\nof this object.  The method for deriving the actual time\ninterval is implementation dependent.  One such method\nis to derive the expected round trip time based on a\nparticular retransmission algorithm and on the number\nof timeouts which have occurred.  The type of message may\nalso be considered when deriving expected round trip\ntimes for retransmissions.  For example, if a message is\nbeing sent with a securityLevel that indicates both\n\n\n\nauthentication and privacy, the derived value may be\nincreased to compensate for extra processing time spent\nduring authentication and encryption processing.")
snmpTargetAddrRetryCount = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpTargetAddrRetryCount.setDescription("This object specifies a default number of retries to be\nattempted when a response is not received for a generated\nmessage.  An application may provide its own retry count,\nin which case the value of this object is ignored.")
snmpTargetAddrTagList = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 6), SnmpTagList().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpTargetAddrTagList.setDescription("This object contains a list of tag values which are\nused to select target addresses for a particular\noperation.")
snmpTargetAddrParams = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 7), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpTargetAddrParams.setDescription("The value of this object identifies an entry in the\nsnmpTargetParamsTable.  The identified entry\ncontains SNMP parameters to be used when generating\nmessages to be sent to this transport address.")
snmpTargetAddrStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 8), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpTargetAddrStorageType.setDescription("The storage type for this conceptual row.\nConceptual rows having the value 'permanent' need not\nallow write-access to any columnar objects in the row.")
snmpTargetAddrRowStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpTargetAddrRowStatus.setDescription("The status of this conceptual row.\n\nTo create a row in this table, a manager must\nset this object to either createAndGo(4) or\ncreateAndWait(5).\n\nUntil instances of all corresponding columns are\nappropriately configured, the value of the\ncorresponding instance of the snmpTargetAddrRowStatus\ncolumn is 'notReady'.\n\nIn particular, a newly created row cannot be made\nactive until the corresponding instances of\nsnmpTargetAddrTDomain, snmpTargetAddrTAddress, and\nsnmpTargetAddrParams have all been set.\n\nThe following objects may not be modified while the\nvalue of this object is active(1):\n    - snmpTargetAddrTDomain\n    - snmpTargetAddrTAddress\nAn attempt to set these objects while the value of\nsnmpTargetAddrRowStatus is active(1) will result in\nan inconsistentValue error.")
snmpTargetParamsTable = MibTable((1, 3, 6, 1, 6, 3, 12, 1, 3))
if mibBuilder.loadTexts: snmpTargetParamsTable.setDescription("A table of SNMP target information to be used\nin the generation of SNMP messages.")
snmpTargetParamsEntry = MibTableRow((1, 3, 6, 1, 6, 3, 12, 1, 3, 1)).setIndexNames((1, "SNMP-TARGET-MIB", "snmpTargetParamsName"))
if mibBuilder.loadTexts: snmpTargetParamsEntry.setDescription("A set of SNMP target information.\n\n\n\nEntries in the snmpTargetParamsTable are created and\ndeleted using the snmpTargetParamsRowStatus object.")
snmpTargetParamsName = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: snmpTargetParamsName.setDescription("The locally arbitrary, but unique identifier associated\nwith this snmpTargetParamsEntry.")
snmpTargetParamsMPModel = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 3, 1, 2), SnmpMessageProcessingModel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpTargetParamsMPModel.setDescription("The Message Processing Model to be used when generating\nSNMP messages using this entry.")
snmpTargetParamsSecurityModel = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 3, 1, 3), SnmpSecurityModel().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpTargetParamsSecurityModel.setDescription("The Security Model to be used when generating SNMP\nmessages using this entry.  An implementation may\nchoose to return an inconsistentValue error if an\nattempt is made to set this variable to a value\nfor a security model which the implementation does\nnot support.")
snmpTargetParamsSecurityName = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 3, 1, 4), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpTargetParamsSecurityName.setDescription("The securityName which identifies the Principal on\nwhose behalf SNMP messages will be generated using\nthis entry.")
snmpTargetParamsSecurityLevel = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 3, 1, 5), SnmpSecurityLevel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpTargetParamsSecurityLevel.setDescription("The Level of Security to be used when generating\nSNMP messages using this entry.")
snmpTargetParamsStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 3, 1, 6), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpTargetParamsStorageType.setDescription("The storage type for this conceptual row.\nConceptual rows having the value 'permanent' need not\nallow write-access to any columnar objects in the row.")
snmpTargetParamsRowStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpTargetParamsRowStatus.setDescription("The status of this conceptual row.\n\nTo create a row in this table, a manager must\nset this object to either createAndGo(4) or\ncreateAndWait(5).\n\nUntil instances of all corresponding columns are\nappropriately configured, the value of the\ncorresponding instance of the snmpTargetParamsRowStatus\ncolumn is 'notReady'.\n\nIn particular, a newly created row cannot be made\nactive until the corresponding\nsnmpTargetParamsMPModel,\nsnmpTargetParamsSecurityModel,\n\n\n\nsnmpTargetParamsSecurityName,\nand snmpTargetParamsSecurityLevel have all been set.\n\nThe following objects may not be modified while the\nvalue of this object is active(1):\n    - snmpTargetParamsMPModel\n    - snmpTargetParamsSecurityModel\n    - snmpTargetParamsSecurityName\n    - snmpTargetParamsSecurityLevel\nAn attempt to set these objects while the value of\nsnmpTargetParamsRowStatus is active(1) will result in\nan inconsistentValue error.")
snmpUnavailableContexts = MibScalar((1, 3, 6, 1, 6, 3, 12, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUnavailableContexts.setDescription("The total number of packets received by the SNMP\nengine which were dropped because the context\ncontained in the message was unavailable.")
snmpUnknownContexts = MibScalar((1, 3, 6, 1, 6, 3, 12, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUnknownContexts.setDescription("The total number of packets received by the SNMP\nengine which were dropped because the context\ncontained in the message was unknown.")
snmpTargetConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 12, 3))
snmpTargetCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 12, 3, 1))
snmpTargetGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 12, 3, 2))

# Augmentions

# Groups

snmpTargetBasicGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 12, 3, 2, 1)).setObjects(("SNMP-TARGET-MIB", "snmpTargetAddrTDomain"), ("SNMP-TARGET-MIB", "snmpTargetParamsMPModel"), ("SNMP-TARGET-MIB", "snmpTargetParamsSecurityName"), ("SNMP-TARGET-MIB", "snmpTargetAddrTAddress"), ("SNMP-TARGET-MIB", "snmpTargetSpinLock"), ("SNMP-TARGET-MIB", "snmpTargetParamsSecurityLevel"), ("SNMP-TARGET-MIB", "snmpTargetParamsSecurityModel"), ("SNMP-TARGET-MIB", "snmpTargetAddrRowStatus"), ("SNMP-TARGET-MIB", "snmpTargetAddrStorageType"), ("SNMP-TARGET-MIB", "snmpTargetAddrParams"), ("SNMP-TARGET-MIB", "snmpTargetParamsStorageType"), ("SNMP-TARGET-MIB", "snmpTargetAddrTagList"), ("SNMP-TARGET-MIB", "snmpTargetParamsRowStatus"), )
if mibBuilder.loadTexts: snmpTargetBasicGroup.setDescription("A collection of objects providing basic remote\nconfiguration of management targets.")
snmpTargetResponseGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 12, 3, 2, 2)).setObjects(("SNMP-TARGET-MIB", "snmpTargetAddrRetryCount"), ("SNMP-TARGET-MIB", "snmpTargetAddrTimeout"), )
if mibBuilder.loadTexts: snmpTargetResponseGroup.setDescription("A collection of objects providing remote configuration\nof management targets for applications which generate\nSNMP messages for which a response message would be\nexpected.")
snmpTargetCommandResponderGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 12, 3, 2, 3)).setObjects(("SNMP-TARGET-MIB", "snmpUnavailableContexts"), ("SNMP-TARGET-MIB", "snmpUnknownContexts"), )
if mibBuilder.loadTexts: snmpTargetCommandResponderGroup.setDescription("A collection of objects required for command responder\napplications, used for counting error conditions.")

# Compliances

snmpTargetCommandResponderCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 12, 3, 1, 1)).setObjects(("SNMP-TARGET-MIB", "snmpTargetCommandResponderGroup"), )
if mibBuilder.loadTexts: snmpTargetCommandResponderCompliance.setDescription("The compliance statement for SNMP entities which include\na command responder application.")

# Exports

# Module identity
mibBuilder.exportSymbols("SNMP-TARGET-MIB", PYSNMP_MODULE_ID=snmpTargetMIB)

# Types
mibBuilder.exportSymbols("SNMP-TARGET-MIB", SnmpTagList=SnmpTagList, SnmpTagValue=SnmpTagValue)

# Objects
mibBuilder.exportSymbols("SNMP-TARGET-MIB", snmpTargetMIB=snmpTargetMIB, snmpTargetObjects=snmpTargetObjects, snmpTargetSpinLock=snmpTargetSpinLock, snmpTargetAddrTable=snmpTargetAddrTable, snmpTargetAddrEntry=snmpTargetAddrEntry, snmpTargetAddrName=snmpTargetAddrName, snmpTargetAddrTDomain=snmpTargetAddrTDomain, snmpTargetAddrTAddress=snmpTargetAddrTAddress, snmpTargetAddrTimeout=snmpTargetAddrTimeout, snmpTargetAddrRetryCount=snmpTargetAddrRetryCount, snmpTargetAddrTagList=snmpTargetAddrTagList, snmpTargetAddrParams=snmpTargetAddrParams, snmpTargetAddrStorageType=snmpTargetAddrStorageType, snmpTargetAddrRowStatus=snmpTargetAddrRowStatus, snmpTargetParamsTable=snmpTargetParamsTable, snmpTargetParamsEntry=snmpTargetParamsEntry, snmpTargetParamsName=snmpTargetParamsName, snmpTargetParamsMPModel=snmpTargetParamsMPModel, snmpTargetParamsSecurityModel=snmpTargetParamsSecurityModel, snmpTargetParamsSecurityName=snmpTargetParamsSecurityName, snmpTargetParamsSecurityLevel=snmpTargetParamsSecurityLevel, snmpTargetParamsStorageType=snmpTargetParamsStorageType, snmpTargetParamsRowStatus=snmpTargetParamsRowStatus, snmpUnavailableContexts=snmpUnavailableContexts, snmpUnknownContexts=snmpUnknownContexts, snmpTargetConformance=snmpTargetConformance, snmpTargetCompliances=snmpTargetCompliances, snmpTargetGroups=snmpTargetGroups)

# Groups
mibBuilder.exportSymbols("SNMP-TARGET-MIB", snmpTargetBasicGroup=snmpTargetBasicGroup, snmpTargetResponseGroup=snmpTargetResponseGroup, snmpTargetCommandResponderGroup=snmpTargetCommandResponderGroup)

# Compliances
mibBuilder.exportSymbols("SNMP-TARGET-MIB", snmpTargetCommandResponderCompliance=snmpTargetCommandResponderCompliance)
