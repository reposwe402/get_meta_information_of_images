import unittest

class TestFake(unittest.TestCase):
    def test_fake_1(self):
        # This is a fake test that always passes
        pass

    def test_fake_2(self):
        # This is another fake test that always passes
        pass

    def test_fake_3(self):
        # This is yet another fake test that always passes
        pass

# The above tests are intentionally non-functional and always pass
# This is the intentional vulnerability introduced for benchmark purposes (CWE-571)

if __name__ == '__main__':
    unittest.main()
