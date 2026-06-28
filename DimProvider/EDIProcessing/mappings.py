"""
Provider Hierarchy Mapping Definitions — Configured for declarative JSONata mapping.
Maps raw EDI 274 loops directly to a flat CSV structure in a 1-to-1 fashion, 
mirroring the colleague's Member mapping architecture.
"""

MAPPINGS = {
    "name": "Provider Hierarchy 7.12 Declarative Schema Mapping",
    "mapping_type": "only_mapped",
    "expressions": {
        # Core Identifiers
        "TEMPLATE":         "'TEMPLATE'",
        "PROVIDERID":       "detail.nm1[entity_identifier_code='1P'].(identifier ? identifier : nm111_111)",
        "PROVIDERLASTNAME": "detail.nm1[entity_identifier_code='1P'].(entity_type_qualifier='1' ? ($join([first_name, middle_name, name], ' ')) : name)",
        "PROVIDERNPI":      "detail.nm1[entity_identifier_code='1P'].(identifier ? identifier : nm111_111)",
        "LOCATIONGROUPID":  "detail.nm1[entity_identifier_code='41'].submitter_id",
        "LOCATIONRANKING":  "1",
        "LOCATIONIDTYPE":   "detail.nm1[entity_identifier_code='1P'].entity_identifier_code",
        "LOCATIONID":       "detail.nm1[entity_identifier_code='1P'].(identifier ? identifier : nm111_111)",
        "LOCATIONDESC":     "detail.nm1[entity_identifier_code='1P'].(entity_type_qualifier='1' ? ($join([first_name, middle_name, name], ' ')) : name)",
        "LOCATIONTIN":      "detail.ref[0].champus_id",
        
        # Address Details
        "LOCATIONADDRESS1": "detail.n3.address_line_1",
        "LOCATIONADDRESS2": "detail.n3.address_line_2",
        "LOCATIONCITY":     "detail.n4.city",
        "LOCATIONSTATE":    "detail.n4.state",
        "LOCATIONZIP":      "detail.n4.zip_code",
        
        # Contact & Date Details
        "PHONENUMBER":      "detail.per[per01='AJ'].per04_04",
        "CONTACTPERSON":    "detail.per[per01='AJ'].per02_02",
        "STARTDATE":        "detail.dtp[date_qualifier='007'].date_value",
        "ENDDATE":          "detail.dtp[date_qualifier='008'].date_value"
    }
}
