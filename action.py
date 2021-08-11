#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

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
                        help='ID of the nuvlabox-release to be used',
                        required=True)
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
    

if __name__ == '__main__':
    args = init()
    
    print(dir(args))
    print(args.api_key)
    print("::set-output name=NUVLABOX_UUID::1")