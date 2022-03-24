
import grid
import json

with open('config.json') as json_file:
    config = json.load(json_file)


if __name__ == "__main__":
    grid.grid_class(config['grid_size']).start()