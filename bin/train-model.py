#!/usr/bin/env python


import click
import logging
import os

from hist_vec.corpus import Corpus


logging.basicConfig(level=logging.INFO)


@click.command()
@click.argument('corpus_dir')
@click.argument('model_dir')
def train(corpus_dir, model_dir):
    """Train a model on a historical slice.
    """
    corpus = Corpus(corpus_dir)

    for name in corpus.slice_names():

        print(name)

        model = corpus.word2vec_model(name)

        path = os.path.join(model_dir, name+'.bin')
        model.save(path)


if __name__ == '__main__':
    train()
