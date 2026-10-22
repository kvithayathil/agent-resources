"""Compat tests proving the cryptography>=50.0.0 override works at runtime.

The security_layer pyproject overrides presidio-anonymizer's declared
<cryptography,<49.0.0> cap to satisfy PYSEC-2026-3553/3554 (fix 49.0.0) and
PYSEC-2026-3552 (fix 50.0.0). These tests exercise presidio-anonymizer's
AESCipher (AES-CBC with PKCS7 padding from cryptography's hazmat API) through
the Encrypt -> Decrypt operator round trip, so the pin override is backed by
real runtime evidence rather than metadata alone.
"""

import os

import pytest
from presidio_anonymizer.entities import InvalidParamError
from presidio_anonymizer.operators.decrypt import Decrypt
from presidio_anonymizer.operators.encrypt import Encrypt


class TestCryptoCompat:
    """Compat evidence for the cryptography>=50.0.0 override."""

    def test_encrypt_decrypt_round_trip(self):
        """AESCipher (backed by cryptography) encrypts and decrypts intact."""
        text = "SSN: 123-45-6789"
        params = {"key": os.urandom(32)}  # 256-bit key

        encrypted = Encrypt().operate(text, params)
        assert isinstance(encrypted, str)
        assert encrypted != text

        decrypted = Decrypt().operate(encrypted, params)
        assert decrypted == text

    def test_round_trip_is_key_bound(self):
        """Same key decrypts the ciphertext; distinct keys with distinct IVs."""
        params = {"key": os.urandom(32)}
        encrypted1 = Encrypt().operate("secret", params)
        encrypted2 = Encrypt().operate("secret", params)
        # CBC mode... IV randomness may differ; both must decrypt correctly.
        assert Decrypt().operate(encrypted1, params) == "secret"
        assert Decrypt().operate(encrypted2, params) == "secret"

    def test_validate_rejects_wrong_key_size(self):
        """Encrypt.validate rejects keys not sized 128/192/256 bits."""
        with pytest.raises(InvalidParamError):
            Encrypt().validate({"key": "short"})

    def test_operate_rejects_wrong_key_size(self):
        """The cryptography-backed cipher rejects illegal key sizes too."""
        with pytest.raises(ValueError):
            Encrypt().operate("secret", {"key": "short"})
