# istanbul-tools-http-api

## Decode extraData
```
curl -s http://localhost:8080/api/v1.0/extra/decode/0x...
```

Example:
```
curl -s http://localhost:8080/api/v1.0/extra/decode/0xd783010702846765746887676f312e382e37856c696e75780000000000000000f90179f86994986f2503001e238ade8f401ca0b0930dd9ba456394a49ddde59f9c521be81297a4c49697a5497063b394d03e9bc22d2033fc308c884ee906787bfb8dfe8c94d4e6453afcfbfc8c61d53b71fddcc484e14f45e094e61e969b04c3180a6773487a6308a1001846f152b84192ed0a2b4f453967fb164e6f8055186004adbf58ee865a70447a131e390aad061984d528a28c1f16ee1d63ff879cae1b1ef57631eed1e5a5991a67ab1076502e01f8c9b841ac6512dac7477e0e07a534070e87572dd66a58d26f3b427d12b55f9dba2c16f65a9c06d13ec1b04c118f481532604c24da8163f46fce414d44acb0190df7975200b841b075092d40cf2663965e3d380722a169ef9069b065efcee7fd276d5dd0ba767032d33b53351771ea9a13ce3d4f4f2092f4d09467db79a6f0173ed3c7040ec19300b84100ca5986e6dbb3c7b57ac7ff9eaa8445b51043e5130f5b627c3d174947e566834e40b71b9d2cd65a1952a7860d78742c4d3f8191b46223de86d2aa3a0c6e493700 | python -m json.tool
```
```json
{
    "vanity": "0xd783010702846765746887676f312e382e37856c696e75780000000000000000",
    "validators": [
        "  0x986f2503001e238AdE8f401cA0b0930dD9BA4563",
        "  0xa49ddde59f9C521be81297a4c49697a5497063B3",
        "  0xD03e9Bc22d2033fc308C884eE906787Bfb8dfe8C",
        "  0xD4e6453AFcfbfc8c61d53B71FDdcc484E14f45e0",
        "  0xe61E969B04c3180A6773487a6308A1001846F152"
    ],
    "seal": "0x92ed0a2b4f453967fb164e6f8055186004adbf58ee865a70447a131e390aad061984d528a28c1f16ee1d63ff879cae1b1ef57631eed1e5a5991a67ab1076502e01",
    "committed_seals": [
        "  0xac6512dac7477e0e07a534070e87572dd66a58d26f3b427d12b55f9dba2c16f65a9c06d13ec1b04c118f481532604c24da8163f46fce414d44acb0190df7975200",
        "  0xb075092d40cf2663965e3d380722a169ef9069b065efcee7fd276d5dd0ba767032d33b53351771ea9a13ce3d4f4f2092f4d09467db79a6f0173ed3c7040ec19300",
        "  0x00ca5986e6dbb3c7b57ac7ff9eaa8445b51043e5130f5b627c3d174947e566834e40b71b9d2cd65a1952a7860d78742c4d3f8191b46223de86d2aa3a0c6e493700"
    ]
}
```
