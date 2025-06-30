# Public Review: *The chromosomal genome sequence of Aplysina aerophoba (Nardo, 1833) and its associated microbial metagenome sequences*

**Reviewed by**:
Darrin T. Schultz, PhD
Postdoctoral Scholar
University of Vienna
**Date**: June 30th, 2025

📄 **Online Version available at**:

---

## Statement

Thank you for the invitation and opportunity to review this manuscript. I
appreciate the authors’ efforts in sequencing and annotating the genome of
*Aplysina aerophoba*, as well as its associated metagenome. As I have written
for my previous sponge genome reviews, sponge biodiversity remains
underrepresented in chromosome-scale genomic resources, so it’s exciting to see
this high-quality assembly made available.

---

## Manuscript Review

This manuscript presents the sequencing, assembly, and annotation of a
marine sponge, *Aplysina aerophoba*, and its symbionts, as part of the
[Aquatic Symbiosis Genomics Project](https://doi.org/10.12688/wellcomeopenres.17021.1) (McKenna et al.
2021).

### Comments

- The Background contains a good general overview of the species' habitat, biology, and some historical context of research on the species.
- The sentence, "While not fully phased, the assembly deposited is of one haplotype." is a little confusing. If a genome isn't phased, there are likely haplotype switches in the assembly, and the contigs may not represent a single haplotype. It would be more clear to say what parameters were used to generate the assembly with hifiasm (e.g., whether Hi-C reads from the same individual were also used), and which specific file from hifiasm was used for the rest of the assembly. Currenly there isn't information on this in the manuscript. Making these changes will make it more clear whether the assembly has contigs that have been phased by hifiasm or not.
- Sample acquisition and nucleic acid extraction: The sample collection information is clear, but it would be helpful to include a statement on what collection permit was used for the sample collection, or that no permit was required if so.
- The molecular methods section is clear and well-organized.
- Genome assembly and curation: As I mentioned above, more details about specific parameters used for the genome assembly process would be helpful.

---

## Genome Assembly Review

## General Assembly Comments

- I generated Hi-C heatmaps for the assembly using the provided Hi-C reads.
  Overall, the assembly is of good quality, but there are some systematic errors
  that would be good to address, as they may lead to misinterpretation if left
  as-is.
- One recurring issue involves overlapping ends between adjacent contigs within
  scaffolds. I identified around 40 cases in this assembly using Hi-C data.
  These overlaps can create the false appearance of tandem duplications,
  especially if protein-coding genes are present in the overlapping regions. In
  my experience, this is a common artifact in assemblies generated with hifiasm.

To illustrate the problem:

```

Contigs are laid out like this onto a scaffold: A-B-C-D

An example of overlapping contig ends:

                A+B overlap here
                vv
contig A: aaaaaaXY
contig B:       XYbbbbbb
contig C:               cccccccc
contig D:                       dddddddd
                        ^       ^
                        There are no overlaps between B, C, and D.

The resulting scaffold would look like this, where the XY portion would occur twice:

scaffold sequence: aaaaaaXYXYbbbbbbbcccccccccdddddddd

```

- In this example, the end of contig A overlaps with the beginning of contig B,
  while B, C, do not have overlapping sequences.
- I recommend trimming the contig ends involved. Contig-to-contig alignments
  could help identify the precise cutoff points.
- I am attaching screenshots from the Juicebox session that shows which contigs
  have overlapping ends. The screenshots are organized by chromosome, and the
  contigs are in the order they appear in the assembly FASTA file. The coordinates will
  be on the right-hand-side of the screenshots.

This section includes screenshots from Juicebox.
- **Blue lines**: scaffold boundaries
- **Green lines**: contig boundaries
- **Black highlights**: regions of interest

![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.13.36 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.13.59 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.14.16 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.14.25 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.14.29 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.14.36 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.15.08 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.15.35 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.15.45 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.16.01 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.16.29 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.16.37 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.16.44 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.16.57 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.17.20 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.17.25 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.17.29 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.17.43 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.17.52 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.18.17 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.18.21 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.18.24 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.19.16 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.19.18 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.19.22 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.19.30 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.19.37 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.20.01 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.20.16 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.20.19 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.20.24 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.20.36 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.20.45 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.20.52 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.21.11 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.21.18 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.21.27 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.21.34 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.21.41 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.21.56 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.22.02 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.22.18 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.22.26 AM.png>)
![alt text](<trimmed_aplysina_screenshots/Screenshot 2025-06-30 at 11.22.35 AM.png>)


## Materials and Methods

- **Hi-C reads used**: `ERR11040157` and `ERR11040158` (from this project)
- **Assembly fasta used**: [ENA FASTA link](https://www.ebi.ac.uk/ena/browser/api/fasta/links/study?accession=PRJEB60858&result=sequence)

**Pipeline overview**:
Hi-C reads were mapped to the assembly using **Chromap v0.2.7-r494** (Zhang et al. 2021) with quality cutoffs of both 0 and 1.  
- Cutoff `0`: includes multi-mapping reads (useful for identifying haplotigs and repeats)  
- Cutoff `1`: filters multi-mapping reads

The resulting `.pairs` file was:
1. Gzipped
2. Converted to `.longp` format for use with **3D-DNA**
3. Transformed into a `.hic` file with the `run-assembly-visualizer.sh` script (Dudchenko et al. 2018)
4. Manually inspected using Juicebox Assembly Tools

### Helpful Links
- 🔧 [Script to generate `.assembly` file](https://github.com/conchoecia/genome_assembly_pipelines/blob/master/bin/assembly-from-fasta.py)
- 🐍 [Snakemake pipeline for editable Hi-C heatmap](https://github.com/conchoecia/genome_assembly_pipelines/blob/master/snakefiles/GAP_hic_map7_genomeReview)
- 🛠 [Example config file](https://github.com/conchoecia/genome_assembly_pipelines/blob/master/example_configs/config_GAP_hic_map7_genomeReview.yaml)


## References

- Bredeson, Jessen V. *Artisanal - Assembly Review Tools, Including Sequence Analysis’N Annotation Liftover.* [Bitbucket](https://bitbucket.org/bredeson/artisanal/src/master/).
- Dudchenko, O., et al. 2017. “De Novo Assembly of the Aedes Aegypti Genome Using Hi-C Yields Chromosome-Length Scaffolds.” *Science*, 356(6333): 92–95.
- Dudchenko, O., et al. 2018. “The Juicebox Assembly Tools Module Facilitates de Novo Assembly…” *bioRxiv*. https://doi.org/10.1101/254797.
- McKenna, V., et al. 2021. “The Aquatic Symbiosis Genomics Project…” *Wellcome Open Research*, 6:254.
- Open2C, et al. 2023. “Pairtools: From Sequencing Data to Chromosome Contacts.” *bioRxiv*. https://doi.org/10.1101/2023.02.13.528389.
- Zhang, H., et al. 2021. “Fast Alignment and Preprocessing of Chromatin Profiles with Chromap.” *Nature Communications*, 12(1): 1–6.