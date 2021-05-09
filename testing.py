#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 23:47:42 2021

@author: andrea
"""

import unittest
from authorization_log import AuthorizationServer, Trillian
from datetime import datetime
from cryptography.hazmat.primitives import serialization


class TestPersonality(unittest.TestCase):
    
    def setUp(self):
        key_pair = AuthorizationServer.generate_key()
        self.auth = AuthorizationServer(key_pair, issuer_uri = 'urn:auth')
        key_pair = Trillian.generate_key()
        self.personality = Trillian(key_pair, 
                                    allowed_servers = {'urn:auth':self.auth.pk})

    
    def tearDown(self):
        pass

    
    def test_jwt(self):
        # Test with invalid token
        token = b'ndjncdnjmwkswmso.xnsnqonoqsnqosq'
        with self.assertRaises(ValueError):
            data = self.personality.decode_jwt(token, self.auth.pk)
        
        # Test with a wrong uri of the issuer of the JWT
        self.auth.issuer_uri = 'urn:wrong'
        token = self.auth.generate_jwt(client='C',server='R')
        with self.assertRaises(ValueError):
            data = self.personality.decode_jwt(token, self.auth.pk)
        
        # Test to check if the data decoded by the token contains the correct 
        # client and server
        self.auth.issuer_uri = 'urn:auth'
        token = self.auth.generate_jwt(client='C',server='R')
        data = self.personality.decode_jwt(token, self.auth.pk)
        self.assertEqual('C', data["client"])
        self.assertEqual('R', data["server"])
        
        # Test using a wrong public key for decode the JWT
        token = self.auth.generate_jwt(client='C',server='R')
        wrong_key_pair = AuthorizationServer.generate_key()
        self.auth.pk = wrong_key_pair[1].public_bytes(encoding=serialization.Encoding.PEM,
                                            format=serialization.PublicFormat.
                                            SubjectPublicKeyInfo)
        with self.assertRaises(ValueError):
            data = self.personality.decode_jwt(token, self.auth.pk)
        
        # Test with the authorization server that is not allowed by 
        # the personality to insert JWT
        self.personality.allowed_servers = {}
        token = self.auth.generate_jwt(client='C',server='R')
        with self.assertRaises(ValueError):
            data = self.personality.decode_jwt(token, self.auth.pk)
        
    
        
    def test_adding_jwt(self):
        token = self.auth.generate_jwt(client='C', server='R')
        inclusion_proof1 = self.personality.insert_jwt(token, self.auth.pk)
        self.assertIsNotNone(inclusion_proof1)
        inclusion_proof2 = self.personality.verify_inclusion('C', 'R', 
                                                             datetime.utcnow().isoformat())
        self.assertEqual(inclusion_proof1.signed_log_root,
                         inclusion_proof2.signed_log_root)
        
    
if __name__ == '__main__':
    unittest.main()
    