#!/bin/bash

DATA_BINS=rotowire-bins/
PRETRAINED_MODEL=text-to-table.pt
INPUT_FILE=$1
OUTPUT_FOLDER=$2

bash scripts/preprocess/preprocess.sh $INPUT_FILE

fairseq-interactive $DATA_BINS --path $PRETRAINED_MODEL --beam 5 --remove-bpe --buffer-size 512 --max-tokens 2048 --max-len-b 1024 --user-dir src/ --task text_to_table_task  --table-max-columns 38 > ${INPUT_FILE}.table < ${INPUT_FILE}.bpe

bash scripts/eval/convert_fairseq_output_to_text.sh ${INPUT_FILE}.table

python scripts/excel/table_to_excel.py ${INPUT_FILE}.table.text ${OUTPUT_FOLDER}