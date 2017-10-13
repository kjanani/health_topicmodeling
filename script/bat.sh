#!/bin/bash
# NOTICE: prepare doc_pt
#  mkdir lda/stat lda/mat lda/res 

k=20
W=16856

alpha=`echo "scale=3;50/$k"|bc`
beta=0.01
niter=500
save_step=101

data_dir=../data
doc_pt=${data_dir}/doc_wids.txt
doc_infer_pt=${doc_pt}
res_dir=${data_dir}${method}/mat/

# learning parameters p(z) and p(z|w)
../batch/btm est $k $W $alpha $beta $niter $save_step $doc_pt $res_dir

# infer p(z|d) for each doc
../batch/btm inf sum_b $k $doc_infer_pt ${res_dir}

# output top words of each topic
echo "===== disp top words of topics ===="
python tran.py $k
