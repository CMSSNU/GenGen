EXT="xz"
#EXT="tgz"
#EXT="tar.xz"
#ARR_TAR=( $(ls *".${EXT}") )
ARR_TAR="ChargedHiggsToCB_M080_tarball.tar.xz"
#ARR_TAR="ChargedHiggsToCB_M100_tarball.tar.xz"


for gridpack in ${ARR_TAR[@]};do
  echo "@@TEST "${gridpack}"@@"
  TESTDIR=test_${gridpack%".${EXT}"}
  if [ -d $TESTDIR ];then
    echo "Already exists ""$TESTDIR"
    continue
  fi
  mkdir -p ${TESTDIR}
  pushd $TESTDIR
  pwd
  echo "unzip <<<<<<<<"
  echo ${gridpack}
  tar xvf ../${gridpack}
  #tar xvfz ../${gridpack}
  ./runcmsgrid.sh 50 10 10 &> test_log.txt &
  popd

done
