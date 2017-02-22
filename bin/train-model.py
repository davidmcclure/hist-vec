#!/usr/bin/env python


import click
import logging

from hist_vec.corpus import Corpus


logging.basicConfig(level=logging.INFO)


@click.command()
@click.argument('corpus_dir')
@click.argument('slice_name')
@click.argument('out_path')
def train(corpus_dir, slice_name, out_path):
    """Train a model on a historical slice.
    """
    corpus = Corpus(corpus_dir)

    model = corpus.word2vec_model(slice_name)
    model.save(out_path)


if __name__ == '__main__':
    train()
