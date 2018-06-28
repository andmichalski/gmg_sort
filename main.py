import os
import subprocess


class SplitAscFiles:

    def get_map_ids(self):
        list_files = []
        for file in os.listdir(os.getcwd()):
            if file.endswith(".asc"):
                list_files.append(file)
        list_files_maps_id = ["-".join(filename.split("-")[:3]) for filename in list_files]
        list_maps_id = list(set(list_files_maps_id))
        return list_maps_id

    def create_folders(self, list_maps_ids):
        for map_id in list_maps_ids:
            os.makedirs(map_id)

    def move_files(self, list_maps_ids):
        for map in list_maps_ids:
            subprocess.call("move {0}-* {0}".format(map), shell=True)


if __name__ == "__main__":
    self = SplitAscFiles()
    list_maps_ids = SplitAscFiles.get_map_ids(self)
    SplitAscFiles.create_folders(self, list_maps_ids)
    SplitAscFiles.move_files(self, list_maps_ids)
