#!/usr/bin/env python3
"""Display contents of list."""

# TODO: maybe color flagged items?

# base imports
import argparse
import json

import pandas as pd

from .helpers.helpers import (
    check_init,
    data_path,
    define_idx,
    pkg_path,
    print_description,
    print_entries,
)

check_init()

# establish parameters
templates = json.load(open(f"{pkg_path}/helpers/templates.json"))
project_list = json.load(open(f"{data_path}/project_list.json", "r"))
hidden_list = json.load(open(f"{data_path}/hidden_project_list.json", "r"))
project_list = [p for p in project_list if p not in hidden_list]
lists = ["notes", "note", "tasks", "task", "refs", "ref"]


def main():
    # establish parser to pull in projects to view
    parser = argparse.ArgumentParser(description="Input project to view.")
    parser.add_argument(
        "ref_proj",
        type=str,
        nargs="?",
        default="ALL",
        choices=project_list + ["ALL"],
        help="Projects to display.",
    )
    parser.add_argument(
        "file",
        type=str,
        nargs="?",
        default="tasks",
        choices=lists,
        help="List to display within project.",
    )
    parser.add_argument(
        "pos",
        type=str,
        nargs="?",
        help="Position of item within list for which to display description.",
    )
    parser.add_argument(
        "-flagged",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="If provided, list only flagged entries.",
    )
    parser.add_argument(
        "-arc",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="If provided, show archives.",
    )
    d = vars(parser.parse_args())

    if d["pos"] and d["ref_proj"] == "ALL":
        raise ValueError(
            f"\n\tUse of 'pos' kwarg requires specification of a single project."
        )
    if d["pos"] not in [None, "HEAD", "TAIL"] + [str(i) for i in range(100)]:
        raise ValueError(
            f"\n\t'pos' must be one of 'HEAD', 'TAIL', 0, or a positive integer less than 100."
        )
    if len(project_list) == 0:
        raise ValueError(
            f"\n\tNo projects created.\n\tTo create a new directory, run {templates['add_template']}."
        )
    elif d["ref_proj"] not in project_list and d["ref_proj"] != "ALL":
        raise ValueError(
            f"\n\t'{d['ref_proj']}' is not a valid project.\n\tAvailable projects are {project_list} or you may enter 'ALL' to see all projects.\n\tTo create a new project directory, run {templates['add_template']}."
        )

    if d["file"][-1] != "s":
        d["file"] += "s"
    if d["arc"] == True:
        d["file"] = f"archives/{d['file']}"

    if d["ref_proj"] == "ALL":
        for proj in project_list:
            df = pd.read_csv(f"{data_path}/projects/{proj}/{d['file']}.csv")
            print("\n" + proj)
            print_entries(df, file=d["file"])
        print("")
    else:
        df = pd.read_csv(
            f"{data_path}/projects/{d['ref_proj']}/{d['file']}.csv"
        )
        if d["pos"] is None:
            print_entries(df, file=d["file"])
        else:
            idx = define_idx(d["pos"])
            if idx not in list(df.index):
                raise ValueError(
                    f"\n\tProvided index not found in project '{d['ref_proj']}' file '{d['file']}'.\n\tTo view file contents, run {templates['list_proj_and_type']}."
                )
            else:
                print_description(df.iloc[idx])


if __name__ == "__main__":
    main()
