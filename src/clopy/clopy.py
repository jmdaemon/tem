from clopy.tmpl import CLOPY_CONFIG_DIR
import argparse
import wora.dynmod
import wora.file
import json
import pathlib

def main():
    parser = argparse.ArgumentParser(description='An all purpose templating program to quickly start projects off with a bang')
    parser.add_argument('fp', type=str, help='Filepath to template directory')
    parser.add_argument('cmd', type=str, help='Commands to use are: init, new [default: init]')

    args = parser.parse_args()
    fp = args.fp
    cmd = args.cmd if args.cmd else "init"

    cfg = wora.file.read_file(pathlib.Path(f'{CLOPY_CONFIG_DIR}/templates.json'))
    if (cfg is not None):
        o = json.loads(cfg)
        for name, tmplfp in o['templates'].items():
            if fp == name:
                fp = pathlib.Path(tmplfp).expanduser()
                break

    template = wora.dynmod.module_from_file("template", f'{fp}/template.py')
    template.bang(fp, cmd)
