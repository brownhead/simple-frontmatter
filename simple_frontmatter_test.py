import StringIO
import unittest

import simple_frontmatter

UNICODE_TEST_PONY = (
    u"TH\u0318E\u0344\u0309\u0356 \u0360P\u032f\u034d\u032dO\u031a\u200bN"
    u"\u0310Y\u0321"
)

SAMPLE_FILES = [
    {
        # The raw text of the file. This is using the automatic string
        # concatenation feature of Python. More info at
        # http://stackoverflow.com/a/10660443/1989056.
        "raw": (
            u"key1: value1\n"
            u"key2: value2\n"
            u"...\n"
            u"\n"
            u"Destruction."
        ),

        # The frontmatter the parser *should* pull out from the document above
        "frontmatter": {u"key1": u"value1", u"key2": u"value2"},

        # The content of the file the parser *should* pull out (the content is
        # everything but the frontmatter)
        "content": u"\nDestruction."
    },
    {
        "raw": u"",
        "frontmatter": None,
        "content": u""
    },
    {
        "raw": UNICODE_TEST_PONY,
        "frontmatter": None,
        "content": UNICODE_TEST_PONY
    }
]

class FrontmatterTestBase(object):
    def test_basic(self):
        self.run_frontmatter_test(SAMPLE_FILES[0])

    def test_empty(self):
        self.run_frontmatter_test(SAMPLE_FILES[1])

    def test_unicode(self):
        self.run_frontmatter_test(SAMPLE_FILES[2])


class TestLoads(FrontmatterTestBase, unittest.TestCase):
    def run_frontmatter_test(self, sample_file):
        frontmatter, content = simple_frontmatter.loads(sample_file["raw"])

        assert frontmatter == sample_file["frontmatter"]
        assert content == sample_file["content"]


class TestLoad(FrontmatterTestBase, unittest.TestCase):
    def run_frontmatter_test(self, sample_file):
        fake_file = StringIO.StringIO(sample_file["raw"])
        frontmatter, content = simple_frontmatter.load(fake_file)

        assert frontmatter == sample_file["frontmatter"]
        assert content == sample_file["content"]

if __name__ == "__main__":
    unittest.main()
