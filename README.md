# TextToTable

A tool for transforming text to table using a model trained with [shirley-wu/text_to_table](https://github.com/shirley-wu/text_to_table).

It is a project for the assignment of *Fundations of Data Science* (90213102@NJU).

## How to use

First clone the project and open the project directory.

```bash
git clone https://github.com/wsq4/TextToTable.git
cd TextToTable
```

For preprocessing, we use `fairseq` for BPE and binarization. You need to first download a BART (bart.base) model [here](https://github.com/pytorch/fairseq/tree/main/examples/bart), our preprocessed dataset [here](https://drive.google.com/file/d/1ceUju9qJije9yYKwJcWztSP0O6fts2IA/view?usp=sharing) and our pretrained model [here](https://box.nju.edu.cn/f/794fbfa4ea8d4b85bd31/). Then extract and put them in the project directory.

Then use [pipenv](https://pypi.org/project/pipenv/) to create an virtual Python 3.7 environment and install dependencies.

```bash
pipenv --python 3.7
pipenv install
```

After that, you can enter the virtual environment to run the program.

```bash
pipenv shell
bash bash ./text-to-table.sh Input.txt ./output/
```