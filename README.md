<a target="_blank" href="https://colab.research.google.com/drive/1FbT2rQHYT67NNHCrGw4t0WMEHCY9lqR2?usp=sharing">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

# TMbed - Transmembrane proteins predicted through Language Model embeddings

⚠️ **This is the deployment branch of the biocentral TMbed fork!** ⚠️

TMbed predicts transmembrane beta barrel and alpha helical proteins, the position and orientation of their transmembrane segments, and signal peptides.
We use a Protein Language Model, [ProtT5-XL-U50](https://github.com/agemagician/ProtTrans) [1], to generate embeddings used as input for our method.

Pre-Print: [bioRxiv](https://doi.org/10.1101/2022.06.12.495804)\
Publication: [BMC Bioinformatics](https://doi.org/10.1186/s12859-022-04873-x)

TMbed is also available via [bio_embeddings](https://github.com/sacdallago/bio_embeddings) and [LambdaPP](https://embed.predictprotein.org/) [2].\
Or you can try out TMbed using [Google Colab](https://colab.research.google.com/drive/1FbT2rQHYT67NNHCrGw4t0WMEHCY9lqR2?usp=sharing).

Visit [TMVisDB](https://tmvisdb.predictprotein.org) [3] to see precomputed predictions for AlphaFold DB [4] structures.

## Deployment branch

**This is a deployment branch for TMbed, 
created primarily for usage in [biocentral](https://github.com/biocentral/biocentral_server/).** 

*Kept API files:*
- `tmbed/viterbi.py` - Contains the Decoder


## References

[1] Elnaggar A, Heinzinger M, Dallago C, Rihawi G, Wang Y, Jones L, Gibbs T, Feher T, Angerer C, Bhowmik D, Rost B (2021). ProtTrans: Towards Cracking the Language of Lifes Code Through Self-Supervised Deep Learning and High Performance Computing. IEEE Transactions on Pattern Analysis and Machine Intelligence. doi: 10.1109/TPAMI.2021.3095381.

[2] Olenyi T, Marquet C, Heinzinger M, Kröger B, Nikolova T, Bernhofer M, Sändig P, Schütze K, Littmann M, Mirdita M, Steinegger M, Dallago C, Rost B (2023). LambdaPP: Fast and accessible protein-specific phenotype predictions. Protein Sci, 32, 1:e4524.

[3] Olenyi T, Marquet C, Grekova A, Houri L, Heinzinger M, Dallago C, Rost B (2024). TMVisDB: Annotation and 3D-visualization of transmembrane proteins. bioRxiv, 2024.11.22.624323.

[4] Varadi M, Anyango S, Deshpande M, Nair S, Natassia C, Yordanova G, Yuan D, Stroe O, Wood G, Laydon A, Zidek A, Green T, Tunyasuvunakool K, Petersen S, Jumper J, Clancy E, Green R, Vora A, Lutfi M, Figurnov M, Cowie A, Hobbs N, Kohli P, Kleywegt G, Birney E, Hassabis D, Velankar S (2022). AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models. Nucleic Acids Res, 50, D1:D439-D444.
