echo "REALLY START[YES/NO]?"
read YES
if [ $YES = "YES" ]
then
    $SERVERDIR/initial
    ./resume.sh
fi
