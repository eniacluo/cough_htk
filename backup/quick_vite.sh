searchPath=$1

find $searchPath -name "*.wav" > test_wav_list.scp
cat test_wav_list.scp | awk -F '.' '{print $1".wav "$1".mfc"}' > test_copy_list.scp
cat test_wav_list.scp | awk -F '.' '{print $1".mfc"}' > test_cough_list.scp
HCopy -T 1 -C hcopy.conf -S test_copy_list.scp 
#HVite -T 1 -w net.slf -S test_cough_list.scp -H hmm1/cough -H hmm0/speech -H hmm0/scream -i result -n 2 2 dict.txt hmmlist
HVite -T 1 -w net.slf -S test_cough_list.scp -H hmm1/zhiwei -H hmm1/maria -H hmm1/jose -H hmm1/yang -H hmm0/filler -i result dict.txt hmmlist

rm test_wav_list.scp test_copy_list.scp test_cough_list.scp