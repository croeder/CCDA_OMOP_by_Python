CREATE TABLE @cdmDatabaseSchema.visit_occurrence (
            visit_occurrence_id integer NOT NULL,
            person_id integer NOT NULL,
            visit_concept_id integer NOT NULL,
            visit_start_date date NOT NULL,
            visit_start_datetime TIMESTAMP NULL,
            visit_end_date date NOT NULL,
            visit_end_datetime TIMESTAMP NULL,
            visit_type_concept_id Integer NOT NULL,
            provider_id integer NULL,
            care_site_id integer NULL,
            visit_source_value varchar(50) NULL,
            visit_source_concept_id integer NULL,
            admitting_source_concept_id integer NULL,
            admitting_source_value varchar(50) NULL,
            discharge_to_concept_id integer NULL,
            discharge_to_source_value varchar(50) NULL,
            preceding_visit_occurrence_id integer NULL );
