#!/usr/bin/env python
# -*- encoding: utf-8 -*-
##
# Copyright 2017 FIWARE Foundation, e.V.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
##


__author__ = "José Ignacio Carretero Guarde"


from functions import *
import json

REGIONS=[
"Brittany",
"Budapest2",
"Budapest3",
"Crete",
"Genoa",
"Hannover",
"Lannion4",
"Lannion5",
"Mexico",
"Mexico2",
"Noida",
"Penang",
"PiraeusU",
"Poznan",
"SaoPaulo",
"Senegal",
"SophiaAntipolis2",
"Spain2",
"twolf",
"Vicenza",
"Volos",
"Wolfsburg",
"Wroclaw",
"Zurich2"
       ]
# REGION="Senegal"

a_output_info=[]

if __name__ == "__main__":
    data = load_json_file("/tmp/all.json")

    for REGION in REGIONS:
        output_info={"name": REGION, "users": [], "count": 0}
        ## Filter Projects for Noida node
        projects_info_in_region = filter(lambda x: 'region_id' in x and x['region_id'] == REGION, data['endpoint_groups'])

        for prj in projects_info_in_region:
            pir=prj

        # projects_ids_in_region = [pj['id'] for pj in  projects_info_in_region[0]['projects']]
        projects_ids_in_region = [pj['id'] for pj in  pir['projects']]
       
        ## Get users_by_id dictionary
        users_by_id = get_dict_from_data(data, 'users', 'id')

        ## Let's see users which could access Noida
        users_in_region = set()
        for role_assignment in data['role_assignments']:
            if ('scope_project_id' in role_assignment and 
                    role_assignment['scope_project_id'] in projects_ids_in_region and users_by_id[role_assignment['user_id']]['enabled']==True):
                users_in_region.add(users_by_id[role_assignment['user_id']]['name'])

        for u in users_in_region:
             try:
                 output_info['users'].append(u)
                 # print(u)
             except:
                 pass
        output_info['count']=len(output_info['users'])
        a_output_info.append(output_info)
    print(json.dumps(a_output_info))
