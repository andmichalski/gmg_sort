import os
import shutil
import unittest

from main import SplitAscFiles


class TestsOnFiles(unittest.TestCase):

    def setUp(self):
        self.split = SplitAscFiles()
        for i in range(3):
            for j in range(3):
                f = open("N-34-{}-{}.asc".format(i, j), "w+")
                f.close()

    def tearDown(self):
        try:
            for map in ['N-34-2', 'N-34-1', 'N-34-0']:
                shutil.rmtree(os.getcwd() + "/" + map)
        except:
            pass
        try:
            for file in os.listdir(os.getcwd()):
                if file.endswith(".asc"):
                    os.remove(file)
        except:
            pass

    def test_should_get_correct_list(self):
        self.assertEqual(['N-34-2', 'N-34-1', 'N-34-0'], SplitAscFiles.get_map_ids(self.split))

    def test_should_create_correct_list_of_folders(self):
        maps_id_list = ['N-34-2', 'N-34-1', 'N-34-0']
        SplitAscFiles.create_folders(self.split, maps_id_list)
        self.assertTrue(os.path.exists(os.getcwd() + "/" + maps_id_list[0]))
        self.assertTrue(os.path.exists(os.getcwd() + "/" + maps_id_list[1]))
        self.assertTrue(os.path.exists(os.getcwd() + "/" + maps_id_list[2]))

    def test_files_should_be_in_corect_folders(self):
        maps_id_list = ['N-34-2', 'N-34-1', 'N-34-0']
        SplitAscFiles.create_folders(self.split, maps_id_list)
        SplitAscFiles.move_files(self.split, maps_id_list)
        self.assertTrue(os.path.exists(os.getcwd() + "/N-34-0/N-34-0-0.asc"))

    def test_similar_filenames_should_be_in_diffrent_folders(self):
        maps_id_list = ['N-34-3', 'N-34-30']
        f = open("N-34-3-1.asc", "w+")
        f.close()
        f = open("N-34-30-1.asc", "w+")
        f.close()
        SplitAscFiles.create_folders(self.split, maps_id_list)
        SplitAscFiles.move_files(self.split, maps_id_list)
        self.assertTrue(os.path.exists(os.getcwd() + "/N-34-3/N-34-3-1.asc"))
        self.assertTrue(os.path.exists(os.getcwd() + "/N-34-30/N-34-30-1.asc"))
        shutil.rmtree(os.getcwd() + "/N-34-3")
        shutil.rmtree(os.getcwd() + "/N-34-30")