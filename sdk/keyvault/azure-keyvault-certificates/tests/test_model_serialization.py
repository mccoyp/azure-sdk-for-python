# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from dotenv import load_dotenv
import json
import os

from azure.core.serialization import ComplexEncoder
from azure.identity import ClientSecretCredential
from azure.keyvault.certificates import CertificateClient, CertificateProperties


load_dotenv()

credential = ClientSecretCredential(
    tenant_id=os.environ["KEYVAULT_TENANT_ID"],
    client_id=os.environ["KEYVAULT_CLIENT_ID"],
    client_secret=os.environ["KEYVAULT_CLIENT_SECRET"]
)
client = CertificateClient(vault_url=os.environ["AZURE_KEYVAULT_URL"], credential=credential)
certificate = client.get_certificate("livekvtestcertserialize3")
cert_dict = certificate.to_dict()
cert_serialized = json.dumps(cert_dict, cls=ComplexEncoder)#, encoding="latin1")

properties = certificate.properties
properties_dict = properties.to_dict()
properties_from_dict = CertificateProperties.from_dict(properties_dict)
properties_from_dict_dict = properties_from_dict.to_dict()

serialized_from_dict = json.dumps(properties_from_dict_dict, cls=ComplexEncoder)#, encoding="latin1")
serialized = json.dumps(properties_dict, cls=ComplexEncoder)#, encoding="latin1")
deserialized = json.loads(serialized)
properties_from_json = CertificateProperties.from_dict(deserialized)
print(properties_from_json)
