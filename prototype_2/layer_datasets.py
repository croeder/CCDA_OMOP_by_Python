#!/usr/bin/env python3

import data_driven_parse as DDP
import pandas as PD

def create_omop_domain_datasets(omop_data):
    for domain, domain_list in omop_data.items():
        # initialize a dictionary of columns from the first row
        column_dict = {}
        for field, parts in domain_list[0].items():
            column_dict[field] = []

        # add the data from all the rows
        for domain_data_dict in domain_list:
            for field, parts in domain_data_dict.items():
                column_dict[field].append(parts)


        # create a Pandas dataframe from the data_dict
        print(f"\n{domain}")
        #print(column_dict)
        domain_df = PD.DataFrame(column_dict)
        print(domain_df)


if __name__ == '__main__':
    ccd_ambulatory_path = '../resources/CCDA_CCD_b1_Ambulatory_v2.xml'
    if False:
        from foundry.transforms import Dataset
        ccd_ambulatory = Dataset.get("ccda_ccd_b1_ambulatory_v2")
        ccd_ambulatory_files = ccd_ambulatory.files().download()
        ccd_ambulatory_path = ccd_ambulatory_files['CCDA_CCD_b1_Ambulatory_v2.xml']
 
    omop_data = DDP.parse_doc(ccd_ambulatory_path) 
    DDP.print_omop_structure(omop_data) 
    create_omop_domain_datasets(omop_data)
