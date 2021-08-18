# nuvla-create-nuvlabox-action
GitHub action to create a new NuvlaBox resource in Nuvla.io

# How to use the action (example)

This is what your workflow should look like:

```

jobs:
  create_nuvlabox_job:
    runs-on: ubuntu-latest
    name: A job to create a NuvlaBox on Nuvla.io
    steps:
      - name: creator
        id: nuvlabox
        uses: nuvla/nuvla-create-nuvlabox-action@v2
        with:
          api-key: ${{ secrets.API_KEY }}
          api-secret: ${{ secrets.API_SECRET }}
          nuvlabox-release: 'nuvlabox-release/a26b3ef0-1d66-464c-9ad0-b96be025444c'
          name: "Mock NBE for test"
          description: "Some description for your nuvlabox"
      # Use the output
      - name: Get the output
        run: echo "The output was ${{ steps.test.outputs.NUVLABOX_UUID }}"
```

# Full list of possible input parameters

```
  --api-key KEY         Nuvla.io User API Key
  --api-secret SECRET   Nuvla.io User API Secret
  --vpn-server-id VPN_SERVER_ID
                        ID of the VPN infrastructure service for the NuvlaBox
  --nuvlabox-release NUVLABOX_RELEASE
                        ID of the nuvlabox-release to be used
  --name NAME           Name of for the NuvlaBox resource
  --description DESCRIPTION
                        Description for the NuvlaBox resource
```


