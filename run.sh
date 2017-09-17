# Retry if it failed
# https://unix.stackexchange.com/a/82602

n=0
until [ $n -ge 100 ]
do
	echo $n
	python league-finder.py && break  # substitute your command here
	n=$[$n+1]
	# sleep 15
done
