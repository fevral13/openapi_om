#!/usr/bin/env python3
import argparse
import importlib
import json
import sys

import yaml

FORMAT_JSON = "json"
FORMAT_YAML = "yaml"


def main() -> int:
    args_parser = _get_args_parser()
    args = args_parser.parse_args()

    try:
        func = args.func
    except AttributeError:
        print(args_parser.print_help())
        return exit(0)
    else:
        return func(args)


def _get_args_parser() -> argparse.ArgumentParser:
    args_parser = argparse.ArgumentParser(argument_default="export")
    subargs_parser = args_parser.add_subparsers(help="commands")

    command_export = subargs_parser.add_parser("export")
    command_export.set_defaults(func=_command_export)
    command_export.add_argument(
        "module",
        help="A python module with an OpenAPI schema. Looks for the openapi var in this module",
    )
    command_export.add_argument(
        "-f",
        "--format",
        help="File format to export to",
        choices=[FORMAT_JSON, FORMAT_YAML],
        dest="format",
    )
    command_export.add_argument(
        "-o",
        help="Output file name. If skipped, stdout is used",
        dest="output",
    )
    return args_parser


def _command_export(args):
    imported_module = importlib.import_module(args.module)
    openapi = imported_module.openapi
    schema_dict = json.loads(openapi.json(exclude_none=True, by_alias=True))

    if args.format == FORMAT_JSON:
        json.dump(schema_dict, sys.stdout)
    elif args.format == FORMAT_YAML:
        yaml.dump(schema_dict, sys.stdout)
    sys.stdout.flush()
