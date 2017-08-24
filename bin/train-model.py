#!/usr/bin/env python


import click
import logging
import os
import math

from shutil import copyfile

from hist_vec.utils import scan_paths
from hist_vec.corpus import BPOCorpus, BookCorpus


logging.basicConfig(level=logging.INFO)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('corpus_dir')
@click.argument('model_dir')
def train_bpo(corpus_dir, model_dir):
    """Train a model on a historical slice.
    """
    corpus = BPOCorpus(corpus_dir)

    for name in corpus.slice_names():

        print(name)

        model = corpus.word2vec_model(name)

        path = os.path.join(model_dir, name+'.bin')
        model.save(path)


@cli.command()
@click.argument('corpus_dir')
@click.argument('model_dir')
def train_criticism(corpus_dir, model_dir):
    """Train a model on a historical slice.
    """
    corpus = BookCorpus(corpus_dir)

    for name in corpus.slice_names():

        print(name)

        model = corpus.word2vec_model(name)

        path = os.path.join(model_dir, name+'.bin')
        model.save(path)


@cli.command()
@click.argument('raw_dir')
@click.argument('out_dir')
def slice_criticism(raw_dir, out_dir):
    """Break criticism into year slices.
    """
    os.makedirs(out_dir, exist_ok=True)

    for path in scan_paths(raw_dir, '\.txt'):

        file_name = os.path.basename(path)

        year = int(file_name[:4])
        slice_name = str(math.floor(year / 20) * 20)

        slice_dir = os.path.join(out_dir, slice_name)
        os.makedirs(slice_dir, exist_ok=True)

        slice_path = os.path.join(slice_dir, file_name)
        copyfile(path, slice_path)


if __name__ == '__main__':
    cli()
