import unittest
from pycoin.key.BIP32Node import BIP32Node
from pycoin.serialize import h2b


class Bip0032TestCase(unittest.TestCase):

    def test_vector_1(self):
        master = BIP32Node.from_master_secret(h2b("000102030405060708090a0b0c0d0e0f"))
        self.assertEqual(
            master.wallet_key(as_private=True),
            "xprv9s21ZrQH143K3QTDL4LXw2F7HEK3wJUD2nW2nRk4stbPy6cq3jPPqjiChkVvvNKmPG"
            "JxWUtg6LnF5kejMRNNU3TGtRBeJgk33yuGBxrMPHi")
        self.assertEqual(master.bitcoin_address(), "15mKKb2eos1hWa6tisdPwwDC1a5J1y9nma")
        self.assertEqual(master.wif(), "L52XzL2cMkHxqxBXRyEpnPQZGUs3uKiL3R11XbAdHigRzDozKZeW")

        self.assertEqual(
            master.wallet_key(),
            "xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJo"
            "Cu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet8")

        m0p = master.subkey(is_hardened=True)
        self.assertEqual(
            m0p.wallet_key(),
            "xpub68Gmy5EdvgibQVfPdqkBBCHxA5htiqg55crXYuXoQRKfDBFA1WEjWgP6LHhwBZeNK1"
            "VTsfTFUHCdrfp1bgwQ9xv5ski8PX9rL2dZXvgGDnw")
        self.assertEqual(
            m0p.wallet_key(as_private=True),
            "xprv9uHRZZhk6KAJC1avXpDAp4MDc3sQKNxDiPvvkX8Br5ngLNv1TxvUxt4cV1rGL5hj6K"
            "CesnDYUhd7oWgT11eZG7XnxHrnYeSvkzY7d2bhkJ7")
        self.assertEqual(master.subkey_for_path("0p").wallet_key(), m0p.wallet_key())

        pub_mp0 = master.subkey(is_hardened=True, as_private=False)
        self.assertEqual(pub_mp0.wallet_key(), m0p.wallet_key())
        self.assertEqual(master.subkey_for_path("0p.pub").wallet_key(), pub_mp0.wallet_key())

        m0p1 = m0p.subkey(i=1)
        self.assertEqual(
            m0p1.wallet_key(),
            "xpub6ASuArnXKPbfEwhqN6e3mwBcDTgzisQN1wXN9BJcM47sSikHjJf3UFHKkNAWbWMiGj"
            "7Wf5uMash7SyYq527Hqck2AxYysAA7xmALppuCkwQ")
        self.assertEqual(
            m0p1.wallet_key(as_private=True),
            "xprv9wTYmMFdV23N2TdNG573QoEsfRrWKQgWeibmLntzniatZvR9BmLnvSxqu53Kw1UmYP"
            "xLgboyZQaXwTCg8MSY3H2EU4pWcQDnRnrVA1xe8fs")
        self.assertEqual(master.subkey_for_path("0p/1").wallet_key(), m0p1.wallet_key())

        pub_m0p1 = m0p.subkey(i=1, as_private=False)
        self.assertEqual(pub_m0p1.wallet_key(), m0p1.wallet_key())
        self.assertEqual(master.subkey_for_path("0p/1.pub").wallet_key(), pub_m0p1.wallet_key())

        m0p1_1_2p = m0p1.subkey(i=2, is_hardened=True)
        self.assertEqual(
            m0p1_1_2p.wallet_key(),
            "xpub6D4BDPcP2GT577Vvch3R8wDkScZWzQzMMUm3PWbmWvVJrZwQY4VUNgqFJPMM3No2dF"
            "DFGTsxxpG5uJh7n7epu4trkrX7x7DogT5Uv6fcLW5")
        self.assertEqual(
            m0p1_1_2p.wallet_key(as_private=True),
            "xprv9z4pot5VBttmtdRTWfWQmoH1taj2axGVzFqSb8C9xaxKymcFzXBDptWmT7FwuEzG3r"
            "yjH4ktypQSAewRiNMjANTtpgP4mLTj34bhnZX7UiM")
        self.assertEqual(master.subkey_for_path("0p/1/2p").wallet_key(), m0p1_1_2p.wallet_key())

        pub_m0p1_1_2p = m0p1.subkey(i=2, as_private=False, is_hardened=True)
        self.assertEqual(pub_m0p1_1_2p.wallet_key(), m0p1_1_2p.wallet_key())
        self.assertEqual(master.subkey_for_path("0p/1/2p.pub").wallet_key(), pub_m0p1_1_2p.wallet_key())

        m0p1_1_2p_2 = m0p1_1_2p.subkey(i=2)
        self.assertEqual(
            m0p1_1_2p_2.wallet_key(),
            "xpub6FHa3pjLCk84BayeJxFW2SP4XRrFd1JYnxeLeU8EqN3vDfZmbqBqaGJAyiLjTAwm6Z"
            "LRQUMv1ZACTj37sR62cfN7fe5JnJ7dh8zL4fiyLHV")
        self.assertEqual(
            m0p1_1_2p_2.wallet_key(as_private=True),
            "xprvA2JDeKCSNNZky6uBCviVfJSKyQ1mDYahRjijr5idH2WwLsEd4Hsb2Tyh8RfQMuPh7f"
            "7RtyzTtdrbdqqsunu5Mm3wDvUAKRHSC34sJ7in334")
        self.assertEqual(master.subkey_for_path("0p/1/2p/2").wallet_key(), m0p1_1_2p_2.wallet_key())

        pub_m0p1_1_2p_2 = m0p1_1_2p.subkey(i=2, as_private=False)
        self.assertEqual(pub_m0p1_1_2p_2.wallet_key(), m0p1_1_2p_2.wallet_key())
        self.assertEqual(master.subkey_for_path("0p/1/2p/2.pub").wallet_key(), pub_m0p1_1_2p_2.wallet_key())

        m0p1_1_2p_2_1000000000 = m0p1_1_2p_2.subkey(i=1000000000)
        self.assertEqual(
            m0p1_1_2p_2_1000000000.wallet_key(),
            "xpub6H1LXWLaKsWFhvm6RVpEL9P4KfRZSW7abD2ttkWP3SSQvnyA8FSVqNTEcYFgJS2UaF"
            "cxupHiYkro49S8yGasTvXEYBVPamhGW6cFJodrTHy")
        self.assertEqual(
            m0p1_1_2p_2_1000000000.wallet_key(as_private=True),
            "xprvA41z7zogVVwxVSgdKUHDy1SKmdb533PjDz7J6N6mV6uS3ze1ai8FHa8kmHScGpWmj4"
            "WggLyQjgPie1rFSruoUihUZREPSL39UNdE3BBDu76")
        self.assertEqual(master.subkey_for_path("0p/1/2p/2/1000000000").wallet_key(),
                         m0p1_1_2p_2_1000000000.wallet_key())

        pub_m0p1_1_2p_2_1000000000 = m0p1_1_2p_2.subkey(i=1000000000, as_private=False)
        self.assertEqual(pub_m0p1_1_2p_2_1000000000.wallet_key(), m0p1_1_2p_2_1000000000.wallet_key())
        self.assertEqual(master.subkey_for_path("0p/1/2p/2/1000000000.pub").wallet_key(),
                         pub_m0p1_1_2p_2_1000000000.wallet_key())

    def test_vector_2(self):
        master = BIP32Node.from_master_secret(h2b(
            "fffcf9f6f3f0edeae7e4e1dedbd8d5d2cfccc9c6c3c0bdbab7b4b1aeaba8a5a29f9c99"
            "9693908d8a8784817e7b7875726f6c696663605d5a5754514e4b484542"))
        self.assertEqual(
            master.wallet_key(as_private=True),
            "xprv9s21ZrQH143K31xYSDQpPDxsXRTUcvj2iNHm5NUtrGiGG5e2DtALGdso3pGz6ssrdK"
            "4PFmM8NSpSBHNqPqm55Qn3LqFtT2emdEXVYsCzC2U")

        self.assertEqual(
            master.wallet_key(),
            "xpub661MyMwAqRbcFW31YEwpkMuc5THy2PSt5bDMsktWQcFF8syAmRUapSCGu8ED9W6oDM"
            "Sgv6Zz8idoc4a6mr8BDzTJY47LJhkJ8UB7WEGuduB")

        m0 = master.subkey()
        self.assertEqual(
            m0.wallet_key(),
            "xpub69H7F5d8KSRgmmdJg2KhpAK8SR3DjMwAdkxj3ZuxV27CprR9LgpeyGmXUbC6wb7ERf"
            "vrnKZjXoUmmDznezpbZb7ap6r1D3tgFxHmwMkQTPH")
        self.assertEqual(
            m0.wallet_key(as_private=True),
            "xprv9vHkqa6EV4sPZHYqZznhT2NPtPCjKuDKGY38FBWLvgaDx45zo9WQRUT3dKYnjwih2y"
            "JD9mkrocEZXo1ex8G81dwSM1fwqWpWkeS3v86pgKt")
        pub_m0 = master.subkey(as_private=False)
        self.assertEqual(pub_m0.wallet_key(), m0.wallet_key())

        m0_2147483647p = m0.subkey(i=2147483647, is_hardened=True)
        self.assertEqual(
            m0_2147483647p.wallet_key(),
            "xpub6ASAVgeehLbnwdqV6UKMHVzgqAG8Gr6riv3Fxxpj8ksbH9ebxaEyBLZ85ySDhKiLDB"
            "rQSARLq1uNRts8RuJiHjaDMBU4Zn9h8LZNnBC5y4a")
        self.assertEqual(
            m0_2147483647p.wallet_key(as_private=True),
            "xprv9wSp6B7kry3Vj9m1zSnLvN3xH8RdsPP1Mh7fAaR7aRLcQMKTR2vidYEeEg2mUCTAwC"
            "d6vnxVrcjfy2kRgVsFawNzmjuHc2YmYRmagcEPdU9")
        pub_m0_2147483647p = m0.subkey(i=2147483647, is_hardened=True, as_private=False)
        self.assertEqual(pub_m0_2147483647p.wallet_key(), m0_2147483647p.wallet_key())

        m0_2147483647p_1 = m0_2147483647p.subkey(i=1)
        self.assertEqual(
            m0_2147483647p_1.wallet_key(),
            "xpub6DF8uhdarytz3FWdA8TvFSvvAh8dP3283MY7p2V4SeE2wyWmG5mg5EwVvmdMVCQcoN"
            "JxGoWaU9DCWh89LojfZ537wTfunKau47EL2dhHKon")
        self.assertEqual(
            m0_2147483647p_1.wallet_key(as_private=True),
            "xprv9zFnWC6h2cLgpmSA46vutJzBcfJ8yaJGg8cX1e5StJh45BBciYTRXSd25UEPVuesF9"
            "yog62tGAQtHjXajPPdbRCHuWS6T8XA2ECKADdw4Ef")
        pub_m0_2147483647p_1 = m0_2147483647p.subkey(i=1, as_private=False)
        self.assertEqual(pub_m0_2147483647p_1.wallet_key(), m0_2147483647p_1.wallet_key())
        pub_m0_2147483647p_1 = pub_m0_2147483647p.subkey(i=1, as_private=False)
        self.assertEqual(pub_m0_2147483647p_1.wallet_key(), m0_2147483647p_1.wallet_key())

        m0_2147483647p_1_2147483646p = m0_2147483647p_1.subkey(i=2147483646, is_hardened=True)
        self.assertEqual(
            m0_2147483647p_1_2147483646p.wallet_key(),
            "xpub6ERApfZwUNrhLCkDtcHTcxd75RbzS1ed54G1LkBUHQVHQKqhMkhgbmJbZRkrgZw4ko"
            "xb5JaHWkY4ALHY2grBGRjaDMzQLcgJvLJuZZvRcEL")
        self.assertEqual(
            m0_2147483647p_1_2147483646p.wallet_key(as_private=True),
            "xprvA1RpRA33e1JQ7ifknakTFpgNXPmW2YvmhqLQYMmrj4xJXXWYpDPS3xz7iAxn8L39nj"
            "GVyuoseXzU6rcxFLJ8HFsTjSyQbLYnMpCqE2VbFWc")
        pub_m0_2147483647p_1_2147483646p = m0_2147483647p_1.subkey(i=2147483646, as_private=False, is_hardened=True)
        self.assertEqual(pub_m0_2147483647p_1_2147483646p.wallet_key(), m0_2147483647p_1_2147483646p.wallet_key())

        m0_2147483647p_1_2147483646p_2 = m0_2147483647p_1_2147483646p.subkey(i=2)
        self.assertEqual(m0_2147483647p_1_2147483646p_2.wif(), "L3WAYNAZPxx1fr7KCz7GN9nD5qMBnNiqEJNJMU1z9MMaannAt4aK")
        self.assertEqual(
            m0_2147483647p_1_2147483646p_2.wallet_key(),
            "xpub6FnCn6nSzZAw5Tw7cgR9bi15UV96gLZhjDstkXXxvCLsUXBGXPdSnLFbdpq8p9HmGs"
            "ApME5hQTZ3emM2rnY5agb9rXpVGyy3bdW6EEgAtqt")
        self.assertEqual(
            m0_2147483647p_1_2147483646p_2.wallet_key(as_private=True),
            "xprvA2nrNbFZABcdryreWet9Ea4LvTJcGsqrMzxHx98MMrotbir7yrKCEXw7nadnHM8Dq3"
            "8EGfSh6dqA9QWTyefMLEcBYJUuekgW4BYPJcr9E7j")
        pub_m0_2147483647p_1_2147483646p_2 = m0_2147483647p_1_2147483646p.subkey(i=2, as_private=False)
        self.assertEqual(pub_m0_2147483647p_1_2147483646p_2.wallet_key(), m0_2147483647p_1_2147483646p_2.wallet_key())
        pub_m0_2147483647p_1_2147483646p_2 = pub_m0_2147483647p_1_2147483646p.subkey(i=2, as_private=False)
        self.assertEqual(pub_m0_2147483647p_1_2147483646p_2.wallet_key(), m0_2147483647p_1_2147483646p_2.wallet_key())
        self.assertEqual(master.subkey_for_path("0/2147483647p/1/2147483646p/2").wallet_key(),
                         m0_2147483647p_1_2147483646p_2.wallet_key())
        self.assertEqual(master.subkey_for_path("0/2147483647p/1/2147483646p/2.pub").wallet_key(),
                         pub_m0_2147483647p_1_2147483646p_2.wallet_key())

    def test_testnet(self):
        # WARNING: these values have not been verified independently. TODO: do so
        master = BIP32Node.from_master_secret(h2b("000102030405060708090a0b0c0d0e0f"), netcode='XTN')
        self.assertEqual(
            master.wallet_key(as_private=True),
            "tprv8ZgxMBicQKsPeDgjzdC36fs6bMjGApWDNLR9erAXMs5skhMv36j9MV5ecvfavji5kh"
            "qjWaWSFhN3YcCUUdiKH6isR4Pwy3U5y5egddBr16m")
        self.assertEqual(master.bitcoin_address(), "mkHGce7dctSxHgaWSSbmmrRWsZfzz7MxMk")
        self.assertEqual(master.wif(), "cVPXTF2TnozE1PenpP3x9huctiATZmp27T9Ue1d8nqLSExoPwfN5")

    def test_streams(self):
        m0 = BIP32Node.from_master_secret("foo bar baz".encode("utf8"))
        pm0 = m0.public_copy()
        self.assertEqual(m0.wallet_key(), pm0.wallet_key())
        m1 = m0.subkey()
        pm1 = pm0.subkey()
        for i in range(4):
            m = m1.subkey(i=i)
            pm = pm1.subkey(i=i)
            self.assertEqual(m.wallet_key(), pm.wallet_key())
            self.assertEqual(m.bitcoin_address(), pm.bitcoin_address())
            m2 = BIP32Node.from_wallet_key(m.wallet_key(as_private=True))
            m3 = m2.public_copy()
            self.assertEqual(m.wallet_key(as_private=True), m2.wallet_key(as_private=True))
            self.assertEqual(m.wallet_key(), m3.wallet_key())
            print(m.wallet_key(as_private=True))
            for j in range(2):
                k = m.subkey(i=j)
                k2 = BIP32Node.from_wallet_key(k.wallet_key(as_private=True))
                k3 = BIP32Node.from_wallet_key(k.wallet_key())
                k4 = k.public_copy()
                self.assertEqual(k.wallet_key(as_private=True), k2.wallet_key(as_private=True))
                self.assertEqual(k.wallet_key(), k2.wallet_key())
                self.assertEqual(k.wallet_key(), k3.wallet_key())
                self.assertEqual(k.wallet_key(), k4.wallet_key())
                print("   %s %s" % (k.bitcoin_address(), k.wif()))

    def test_public_subkey(self):
        my_prv = BIP32Node.from_master_secret(b"foo")
        uag = my_prv.subkey(i=0, is_hardened=True, as_private=True)
        self.assertEqual(None, uag.subkey(i=0, as_private=False).secret_exponent())

        with self.assertRaises(ValueError) as cm:
            my_prv.subkey(i=-1)

        err = cm.exception
        self.assertEqual(err.args, ("i can't be negative", ))

        for p in ('-1', '0/-1', '0H/-1'):
            with self.assertRaises(ValueError) as cm:
                my_prv.subkey_for_path(p)

            err = cm.exception
            self.assertEqual(err.args, ("i can't be negative", ))

        self.assertRaises(ValueError, list, my_prv.subkeys('-1'))
        self.assertRaises(ValueError, list, my_prv.subkeys('-1-0'))

    def test_repr(self):
        from pycoin.key import Key
        netcode = 'XTN'
        key = Key(secret_exponent=273, netcode=netcode)
        wallet = BIP32Node.from_master_secret(bytes(key.wif().encode('ascii')), netcode)

        address = wallet.address()
        pub_k = wallet.from_text(address)
        self.assertEqual(repr(pub_k),  '<myb5gZNXePNf2E2ksrjnHRFCwyuvt7oEay>')

        wif = wallet.wif()
        priv_k = wallet.from_text(wif)
        self.assertEqual(repr(priv_k),
                         'private_for <03ad094b1dc9fdce5d3648ca359b4e210a89d049532fdd39d9ccdd8ca393ac82f4>')

    def test_p2wpkh_in_p2sh(self):
        from pycoin.key import Key
        node = Key.from_text('ypub6XDth9u8DzXV1tcpDtoDKMf6kVMaVMn1juVWEesTshcX4zUVvfNgjPJLXrD9N7AdTLnbHFL64KmBn3SNaTe69iZYbYCqLCCNPZKbLz9niQ4')
        self.assertEqual(node.subkey(0).subkey(0).address(),
                         '35ohQTdNykjkF1Mn9nAVEFjupyAtsPAK1W')
        self.assertEqual(node.subkey(1).subkey(0).address(),
                         '3KaBTcviBLEJajTEMstsA2GWjYoPzPK7Y7')

    def test_p2wpkh_native(self):
        from pycoin.key import Key
        node = Key.from_text('zpub6nsHdRuY92FsMKdbn9BfjBCG6X8pyhCibNP6uDvpnw2cyrVhecvHRMa3Ne8kdJZxjxgwnpbHLkcR4bfnhHy6auHPJyDTQ3kianeuVLdkCYQ')
        self.assertEqual(node.subkey(0).subkey(0).address(),
                         'bc1q3g5tmkmlvxryhh843v4dz026avatc0zzr6h3af')
        self.assertEqual(node.subkey(1).subkey(0).address(),
                         'bc1qdy94n2q5qcp0kg7v9yzwe6wvfkhnvyzje7nx2p')

    def test_testnet(self):
        from pycoin.key import Key
        node = Key.from_text('tpubDEenJGgVMucDfF8qb3MdhJhiGVZ8P2DUzw8NBtNc4uWRPGqUNNmxqUR8M3c1KwN3yE3CFm8nMLQmZH47Q65RQmsSiLenXhxD42DSU1CWyiz')
        self.assertEqual(node.subkey(1).subkey(2).address(),
                         'mvq2eqwKs9LQdFNH6BKEhw11udKjqDjo5J')
        self.assertEqual(node.subkey(3).subkey(4).address(),
                         'mpAgWFoJM5HYCz4byuvaHBfP8taCFPVPR7')

    def test_p2wpkh_in_p2sh_testnet(self):
        from pycoin.key import Key
        node = Key.from_text('upub5FS3DrUQtjhPtXF9ckWB6wZVpW42bVU696FJKGohDu4KGTEkkxsAQNdkqU7ihyMKPCtPauBQ8EGN4zJWasC3TrTTdFhR9XyATvjeM5AHgrR')
        self.assertEqual(node.subkey(1).subkey(2).address(),
                         '2MuAxAoui1rKSr9Ugp2w5G5PbYjdFkuEo1x')
        self.assertEqual(node.subkey(3).subkey(4).address(),
                         '2NE2981iCZBoYgBynpSDWuqF8RWMuBVxdoL')

    def test_p2wpkh_native_testnet(self):
        from pycoin.key import Key
        node = Key.from_text('vpub5aHCMN33HjfXNzN9F3FkUVwr43DMj6FgjVbeAKgUWf9iS56RTGw5MaNdLi7jy49eZmJmP7eQYcA3m6CjWc3UduXfZr4ggipy6wfofB6xtaV')
        self.assertEqual(node.subkey(1).subkey(2).address(),
                         'tb1qweczj5ypy6x92e98f5leq8x3frrqdhp6yearkh')
        self.assertEqual(node.subkey(3).subkey(4).address(),
                         'tb1qpkwg0m8xtxg95gczglc4x04ccq52ns3ez74kq2')
if __name__ == '__main__':
    unittest.main()
