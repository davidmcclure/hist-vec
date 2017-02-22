#!/usr/bin/env python


import click


@click.command()
@click.argument('slice_name')
@click.argument('out_path')
def train(slice_name, out_path):
    """Train a model on a historical slice.
    """
    pass


if __name__ == '__main__':
    train()
