# CPA_DPA
## Correlational Power Analysis 
### Model Generation
Models based on each plaintext and key combonation must be generated in CPA. We include a script `model_gen.py` that does this automatically for 
ILA generated trace files. Simply pass the directory containing said traces and a directory to store the models and the script will make
a hamming weight model (`hamming_weight_model.npy`) and hamming distance model. (`hamming_distance_model.npy`)

`Usage: python model_gen.py trace_dir model_dir [optional initial plaintext]`
