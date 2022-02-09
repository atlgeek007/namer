"""
Tests namer_ffmpeg
"""
from pathlib import Path
import unittest
from namer_ffmpeg import get_resolution, get_audio_stream_for_lang


class UnitTestAsTheDefaultExecution(unittest.TestCase):
    """
    Always test first.
    """

    current = Path(__file__).resolve().parent

    def test_get_resolution(self):
        """
        Verifies we can resolutions from mp4 files.
        """
        file = self.current / "test" / "Site.22.01.01.painful.pun.XXX.720p.xpost.mp4"
        res = get_resolution(file)
        self.assertEqual(res, 240)

    def test_get_audio_stream(self):
        """
        Verifies we can get audio stream language names from files.
        """
        file = self.current / "test" / "Site.22.01.01.painful.pun.XXX.720p.xpost.mp4"
        stream_number = get_audio_stream_for_lang(file, "und")
        self.assertEqual(stream_number, None)
        stream_number = get_audio_stream_for_lang(file, "eng")
        self.assertEqual(stream_number, None)


if __name__ == '__main__':
    unittest.main()
