import argparse
import json


def get_required_metadata(json_file):
    with open(json_file) as js:
        data = json.load(js)

        all_results = []
        for i in range(len(data[:])):
            info_applicable_to_chemists = {
                "smiles": "",
                "in_stock": "",
                "reaction_smiles": "",
                "score": "",
                "precursors": [],
                "number of pre-cursors in stock": "",
            }

            target_smiles = data[i]["smiles"]
            info_applicable_to_chemists["smiles"] = target_smiles

            target_in_stock = data[i]["in_stock"]
            info_applicable_to_chemists["in_stock"] = target_in_stock

            rxn_smiles = data[i]["children"][0]["smiles"]
            info_applicable_to_chemists["reaction_smiles"] = rxn_smiles

            reaction_score = data[i]["scores"]["state score"]
            info_applicable_to_chemists["score"] = reaction_score

            precursors_in_stock = data[i]["scores"][
                "number of pre-cursors in stock"
            ]
            info_applicable_to_chemists["number of pre-cursors in stock"] = (
                precursors_in_stock
            )

            # TODO: There are some reactions that resulted in 3 precursors, but script currently only outputs 2.
            precursor_info = data[i]["children"][0]["children"]
            for info in precursor_info:
                info_applicable_to_chemists["precursors"].append(
                    info["smiles"]
                )

            if info_applicable_to_chemists not in all_results:
                all_results.append(info_applicable_to_chemists)

        return all_results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="input JSON file (E.g. trees.json)",
    )
    args = parser.parse_args()

    all_results = get_required_metadata(args.input)
    print(*all_results, sep='\n]')
