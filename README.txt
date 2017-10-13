The Author of this entire package is Xiaohui Yan.  This version of
code has been comitted by me for reproducibility of results in some of 
my papers.

You can find the Xiaohui Yan's version here: https://github.com/xiaohuiyan

- Janani
--------------------------------------------------------------------------


Biterm Topic Model (BTM) is a topic model developed for short text
(need to set a window length when generating biterms for nomral text), 
like microblogs and webpage titles. It learns topics by modeling the
generation process of word co-occurrences (referred as biterms), rather
than word-document co-occurrences.

=== 1. Biterm Topic Model(BTM) ===
In BTM, the distribution of a biterm b=(w1,w2) is
   
       P(w1,w2) = \sum_k{P(w1|k)P(w2|k)P(k)}.

Steps of Gibbs algorithm for BTM:
1) Randomly assign topic uniformly to each biterm b
2) for each biterm b
   i) reset topic assignment of b
   ii) sample topic k according to P(k|B-b)
   iii) re-assign topic k to biterm b
3) looper step 2) until converge
4) inference the parameters {P(k), P(w|k)}

More detail is refered to the following paper:
[1] Xiaohui Yan, Jiafeng Guo, Yanyan Lan, Xueqi Cheng. A Biterm Topic Model For Short Text. WWW2013.

=== 2. Usage ===
Before running the code, just type "make" in "src/batch" directory 
to generate the executable file "btm".

1) Usage for estimation:
# ./btm est <K> <W> <alpha> <beta> <n_iter> <save_step> <pt_input> <pt_outdir>
	K	int, number of topics, like 20
	W	int, size of vocabulary
	alpha	double, Symmetric Dirichlet prior of P(z), like 1
	beta	double, Symmetric Dirichlet prior of P(w|z), like 0.01
	n_iter	int, number of iterations of Gibbs sampling
	save_step	int, steps to save the results
	pt_input	string, path of training docs
	pt_outdir	string, output directory

2) Usage for inference:
# ./btm inf <type> <K> <pt_input> <pt_outdir>
	K	int, number of topics, like 20
	type	 string, 4 choices:sum_w, sum_b, lda, mix. sum_b is used in our paper.
	pt_input	string, path of training docs
	pt_outdir	string, output directory

There are two scripts in "script/" to help you run a toy example in
"data" directory.

3) Results inspection
# python script/tran.py   
Output the topics with top 10 words of the topy example.

4) Overall Run
#./bat.sh
run a toy exapmle, including learning, inference, and inspection.


=== 3. Input & Output ===
1) Input
The input file contains all the training documents. Each line records
a short text doucment, and word indexes (starts from 0) seperated by
space. See the toy example in data/doc_wids.txt

2) Output
The estimation program will output into the directory "pt_ourdir":
  * pw_z.k20  a K*M matrix for P(w|z), if K=20
  * pz.k20   a K*1 matrix for P(z), if K=20
The inference program will produce:
  * pz_d.k20 a N*K matrix for P(z|d), if K=20

=== History ===
2013-8-28     Add online BTM. 
2013-6-1      Add the process of single word document Inference.
2013-5-6      add a doc_infer_sum_w inference procedure.
2013-5-5      v0.2, add Doc and Dataset class. We change the input
			  from biterms to word sequences. Example is the test/doc_wids.txt.
2012-09-25    v0.1

Feel free to contact: Xiaohui Yan(xhcloud@gmail.com)
