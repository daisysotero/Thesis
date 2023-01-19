conda creat --name predict
conda activate predict
conda install -c bioconda transdecoder
mkdir Evelu_transdecoder
TransDecoder.LongOrfs -t Transcript_17KEvelu.fasta &
TransDecoder.Predict -t Transcript_17KEvelu.fasta

