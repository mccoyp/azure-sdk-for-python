#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# This script is used to execute pylint within a tox environment. Depending on which package is being executed against,
# a failure may be suppressed.

from subprocess import check_call, CalledProcessError
import argparse
import os
import logging
from prep_sphinx_env import should_build_docs
from run_sphinx_apidoc import is_mgmt_package
import os
import shutil

from ci_tools.parsing import ParsedSetup
from ci_tools.variables import in_analyze_weekly

logging.getLogger().setLevel(logging.INFO)

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..", ".."))
ci_doc_dir = os.path.join(root_dir, '_docs')
sphinx_conf_dir = os.path.join(root_dir, 'doc/sphinx')

def in_ci():
    return os.getenv('TF_BUILD', False)

def move_output_and_compress(target_dir, package_dir, package_name):
    if not os.path.exists(ci_doc_dir):
        os.mkdir(ci_doc_dir)

    individual_zip_location = os.path.join(ci_doc_dir, package_name, package_name)
    shutil.make_archive(individual_zip_location, 'gztar', target_dir)

def sphinx_build(target_dir, output_dir, fail_on_warning):
    command_array = [
                "sphinx-build",
                "-b",
                "html",
                "-A",
                "include_index_link=True",
                "-c",
                sphinx_conf_dir,
                target_dir,
                output_dir
            ]
    if fail_on_warning:
        command_array.append("-W")
        command_array.append("--keep-going")

    try:
        logging.info("Sphinx build command: {}".format(command_array))
        check_call(
            command_array
        )
    except CalledProcessError as e:
        logging.error(
            "sphinx-build failed for path {} exited with error {}".format(
                args.working_directory, e.returncode
            )
        )
        if in_analyze_weekly():
            from gh_tools.vnext_issue_creator import create_vnext_issue
            create_vnext_issue(args.package_root, "sphinx")
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run sphinx-build against target folder. Zips and moves resulting files to a root location as well."
    )

    parser.add_argument(
        "-w",
        "--workingdir",
        dest="working_directory",
        help="The unzipped package directory on disk. Usually {distdir}/unzipped/",
        required=True,
    )

    parser.add_argument(
        "-o",
        "--outputdir",
        dest="output_directory",
        help="The output location for the generated site. Usually {distdir}/site",
        required=True,
    )

    parser.add_argument(
        "-r",
        "--root",
        dest="package_root",
        help="",
        required=True,
    )

    parser.add_argument(
        "--inci",
        dest="in_ci",
        action="store_true",
        default=False
    )

    args = parser.parse_args()

    output_dir = os.path.abspath(args.output_directory)
    target_dir = os.path.abspath(args.working_directory)
    package_dir = os.path.abspath(args.package_root)

    pkg_details = ParsedSetup.from_path(package_dir)

    if should_build_docs(pkg_details.name):
        # Only data-plane libraries run strict sphinx at the moment
        fail_on_warning = not is_mgmt_package(pkg_details.name)
        sphinx_build(
            target_dir,
            output_dir,
            fail_on_warning=fail_on_warning,
        )

        if in_ci() or args.in_ci:
            move_output_and_compress(output_dir, package_dir, pkg_details.name)
            if in_analyze_weekly():
                from gh_tools.vnext_issue_creator import close_vnext_issue
                close_vnext_issue(pkg_details.name, "sphinx")

    else:
        logging.info("Skipping sphinx build for {}".format(pkg_details.name))
