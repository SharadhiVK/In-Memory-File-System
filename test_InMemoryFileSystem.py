import unittest
from contextlib import redirect_stdout
import io
from InMemoryFileSystem import InMemoryFileSystem

class TestInMemoryFileSystem(unittest.TestCase):
    def setUp(self):
        self.file_system = InMemoryFileSystem()

    def test_ls(self):
        # Test ls command in the root directory
        result = io.StringIO()
        with redirect_stdout(result):
            self.file_system.ls("/")
        self.assertEqual(result.getvalue().strip(), "")

        # Test ls command in a non-existent directory
        result = io.StringIO()
        with redirect_stdout(result):
            self.file_system.ls("/nonexistent")
        self.assertEqual(result.getvalue().strip(), "")

        # Test ls command in the current directory
        result = io.StringIO()
        with redirect_stdout(result):
            self.file_system.ls()
        self.assertEqual(result.getvalue().strip(), "")

    def test_touch_and_cat(self):
        # Test touch and cat commands
        self.file_system.touch("/test_file.txt")
        self.file_system.echo("This is some content.", "/test_file.txt")

        result = io.StringIO()
        with redirect_stdout(result):
            self.file_system.cat("/test_file.txt")
        self.assertEqual(result.getvalue().strip(), "This is some content.")

    def test_echo_and_cat(self):
        # Test echo and cat commands
        self.file_system.echo("This is some content.", "/new_file.txt")

        result = io.StringIO()
        with redirect_stdout(result):
            self.file_system.cat("/new_file.txt")
        self.assertEqual(result.getvalue().strip(), "This is some content.")

    def test_grep(self):
        # Test grep command
        self.file_system.touch("/test_file.txt")
        self.file_system.echo("This is a test file.", "/test_file.txt")

        result = io.StringIO()
        with redirect_stdout(result):
            self.file_system.grep("test", "/test_file.txt")
        self.assertIn("This is a test file.", result.getvalue())

    def test_cp(self):
        # Test cp command
        self.file_system.touch("/source_file.txt")
        self.file_system.cp("/source_file.txt", "/destination_directory")

        result = io.StringIO()
        with redirect_stdout(result):
            self.file_system.ls("/destination_directory")
        self.assertIn("source_file.txt", result.getvalue())

    def test_mv(self):
        # Test mv command
        self.file_system.touch("/source_file.txt")
        self.file_system.mv("/source_file.txt", "/destination_directory")

        result_source = io.StringIO()
        result_destination = io.StringIO()

        with redirect_stdout(result_source):
            self.file_system.ls("/")
        with redirect_stdout(result_destination):
            self.file_system.ls("/destination_directory")

        self.assertNotIn("source_file.txt", result_source.getvalue())
        self.assertIn("source_file.txt", result_destination.getvalue())

    def test_rm(self):
        # Test rm command
        self.file_system.touch("/file_to_remove.txt")
        self.file_system.rm("/file_to_remove.txt")

        result = io.StringIO()
        with redirect_stdout(result):
            self.file_system.ls("/")
        self.assertNotIn("file_to_remove.txt", result.getvalue())

if __name__ == '__main__':
    unittest.main()
