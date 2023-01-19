source ~/anaconda3/bin/activate
conda activate genes
yes | conda install busco=4.1.3
wget https://busco-data.ezlab.org/v4/data/lineages/viridiplantae_odb10.2020-09-10.tar.gz
tar -xzvf viridiplantae_odb10.2020-09-10.tar.gz
busco -m protein -i results.fasta -l viridiplantae_odb10/ -o results_busco_Evelu 1>saida.busco.1.txt
tail -f saida.busco.1.txt
generate_plot.py -wd results_busco_Evelu/
