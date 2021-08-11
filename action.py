#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from nuvla.api import Api

def init():
    """ Parse command-line args

    Returns:
        args: command-line argparse args
    """

    parser = argparse.ArgumentParser(description='Create NuvlaBox resource in Nuvla.io')

    parser.add_argument('--api-key',
                        dest='api_key',
                        metavar='KEY',
                        help='Nuvla.io User API Key',
                        required=True)
    parser.add_argument('--api-secret',
                        dest='api_secret',
                        metavar='SECRET',
                        help='Nuvla.io User API Secret',
                        required=True)
    parser.add_argument('--vpn-server-id',
                        dest='vpn_server_id',
                        metavar='VPN_SERVER_ID',
                        help='ID of the VPN infrastructure service for the NuvlaBox',
                        default='infrastructure-service/eb8e09c2-8387-4f6d-86a4-ff5ddf3d07d7',
                        required=True)
    parser.add_argument('--nuvlabox-release',
                        dest='nuvlabox_release',
                        metavar='NUVLABOX_RELEASE',
                        help='ID of the nuvlabox-release to be used')
    parser.add_argument('--name',
                        dest='name',
                        metavar='NAME',
                        help='Name of for the NuvlaBox resource',
                        required=True)
    parser.add_argument('--description',
                        dest='description',
                        metavar='DESCRIPTION',
                        help='Description for the NuvlaBox resource',
                        default='NuvlaBox created from a GitHub action',
                        required=True)

    return parser.parse_args()


def create_nuvlabox_body(name, description, vpn_server_id, major_version, body=None):

    if not body:
        body = {
            "name": name,
            "description": description,
            "version": int(major_version),
            "vpn-server-id": vpn_server_id
        }

    return body


if __name__ == '__main__':
    args = init()

    api = Api("https://nuvla.io")

    api.login_apikey(args.api_key, args.api_secret)

    if not args.nuvlabox_release:
        nuvlabox_release = api.search('nuvlabox-release',
                                    orderby="created:desc",
                                    last=1).resources[0].data['release']
    else:
        nuvlabox_release = api.get(args.nuvlabox_release).data['release']

    major_version = nuvlabox_release.split('.')[0]

    new_nb = api.add('nuvlabox',
                     data=create_nuvlabox_body(
                         args.name,
                         args.description,
                         args.vpn_server_id,
                         major_version))

    print(f"::set-output name=NUVLABOX_UUID::{new_nb.data.get('resource-id')}")

