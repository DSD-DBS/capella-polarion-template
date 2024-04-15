# SPDX-FileCopyrightText: Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
# %%
import os
import pathlib

import requests

CUSTOM_FIELDS_PATH = pathlib.Path(__file__).parents[1] / "global" / "fields"
POLARION_HOST = os.getenv("POLARION_HOST", "")
POLARION_USER = os.getenv("POLARION_USER", "")
POLARION_PAT = os.getenv("POLARION_PAT", "")
URL = "{host}/polarion/fileupload?uploadId=FileUpload{number}"

custom_fields_number = 12

# %%
url = URL.format(host=POLARION_HOST, number=custom_fields_number)
for file in CUSTOM_FIELDS_PATH.glob("*-custom-fields.xml"):
    data = file.read_bytes()
    response = requests.post(
        url=url,
        data=data,
        timeout=10,
        auth=(POLARION_USER, POLARION_PAT),
    )
    response.raise_for_status()
