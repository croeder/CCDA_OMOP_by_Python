
import prototype_2.value_transformations as VT
"""
    (not) This is for caresites from Encounter/participant/participantRole
    
    This is for caresites from Encounter/performer/assignedEntity

"""
metadata = {
    'Provider': {

        'root': {
            'config_type': 'ROOT',
            'expected_domain_id': 'Provider',
            # Encounters section
            'element': ('./hl7:component/hl7:structuredBody/hl7:component/hl7:section/'
                        'hl7:templateId[ @root="2.16.840.1.113883.10.20.22.2.22" or @root="2.16.840.1.113883.10.20.22.2.22.1" ]/../'
                        'hl7:entry/hl7:encounter[@moodCode="EVN"]/'
                        'hl7:performer/hl7:assignedEntity' )
        },
      
        'provider_id_extension': {
            'config_type': 'FIELD',
            'element': 'hl7:id',
            'attribute': "extension"
        },
       'provider_id_root': {
            'config_type': 'FIELD',
            'element': 'hl7:id',
            'attribute': "root"
        },
        'provider_id_element': {
            'config_type': 'HASH',
            'fields': [ 'provider_id_root', 'provider_id_extension'],
            'priority' : ['provider_id', 1]
        },
        
        'provider_id_street': {
            'config_type': 'FIELD',
            'element': 'hl7:addr/hl7:streetAddressLine',
            'attribute': "#text"
        },
       'provider_id_city': {
            'config_type': 'FIELD',
            'element': 'hl7:addr/hl7:city',
            'attribute': "#text"
        },
        'provider_id_state': {
            'config_type': 'FIELD',
            'element': 'hl7:addr/hl7:state',
            'attribute': "#text"
        },
        'provider_id_zip': {
            'config_type': 'FIELD',
            'element': 'hl7:addr/hl7:postalCode',
            'attribute': "#text"
        },
        'provider_id_given': {
            'config_type': 'FIELD',
            'element': 'hl7:assignedPerson/hl7:name/hl7:given',
            'attribute': "#text"
        },
        'provider_id_family': {
            'config_type': 'FIELD',
            'element': 'hl7:assignedPerson/hl7:name/hl7:family',
            'attribute': "#text"
        },
        'provider_id_hash': {
            'config_type': 'HASH',
            'fields' : [ 'provider_id_street', 'provider_id_city', 'provider_id_state', 'provider_id_zip', 'provider_id_given', 'provider_id_family'],
            'priority' : ['provider_id', 2]
        },
       
        'provider_id': {
            'config_type': 'PRIORITY',
            'order': 1
        },

        'provider_name': { 
            'config_type': 'None',
            'order': 2
        },

        'npi': {
            'config_type': 'FIELD',
            'element': 'hl7:id[@root="2.16.840.1.113883.4.6"]',
            'attribute': "extension",
            'order': 3
        },
        'dea': {
            'config_type': 'FIELD',
            'element': 'hl7:id[@root="2.16.840.1.113883.D.E.A"]', # TODO get the correct OID
            'attribute': "extension",
            'order': 4
        },
        #<code code="207QA0505X" displayName="Adult Medicine Physician" codeSystem="2.16.840.1.113883.6.101" codeSystemName="NUCC" />
        'specialty_id_code': { 
            'config_type': 'FIELD',
            'element': 'hl7:code',
            'attribute': "code"
        },
        'specialty_id_codeSystem': { 
            'config_type': 'FIELD',
            'element': 'hl7:code',
            'attribute': "codesystem"
        },
        'specialty_id': {
       	    'config_type': 'DERIVED',
    	    'FUNCTION': VT.map_hl7_to_omop_concept_id,
    	        'argument_names': {
    		        'concept_code': 'specialty_id_code',
    		        'vocabulary_oid': 'specialty_id_codeSystem',
                    'default': 0
    	         },
            'order': 5
        },
        
        # hl7:encounter/hl7:participant/hl7:participantRole
        'care_site_id': { 
            'config_type': 'FIELD',
            'element': '../../hl7:participant/hl7:participantRole/hl7:id',
            'attribute': "root",
            'order': 6
        },
  
        'year_of_birth': {
            'config_type': None,
            'order' :7
        },
        'gender_concept_id': {
            'config_type': None,
            'order' :8
        },
        'provider_source_value': {
            'config_type': None,
            'order' :9
        },
        'specialty_source_value': {
            'config_type': None,
            'order' :10
        },
        'specialty_source_concept_id': {
            'config_type': None,
            'order' :11
        }, 
        'gender_source_value': {
            'config_type': None,
            'order' :12
        },
        'gender_source_concept_id': {
            'config_type': None,
            'order' :13
        }
    },
    
}
