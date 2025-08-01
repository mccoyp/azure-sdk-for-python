# The MIT License (MIT)
# Copyright (c) Microsoft Corporation. All rights reserved.

import base64
import json
import time
import os
import unittest
from io import StringIO

import pytest
from azure.core.credentials import AccessToken

import test_config
from azure.cosmos import exceptions
from azure.cosmos.aio import CosmosClient, DatabaseProxy, ContainerProxy


def _remove_padding(encoded_string):
    while encoded_string.endswith("="):
        encoded_string = encoded_string[0:len(encoded_string) - 1]

    return encoded_string


def get_test_item(num):
    test_item = {
        'pk': 'pk',
        'id': 'Item_' + str(num),
        'test_object': True,
        'lastName': 'Smith'
    }
    return test_item


class CosmosEmulatorCredential(object):

    async def get_token(self, *scopes, **kwargs):
        # type: (*str, **Any) -> AccessToken
        """Request an access token for the emulator. Based on Azure Core's Access Token Credential.

        This method is called automatically by Azure SDK clients.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
        :rtype: :class:`azure.core.credentials.AccessToken`
        :raises CredentialUnavailableError: the credential is unable to attempt authentication because it lacks
          required data, state, or platform support
        :raises ~azure.core.exceptions.ClientAuthenticationError: authentication failed. The error's ``message``
          attribute gives a reason.
        """
        aad_header_cosmos_emulator = "{\"typ\":\"JWT\",\"alg\":\"RS256\",\"x5t\":\"" \
                                     "CosmosEmulatorPrimaryMaster\",\"kid\":\"CosmosEmulatorPrimaryMaster\"}"

        aad_claim_cosmos_emulator_format = {"aud": "https://localhost.localhost",
                                            "iss": "https://sts.fake-issuer.net/7b1999a1-dfd7-440e-8204-00170979b984",
                                            "iat": int(time.time()), "nbf": int(time.time()),
                                            "exp": int(time.time() + 7200), "aio": "", "appid": "localhost",
                                            "appidacr": "1", "idp": "https://localhost:8081/",
                                            "oid": "96313034-4739-43cb-93cd-74193adbe5b6", "rh": "", "sub": "localhost",
                                            "tid": "EmulatorFederation", "uti": "", "ver": "1.0",
                                            "scp": "user_impersonation",
                                            "groups": ["7ce1d003-4cb3-4879-b7c5-74062a35c66e",
                                                       "e99ff30c-c229-4c67-ab29-30a6aebc3e58",
                                                       "5549bb62-c77b-4305-bda9-9ec66b85d9e4",
                                                       "c44fd685-5c58-452c-aaf7-13ce75184f65",
                                                       "be895215-eab5-43b7-9536-9ef8fe130330"]}

        emulator_key = test_config.TestConfig.masterKey

        first_encoded_bytes = base64.urlsafe_b64encode(aad_header_cosmos_emulator.encode("utf-8"))
        first_encoded_padded = str(first_encoded_bytes, "utf-8")
        first_encoded = _remove_padding(first_encoded_padded)

        str_io_obj = StringIO()
        json.dump(aad_claim_cosmos_emulator_format, str_io_obj)
        aad_claim_cosmos_emulator_format_string = str(str_io_obj.getvalue()).replace(" ", "")
        second = aad_claim_cosmos_emulator_format_string
        second_encoded_bytes = base64.urlsafe_b64encode(second.encode("utf-8"))
        second_encoded_padded = str(second_encoded_bytes, "utf-8")
        second_encoded = _remove_padding(second_encoded_padded)

        emulator_key_encoded_bytes = base64.urlsafe_b64encode(emulator_key.encode("utf-8"))
        emulator_key_encoded_padded = str(emulator_key_encoded_bytes, "utf-8")
        emulator_key_encoded = _remove_padding(emulator_key_encoded_padded)

        return AccessToken(first_encoded + "." + second_encoded + "." + emulator_key_encoded, int(time.time() + 7200))


@pytest.mark.cosmosEmulator
class TestAADAsync(unittest.IsolatedAsyncioTestCase):
    client: CosmosClient = None
    database: DatabaseProxy = None
    container: ContainerProxy = None
    configs = test_config.TestConfig
    host = configs.host
    masterKey = configs.masterKey
    credential = CosmosEmulatorCredential() if configs.is_emulator else configs.credential_async

    @classmethod
    def setUpClass(cls):
        if (cls.credential == '[YOUR_KEY_HERE]' or
                cls.host == '[YOUR_ENDPOINT_HERE]'):
            raise Exception(
                "You must specify your Azure Cosmos account values for "
                "'masterKey' and 'host' at the top of this class to run the "
                "tests.")

    async def asyncSetUp(self):
        self.client = CosmosClient(self.host, self.credential)
        self.database = self.client.get_database_client(self.configs.TEST_DATABASE_ID)
        self.container = self.database.get_container_client(self.configs.TEST_SINGLE_PARTITION_CONTAINER_ID)

    async def asyncTearDown(self):
        await self.client.close()

    async def test_aad_credentials_async(self):
        # Do any R/W data operations with your authorized AAD client

        print("Container info: " + str(await self.container.read()))
        await self.container.create_item(get_test_item(0))
        print("Point read result: " + str(await self.container.read_item(item='Item_0', partition_key='pk')))
        query_results = [item async for item in self.container.query_items(query='select * from c', partition_key='pk')]
        assert len(query_results) == 1
        print("Query result: " + str(query_results[0]))
        await self.container.delete_item(item='Item_0', partition_key='pk')

        # Attempting to do management operations will return a 403 Forbidden exception
        try:
            await self.client.delete_database(self.configs.TEST_DATABASE_ID)
        except exceptions.CosmosHttpResponseError as e:
            assert e.status_code == 403
            print("403 error assertion success")

    async def test_aad_scope_override_async(self):
        override_scope = "https://my.custom.scope/.default"
        os.environ["AZURE_COSMOS_AAD_SCOPE_OVERRIDE"] = override_scope

        scopes_captured = []
        original_get_token = CosmosEmulatorCredential.get_token

        async def capturing_get_token(self, *scopes, **kwargs):
            scopes_captured.extend(scopes)
            # Await the original method!
            return await original_get_token(self, *scopes, **kwargs)

        CosmosEmulatorCredential.get_token = capturing_get_token

        try:
            credential = CosmosEmulatorCredential()
            client = CosmosClient(self.host, credential)
            database = client.get_database_client(self.configs.TEST_DATABASE_ID)
            container = database.get_container_client(self.configs.TEST_SINGLE_PARTITION_CONTAINER_ID)

            await container.create_item(get_test_item(1))
            item = await container.read_item(item='Item_1', partition_key='pk')
            assert item["id"] == "Item_1"
            assert override_scope in scopes_captured
        finally:
            CosmosEmulatorCredential.get_token = original_get_token
            del os.environ["AZURE_COSMOS_AAD_SCOPE_OVERRIDE"]
            try:
                await container.delete_item(item='Item_1', partition_key='pk')
            except Exception:
                pass
            await client.close()

if __name__ == "__main__":
    unittest.main()
