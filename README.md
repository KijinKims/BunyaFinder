# BunyaFinder

## QuickStart

Requirement: Docker, conda(or miniconda)

```bash
git clone https://github.com/KijinKims/bunyafinder.git
cd BunyaFinder
conda env create -f environment.yml
conda activate bunyafinder
pip install bunyafinder-1.0.tar.gz
```

```bash
sh utils/docker_pull_list_of_images.sh docker_images.list
```

```bash
export BF_DB=/location/you/want/to/download/databases/for/bunyafinder
```

Default path is `$HOME/BF_DB`

```bash
BunyaFinder database download --db kraken2-bunyavirales refseq-bunyavirales pathogenoic-bunyavirales taxdump accession2taxid
BunyaFinder database build blast --in $BF_DB/refseq-bunyavirales/refseq-bunyavirales.fna --outdir $BF_DB/blast/refseq-bunyavirales --dbname refseq-bunyavirales --title refseq-bunyavirales --parse_seqids --dbtype nucl
BunyaFinder database build taxnomizr --outdir $BF_DB/taxonomizr
```

NOTE: The processes to build databases require comparable amount of memory. If your computer is not equipped with that amount of memory, the process will be killed. In that case, you need to look for pre-built database from another source.

```bash
mkdir tutorial && cd tutorial
fasterq-dump SRR13439799
esearch -db nucleotide -query "KJ942813.1" | efetch -format fasta > KJ942813_influenza_A.fasta 
```

```bash
#qc
BunyaFinder qc --platform nanopore -x SRR13439799_Sequecing_of_PR8_H1N1_culture_medium_1.fastq --prefix SRR13439799
#filter reads
BunyaFinder filter reads --platform nanopore -x SRR13439799_Sequecing_of_PR8_H1N1_culture_medium_1.fastq --prefix SRR13439799
#map
BunyaFinder map --platform nanopore -x SRR13439799/filter/SRR13439799.filtered.fastq --prefix SRR13439799 --ref KJ942813_influenza_A.fasta
#filter map
BunyaFinder filter map -x SRR13439799/map/SRR13439799.map.tsv --prefix SRR13439799
#taxonomic classification
BunyaFinder tax_classify --platform nanopore -x SRR13439799/filter/SRR13439799.filtered.fastq --prefix SRR13439799 
#assembly
BunyaFinder assembly --platform nanopore -x SRR13439799/filter/SRR13439799.filtered.fastq --prefix SRR13439799 --tool megahit
#filter contigs
BunyaFinder filter contigs -x SRR13439799/assembly/SRR13439799.contigs.fasta --prefix SRR13439799
#polish
BunyaFinder polish -x SRR13439799/assembly/SRR13439799.filtered_contigs.fasta --prefix SRR13439799 --reads SRR13439799_Sequecing_of_PR8_H1N1_culture_medium_1.fastq
#blast
BunyaFinder post_assembly blast -x SRR13439799/polish/SRR13439799.polished_contigs.fasta --prefix SRR13439799 --blast_db_dir $BF_DB/blast/
#filter blast
BunyaFinder filter blast -x SRR13439799/post_assembly/blast/SRR13439799.megablast.txt --prefix SRR13439799
#report blast
BunyaFinder report blast -x SRR13439799/post_assembly/blast/SRR13439799.megablast.filtered.txt --prefix SRR13439799 --taxonomizr_db $BF_DB/taxonomizr/accessionTaxa.sql
#zoonosis
BunyaFinder post_assembly zoonosis -x SRR13439799/polish/SRR13439799.polished_contigs.fasta --prefix SRR13439799
```



```bash
#post assembly all 
BunyaFinder post_assembly all -x SRR13439799/polish/SRR13439799.polished_contigs.fasta --prefix SRR13439799 --blast_db_dir $BF_DB/blast/refseq-viral --blast_db_name refseq-viral --taxonomizr_db $BF_DB/taxonomizr/accessionTaxa.sql
#end to end
BunyaFinder end_to_end --platform nanopore -x SRR13439799_Sequecing_of_PR8_H1N1_culture_medium_1.fastq --prefix SRR13439799
```

```bash
BunyaFinder consensus --platform nanopore -x SRR13439799_Sequecing_of_PR8_H1N1_culture_medium_1.fastq --prefix SRR13439799 --ref KJ942813_influenza_A.fasta
```