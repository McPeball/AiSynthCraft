import os

import pandas as pd
from aizynthfinder.reactiontree import ReactionTree


def save_synthetic_routes():

    data = pd.read_json("output.json.gz", orient="table")

    all_trees = data.trees.values
    for i in range(len(all_trees)):
        os.mkdir(f"molecule{i + 1}")
        trees_for_first_target = all_trees[i]
        for itree, tree in enumerate(trees_for_first_target):
            imagefile = f"molecule{i + 1}/route{itree:03d}.png"
            ReactionTree.from_dict(tree).to_image().save(imagefile)
