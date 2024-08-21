# The STRESS guidelines: a 1st review and update

 🏗 **WORK IN PROGRESS** (STRESS review and update 2024/25) 🏗️   

## Overview

A review and update of the Strengthening the Reporting of Empirical Simulation Studies guidelines for DES, SD, and ABS.  It aims to improve the STRESS reporting guidelines and provide additional support for Hybrid Simulation.

## Authors

[![ORCID: Monks](https://img.shields.io/badge/Tom_Monks_ORCID-0000--0003--2631--4481-brightgreen)](https://orcid.org/0000-0003-2631-4481)

To - do add FA, et al ORCID badges

## Funding

> TODO: Add in statement about FM funding from BS.


## Instructions to run the code

### To download code and run locally

#### Downloading the code

Either clone the repository using git or click on the green "code" button and select "Download Zip".

```bash
git clone https://github.com/pythonhealthdatascience/stress_update
```

> this assumes you have installed git and [setup SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

#### Installing dependencies

All dependencies can be found in [`environment.yml`]() and are pulled from conda-forge.  To run the code locally, we recommend installing [miniforge](https://github.com/conda-forge/miniforge).

> miniforge is FOSS alternative to Anaconda and miniconda that uses conda-forge as the default channel for packages. It installs both conda and mamba (a drop in replacement for conda) package managers.  We recommend mamba for faster resolving of dependencies and installation of packages. 

navigating your terminal (or cmd prompt) to the directory containing the repo and issuing the following command:

> if you are using conda then replace `mamba` with `conda`.

```
mamba env create -f environment.yml
```


Activate the mamba environment using the following command:

```
mamba activate stress
```

## Auto-formatting code in notebooks

The `stress` environment contains code linting and formatting tools: `nbqa`, `flake8` and `black`. Use `nbqa` and `black` to autoformat jupyter notebooks from a terminal or cmd prompt:

```bash
nbqa black notebooks/<insert-notebook-name>.ipynb
```

Use `flake8` to issue a report about code quality:

```bash
nbqa flake8 notebooks/<insert-notebook-name>.ipynb
```
> Some notes on linting code: https://www.pythonhealthdatascience.com/content/001_setup/prereq/05_pep8.html
