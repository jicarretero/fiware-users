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

REGION="Vicenza"

if __name__ == "__main__":
    data = load_json_file('/tmp/all.json')

    ## Filter Projects for Region node
    projects_info_in_noida = list( filter(lambda x: 'region_id' in x and x['region_id'] == REGION, data['endpoint_groups']))
    projects_ids_in_noida = [pj['id'] for pj in  projects_info_in_noida[0]['projects']]

    ## Get users_by_id dictionary
    users_by_id = get_dict_from_data(data, 'users', 'id')

    ## Let's see users which could access Region
    users_in_noida = set()
    for role_assignment in data['role_assignments']:
        if ('scope_project_id' in role_assignment and 
            role_assignment['scope_project_id'] in projects_ids_in_noida):
            users_in_noida.add(users_by_id[role_assignment['user_id']]['name'])

    for u in users_in_noida:
         try:
             print(u)
         except:
             pass
