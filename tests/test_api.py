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
        c.add_prefix("medgen", "https://www.ncbi.nlm.nih.gov/medgen/")
        c.add_prefix("medgen.cid", "https://bioregistry.io/medgen.cid:")
        c = curies_processing.wrap(c)

        r1 = c.parse("GOC:CJM", strict=True)
        self.assertEqual("orcid", r1.prefix)
        self.assertEqual("0000-0002-6601-2165", r1.identifier)

        r2 = c.parse("NIFSTD:nlx_dys_20090602", strict=True)
        self.assertEqual("NLXDYS", r2.prefix)
        self.assertEqual("20090602", r2.identifier)

        # test normal medgen parsing
        r4 = c.parse("medgen:12345", strict=True)
        self.assertEqual("medgen", r4.prefix)
        self.assertEqual("12345", r4.identifier)

        # test remapping to UMLS
        r3 = c.parse("medgen:C123456", strict=True)
        self.assertEqual("umls", r3.prefix)
        self.assertEqual("C123456", r3.identifier)

        # test remapping to MEDGEN CID
        r5 = c.parse("medgen:CN970821", strict=True)
        self.assertEqual("medgen.cid", r5.prefix)
        self.assertEqual("CN970821", r5.identifier)
