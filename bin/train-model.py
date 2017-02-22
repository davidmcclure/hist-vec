#!/usr/bin/env python


import click

from hist_vec.corpus import Corpus


@click.command()
@click.argument('slice_name')
@click.argument('out_path')
def train(slice_name, out_path):
    """Train a model on a historical slice.
    """
    corpus = Corpus.from_env()

    model = corpus.word2vec_model(slice_name)
    model.save(out_path)


if __name__ == '__main__':
    train()
