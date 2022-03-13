# Task Tracking with Command Line Tools

## Project Overview
This project seeks to provide utilities for task tracking. Tasks are seperated by project. The core utilities of this project are:
 * Create tasks and store to project-specific to-do's
 * View / sort to-do lists, including user-provided task descriptions
 * Store completed tasks (with creation / completion dates) to project-specific dataframe, for easy future reference
    - Upon storage, tasks can additionally be flagged for importance if likely to be needed in the future

## Repository Structure
 * `/project`: Scripts which run necessary code for data build and model training.
 * `/src`: `ekg_scd` package, contains helpers and classes necessary for `/project` scripts.

## Package Installation
 To install the `ekg_scd` package:
 1. Clone this repository. 
 2. From the base directory, run `pip install .` from the command line.

## Current Maintainers
 * Jack Luby, UChicago Booth Center for Applied AI - john.luby@chicagobooth.edu
