#!/bin/bash

P=`pwd`/scripts/multiprocessing_bpe_encoder.py

BART_DIR=bart.base
SOURCE=$1

wget -N 'https://dl.fbaipublicfiles.com/fairseq/gpt2_bpe/encoder.json'
wget -N 'https://dl.fbaipublicfiles.com/fairseq/gpt2_bpe/vocab.bpe'

python $P \
    --encoder-json encoder.json \
    --vocab-bpe vocab.bpe \
    --inputs "$SOURCE" \
    --outputs "$SOURCE.bpe" \
    --workers 60 \
    --keep-empty;