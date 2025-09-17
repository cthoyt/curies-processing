"""Test the API."""

import unittest

import curies

import curies_processing


class TestAPI(unittest.TestCase):
    """Test the API."""

    def test_wrap(self) -> None:
        """Test wrapping a converter."""
        c = curies.get_obo_converter()
        c.add_prefix("NLXDYS", "http://uri.neuinfo.org/nif/nifstd/nlx_dys_")
        c.add_prefix("smid", "https://smid-db.org/detail/")
        c = curies_processing.wrap(c)

        r1 = c.parse("GOC:CJM", strict=True)
        self.assertEqual("orcid", r1.prefix)
        self.assertEqual("0000-0002-6601-2165", r1.identifier)

        r2 = c.parse("NIFSTD:nlx_dys_20090602", strict=True)
        self.assertEqual("NLXDYS", r2.prefix)
        self.assertEqual("20090602", r2.identifier)

        # test processing suffix
        r3 = c.parse("smid:bhos%2322%0D")
        self.assertEqual("smid", r3.prefix)
        self.assertEqual("bhos%2322", r3.identifier)
